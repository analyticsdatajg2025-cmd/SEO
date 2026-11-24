# 10 · Auditoría La Curacao (lacuracao.pe) · orgánico no-brand

Revisión: **24 nov 2026**. Pedido de Elias: auditar el canal orgánico **no-brand** (impresiones, clics, CTR, ventas SEO, GEO) por categoría, subcategoría y producto, con 7 de cada uno, y encontrar lo que está en **posición 5-10 para llevarlo al top 3**.

Etiquetas como en `docs/02`: `COMPROBADO` (visto en el HTML/sitemap hoy), `HIPÓTESIS`, `SIN DATO`.

## 0. Estado de los datos

| Fuente | Estado | Qué falta |
|---|---|---|
| Search Console | **SIN DATO**: no llegó ningún exporte y el equipo sigue sin acceso (`docs/06`, A1) | Consulta + página + clics + impresiones + posición, últimos 3 meses y mismo periodo del año pasado |
| GA4 | **SIN DATO** en esta revisión (solo el total anual de `docs/01 §3`: orgánico S/ 7 M = 12% de S/ 60 M) | Página de destino + sesiones + transacciones + ingresos, filtrado a Organic Search |
| Yandex Webmaster | **SIN DATO** | Consultas (y página si se puede) + impresiones + clics + posición. En Perú Yandex pesa poco: sirve de referencia, no para decidir |

**Consecuencia**: hoy no se puede decir qué URL está en posición 5-10 ni cuánto vende. Lo que sigue es (1) la auditoría pública, que sí está comprobada, (2) las 7 categorías, 7 subcategorías y 7 productos que conviene seguir y por qué, y (3) el script `herramientas/oportunidades_top3.py`, que hace el cálculo 5-10 → top 3 apenas lleguen los exportes (§5).

## 1. Hallazgos técnicos que frenan el no-brand (COMPROBADO 24-nov)

| # | Hallazgo | Impacto en no-brand | Arreglo | Quién |
|---|---|---|---|---|
| T1 | **19 de 49 fichas revisadas (39%) usan la meta descripción genérica de la home** ("Compra online en La Curacao laptops, televisores y electrodomésticos…") | Alto en CTR: Google reescribe o muestra un texto que no habla del producto. Es la palanca más barata para subir CTR sin mover posición | Plantilla por categoría: `{producto} {atributo clave} a S/ {precio}. Paga en cuotas con Efectiva, envío a todo el Perú y retiro en tienda.` | Carol (CMS) con borradores de Claude; JK revisa |
| T2 | **Categorías y subcategorías sin texto útil**: el bloque `category-description` solo tiene estilos de Page Builder (banner), sin texto; no hay FAQ propias | Alto: para "refrigeradoras", "lavadoras", "aire acondicionado" Google y los motores de IA no tienen qué citar fuera de la grilla | 100-150 palabras arriba (qué elegir, tamaños, precios desde) + 4-6 preguntas abajo, por las 7 subcategorías de §3 | Rolando/Ronald o Carol con Claude; Comercial valida |
| T3 | **Product JSON-LD pobre**: `description` de una línea ("Electrolux tiene lo mejor en refrigeradoras."), `category: null`, sin `gtin`, sin `shippingDetails` ni `hasMerchantReturnPolicy`, sin `aggregateRating` | Medio-alto: menos fichas con precio/envío/devolución en resultados y en Shopping orgánico (listados gratuitos) | Completar desde Magento (TI): GTIN del feed (ya existe para Meta/TikTok), envío y devoluciones a nivel tienda, reseñas reales si hay | TI Magento · JK spec |
| T4 | **981 URLs técnicas `/catalog/category/view/id/…` en el sitemap**, bloqueadas en `robots.txt` (`Disallow: /catalog/`) y con canonical a otra variante técnica (`/catalog/category/view/s/samsung/id/1374/`) | Medio: señales contradictorias (sitemap dice "indexa", robots dice "no entres"); presupuesto de rastreo | Sacarlas del sitemap; que el canonical apunte a la URL amigable (`/curacao/samsung.html` o la que corresponda) | TI |
| T5 | **Categoría rota `/tecnolog-a.html`** (título "Tecnolog a", 0 productos, meta de la home) y subcategorías hijas (`/tecnolog-a/smart-home-y-dom-tica/c-maras-de-seguridad.html`) en el sitemap e indexables | Bajo-medio: páginas vacías indexables, duplican `/tecnologia/` | 301 a la categoría correcta o noindex y fuera del sitemap | Carol (CMS) + TI |
| T6 | **Subcategorías duplicadas**: `lavavajillas` en Cocina y en Lavado (6 y 9 productos), `audífonos` en Tecnología y en Celulares, `soundbars` en Televisores y en Audio. Títulos casi iguales | Medio: canibalización (HIPÓTESIS hasta ver en GSC si se alternan) | Elegir una URL principal por término; la otra con canonical a la principal o con un enfoque distinto ("audífonos para celular") | JK decide con GSC; Carol ejecuta |
| T7 | **Enlaces internos con parámetro `?bid_id=`** desde las grillas de categoría (productos patrocinados) | Bajo: el canonical lo corrige, pero gasta rastreo y diluye enlaces | Que el enlace de la grilla sea la URL limpia y el parámetro vaya por JS/data-atributo | TI |
| T8 | **Home sin `canonical`**; títulos de ficha con "Cyber WOW" en 2 de 49 | Bajo; el "Cyber WOW" hay que retirarlo al cerrar el evento para no arrastrar fechas | Canonical en home; registro de títulos de evento para revertir | TI · Carol |
| T9 | Títulos que no coinciden con el H1 ni entre sí (ventilador Bord 15718: título "55W", H1 "60W"; laptops sin la palabra "Laptop" en el título) | Medio: calidad del catálogo y relevancia para la consulta genérica | Regla de título: `{tipo de producto} {marca} {atributo} {modelo}`; revisar datos con Comercial | Carol · Comercial |
| T10 | Sitemap de **92.926 URLs** (90.214 fichas) contra ~16.9 K SKU en el feed (`docs/01`) | Medio: igual que en `docs/02` (antes ~99.5 K; bajó ~6.6 K) | Depurar sin stock/descontinuados después de Cyber (acción 2.12 de `docs/04`) | JK + TI |

Cambió desde el 16-oct: `robots.txt` de La Curacao **ya declara bien** el sitemap (`Sitemap: https://…`, sin espacio). Actualizado en `docs/02`.

## 2. GEO (motores de IA)

| Punto | Estado |
|---|---|
| `llms.txt` publicado con departamentos, categorías clave y crédito con Financiera Efectiva | COMPROBADO · bien. Pendiente: actualizar el nombre a **Efectibank** y sumar las 7 subcategorías de §3 |
| `robots.txt` no bloquea bots de IA (solo `User-agent: *` con rutas de Magento) | COMPROBADO |
| **El CDN (Fastly/Varnish) responde 403 a `GPTBot` y `ClaudeBot`** en todas las URLs, incluido `robots.txt` ("Error 54113", respuesta en el borde en <0,1 s). Es una regla por user-agent que distingue mayúsculas (`gptbot` en minúsculas pasa). **Igual en efe.com.pe**. Pasan con 200: OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, PerplexityBot, Perplexity-User, Googlebot, Bingbot, Applebot, meta-externalagent, Amazonbot, CCBot, Bytespider, DuckAssistBot, MistralAI-User. Prueba del 24-nov con user-agent simulado desde un servidor externo: no detecta bloqueos por IP que apliquen solo a las IP reales de cada bot | COMPROBADO |
| Efecto: ChatGPT Search y Claude con búsqueda **sí pueden leer y citar** el sitio (sus bots de búsqueda pasan). Lo bloqueado son los rastreadores de **entrenamiento** de OpenAI y Anthropic: los modelos conocen menos el catálogo y la marca, y la regla contradice el `llms.txt`. Decisión de negocio (Elias): quitar la regla del CDN y, si se quiere limitar, hacerlo en `robots.txt` o con límite de velocidad | HIPÓTESIS sobre el impacto |
| Lo que la IA puede citar: categorías sin texto ni FAQ (T2), fichas con descripción de una línea en el schema (T3) | COMPROBADO · es la brecha GEO principal: sin texto propio, la respuesta de la IA cita a otro retail |
| Visibilidad real en ChatGPT/Perplexity/AI Overviews para "mejor refrigeradora", "aire acondicionado precio Perú" | SIN DATO · se mide a mano con 20 consultas fijas por mes (planilla de Carol) |

## 3. Qué seguir: 7 categorías, 7 subcategorías, 7 productos

Elegidos por **peso comercial (línea blanca, TV, celulares, cómputo, calor por verano y El Niño)** y por los problemas on-page encontrados. **No** están elegidos por posición ni venta, porque esa data no llegó: las columnas de GSC/GA4 quedan en `SIN DATO` hasta correr el script.

### 3a. Categorías

| Categoría | URL | Título / H1 hoy | Problema principal | Impr. · Clics · CTR · Pos. · Venta orgánica |
|---|---|---|---|---|
| Televisores | `/tecnologia/televisores.html` | "Televisores en Oferta \| Tecnología \| La Curacao" / "Televisores" | Sin texto ni FAQ (T2); soundbars duplicadas (T6) | SIN DATO |
| Celulares | `/tecnologia/celulares.html` | "Celulares \| Tecnología \| La Curacao" / "Celulares" | Título sin modificador ("precios", "en cuotas"); audífonos duplicados (T6) | SIN DATO |
| Computación | `/tecnologia/computacion.html` | "Computación \| La Curacao" / "Computación" | **Meta genérica de la home** (T1) | SIN DATO |
| Refrigeración | `/electrohogar/refrigeracion.html` | "Refrigeración \| Electrohogar \| La Curacao" | Meta de plantilla ("…Consulta sus características y condiciones") | SIN DATO |
| Lavado | `/electrohogar/lavado.html` | "Lavado \| Electrohogar \| La Curacao" | Lavavajillas duplicado con Cocina (T6) | SIN DATO |
| Climatización | `/electrohogar/climatizacion.html` | "Climatización \| Electrohogar \| La Curacao" | Temporada de calor + El Niño (`docs/05`): es la que más rápido puede pagar | SIN DATO |
| Cocina | `/electrohogar/cocina.html` | "Cocina \| Electrohogar \| La Curacao" | "Cocina" es ambiguo (menaje vs cocina a gas); el H1 no dice "cocinas y hornos" | SIN DATO |

### 3b. Subcategorías

| Subcategoría | URL | Consulta no-brand objetivo (HIPÓTESIS) | Problema principal | Impr. · Clics · CTR · Pos. · Venta |
|---|---|---|---|---|
| Smart TV | `/tecnologia/televisores/smart-tv.html` | "smart tv", "televisor 55 pulgadas" | Sin texto/FAQ; compite con la categoría padre | SIN DATO |
| Celulares y smartphones | `/tecnologia/celulares/celulares-y-smartphones.html` | "celulares", "celulares en oferta" | Compite con `/tecnologia/celulares.html` (HIPÓTESIS de canibalización) | SIN DATO |
| Laptops | `/tecnologia/computacion/laptops.html` | "laptops", "laptop precio" | Título sin "Ofertas"/"Precios"; fichas sin "Laptop" en el título (T9) | SIN DATO |
| Refrigeradoras | `/electrohogar/refrigeracion/refrigeradoras.html` | "refrigeradoras", "refrigeradora precio" | Sin texto; fichas con meta genérica (T1) | SIN DATO |
| Lavadoras | `/electrohogar/lavado/lavadoras.html` | "lavadoras", "lavadora 13 kg" | Sin texto; 4 de 7 fichas con meta genérica | SIN DATO |
| Aires acondicionados | `/electrohogar/climatizacion/aires-acondicionados.html` | "aire acondicionado", "aire acondicionado precio" | Sin texto; calor y El Niño | SIN DATO |
| Ventiladores | `/electrohogar/climatizacion/ventiladores.html` | "ventiladores", "ventilador de pie" | Datos inconsistentes en fichas (T9); temporada | SIN DATO |

### 3c. Productos (uno por categoría; los 49 revisados están en §6)

| Producto | URL | Precio (24-nov) | Problema on-page | Impr. · Clics · CTR · Pos. · Venta |
|---|---|---|---|---|
| TV Samsung 55" UHD U8000H | `/55-uhd-u8000h-vision-ai-smart-tv-un55u8000hgxpe.html` | S/ 1,399 | Meta genérica (T1) | SIN DATO |
| Celular Samsung Galaxy A17 256GB | `/galaxy-a17-256gb-negro-sm-a175fzkkltp.html` | S/ 1,099 | Sin reseñas ni GTIN (T3) | SIN DATO |
| Laptop Lenovo IdeaPad Slim 3 R5 512GB | `/lap-ip3-15f-r5-75-8gb-512ssd-82xq00ltlm.html` | S/ 2,529 | Título sin "Laptop" (T9) | SIN DATO |
| Refrigeradora Electrolux 237L Inverter | `/refri-eltlx-btm-frz-237l-inv-c-frio-ngr-erb25a2p5ab.html` | S/ 899 | Meta genérica; schema con descripción de una línea y `category: null` (T1, T3) | SIN DATO |
| Lavadora LG TurboDrum 13 kg | `/lavadora-wt13bvtb-lg-wt13bvtb.html` | S/ 899 | Sin envío/devolución en schema (T3) | SIN DATO |
| Aire acondicionado portátil Coldex 9000 BTU | `/aire-acond-portatil-9mil-btu-coldex-aax-9000.html` | S/ 1,699 | Meta genérica (T1) | SIN DATO |
| Ventilador torre Bord 15718 | `/vent-15718-torre-rmto-ne-bord-15718r-ne-bord.html` | S/ 269 | Título "55W" vs H1 "60W" (T9) | SIN DATO |

## 4. Cómo se pasa de posición 5-10 a top 3 (receta por tipo)

Se aplica solo a las URLs que el script marque en 5-10 con impresiones suficientes; el orden lo da la venta extra estimada.

| Tipo | Acciones (de más barata a más cara) |
|---|---|
| Categoría / subcategoría | 1) Título con la consulta no-brand principal + modificador que gane clic ("Refrigeradoras: precios y ofertas en cuotas \| La Curacao"). 2) Meta propia con precio desde y beneficios (cuotas Efectiva, envío, retiro). 3) Texto de 100-150 palabras + FAQ. 4) Enlaces internos desde home, menú y fichas hermanas con el texto de la consulta. 5) Resolver duplicados (T6). |
| Producto | 1) Meta propia (T1). 2) Título `{tipo} {marca} {atributo} {modelo}` (T9). 3) Schema completo: GTIN, envío, devolución, reseñas reales (T3). 4) Descripción útil (150+ palabras, sin copiar al fabricante) y bloque "paga en cuotas con Efectibank" (puente al crédito, `docs/08`). 5) Enlace desde la subcategoría en la primera fila si hay stock. |
| Medición | Registro de cambios (fecha, URL, antes/después) y comparación 28 días antes/después contra un grupo de control de URLs no tocadas (`docs/04 §1.2`). |

Plazos de rastreo e indexación en `docs/09`. **No se promete** que lleguen al top 3: se mide.

## 5. Cálculo 5-10 → top 3 cuando lleguen los datos

`herramientas/oportunidades_top3.py` (requiere pandas):

```bash
python3 herramientas/oportunidades_top3.py --gsc datos/gsc_query_page.csv --ga4 datos/ga4_landing_organico.csv --yandex datos/yandex_queries.csv --gsc-prev datos/gsc_query_page_PY.csv --out datos/salida
```

- Separa marca/no-marca con una expresión regular (`curacao`, `la cura`, variantes con errores de tipeo; ajustable con `--marca`).
- Clasifica cada URL en home, categoría, subcategoría, producto y marca por la estructura de rutas del sitemap.
- Toma las URLs no-brand con posición media 4.5-10.5 y 200+ impresiones.
- **CTR objetivo del top 3 = el CTR real del propio sitio en posiciones 1-3**, no-brand, por tipo. Si no hay muestra suficiente, queda `SIN DATO` (no usa curvas genéricas).
- Venta extra = impresiones × (CTR top 3 − CTR actual) × ingreso orgánico por sesión de esa URL en GA4. Es un **escenario**, no una proyección.
- Entrega `informe_oportunidades.md` con el top 7 por tipo y dos CSV. Todo queda en `datos/` (fuera del repo).

## 6. Anexo · las 49 fichas revisadas (7 por categoría)

Primeros 7 productos de la grilla de cada categoría el 24-nov. "Meta" = usa la descripción genérica de la home.

| Categoría | Productos (precio) | Meta genérica |
|---|---|---|
| Televisores | Samsung 50" Mini LED M60H (999) · Samsung 65" Mini LED M70H (2,199) · Samsung 75" UHD U8000H (1,999) · Samsung 55" UHD U8000H (1,399) · LG 70" Nano 4K (1,999) · LG 75" Nano 4K (1,999) · Samsung 55" Mini LED M70H (1,399) | 5 de 7 |
| Celulares | iPhone 18 Pro Max 256GB Black (6,799) · iPhone 18 Pro Max 256GB Burgundy (6,499) · Galaxy A57 5G 256GB (1,699) · iPhone 17 Pro 256GB Silver (5,499) · iPhone 17 Pro 256GB Naranja (4,999) · Galaxy A17 256GB (1,099) · iPhone 17 Pro Max 256GB Orange (5,899) | 3 de 7 |
| Computación | Lenovo IdeaPad Slim 3 R5 (2,529) · HP OMEN HyperX (5,949) · HP 15.6" R7 (2,999) · HP Smart Tank 580 (549) · Lenovo IdeaPad Slim 3i i7 (3,999) · HP OmniBook 3 14" (2,399) · HP Victus R7 RTX 4050 (3,999) | 1 de 7 |
| Refrigeración | Electrolux 237L Inverter (899) · Electrolux 419L Side by Side (1,599) · LG 215L Multi Air Flow (899) · Mabe 243L (899) · Indurama 529L (1,699) · LG 374L Door Cooling+ (1,699) · Bord 511L Side by Side (1,799) | 1 de 7 |
| Lavado | LG TurboDrum 17 kg (1,299) · LG TurboDrum 13 kg (899) · Samsung 19 kg Ecobubble (1,299) · Samsung 19 kg AI Wash (1,599) · Samsung 13 kg EcoBubble (1,099) · Mabe 21 kg Direct Motion (1,399) · Mabe 10 kg Aqua Care (699) | 4 de 7 |
| Climatización | Ventilador torre Bord 15718 (269) · Ventilador Bord 45W 4896 (149) · Ventilador de pie Bord doble aspa (199) · Aire portátil Coldex 9000 BTU (1,699) · Ventilador Bord 15830 (249) · Ventilador industrial Bord V2000 (229) · Ventilador Bord 15752 (199) | 3 de 7 |
| Cocina | Mabe 51 cm a gas (499) · Bord 20" 4 hornillas (399) · Coldex 60 cm CX605 Plus (599) · Mabe 4 hornillas CMP6010FG1 (759) · Coldex 60 cm CX608 Plus (799) · Electrolux 60 cm VaporBake (799) · Indurama Granada (899) | 2 de 7 |

3 de las 7 fichas de Computación se enlazan desde la grilla con `?bid_id=` (T7).
