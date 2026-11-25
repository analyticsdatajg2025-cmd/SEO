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

**8 · Medir.** Cada cambio queda en un **registro**: fecha, URL, antes, después y quién aprobó. A los 28 días se compara la URL contra sí misma y contra un **grupo de control** que no se tocó, para descontar la estacionalidad. Qué se mide: §9.

**9 · Aprender**: los tipos de cambio que movieron la aguja suben de prioridad en el ciclo siguiente.

## 5. Qué toca y qué no
| Sí, con aprobación de Kevin | No, salvo decisión expresa |
|---|---|
| Blog: artículos nuevos, ajustes, títulos, metas, H2, FAQ, enlaces, JSON-LD | Home y lo visible de primer nivel (banners, menús) |
| Textos de categorías, títulos y metas de categorías | Plantillas, configuración global, checkout |
| Fichas: título SEO, meta, descripción propia | Precios, promociones, landings en pauta |
| Tickets técnicos a TI: páginas ajenas, sitemap, 301, H1 de la home sin cambio visual | Cambios en el Magento compartido sin ticket ni reversión |

**Ritmo** (decisión de Elias, 24-nov-2026; Kevin ajusta):

| Periodo | Blogs nuevos | Ajustes (títulos, metas, textos, blogs viejos) |
|---|---|---|
| Semana normal | **3-4 por semana** | hasta 10 |
| 4-8 semanas antes de un Cyber | **4-5 por semana** (o diario en las semanas pico), enfocados en el Cyber | hasta 15 |
| Semana del Cyber | Sin blogs nuevos: solo actualizar los ya publicados (ofertas, stock, fechas) | Lo urgente |

Cuidados que el agente aplica solo:
- **Arranque gradual**: las primeras 4 semanas, 2-3 por semana. Se sube a 3-4 si Kevin aprueba sin cambios grandes al menos 8 de cada 10 borradores y no aparece canibalización.
- **Un tema = una búsqueda distinta.** Skullcandy tiene ~48 productos; 3-4 blogs por semana son ~150-200 al año (`ESTIMACIÓN`). Sin control, los blogs empiezan a competir entre sí. Antes de proponer un blog, el agente revisa el mapa de zonas (§3) y los blogs existentes. Si el tema ya tiene página, propone actualizar en vez de crear.
- **El contenido de Cyber se publica antes.** Un blog nuevo tarda semanas en indexarse y posicionar (`docs/09`), así que lo de Cyber sale 4-8 semanas antes. La fecha del próximo Cyber es `SIN DATO`.
- **Capacidad de revisión**: con 3-4 blogs a la semana, Kevin necesita unas 2-4 horas semanales para revisar (`ESTIMACIÓN`, 30-60 min por blog).

**Se respeta el plan de `docs/04`**: sin cambios de plantillas después del 10-dic y congelamiento 72 h antes de cada Cyber. Los blogs no son plantillas.

### 5b. Regla de oro: cero invención
- **Cada dato tiene fuente**:
  - Las búsquedas y su volumen salen de GSC, del Planificador o de Trends.
  - Los modelos, precios, especificaciones y stock salen del catálogo de skullcandy.com.pe o de la ficha oficial de la marca.
  - El envío, la garantía y las devoluciones salen de las políticas publicadas en el sitio.
- **Cada borrador trae sus fuentes al lado** (visibles solo para el aprobador): de dónde sale cada cifra y cada especificación.
- **Si falta un dato, no se rellena.** El borrador lo marca `PENDIENTE` en amarillo y Kevin decide.
- **Prohibido en el texto publicado**:
  - Cifras sin fuente ("el 80% de los peruanos...").
  - Reseñas, testimonios o citas inventadas.
  - Comparaciones con datos de otras marcas sin fuente.
  - Fechas de lanzamiento no confirmadas.
- **El verificador automático (paso 5) rechaza el borrador** si encuentra un precio, una especificación o una cifra que no esté en las fuentes del lote.

### 5c. Cómo se arma cada blog (Google + búsquedas con IA)
Cada blog sigue una plantilla pensada para dos lectores. El primero es Google clásico. El segundo son los buscadores con IA: AI Overviews y modo IA de Google, ChatGPT, Perplexity y Gemini, que citan fuentes claras y bien estructuradas.

| Parte | Para qué |
|---|---|
| **Una búsqueda objetivo** (de GSC o del Planificador) y 3-5 relacionadas | Que el blog compita por algo que la gente busca de verdad |
| **Título ≤ 60 caracteres** con la búsqueda; meta ≤ 155 | Que Google lo muestre y la gente haga clic |
| **Respuesta directa en el primer párrafo** (40-60 palabras) | Es lo que citan los fragmentos destacados y las respuestas de IA |
| **H2 escritos como preguntas reales** (de "Más preguntas" de Google y de las consultas de GSC) | Cada H2 responde una pregunta; las IA extraen por sección |
| **Tabla comparativa** con especificaciones reales del catálogo | Las tablas se citan mucho y ayudan a decidir |
| **Modelos con su nombre exacto** (Crusher ANC 2, Method 360 ANC...), enlazados a su ficha con stock | Entidades claras para Google y las IA; puente a la venta |
| **FAQ** de 4-6 preguntas con `FAQPage`, más `BlogPosting` con autor y fecha | Datos estructurados para resultados enriquecidos |
| **"Actualizado el..."** visible, y autor (Skullcandy Perú / equipo) | Frescura y confianza (E-E-A-T) |
| **Dato local**: envío en Perú, garantía, tiendas o recojo (de las políticas publicadas) | Lo que el sitio global y los revendedores no dicen |
| **Sin relleno**: 800-1,500 palabras según la búsqueda | Se gana por utilidad, no por largo |


## 6. Dónde corre

**Recomendación** (lo más visual y lo más fácil, sin servidores ni instalaciones):

| Pieza | Qué es | Por qué |
|---|---|---|
| **Panel** | Página privada en claude.ai, como el dashboard de martech, con base de datos propia. Elias y Kevin entran por un enlace | Ahí se ve, se edita y se aprueba todo; mismo patrón que ya usan |
| **Motor** | Una **tarea programada** de Claude que corre sola cada semana (lunes): lee los datos, detecta, genera 3-4 borradores, los verifica y los deja en el panel | Sin servidores ni clave de API aparte; se pausa o se cambia el día cuando se quiera |
| **Datos** | Al inicio, exportes de GSC y GA4 que se suben al chat (ver §8). Después, exportación de GSC a BigQuery para que el motor lea solo | Se arranca ya; se automatiza cuando haya proyecto de Google Cloud |

**Panel publicado** (25-nov-2026, privado; Elias lo comparte con Kevin desde *Compartir*): https://claude.ai/artifact/Aq9rmVL6sMC4iNPuRScyTw · fuente: `panel/agente-seo-skullcandy.html`. Guarda todo en su base de datos: colecciones `borradores` (blogs, ajustes, categorías, fichas y tickets técnicos), `metricas` (`base` y una foto por fecha) y `config/agente` (ritmo, inicio, fechas clave). El motor escribe ahí con la herramienta de datos del artifact; el panel solo muestra y edita. Ya tiene cargados los 9 tickets técnicos S1-S9 y la línea base parcial de la auditoría.

**Pestañas del panel**:
1. **Esta semana**: los borradores del lunes, cada uno con la búsqueda objetivo, por qué se eligió (datos de GSC) y su estado (borrador, en revisión, aprobado, publicado, rechazado).
2. **Editor**: vista previa del blog tal como se verá en el sitio y edición directa del texto, el título, la meta y la FAQ. Al lado, las fuentes de cada dato y los `PENDIENTE`. Botones: *Aprobar*, *Pedir cambios a la IA* (con un comentario), *Rechazar*, *Copiar HTML para Magento*.
3. **Ajustes**: los cambios propuestos a blogs, categorías y fichas existentes, con el antes y el después lado a lado.
4. **Calendario**: lo programado por semana, con las ventanas de Cyber y los congelamientos.
5. **Medición**: los indicadores de §9, antes y después, por blog y en total, contra el grupo de control.

Publicar sigue siendo manual: se copia el HTML aprobado al admin de Magento (Mageplaza Blog). Si la edición del módulo tiene API, más adelante el motor deja el borrador directo en Magento, sin publicarlo.

### Otras opciones evaluadas
| Opción | Cómo | Costo | Cuándo |
|---|---|---|---|
| **A · Copiloto** | Cada 2 semanas una sesión de Claude Code lee los datos, corre los chequeos y llena la cola de propuestas | Cuenta actual | **Piloto** (ya) |
| **B · Recolector automático** | Apps Script en una Google Sheet (como el hub del dashboard) baja GSC y GA4 cada semana con su propio permiso de Google, sin claves en el código | Gratis | Cuando el piloto valide el método |
| **C · Agente en ciclo** | Una tarea programada (sesión de Claude que corre sola cada 2 semanas) o la API de Claude desde Apps Script genera las propuestas y avisa | API: `ESTIMACIÓN` de pocos USD al mes para este volumen; alguien tiene que pagarla | Fase 2 |

Opcional, y simplifica mucho la lectura: la **exportación masiva de Search Console a BigQuery**.
- Se configura en GSC y necesita un proyecto de Google Cloud con facturación. El costo es bajo para un sitio de este tamaño (`ESTIMACIÓN`).
- Esta sesión tiene conexión a BigQuery, así que con la exportación activa el agente consulta GSC directo, sin descargas.
- La exportación no trae historia hacia atrás: conviene activarla pronto.



## 7. Piloto (6-8 semanas)
| Semana | Qué | Resultado observable |
|---|---|---|
| 0 (hecho) | Auditoría pública (§2) | `COMPROBADO`: 143 URLs, ~65 ajenas o de prueba |
| 1 | **Línea base** en GSC: consultas y páginas de 16 meses, páginas indexadas, las ~65 páginas basura. Segmento orgánico en GA4. Grupo de control | Tabla base por URL y por zona (§3) |
| 1 | Ticket a TI: S1-S4 y S8, con lista de URLs y reversión | Ticket abierto o aplicado |
| 2 | Lote 1 (solo contenido): patrón de títulos de fichas y categorías y metas propias (S5, S7) | ~40 cambios en el registro |
| 2 | Panel publicado y tarea programada semanal activa | Primeros borradores en el panel |
| 3-4 | Lote 2: textos de 4-6 categorías por zona (inalámbricos, ANC, deporte, gamer, niños); blog propio de Skullcandy a **2-3 por semana** (arranque gradual, §5) | Publicados y aprobados por Kevin |
| 5-6 | Lote 3: lo que digan los datos (posición 5-20, CTR bajo) y temporada (regreso a clases); blog a **3-4 por semana** si la calidad lo permite | Cambios en el registro |
| 8 | **Lectura**: indicadores de §9, cambiados frente a control a 28 días; qué tipo de acción funcionó | Informe: seguir, ajustar o parar |

Para pasar a la fase 2 (lectura automática de datos con BigQuery y textos de fichas a escala), los cambios del piloto tienen que mejorar clics o posición frente al control, sin incidentes. Si no, se ajusta el método antes de automatizar.

## 8. Lo que falta para arrancar
1. **Kevin**: validar el ritmo de §5 y ser el aprobador.
2. **Línea base**: exportes de GSC y GA4 (paso a paso en §8b). Se suben al chat de la sesión, **nunca al repo**.
3. **Planificador de palabras clave**: está en Google Ads, en *Herramientas → Planificación → Planificador de palabras clave*. Da el volumen mensual de búsquedas en Perú y funciona desde cualquier cuenta con acceso. La cuenta de la captura (un MCC de HP, con campañas de impresoras de La Curacao) sirve para consultar volúmenes. Para ver qué búsquedas reales disparan los anuncios de **Skullcandy** hace falta su propia cuenta de Ads, en *Estadísticas e informes → Términos de búsqueda*. Pedírsela a Paid.
4. **Elias**: ¿hay un proyecto de Google Cloud del grupo para exportar GSC a BigQuery? Con la recomendación de §6 no hace falta pagar la API de Claude aparte.
5. **TI**: quién aplica S1-S4 y S8, y qué edición de Mageplaza Blog hay (si tiene API).
6. **Marca**: ¿el contrato con Skullcandy global pone reglas de uso de marca, textos o imágenes? Si no se sabe, el piloto escribe textos propios y no copia los de la marca global.

### 8b. Cómo hacer los exportes (una vez para la línea base; luego cada mes hasta automatizar)

**A · Search Console: rendimiento** (lo más importante)
1. Entrar a search.google.com/search-console y elegir la propiedad **skullcandy.com.pe** arriba a la izquierda.
2. Menú izquierdo: **Rendimiento → Resultados de búsqueda**.
3. Arriba, en los filtros:
   - **Tipo de búsqueda: Web**.
   - **Fecha → Personalizar → "Últimos 16 meses"** → Aplicar.
4. Encender las cuatro tarjetas del gráfico (**Clics totales, Impresiones totales, CTR medio, Posición media**) para que salgan las cuatro columnas.
5. Arriba a la derecha: **Exportar → Descargar Excel**. Sale un solo archivo con pestañas: Consultas, Páginas, Países, Dispositivos, Apariencia en búsqueda y Fechas. Cada pestaña trae hasta 1,000 filas, suficiente para Skullcandy.
6. Repetir el paso 5 con **Fecha → "Últimos 28 días"**: es el "antes" fino del piloto.
7. Opcional, para ver qué consultas trae cada página importante: en el filtro **+ Nuevo → Página → "La URL contiene"**, poner la URL (por ejemplo `/headphones.html`) y exportar. Hay que hacerlo página por página; por eso después conviene automatizar (BigQuery).

**B · Search Console: indexación**
1. Menú: **Indexación → Páginas**.
2. Arriba a la derecha: **Exportar → Descargar Excel** (resumen con los motivos de "no indexada").
3. Bajo **"Por qué las páginas no se indexan"**, entrar a cada motivo (por ejemplo *"Rastreada: actualmente sin indexar"*, *"Excluida por etiqueta noindex"*, *"Página alternativa con etiqueta canónica adecuada"*) y exportar su lista de ejemplos.
4. Clic en **"Ver datos sobre las páginas indexadas"** (debajo del gráfico) → Exportar: la lista de URLs que Google sí tiene. Así sabemos cuántas de las ~65 páginas ajenas están dentro.
5. Menú **Indexación → Sitemaps**: una captura de pantalla basta (estado y URLs descubiertas).

**C · GA4** (para el lado de negocio)
1. En analytics.google.com, propiedad de Skullcandy: **Informes → Interacción → Página de destino**.
2. Fecha: **los mismos 16 meses** (o lo máximo disponible).
3. **Agregar filtro → "Grupo de canales predeterminado de la sesión" = "Organic Search"**.
4. Columnas: sesiones, usuarios, sesiones con interacción, tasa de interacción, eventos clave (compras), ingresos totales.
5. Botón **Compartir este informe (↗) → Descargar archivo → CSV**.
6. Repetir sin el filtro de canal, en **Adquisición → Adquisición de tráfico** (sesiones e ingresos por canal: orgánico vs pagado vs directo).

**Dónde se suben**: se adjuntan en el chat de la sesión. Los exportes son datos crudos: no van al repo (regla del `CLAUDE.md`) y se guardan en Drive.

## 9. Qué medir antes y después (además de venta y sesiones)

Se toma la **foto "antes"** con los exportes de §8b (16 meses y últimos 28 días). Cada lote queda fechado en el registro y se compara a los 28 y a los 90 días, contra el grupo de control y, en temporadas como Cyber o Navidad, contra las mismas semanas del año anterior.

**1 · Visibilidad en Google** (GSC): ¿estamos ocupando más terreno?
| Indicador | Qué dice |
|---|---|
| **Impresiones** (total y sin marca) | Cuántas veces aparecemos. Es lo primero que se mueve, antes que los clics |
| **N.º de consultas distintas con impresiones** | **Tamaño del terreno ocupado**: el indicador más directo de lo que buscas |
| **Consultas en top 3 y top 10** | Cuántas búsquedas ganamos de verdad |
| **Posición media** por zona (§3) y por tipo de página | Si subimos, y dónde |
| **CTR** por posición | Si los títulos y metas nuevos convencen |
| **Clics sin marca** (sin "skullcandy" en la consulta) | Tráfico que **no nos conocía**: lo que no traería la marca sola |

**2 · Salud técnica** (GSC): ¿Google ve bien el sitio?
| Indicador | Qué dice |
|---|---|
| Páginas indexadas vs enviadas en el sitemap | Cobertura |
| **Páginas ajenas o de prueba indexadas** (hoy ~65 en el sitemap) | Tiene que bajar a 0 |
| **Días hasta indexar un blog nuevo** | Velocidad: si tarda mucho, se ajusta antes de Cyber |
| Errores y resultados enriquecidos válidos (Productos, FAQ) | Que los datos estructurados funcionen |

**3 · Calidad del tráfico** (GA4, solo orgánico)
| Indicador | Qué dice |
|---|---|
| **Tasa de interacción** y tiempo de interacción por blog | Si el contenido sirve o rebota |
| **Clics de blog a ficha de producto** | Si el blog lleva a la venta (puente comercial) |
| **Agregar al carrito y tasa de conversión orgánica** | Intención de compra |
| **Ventas asistidas por blog** (rutas de conversión) | El blog rara vez cierra la venta en la misma visita; asiste |
| Usuarios nuevos orgánicos | Alcance a gente que no conocía la marca |

**4 · Negocio**: ¿deja plata?
| Indicador | Qué dice |
|---|---|
| **% de la venta que viene de orgánico vs pagado** | Menos dependencia de pauta (hoy la pauta es 25% de la venta) |
| **Valor equivalente en pauta del tráfico orgánico**: clics sin marca × CPC del Planificador | Cuánto costaría comprar ese tráfico; argumento ante gerencia (`ESTIMACIÓN`, no ingreso) |
| Margen orgánico: venta orgánica × ~42% | Plata neta (`docs/03`) |

**5 · Búsquedas con IA**: ¿nos citan?
| Indicador | Cómo se mide |
|---|---|
| **Visitas desde asistentes de IA** | GA4 → Adquisición → fuente de la sesión: `chatgpt.com`, `perplexity.ai`, `gemini.google.com`, `copilot.microsoft.com` |
| **Presencia en respuestas de IA** | Panel fijo de ~30 búsquedas clave, revisado una vez al mes a mano en el resumen de IA y el modo IA de Google, ChatGPT y Perplexity: ¿aparece Skullcandy Perú o se cita el sitio? Search Console no separa los resúmenes de IA |
| Fragmentos destacados y "Más preguntas" ganados | Revisión mensual del mismo panel |

**6 · Operación del agente**: ¿la IA trabaja bien?
| Indicador | Qué dice |
|---|---|
| Blogs publicados por semana vs meta (3-4; 4-5 pre-Cyber) | Cumplimiento del ritmo |
| **% aprobado sin cambios grandes** | Calidad de la IA (meta: 8 de cada 10) |
| `PENDIENTE` por borrador y rechazos del verificador | Cuánto le falta de datos |
| Tiempo de revisión de Kevin por blog | Costo humano real |

Lectura honesta: en SEO los clics y la venta tardan; **las primeras señales (2-6 semanas) son indexación, impresiones y número de consultas**. La venta orgánica se lee a los 2-3 meses (`docs/09`).

## 10. Accesos para que el agente lea los datos y publique solo (estado al 25-nov-2026)

**Lo que el agente tiene hoy**: lectura pública de skullcandy.com.pe (la auditoría) y el panel. **No tiene** acceso a Search Console, GA4 ni Magento. El acceso de Elias es de su cuenta de Google y del admin de Magento; no pasa al agente.

### 10a. Leer Search Console y GA4 sin descargas
| Opción | Qué hace Elias / TI | Resultado |
|---|---|---|
| **BigQuery (recomendada)** | Un proyecto de Google Cloud con facturación. En GSC: *Configuración → Exportación masiva de datos* hacia ese proyecto. En GA4: *Administrar → Vínculos de productos → BigQuery* (exportación diaria). Dar a la cuenta conectada a Claude permiso de lectura en ese dataset | El agente consulta todo directo cada semana, con consultas × página (lo que el export manual no da). Costo `ESTIMACIÓN`: bajo para este tamaño. Sin historia hacia atrás: activar pronto |
| Apps Script | Script en una Google Sheet que baja GSC y GA4 con el permiso de Elias | Funciona, pero el agente igual necesita leer esa hoja |
| Exportes manuales | Subirlos al chat cada mes (§8b) | Sirve para arrancar ya |

### 10b. Publicar en Magento con un "go"
Flujo propuesto: Kevin aprueba en el panel → Elias o Kevin aprieta **Subir a Magento** (o escribe "go") → el agente sube **solo lo aprobado**, guarda el antes para revertir, verifica la URL en vivo y marca *Publicado* en el panel.

Lo que hace falta:
1. **Token de integración de Magento** (*Sistema → Extensiones → Integraciones*), creado por TI, con **permisos mínimos**: Contenido (páginas y bloques CMS), Catálogo (productos y categorías: solo título SEO, meta y descripción) y el blog. Sin acceso a pedidos, clientes, precios, stock ni configuración.
2. **Que la API del blog exista**: confirmar con TI la edición de Mageplaza Blog. Si no tiene API REST, los blogs se siguen pegando a mano y solo se automatizan metas, categorías y fichas. `HIPÓTESIS`.
3. **Escribir solo en la tienda Skullcandy**: todas las llamadas van al store view de Skullcandy, nunca al global. El Magento es compartido con EFE, La Curacao y Motocorp; un cambio global los afecta. TI confirma el código de la tienda.
4. **Red**: TI permite que el agente llegue a la API (si está detrás de VPN o lista de IPs) y se agrega el host al entorno del agente.
5. **Dónde vive el token**: en el almacén de secretos del entorno (formulario seguro). Nunca en el chat, el repo ni el código.
6. **Primero en staging**: 5-10 subidas de prueba en un ambiente de pruebas, si existe; si no, empezar por metas de 3 fichas y revisar.
7. **Caché**: confirmar con TI si hay que limpiar la caché (Varnish/FPC) para que el cambio se vea, y si el agente puede hacerlo.

Salvaguardas del agente: sube solo ítems en estado *Aprobado* y con "go"; los blogs nuevos se crean **desactivados**, se revisan en vivo y recién se activan; cada subida guarda el antes en el panel para revertir con un clic; nada fuera del catálogo de cambios permitido de §5.

Lo que no se recomienda: darle al agente un usuario y contraseña del admin para que navegue con un navegador. Es frágil, tiene más permisos de los necesarios y no deja registro limpio.

## 11. Objetivo final del agente y decisiones de Elias (25-nov-2026)

**Objetivo, en palabras de Elias**: que la IA, sola y con data real, (1) investigue qué es lo que más se busca y lo que se va a buscar, (2) con ese análisis potencie la página con SEO orgánico, técnico y GEO (blogs, encabezados, metadatos, lo que haga falta) de forma automática, y (3) mida el antes y el después para saber qué funciona.

**Decisiones**:
| Tema | Decisión |
|---|---|
| Autonomía | **Por niveles.** *Automático* (sin aprobación, reversible con un clic): títulos y metas de páginas existentes, preguntas frecuentes, menciones y fechas de campaña. *Con aprobación de Kevin*: blogs nuevos, textos largos de categorías y fichas, todo lo técnico. Lo automático se activa cuando exista el token de Magento (§10b); hasta entonces todo pasa por el panel |
| Investigación | **Demanda global**, no solo competidores: lo que la gente busca en Perú alrededor de audífonos, parlantes y accesorios. Los competidores (Falabella, Ripley, Oechsle, Mercado Libre, Hiraoka, Coolbox, skullcandy.com global, JBL, Sony) son una fuente más, por confirmar |
| Herramientas de pago | **No hay presupuesto** (Semrush/Ahrefs). La data igual es real: Search Console, GA4, Planificador de palabras clave, Google Trends, preguntas y autocompletado de Google, respuestas de IA y páginas públicas. Lo que no se puede ver: el tráfico de los competidores |
| Calendario comercial | Marketing avisa **~1 mes antes**. Se arma poco a poco |

**Fuentes del radar y qué aporta cada una** (todas reales; si una cifra no tiene fuente, no entra):
| Fuente | Qué da | Acceso |
|---|---|---|
| Search Console | Qué búsquedas ya nos muestran, impresiones, posición, CTR; 16 meses para ver cómo subió el Cyber pasado | Exporte o BigQuery (§10a) |
| GA4 | Qué páginas venden desde orgánico; visitas desde asistentes de IA | Exporte o BigQuery |
| Planificador de palabras clave | Volumen mensual en Perú y su estacionalidad | Cuenta de Google Ads (exporte manual al inicio) |
| Google Trends | Lo que está subiendo y el patrón del año pasado | Consulta pública (`HIPÓTESIS`: verificar si el agente puede leerla directo o se exporta) |
| Preguntas y autocompletado de Google, respuestas de IA | Cómo pregunta la gente y quién sale citado | Revisión del agente con búsqueda web |
| Páginas públicas (competidores, marca global, medios) | Qué temas, títulos y preguntas cubren otros | Lectura pública, como la auditoría |
| Calendario comercial | Fechas de Cyber, campañas, lanzamientos y stock a empujar | Marketing, ~1 mes antes |

**Anticipación, con el aviso de ~1 mes**:
| Cuándo | Qué hace el agente |
|---|---|
| Siempre | Mantiene un calendario de fechas que se repiten (Cyber Wow, Cyber Days, Navidad, regreso a clases, Día del Padre/Madre) con la curva del año pasado de GSC y Trends |
| ~4 semanas antes (aviso de Marketing) | Blogs nuevos de la campaña (con aprobación); ritmo 4-5 por semana |
| 1-2 semanas antes | Ajustes automáticos a páginas ya indexadas: títulos, metas, preguntas frecuentes con fechas y menciones de la campaña |
| Semana del evento | Solo actualizar lo publicado (ofertas, stock, fechas) |
| 1-2 semanas después | Quitar fechas vencidas y medir |

Como el aviso llega con ~1 mes, los blogs de campaña llegan justos para posicionar. Por eso el calendario fijo (fechas que se repiten cada año) importa: permite preparar contenido "evergreen" de la temporada antes de que llegue el aviso.

**Panel**: nueva pestaña **Radar** (lo que más se busca, lo que sube, lo que viene, lo que pregunta la gente), cada hallazgo con fuente, fecha y la acción que propone; colección `radar` en la base. Cada propuesta lleva su nivel (*Automático* o *Con aprobación*).
