# 10 · Agente SEO con IA · Skullcandy (propuesta)

Última revisión: **24 nov 2026**. Estado: **exploración y pruebas**. Propuesta para Elias, Kevin, Marketing y gerencia. Etiquetas: `COMPROBADO` · `HIPÓTESIS` · `ESTIMACIÓN` (con supuesto al lado) · `SIN DATO`. No promete ventas: dice qué se hace, cómo se controla y cómo se mide.

## 1. La idea en tres líneas
1. Un **agente de IA en ciclo** lee lo que la gente busca (Search Console, GA4, tendencias). Encuentra dónde Skullcandy aparece poco o mal y **propone** cuatro cosas: blogs nuevos, ajustes a lo publicado, textos de categorías y fichas, y correcciones técnicas.
2. **La IA propone, una persona aprueba (Kevin).** Nada se publica solo. Los cambios son chicos, por lotes, reversibles y registrados. La home y lo visible de primer nivel no se tocan.
3. El terreno se gana por capas: primero **limpiar** lo que confunde a Google, luego **ordenar** categorías y fichas, y después **conquistar** búsquedas con blog y guías.

Por qué Skullcandy es buen piloto:
- Es un sitio chico: 143 URLs en el sitemap, de las cuales ~80 son de Skullcandy.
- El margen es alto (~42%).
- Hoy depende de pauta: S/ 4.5 K al mes, 25% de la venta, ROAS 4x (`docs/01`). Cada venta que traiga el orgánico es casi toda margen.
- Lo que se aprenda aquí se lleva a La Curacao y EFE.

## 2. Punto de partida (`COMPROBADO`, 24-nov-2026, `herramientas/auditar_sitio.py`)

Revisión pública de las 143 URLs del sitemap de skullcandy.com.pe (Magento compartido con EFE, La Curacao y Motocorp):

| # | Hallazgo | Cuántos | Arreglo | Tipo / riesgo |
|---|---|---|---|---|
| S1 | **El sitemap está lleno de páginas que no son de Skullcandy**: pruebas (`test123`, `testprod`, `qr-test`, `temp-2`, `prueba-carousel`...), páginas de Tiendas EFE, La Curacao, Motocorp y Financiera Efectiva (`home-sistemas`, `cyber-2025-wow`, `gracias-financiera-efectiva`...), el `503 service-unavailable` y dos "no encontrado" de otras tiendas | **~65 de 143 (45%)** | Sacarlas de la tienda Skullcandy (store view) o `noindex`, y que no salgan en el sitemap | Técnico interno · bajo, pero Magento es compartido: ticket a TI con lista y reversión |
| S2 | Una página de prueba (`hablamas22222`) declara **canonical hacia `tusitio.pe`**, un dominio de ejemplo | 1 | Quitarla | Técnico · muy bajo |
| S3 | **Productos de EFE en el sitemap de Skullcandy**: juego de sartenes y cocina Oster | 2 | Sacarlos del catálogo de la tienda Skullcandy | Catálogo · bajo |
| S4 | **El blog no tiene artículos de Skullcandy**: sus 2 artículos son de iPhone 17 y tablets (contenido de EFE/LC que se filtra por el módulo compartido) | 2/2 | Asignar los artículos a su tienda; crear el blog propio de Skullcandy | Contenido + config · bajo |
| S5 | **Meta descripción repetida** en 94 de 142 páginas; 7 con la meta de Tiendas EFE | 94 + 7 | Una meta propia por página (la IA la redacta) | Contenido · muy bajo |
| S6 | **H1**: 32 páginas sin H1 (incluida la home) y 52 con más de uno | 84 | Un H1 por página; en la home, vía TI y sin cambio visual | Contenido / plantilla · bajo |
| S7 | **Títulos de producto inconsistentes**: la mitad dice "Audífonos Crusher ANC 2 Black \| Skullcandy" y la otra mitad solo "Crusher Anc 2 Plasma", sin tipo de producto ni marca. Las categorías mezclan "Headphones" con "Auriculares", pero en Perú se busca "audífonos" | ~25 productos · 17 categorías | Patrón único: `Audífonos {tipo} Skullcandy {modelo} {color}`; categorías con la palabra que se busca | Contenido · muy bajo |
| S8 | `www` redirige a sin `www` con **302 (temporal)** en vez de 301; `robots.txt` declara el sitemap en `www` y con `Sitemap :` | — | 301 permanente y sitemap con el dominio final | Técnico · bajo |
| S9 | 5 productos agotados en el sitemap; `/como-comprar` da 404 | 5 + 1 | Revisar el criterio de stock del sitemap; corregir el enlace | Técnico · muy bajo |
| ✓ | **A favor**: los productos tienen datos estructurados `Product` + `Offer` + `Brand`, y las categorías `CollectionPage` | 48 / 17 | Mantener | — |

Lectura:
- S5 y S7 son **solo contenido**: el equipo puede hacerlos ya, desde el admin.
- S1-S4 y S8 son **técnicos e internos**: no cambian nada visible, pero tocan el Magento compartido. Van por ticket a TI con plan de reversión.
- Lo que no sabemos sin Search Console: cuántas de esas ~65 páginas basura están indexadas y qué consultas traen hoy a Skullcandy. Queda `SIN DATO` hasta tener la línea base; el acceso admin está `CONFIRMADO`.

`HIPÓTESIS` a revisar: la mayoría de fichas tiene en texto solo el lema de la marca ("Bajos sensoriales definitivos...") y el resto quizá en imágenes. Google lee poco texto propio por producto.

## 3. El terreno: dónde busca la gente (a medir, no supuesto)
Las búsquedas se agrupan en "zonas". El agente mide cada zona con GSC y el Planificador de palabras clave, y decide qué página la defiende:

| Zona | Ejemplos de búsqueda (a validar con datos) | Página que la defiende |
|---|---|---|
| **Marca** | "skullcandy perú", "skullcandy tienda oficial", "skullcandy lima" | Home e institucionales; compite con revendedores (Falabella, Ripley, Mercado Libre) |
| **Modelo** | "crusher anc 2", "skullcandy dime 3 precio", "method 360 anc" | Ficha del producto (título y texto propios) |
| **Tipo de producto** | "audífonos inalámbricos", "audífonos bluetooth", "audífonos con cancelación de ruido", "audífonos gamer", "audífonos para niños" | Categorías con texto propio |
| **Uso / necesidad** | "audífonos para correr", "audífonos para gym", "audífonos con mucho bajo" | Categoría o guía del blog |
| **Comparación / duda** | "crusher vs hesh", "anc vs sin anc", "cómo elegir audífonos", "cómo limpiar audífonos" | Blog (guías y comparativas) |
| **Temporada** | "regalos navidad audífonos", "útiles regreso a clases", Cyber | Blog y categorías de ofertas, 6-8 semanas antes |

Realismo: en marca y modelo Skullcandy puede ser primero. En "audífonos bluetooth" compite con los grandes retailers; ahí se gana por la cola larga (uso, comparación, temporada), no de golpe.

## 4. Cómo funciona el agente (el ciclo)

```
 1 LEER ─▶ 2 DETECTAR ─▶ 3 PRIORIZAR ─▶ 4 GENERAR ─▶ 5 VERIFICAR ─▶ 6 APROBAR ─▶ 7 PUBLICAR ─▶ 8 MEDIR
   ▲                                                (automático)    (Kevin)      (equipo)    (28 días)
   └────────────────────────── 9 APRENDER: lo que funcionó sube de prioridad ◀─────────────────────┘
```

**1 · Leer** (solo lectura, nunca toca el sitio)
- **Search Console** (admin `CONFIRMADO`): consultas × página, impresiones, clics, CTR y posición de los últimos 16 meses. También la inspección de URL: si está indexada y qué canonical eligió Google.
- **GA4** (acceso `CONFIRMADO`): sesiones orgánicas, ingresos y conversión por página de entrada.
- **El sitio**: `herramientas/auditar_sitio.py` (títulos, H1, metas, canonical, schema, stock, páginas ajenas).
- **Demanda externa**:
  - Planificador de palabras clave de Google Ads, para el volumen mensual. Ver §8.
  - Google Trends, para la estacionalidad.
  - Las preguntas que muestra Google ("Más preguntas").
- **Catálogo**: stock y precio reales, para no recomendar lo que no hay.

**2 · Detectar.** Cada señal en los datos lleva a una acción:

| Señal | Qué significa | Acción que propone la IA | Intrusión |
|---|---|---|---|
| Consulta en posición 5-20 con muchas impresiones | Estamos cerca del top | Reforzar la página: sección o H2, FAQ, enlaces internos | Baja |
| Posición 1-5 pero CTR bajo | Aparecemos pero no nos eligen | Reescribir título y meta | Muy baja |
| Consultas con impresiones que caen en una página que no responde | Hueco de contenido | Brief y borrador de **blog nuevo** o texto de categoría | Baja |
| Clics de una página caen más de 30% frente a los 3 meses previos | Contenido envejecido | Actualizar modelos, año y datos | Baja |
| Dos URLs propias compiten por la misma consulta | Canibalización | Fusionar o diferenciar (con aprobación) | Media |
| Pico estacional en Trends | Demanda que viene | Publicar o actualizar 6-8 semanas antes | Baja |
| Página ajena, de prueba, error o canonical raro | Google ve basura | Ticket para TI con lista y reversión | Según el caso |

**3 · Priorizar** con una fórmula visible: impresiones en juego × distancia al top 3 × ticket del producto × facilidad. Sale un **lote chico** por ciclo.

**4 · Generar** borradores listos para pegar en Magento:
- Título, meta, H1 y H2.
- Texto y FAQ con su JSON-LD.
- Enlaces internos a fichas con stock.
- En los ajustes, el **antes y después** lado a lado.

**5 · Verificar** (automático, antes de que lo vea una persona):
- Ningún precio, especificación ni fecha que no venga del catálogo o de la ficha oficial de la marca. Nada de stock garantizado ni promociones no vigentes.
- Un H1, título de 60 caracteres o menos, meta de 155 o menos.
- Enlaces que responden 200 y apuntan a productos con stock.
- Que no repita una página existente.
- Español peruano y tono de la marca. Que no copie tal cual textos de skullcandy.com global (Google lo ve como duplicado).

**6 · Aprobar**: Kevin aprueba, edita o rechaza cada propuesta. Ese es el doble check humano.

**7 · Publicar**: al inicio el equipo pega lo aprobado en el admin. Más adelante, si el módulo de blog (Mageplaza) tiene API en la edición instalada, el agente puede dejar el **borrador** en Magento, nunca publicado. Esto es `HIPÓTESIS`: hay que verificar la edición.

**8 · Medir.** Cada cambio queda en un **registro**: fecha, URL, antes, después y quién aprobó. A los 28 días se compara la URL contra sí misma y contra un **grupo de control** que no se tocó, para descontar la estacionalidad. Se mide:
- Clics, impresiones, posición y CTR.
- Vía GA4: sesiones, ventas orgánicas y su efecto en la dependencia de pauta.

**9 · Aprender**: los tipos de cambio que movieron la aguja suben de prioridad en el ciclo siguiente.

## 5. Qué toca y qué no
| Sí, con aprobación de Kevin | No, salvo decisión expresa |
|---|---|
| Blog: artículos nuevos, ajustes, títulos, metas, H2, FAQ, enlaces, JSON-LD | Home y lo visible de primer nivel (banners, menús) |
| Textos de categorías, títulos y metas de categorías | Plantillas, configuración global, checkout |
| Fichas: título SEO, meta, descripción propia | Precios, promociones, landings en pauta |
| Tickets técnicos a TI: páginas ajenas, sitemap, 301, H1 de la home sin cambio visual | Cambios en el Magento compartido sin ticket ni reversión |

**Ritmo** (`ESTIMACIÓN`, ajustable con Kevin): por ciclo de 2 semanas, hasta 10 ajustes de títulos, metas y textos, más 2-3 artículos nuevos. Google castiga el contenido generado en masa sin valor. Por eso se trabaja en lotes chicos, revisados, con datos propios (modelos, precios reales, garantía, envío en Perú). **Se respeta el plan de `docs/04`**: sin cambios de plantillas después del 10-dic y congelamiento 72 h antes de cada Cyber.

## 6. Dónde corre (de menos a más automático)
| Opción | Cómo | Costo | Cuándo |
|---|---|---|---|
| **A · Copiloto** | Cada 2 semanas una sesión de Claude Code lee los datos, corre los chequeos y llena la cola de propuestas | Cuenta actual | **Piloto** (ya) |
| **B · Recolector automático** | Apps Script en una Google Sheet (como el hub del dashboard) baja GSC y GA4 cada semana con su propio permiso de Google, sin claves en el código | Gratis | Cuando el piloto valide el método |
| **C · Agente en ciclo** | Una tarea programada (sesión de Claude que corre sola cada 2 semanas) o la API de Claude desde Apps Script genera las propuestas y avisa | API: `ESTIMACIÓN` de pocos USD al mes para este volumen; alguien tiene que pagarla | Fase 2 |

Opcional, y simplifica mucho la lectura: la **exportación masiva de Search Console a BigQuery**.
- Se configura en GSC y necesita un proyecto de Google Cloud con facturación. El costo es bajo para un sitio de este tamaño (`ESTIMACIÓN`).
- Esta sesión tiene conexión a BigQuery, así que con la exportación activa el agente consulta GSC directo, sin descargas.
- La exportación no trae historia hacia atrás: conviene activarla pronto.

**Dónde se ve**: un **panel HTML privado**, como el dashboard de martech, con tres pestañas:
- *Cola*: propuestas con antes y después, y botones para aprobar, editar o rechazar.
- *Registro*: lo publicado.
- *Resultados*: cada cambio a los 28 días frente al grupo de control.

Para el piloto basta una Google Sheet con las mismas columnas.

## 7. Piloto (6-8 semanas)
| Semana | Qué | Resultado observable |
|---|---|---|
| 0 (hecho) | Auditoría pública (§2) | `COMPROBADO`: 143 URLs, ~65 ajenas o de prueba |
| 1 | **Línea base** en GSC: consultas y páginas de 16 meses, páginas indexadas, las ~65 páginas basura. Segmento orgánico en GA4. Grupo de control | Tabla base por URL y por zona (§3) |
| 1 | Ticket a TI: S1-S4 y S8, con lista de URLs y reversión | Ticket abierto o aplicado |
| 2 | Lote 1 (solo contenido): patrón de títulos de fichas y categorías y metas propias (S5, S7) | ~40 cambios en el registro |
| 3-4 | Lote 2: textos de 4-6 categorías por zona (inalámbricos, ANC, deporte, gamer, niños); 2 guías del blog de Skullcandy | Publicados y aprobados por Kevin |
| 5-6 | Lote 3: lo que digan los datos (posición 5-20, CTR bajo) y temporada (regreso a clases) | Cambios en el registro |
| 8 | **Lectura**: cambiados frente a control a 28 días; qué tipo de acción funcionó | Informe: seguir, ajustar o parar |

Para pasar a la fase 2 (opciones B y C), los cambios del piloto tienen que mejorar clics o posición frente al control, sin incidentes. Si no, se ajusta el método antes de automatizar.

## 8. Lo que falta para arrancar
1. **Kevin**: validar el ritmo de §5 y ser el aprobador.
2. **Línea base**: exportar desde GSC (Rendimiento, 16 meses: consultas y páginas) o darle al agente una vía de lectura (opción B o BigQuery).
3. **Planificador de palabras clave**: está en Google Ads, en *Herramientas → Planificación → Planificador de palabras clave*. Da el volumen mensual de búsquedas en Perú y funciona desde cualquier cuenta con acceso. La cuenta de la captura (un MCC de HP, con campañas de impresoras de La Curacao) sirve para consultar volúmenes. Para ver qué búsquedas reales disparan los anuncios de **Skullcandy** hace falta su propia cuenta de Ads, en *Estadísticas e informes → Términos de búsqueda*. Pedírsela a Paid.
4. **Elias**: ¿hay un proyecto de Google Cloud del grupo para exportar GSC a BigQuery? ¿Quién paga la API si se va a la opción C?
5. **TI**: quién aplica S1-S4 y S8, y qué edición de Mageplaza Blog hay (si tiene API).
6. **Marca**: ¿el contrato con Skullcandy global pone reglas de uso de marca, textos o imágenes? Si no se sabe, el piloto escribe textos propios y no copia los de la marca global.
