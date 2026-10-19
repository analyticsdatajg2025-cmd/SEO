# GSC → BigQuery → Looker Studio · piloto Efectibank

Datos de Search Console actualizados cada día, dashboard sin costo de licencia y reportes rápidos, **sin gastar tokens en el flujo diario**. Se arma primero con Efectibank (238 URLs en el sitemap del 19-oct-2026) y está hecho para sumar después La Curacao, EFE y Juntoz (más de 100 K URLs cada uno) sin rehacer nada.

```
GSC (exportación masiva, diaria) ─► BigQuery: searchconsole_<marca>   (crudo, particionado por día)
                                      │  consulta programada diaria (sql/20)
                                      ▼
                                    BigQuery: seo.*   (resúmenes chicos)
                                      ├─► Looker Studio  (dashboard)
                                      └─► scripts/reporte.sh  (reportes de 20-50 filas; Claude lee solo esto)
```

## Qué hay aquí
| Archivo | Para qué |
|---|---|
| `sql/00_tablas.sql` | Dataset `seo` y tablas del modelo (una vez) |
| `sql/01_config_efectibank.sql` | Marca, regex de consultas de marca y **reglas de grupos de URL** de Efectibank |
| `sql/02_vistas_gsc.sql` | Vistas que unen las exportaciones de todas las marcas con una columna `marca` |
| `sql/20_actualizar_diario.sql` | La consulta programada: reprocesa los últimos 5 días |
| `sql/21_reasignar_grupos.sql` | A mano, después de cambiar reglas o de cargar historial |
| `sql/reportes/r01…r07` | Reportes rápidos (ver `scripts/reporte.sh lista`) |
| `scripts/desplegar.sh` | Crea todo y programa la actualización diaria |
| `scripts/reporte.sh` | Corre un reporte con tope de bytes y pocas filas |
| `scripts/cargar_historial_api.py` | Carga una vez los 16 meses anteriores vía API |

Tablas resultado: `seo.grupo_dia` (dashboard), `seo.sitio_dia` (marca / no marca), `seo.url_dia` (por URL), `seo.consulta_grupo_semana` (consultas), `seo.url_grupo` (URL → grupo).

## Pasos (≈1 día de Kevin, después de tener el acceso)

**0. Requisitos** (Elias / TI de Efectibank; accesos A1 y EF5 de `docs/06` y `docs/08 §5`)
- Ser **propietario** de la propiedad de GSC de Efectibank (la exportación solo la activa un propietario). Preferible propiedad de dominio `sc-domain:efectibank.pe`.
- Un proyecto de Google Cloud con facturación activa (BigQuery lo exige para la exportación aunque el uso quede en el nivel gratis).

**1. Activar la exportación** (5 minutos)
1. En Google Cloud: activar la API de BigQuery y dar el rol **BigQuery Job User** y **BigQuery Data Editor** a `search-console-data-export@system.gserviceaccount.com` en el proyecto.
2. En GSC → Configuración → **Exportación masiva de datos**: id del proyecto, dataset `searchconsole_efectibank` (si la pantalla no deja poner sufijo, usar `searchconsole` y cambiar el nombre en `sql/02` y `sql/01`), ubicación **US** (la misma para todas las marcas).
3. GSC empieza a escribir **desde el día siguiente**. No trae historial: eso lo hace el paso 4.

**2. Crear el modelo** (desde una terminal con `gcloud`/`bq` y permiso de edición en el proyecto)
```bash
cd gsc-bigquery
PROYECTO=<id-proyecto> UBICACION=US scripts/desplegar.sh tablas      # hoy mismo
# cuando ya aparezcan las tablas searchdata_* (1-2 días después):
PROYECTO=<id-proyecto> UBICACION=US scripts/desplegar.sh vistas
PROYECTO=<id-proyecto> UBICACION=US scripts/desplegar.sh correr 20   # primera carga
PROYECTO=<id-proyecto> UBICACION=US scripts/desplegar.sh programar   # todos los días 07:00 Lima
```

**3. Dashboard en Looker Studio** (1-2 horas). Fuente: conector BigQuery → `seo.grupo_dia` y `seo.sitio_dia` (nunca las tablas `searchconsole_*`). Campos calculados: `CTR = SUM(clics)/SUM(impresiones)` y `Posición = SUM(suma_posicion)/SUM(impresiones) + 1` (la posición **no se promedia**: se calcula así). Páginas sugeridas:
1. Resumen: clics, impresiones, CTR y posición por semana; marca vs no marca.
2. Préstamos y ahorros por subgrupo (efectivo, electro, motos, MiVivienda, cuenta, depósito): son el dinero (`docs/08 §2`).
3. Dilución: peso de promociones, pruebas y otros hosts.
4. Consultas: `seo.consulta_grupo_semana` filtrada por grupo.
Filtro de marca en todas las páginas: así el mismo dashboard sirve para LC, EFE y Juntoz.

**4. Historial** (una vez, corre solo unas horas, sin Claude)
```bash
pip install -r scripts/requirements.txt
GOOGLE_APPLICATION_CREDENTIALS=<ruta-clave.json> python3 scripts/cargar_historial_api.py \
  --proyecto <id-proyecto> --marca efectibank --propiedad sc-domain:efectibank.pe \
  --desde <16 meses atrás> --hasta <día anterior al primero exportado>
PROYECTO=<id-proyecto> scripts/desplegar.sh correr 21
```
La cuenta de servicio va como usuario restringido en GSC. Las consultas del historial no llegan a `consulta_grupo_semana` (solo totales y URLs).

**5. Validar las reglas** con `r06` (URLs sin regla u otros hosts) y `r04` (si la regex de marca clasifica bien). Corregir `sql/01_config_efectibank.sql` → `desplegar.sh tablas` → `desplegar.sh correr 21`.

## Reportes rápidos (y cómo los usa Claude sin gastar tokens)
```bash
scripts/reporte.sh lista
PROYECTO=<id-proyecto> scripts/reporte.sh r01            # semana vs anterior por grupo
PROYECTO=<id-proyecto> scripts/reporte.sh r03 efectibank # oportunidades de CTR
```
Cada reporte lee **solo los resúmenes**, devuelve como máximo 100 filas y tiene un tope de 5 GB leídos. Para que Claude los corra en la sesión en la nube: crear una **cuenta de servicio de solo lectura** (BigQuery Data Viewer sobre el dataset `seo` + BigQuery Job User en el proyecto) y guardar su clave en la configuración del entorno (menú del entorno → Edit → variable `GOOGLE_APPLICATION_CREDENTIALS_JSON`). **Nunca en el repo ni en el chat.**

## Costo (`HIPÓTESIS`, medir el primer mes)
- Efectibank: datos chicos; debería quedar dentro del nivel gratis de BigQuery (10 GB de almacenamiento y 1 TB de consultas al mes).
- LC, EFE, Juntoz: las tablas crudas por URL pueden ser millones de filas al día. El diseño lo contiene: la consulta diaria lee solo 5 días, el dashboard y los reportes leen resúmenes, y hay topes de bytes por consulta. Revisar el gasto en Facturación → BigQuery al mes de sumarlos.

## Sumar una marca (LC, EFE, Juntoz)
1. Activar su exportación a `searchconsole_<marca>` en el mismo proyecto y ubicación (**LC y EFE antes de Cyber**, para no perder ese periodo).
2. Copiar `sql/01_config_efectibank.sql` a `sql/01_config_<marca>.sql` con su dominio, regex de marca y reglas (categoría, listado, producto, marca, tiendas, blog). Partir de los patrones vistos en `docs/02` y validarlos con Kevin.
3. Descomentar su bloque en `sql/02_vistas_gsc.sql` → `desplegar.sh tablas` → `desplegar.sh vistas`.
4. Si `consulta_grupo_semana` crece demasiado, subir `min_impresiones_consulta` en `sql/20`.
5. Revisar con BI el tope de 1 M eventos diarios de la exportación de GA4 antes de cruzar con venta (`HIPÓTESIS`: LC y EFE podrían pasarlo).

## Estado
Escrito y revisado sin conexión el 19-oct-2026: SQL validado en dialecto BigQuery con un parser, reglas probadas contra las 236 páginas del sitemap (ninguna sin grupo) y lógica del historial probada con datos de prueba. **No se ha ejecutado en BigQuery**: falta el proyecto de Google Cloud y el acceso de propietario a GSC.
