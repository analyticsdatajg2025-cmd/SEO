# 10 · Competencia Cyber Wow 2026: Hiraoka, Falabella, Ripley, Sodimac

Revisión: **20 oct 2026**, 13 días antes del evento (2 al 5 de noviembre, según las landings de Hiraoka, Falabella y Sodimac). Método: HTML servido sin JavaScript (`curl`) de la landing Cyber, la home, una PLP de televisores y una o dos PDP por sitio. Lo que el HTML muestra es lo que el sitio declara, no lo que Google indexa ni cuánto vende. Etiquetas: `COMPROBADO`, `HIPÓTESIS`, `SIN DATO`.

Páginas revisadas:

| Sitio | Landing Cyber | PLP | PDP |
|---|---|---|---|
| Hiraoka (Magento) | `/cyber-wow` | `/televisores/televisores`, `/televisores-55-pulgadas`, `/combos` | laptop Lenovo IdeaPad Slim 3, TV Hisense 55QD5SV |
| Falabella (Next.js, plataforma del grupo) | `/falabella-pe/page/Cyber-WOW` | `/category/cat210477/TV-Televisores` | TV TCL 55T6C |
| Sodimac (misma plataforma que Falabella) | `/sodimac-pe/content/cyber-wow` | `/lista/cat6370551/Televisores-Smart-TV` | TV Caixun 43" |
| Ripley | `/minisitios/cyber-wow` | — | — |

**Ripley: SIN DATO.** Cloudflare responde 403 ("Un momento…") a `curl`, a un navegador headless y a WebFetch. No se intentó saltar el bloqueo. Lo único que se ve desde fuera (buscador, 20-oct): Ripley tiene **dos URLs del evento**, `/cyber-wow` (con texto de la edición de julio) y `/minisitios/cyber-wow` (la del enlace), además de landings de campaña por categoría como `/belleza/campanas/perfumes-cyber`. HIPÓTESIS: canibalización entre las dos URLs. Para cerrarlo hace falta abrirla en un navegador normal (Carol, 10 min) o una herramienta con navegador no bloqueado.

---

## 1. Arquitectura y enlazado interno

### 1a. URL del evento

| Sitio | URL | Tipo | Nota |
|---|---|---|---|
| Hiraoka | `/cyber-wow` | **Evergreen** | Además mantiene `/cyber-days`, `/black-friday` y `/lo-mejor-del-cyber` como URLs fijas. Su blog tiene posts de apoyo (`/blog/post/cyber-wow-hiraoka-ofertas-online`). COMPROBADO |
| Falabella | `/page/Cyber-WOW` | **Evergreen** | Canonical a sí misma. Mismo patrón para `/page/Hot-Sale` (enlazado en el footer). COMPROBADO |
| Sodimac | `/content/cyber-wow` | **Evergreen** | Canonical + `BreadcrumbList`. `/content/black-friday` con el mismo patrón. COMPROBADO |
| Ripley | `/cyber-wow` y `/minisitios/cyber-wow` | Evergreen duplicada | Ver arriba. HIPÓTESIS |

**Conclusión:** los tres que se pudieron leer usan **una sola URL fija por evento**, la reutilizan cada edición y solo cambian año y fechas en title/H1/textos. Así acumulan enlaces e historial año tras año. Es lo contrario de lo que tienen EFE y La Curacao (`docs/02`: `/cyber-days`, `/efe/cyberdays.html`, `/previa-cyber`, `/cyber-wow`, `/contenido/cyberdays-604`, todas en 200 y en el sitemap).

### 1b. Landings secundarias que priorizan

| Tipo de landing | Hiraoka | Falabella | Sodimac |
|---|---|---|---|
| Por categoría con "Cyber Wow X" | 8 bloques H2 ("Cyber WOW Televisores y Audio", "...Laptops y Tablets", "...Refrigeradoras, Cocinas y Lavadoras", "...videojuegos y PS5") que enlazan a las PLP normales | 15+ H3 "Cyber Wow Celulares / Electrodomésticos / Smart TV / Tecnología..." con texto de ~80 palabras y enlaces a PLP, marcas y modelos | H2 "Cyber Wow Televisores 📺 / Electrodomésticos / Audífonos / Celulares / Laptops / Muebles..." |
| Por marca | `/televisores/marca-sony`, `/electrohogar/marca-lg`, `/computo-y-tecnologia/marca-hp` (rutas limpias) | `/brand/SAMSUNG`, `/brand/APPLE` + PLP filtrada `?f.product.brandName=hp` | `/marca/SAMSUNG`, `/marca/HOLZTEK` (marca propia) + "Cyber Wow Samsung / Lg / Xiaomi" |
| Por modelo (cabeza de búsqueda) | — | `/shop/samsung-galaxy-s26`, `/collection/iphone-17`, `/shop/xiaomi-15`, `/shop/nintendo-switch-2` | — |
| Por atributo (tamaño) | `/televisores-32-pulgadas`, `-50-`, `-55-`, `-65-` | Facetas en PLP | Facetas en PLP |
| Por precio | `/ofertas-con-precios-hasta-99-soles` (desde la home) | — | — (solo "Precio x volumen" y "6 cuotas sin intereses" en el menú) |
| Combos / bundles | **`/combos`** (6 enlaces desde la landing Cyber; H1 "Combos de Electrodomésticos") y productos "+ Maletín" | `2x1` aparece en textos | "Combos" en el menú de gasfitería |
| Por urgencia / stock | — | — | **"Últimas unidades"** como entrada del menú de muebles |
| Bloque "Búsquedas populares" | Sí: lista de enlaces a búsquedas frecuentes ("iphone 15"...), pero con parámetro `?cat=2828` | — | — |

COMPROBADO en el HTML. Ninguno tiene hoy una landing tipo `/hasta-500-soles` dedicada al Cyber; Hiraoka es el único con landing por rango de precio (hasta S/ 99) y por tamaño de TV.

### 1c. Distribución de autoridad Home → landing → PLP/PDP

| Sitio | Home → landing Cyber | Landing Cyber → PLP/PDP | Observación |
|---|---|---|---|
| Hiraoka | 4 enlaces a `/cyber-wow` + `/cyber-days` + 2 posts de blog | **775 enlaces** (515 únicos): PLP de laptops (8), refrigeradoras (7), TV (6), lavadoras (6), iPhone (6), combos (6) y PDP sueltas (TV, laptops, refris) | Mucho volumen; prioriza electro/tecnología, igual que EFE. Enlaces internos con `utm_source=home` y campañas viejas (`cyber_days_marzo_2025`) desde la home: mala práctica, crea variantes de URL |
| Falabella | 2-3 enlaces (menú y footer "Únete a nuestros programas") | 191 enlaces: mezcla moda, deco, tecnología; marcas y colecciones de modelo | Menos enlaces, más selectivos. La landing también se enlaza desde el footer de todas las PDP (COMPROBADO en la PDP de TCL) |
| Sodimac | 1 enlace + footer de todo el sitio ("Nuestros canales" → Cyber Wow, Black Friday) | **1,717 enlaces** (1,035 únicos); el más repetido es TV Smart TV (26) | Footer sitewide = la landing recibe un enlace desde cada página del sitio todo el año |

**Patrón común:** URL fija + enlace permanente en el footer o menú (no solo en el banner de temporada) + la landing funciona como **hub de enlaces hacia las PLP de siempre**, no hacia PLP temporales. La autoridad del evento termina en las categorías que ya rankean.

---

## 2. On-page y estrategia e-commerce

### 2a. Landing Cyber: title, H1, meta description

| Sitio | Title | H1 | Meta description | Disparadores |
|---|---|---|---|---|
| Hiraoka | `Cyber Wow 2026 ▷ Ofertas Hasta 50% dscto!  ✅` | **No tiene H1** (53 H2) | "▷ Cyber Wow Perú 2026: Encuentra las mejores ofertas hasta 50% de dscto..." | Año, "Perú", **% de descuento**, emojis/símbolos (▷ ✅) |
| Falabella | `Cyber Wow 2026 ¡Muy pronto las mejores OFERTAS! \| falabella.com` | `Cyber Wow 2026` | "Prepárate para el Cyber Wow 2026 del 2 al 5 de noviembre... Tecnología, Zapatillas, Moda..." | Año, **fechas**, "muy pronto" (fase previa), categorías |
| Sodimac | `Cyber WOW 2026🚨Regresa pronto con grandes OFERTAS` | `Cyber Wow 2026` | "¡Regresamos con grandes ofertas! 🚀 Del 02 al 05 de noviembre..." | Año, **fechas**, emoji de alerta |

Todos: keyword exacta "Cyber Wow 2026" al inicio, fechas y "ofertas". **Ninguno pone en el title o meta de la landing** "envío gratis", "retiro en tienda", "cuotas sin intereses" ni "garantía": esos disparadores aparecen en el cuerpo, en el FAQ y en las fichas. COMPROBADO. Falabella y Sodimac usan el title en "modo previa" ("Muy pronto", "Regresa pronto") y lo cambiarán al empezar el evento (HIPÓTESIS por su historial; verificar el 2-nov).

### 2b. PLP y PDP

| Sitio | PLP TV: title / H1 | PDP: title / meta |
|---|---|---|
| Hiraoka | `▷ Televisores: Ofertas en LG, Samsung, Hisense, TCL ✅` / H1 `Televisores en Oferta` | Title = nombre del producto sin marca de la tienda; meta = copia del title (no aporta CTR) |
| Falabella | `SMART TV 📺 Televisores \| Falabella Perú` / `TV Televisores` | `[Producto] [Marca] \| Falabella Perú`; meta plantilla "Compra online... conoce sus características" |
| Sodimac | `Televisores y Smart TV en OFERTA 🚀 \| Sodimac Perú` / `Televisores Smart TV` | Meta plantilla con disparadores: "**precio increíble de venta exclusiva**... **elige entre delivery y retiro en tienda. El stock es limitado.**" |

Sodimac es el único que mete disparadores de conversión (exclusividad, retiro en tienda, stock limitado) en la meta de **todas** sus fichas por plantilla. COMPROBADO.

### 2c. Contenido long-tail y FAQ

| Sitio | Landing Cyber | PLP |
|---|---|---|
| Hiraoka | FAQ largo (12 preguntas en `FAQPage` + ~20 H2 de preguntas: "¿Cuándo es el Cyber Wow Perú 2026?", "¿Cuántos Cyber Wow hay en el año?", "¿Cómo puedo recoger las compras?", "¿Las promociones se pueden comprar en tienda física?") + tips de compra (H3 numerados) + bloque de marcas | PLP TV con guía ("¿Qué debo considerar antes de comprar un televisor?", "Consejos de nuestro Experto Hiraoka") y bloque por marca. **Error de plantilla**: la PLP de TV 55" muestra "Preguntas frecuentes de Laptop HP" |
| Falabella | FAQ de 10 preguntas (`FAQPage`) + texto por categoría (~80 palabras cada uno, con marcas y modelos enlazados) | Texto SEO al pie ("Smart TV - ofertas imperdibles", "Características de las TV LED") |
| Sodimac | Caja "Datos clave" (fechas, duración, organizador IAB Perú, "envío gratis o en 120 minutos"), FAQ de 15 preguntas (`FAQPage`) | **Módulo FAQ long-tail** en la PLP de TV: "¿Qué diferencia hay entre un televisor LED y uno OLED?", "¿Cuál es el tamaño de smart tv más recomendado para una sala?", "¿Por qué conviene revisar las ofertas de televisores en eventos de temporada?", "¿Cuándo es mejor comprar un televisor?" |

Los tres apuntan a las mismas búsquedas informativas del evento ("cuándo es el Cyber Wow", "qué es", "cuánto dura", "qué tiendas participan") para ganar visibilidad desde semanas antes. Desde 2023 Google solo muestra resultados enriquecidos de FAQ a sitios de gobierno y salud, así que el valor del FAQ hoy es **el texto visible** (relevancia y respuestas para buscadores con IA), no el rich snippet.

---

## 3. Datos estructurados y Google Shopping

### 3a. Schema por página

| Marcado | Hiraoka | Falabella | Sodimac |
|---|---|---|---|
| `Event` en la landing | 4 bloques (TV, laptops, celulares, electrohogar) con `startDate`/`endDate` y `Offer` | 1 | 1 (con `@id`) |
| `FAQPage` en la landing | 12 preguntas | 10 | 15 |
| `CollectionPage` / `ItemList` | Sí, pero `ItemList` con **1 solo producto** | `ItemList` en PLP | `ItemList` en PLP |
| `BreadcrumbList` | **No** (ni landing ni PDP) | PLP y PDP | Landing, PLP y PDP |
| `WebSite` / `WebPage` / `OnlineStore` | — | — | Sí (`OnlineStore` repetido 2 veces) |
| `SpecialAnnouncement` | No | No | No |
| `Product` + `Offer` en PDP | Sí: `brand`, `mpn` (modelo), `price`, `availability`, `priceValidUntil`, `priceSpecification` (SalePrice) | Sí: `brand`, `sku`, 2 `Offer` (precio normal y oferta), `availability`, `seller`, **`aggregateRating` (4.7, 185 reseñas)** y 5 `Review` | Igual que Falabella (`aggregateRating` 4.5, 176 reseñas) |
| GTIN | No | `"gtin13":"null"` (texto, inválido) | `"gtin13":"null"` |

Errores COMPROBADOS en el marcado de los competidores (útiles para no repetirlos):
- Hiraoka: `Event.description` dice "del 02 **al 50** de Noviembre"; el `Offer` del evento tiene `price: 0` y `validFrom` igual al último día; en la laptop Lenovo `priceValidUntil` es **2026-10-19** (vencido el día de la revisión); en la TV Hisense el campo `description` del Product trae CSS y un `<script>` de un tercero.
- Falabella/Sodimac: dos `Offer` sueltos con precios distintos sin decir cuál es el tachado (Google puede tomar el mayor o el menor); `gtin13` como texto "null"; en Sodimac la `description` del Product es HTML escapado.
- **`SpecialAnnouncement` no lo usa nadie y no conviene usarlo**: Google lo creó para avisos de COVID-19 y ya no lo muestra. Para un evento comercial lo correcto es `Event` (aunque Google tampoco garantiza rich result de eventos de venta) y, sobre todo, `Product`/`Offer` bien hechos en las fichas.

**Ventaja real de Falabella y Sodimac:** `aggregateRating` con cientos de reseñas → estrellas en resultados orgánicos y en Shopping. Hiraoka no tiene reseñas en el marcado. SIN DATO sobre EFE/LC en este punto (revisar).

### 3b. Títulos de producto para Shopping (pestaña orgánica)

| Sitio | Ejemplo de título | Estructura |
|---|---|---|
| Hiraoka | `Televisor Hisense Smart TV 55" Hi-QLED 4K UHD 55QD5SV` | Tipo + marca + tamaño + tecnología + resolución + modelo |
| Hiraoka | `Laptop Lenovo IdeaPad Slim 3 de 15.6", AMD Ryzen 5 7520U, 16GB RAM, disco sólido de 512GB, modelo 82XQ00LYLM + Maletín` | Tipo + marca + línea + specs + modelo + bundle |
| Falabella | `Televisor Smart TV TCL 55" 4K QLED Google TV 55T6C` | Tipo + marca + tamaño + resolución + panel + SO + modelo |
| Sodimac | `Televisor Caixun LED 43" Full HD Roku TV C43V1FR` | Igual |

Los tres siguen la fórmula **tipo + marca + atributo clave + modelo**. **Ninguno mete "oferta", "Cyber" o "% dscto" en el título del producto**, y está bien: la política de Merchant Center prohíbe texto promocional en el título. La oferta se comunica con `sale_price` + `sale_price_effective_date` en el feed y con Promociones de Merchant Center (insignia de oferta en Shopping). Lo que el usuario pidió ("marca + modelo + atributo de oferta") aplica al **title HTML de la landing y de las PLP**, no al título del producto.

Como nadie tiene GTIN válido en el HTML, el **GTIN en el feed y en el schema** es una diferencia que EFE/LC pueden ganar (mejor emparejamiento en Shopping). HIPÓTESIS hasta revisar el feed en Merchant Center.

---

## 4. Captura y retención (CRO + SEO)

### 4a. Stock bajo o agotado

| Sitio | Qué hace | Fuente |
|---|---|---|
| Falabella / Sodimac | Disponibilidad por canal: "Sin stock en tienda", "No disponible para retiro en tienda", "Producto sin stock :(" + **"Prueba buscando otros productos en..."** (manda a alternativas, no deja al usuario en un callejón). La PDP sigue en 200 e indexable. Sodimac usa "Últimas unidades" como sección del menú y "El stock es limitado" en la meta de todas las PDP | COMPROBADO (textos de la app en el HTML) |
| Sodimac (landing) | "no esperes a que llegue la última fecha porque **el stock de productos con oferta es limitado**" | COMPROBADO |
| Hiraoka | No se vio texto de agotado ni de stock bajo en el HTML servido. `availability: InStock` en el schema | SIN DATO (puede pintarse por JavaScript) |

### 4b. Urgencia e incentivos

| Mecanismo | Hiraoka | Falabella | Sodimac |
|---|---|---|---|
| Contador regresivo | Widget propio en la plataforma (`Hiraoka_Countdownwidget`, tipo `countdown_offer`) cargado en landing, PLP y PDP; **sin instancia activa en la landing el 20-oct** | SIN DATO (no visto en el HTML) | SIN DATO |
| Insignias en el listado (PLP) | SIN DATO | `badges` por producto: **"Llega mañana"**, **"Retira mañana"**, **"Retira hoy"** | Las mismas + "Retira desde 120 min" + **insignia de evento** ("HOT SALE", fondo azul) en ~36 de 50 productos |
| Descuento % | "Hasta 50% dscto" en title y meta | `-%` en las fichas | `-%` en las fichas |
| Medio de pago propio | Interbank / Izipay / PagoEfectivo (landings `/interbank`, `/promociones-interbank`) | **CMR** (184 menciones en la landing), "cuotas sin intereses" | CMR, "6 cuotas sin intereses" en menú |
| Captura de datos | Newsletter "beneficios exclusivos" | **"Regístrate para este CyberWow o actualiza tus datos"** (formulario en la landing antes del evento) | — |
| Despacho como argumento | "retiro en tienda o envío a domicilio" en el FAQ | "Envío gratis", "Retiro en tienda" | "envío gratis o en **120 minutos**" en la caja de datos clave |

**Lo más fuerte que hacen y que se ve en el código:** las insignias de **velocidad de entrega** por producto (Llega mañana / Retira hoy) y la insignia de evento en el listado se manejan como datos del producto (`badges` en el JSON de Next.js), no como imágenes de banner. Se encienden y apagan por campaña sin tocar la plantilla. Ojo: en Sodimac la insignia "HOT SALE" seguía activa el 20-oct, a dos semanas del Cyber (o es una campaña propia en curso o se quedó prendida).

---

## 5. Qué significa para EFE y La Curacao

Comparado con `docs/02`, la brecha más grande **no es de contenido sino de base técnica**: los competidores tienen una URL fija por evento con canonical, y EFE/LC tienen varias URLs por evento, landings sin canonical (EFE) o con canonical roto (LC `/cyber-days` → `/cyber-Days` → 301 de vuelta) y metadatos de otra edición.

Acciones sugeridas, en el orden en que conviene evaluarlas con Elias (`docs/04`). **Ninguna lleva estimación de ventas**; el efecto se mide en GSC por URL (impresiones y clics de "cyber wow" + marca) contra la edición anterior.

**Antes del congelamiento (~30-oct), solo cambios de CMS sin riesgo:**
1. **Una URL por evento por sitio**, la que más enlaces/impresiones tenga en GSC (HIPÓTESIS: `/cyber-wow`). Title con "Cyber Wow 2026", fechas "2 al 5 de noviembre" y un disparador; H1 visible y único; quitar textos de julio. Sin redirecciones durante el evento (regla de `ESTADO.md`); las demás URLs se consolidan después de Cyber.
2. **Enlace fijo a la landing en el footer o menú** de todo el sitio (como Falabella y Sodimac), no solo en el banner.
3. **Bloque de texto + FAQ visible** en la landing con las búsquedas del evento (cuándo es, cuánto dura, cómo recoger, cuotas, despacho) y bloques "Cyber Wow Televisores / Refrigeradoras / Lavadoras / Motos" que enlacen a las PLP de siempre.
4. Agregar "envío gratis / retiro en tienda / cuotas" al title o meta donde aplique, solo si es cierto para todo el surtido (requiere validar con comercial; si no, no ponerlo).

**Durante el evento:**
5. Insignia de evento y de despacho en el listado si la plataforma lo permite sin desarrollo (Magento: etiquetas de producto). SIN DATO sobre la capacidad actual de EFE/LC.
6. Agotados: la PDP sigue en 200 con alternativas de la misma categoría; nunca 404 ni redirección en plena campaña.

**Después del evento (noviembre-diciembre):**
7. Schema de PDP completo: `brand`, `gtin` real, `priceValidUntil` vigente, `priceSpecification` para el precio tachado, `BreadcrumbList`, y `aggregateRating` si hay reseñas reales.
8. Landings por atributo que la competencia ya tiene y EFE/LC no (validar con GSC/Keyword Planner antes): tamaño de TV, combos, rango de precio, y para EFE/LC lo propio: **"en cuotas sin tarjeta" / crédito Efectibank** (ningún competidor puede usarlo y conecta con `docs/08`).
9. Merchant Center: `sale_price` con fechas y Promociones para la insignia de oferta en Shopping, en vez de texto promocional en el título.

## 6. Pendientes de esta revisión
- Ripley: abrir en navegador normal y completar la tabla (Carol).
- Repetir la revisión el **2-nov** (primer día) para ver los titles en modo evento, contadores e insignias activas, y el **6-nov** para ver qué hacen con la landing al cerrar.
- Revisar EFE y LC con el mismo método (title, H1, schema de PDP, reseñas, insignias) para tener la tabla lado a lado.
