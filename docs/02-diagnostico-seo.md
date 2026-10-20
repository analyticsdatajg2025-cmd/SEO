# 02 · Diagnóstico SEO por sitio

Última revisión: **16 oct 2026**. Dos fuentes: la revisión pública hecha en esta sesión (**W**) y la hecha por la sesión "SEO" el mismo día (**S**, artifact "Plan SEO Cyber 2026" y análisis de marcas). Nada de esto está validado en Search Console: **el HTML dice lo que el sitio declara, no lo que Google decidió.** Etiquetas: `COMPROBADO` (visto en el HTML), `HIPÓTESIS`, `SIN DATO`.

> Las prioridades y decisiones de la sesión "SEO" **no se adoptan aquí**: se evalúan con Elias en `docs/04`.

## 1. Conecta · Tiendas EFE (efe.com.pe) y La Curacao (lacuracao.pe) · Magento 2

| Hallazgo | Estado | Impacto | Fuente |
|---|---|---|---|
| `robots.txt` declara el sitemap como `Sitemap : https://...` (espacio antes de los dos puntos). Google suele tolerarlo, pero no está garantizado; en ambos sitios | COMPROBADO | Medio · verificar en GSC que el sitemap esté enviado a mano | W |
| Sitemap: índice de 9 archivos, **~99 K URLs** por sitio (99.210 EFE, 99.554 LC; 68 y 21 repetidas) contra ~17 K SKU en el feed. HIPÓTESIS: incluye productos sin stock, descontinuados o variantes | COMPROBADO conteo | Medio · presupuesto de rastreo; no depurar antes de Cyber | S, feeds |
| **Tiendas EFE sin `canonical`** en home, landings Cyber, categorías y fichas | COMPROBADO | Alto · Google puede elegir variantes con parámetros | S |
| **La Curacao**: canonical de `/cyber-days` apunta a `/cyber-Days`, que redirige (301) de vuelta | COMPROBADO | Medio · arreglo de minutos en CMS | S |
| Landings Cyber con metadatos sucios: título "Del 06 al 10 de Julio", H1 oculto, varias `<title>` por página (HTML completo pegado en el CMS) | COMPROBADO | Alto en Cyber | S |
| Varias URLs por evento (`/cyber-days`, `/efe/cyberdays.html`, `/previa-cyber`, `/cyber-wow`), todas 200 y en sitemap | COMPROBADO · canibalización HIPÓTESIS | Medio | S |
| **Páginas de Tiendas EFE indexables dentro de skullcandy.com.pe y motocorp.pe** (ej. "Cyber wow 2026 \| Tiendas EFE" en Skullcandy; `motocorp.pe/home-6424...` con título "Tiendas EFE"). Probable asignación de páginas CMS a "todas las tiendas" en Magento | COMPROBADO | Alto · contenido duplicado entre dominios y señales de marca mezcladas | S |
| Home: sin JSON-LD visible (Organization/WebSite sí en Motocorp y Skullcandy, que comparten plataforma); sin canonical ni hreflang; H1 ok ("Tiendas EFE: Tecnología y Electrodomésticos Online") | COMPROBADO parcial | Medio | W |
| Ficha de producto (muestra EFE): sin reseñas/AggregateRating, sin breadcrumb visible, descripción ~100 palabras con errores ("con el con el", "Tipo de refrigeradora: Industrial" en un termoradiador, cobertura 30 m² vs 15 m²), título repetido 3 veces. Precio y stock sí; "Disponible retiro en tienda" depende de la ubicación. **Sin texto de cuotas/financiamiento** en la ficha, solo enlace "Evalúa tu crédito Efectiva" | COMPROBADO | Alto · calidad de catálogo y rich results; puente al crédito perdido | W |
| Las tres webs retail enlazan al dominio viejo `efectiva.com.pe`; el enlace del footer a la línea ética termina en 404 | COMPROBADO | Bajo-medio | S |
| Navegación con errores: "Equipamento Gastronómico", "C modas y Tocadores", slug `camas-box-tarina`; categorías repetidas en el menú | COMPROBADO | Bajo | W |
| **Localizador de tiendas**: una sola página `/localizador-tiendas/`, sin URL por tienda, datos cargados por JS (HTML vacío: "Dirección: , ,"), sin schema `Store`/`LocalBusiness`; el footer dice "200 tiendas y puntos de retiro" pero lista 11 ciudades que apuntan a la misma URL | COMPROBADO | **Alto para SEO local**: Google no tiene una página por tienda que indexar | W |
| `/pagina-que-no-existe` responde 404 con título de búsqueda; ok | COMPROBADO | — | S |
| Venta web: LC orgánico 12% vs EFE 23% con la misma plataforma y catálogo similar → brecha de ~S/ 5 M/año si LC llegara al 20% (escenario, no proyección) | Datos F1 | Alto | S, F1 |
| EFE: Search -31% y PMax +64% → HIPÓTESIS de canibalización de búsquedas de marca por PMax (se paga lo que el orgánico ya gana) | HIPÓTESIS | **Alto en dinero neto** (ahorro de pauta) | S, F1 |

## 2. Juntoz (juntoz.com) y malls · Next.js

Restricción operativa: las plataformas de Juntoz, Diners Club Mall y BanBif Mall tienen **accesos y funciones de CMS en implementación**. Por eso cada hallazgo lleva además: qué puede hacer SEO hoy, qué depende de desarrollo y qué requiere habilitar el CMS.

| Incidencia reportada o detectada | Estado | Hoy desde SEO | Desarrollo | CMS |
|---|---|---|---|---|
| Sin sitemap; robots sin `Sitemap:` | COMPROBADO (404 en raíz; sin GSC no se sabe si hay uno enviado con otra ruta) | Verificar en GSC; especificar contenido (categorías, landings, fichas con stock) | Generar y mantener el sitemap | — |
| Sin canonical (Juntoz, Diners); doble barra en BanBif; mismas fichas `/p/…` en 3 dominios | COMPROBADO en muestra; duplicidad entre dominios HIPÓTESIS hasta ver GSC | Inspeccionar en GSC qué dominio rankea cada ficha; proponer regla con socios | Implementar canonical por dominio | — |
| URLs no amigables | **PENDIENTE DE VERIFICACIÓN** (reportado; no se midió el alcance) | Inventario por muestra | Reescritura y redirecciones (después de campañas) | — |
| Problemas de rastreo e indexación | PENDIENTE DE VERIFICACIÓN (sin GSC); render JS de Next.js no revisado | Pedir GSC; muestra con render (sin herramienta de pago es limitado) | Pre-render/SSR si hiciera falta | — |
| Sin `Product` JSON-LD; título con el vendedor delante; home sin H1 | COMPROBADO en muestra | Especificar plantilla | Cambiar plantillas de ficha y home | — |
| Limitación para crear landings SEO y editar páginas transaccionales | CONFIRMADO por el equipo | Solo metadatos donde el CMS lo permita | — | **Habilitar edición de títulos, descripciones, H1 y creación de landings** |
| Landing Cyber "cyberdays" y cupones con metadatos pobres; cupones bancarios no enlazados | COMPROBADO | Cambiar metadatos si el CMS lo permite; inventario de cupones con GSC | — | Edición de metadatos |

**No se asume que se puedan crear y posicionar landings nuevas en Juntoz en 90 días.**

| Hallazgo | Estado | Impacto | Fuente |
|---|---|---|---|
| `robots.txt` sin `Sitemap:`; `/sitemap.xml` → 404 | COMPROBADO | Medio-alto · descubrimiento de 42 K SKU y categorías depende de enlaces | W, S |
| Home **sin H1**; secciones con H3 ("Cupones para ti", "Lo más caliente") | COMPROBADO | Medio | W |
| Sin canonical declarado (Juntoz y Diners); BanBif con doble barra `banbifmall.pe//p/…` | COMPROBADO | Alto · las **mismas fichas `/p/...` indexables en 3 dominios** (Juntoz, Diners, BanBif) | S |
| Fichas sin datos estructurados `Product`; título con el vendedor delante ("NEOSHOP IMPORTACIONES - IPHONE 17…") | COMPROBADO muestra | Medio-alto · sin rich results de precio, CTR bajo | S |
| `/categoria/tecnologia` → 404 (la estructura de URLs de categoría no es la supuesta; mapear) | COMPROBADO | — | W |
| Landing Cyber `/contenido/cyberdays-604` con título/H1 "cyberdays"; página de cupones repite el título de la home; cupones bancarios (Scotiabank, BBVA, BCP) no enlazados desde la home | COMPROBADO | Medio | S |
| Negocio: 83% de la meta de sesiones, orgánico sin dato por canal; "Efectibank" aparece como categoría del menú | F2, W | — | |

## 3. Motocorp (motocorp.pe) · Magento 2

| Hallazgo | Estado | Impacto | Fuente |
|---|---|---|---|
| Robots sin bloqueos raros; sitemap `sitemap_motocorp.xml` con 842 URLs; `INDEX,FOLLOW`; home con Organization/WebSite/SearchAction; categoría motos con `CollectionPage` + `ItemList`; fichas con `Product` + `Offer` + `BreadcrumbList` | COMPROBADO | Buena base técnica | S |
| Home y categorías **sin H1**; ficha Bajaj con meta description que es un legal ("Precio referencial para Lima…") | COMPROBADO | Medio | S, W |
| Talleres: `/servicios/nuestros-talleres.html` con título "Workshops" y redirección; localizador sin páginas por tienda ni por taller; "22 tiendas de retiro" | COMPROBADO | **Alto para SEO local** (tiendas + talleres = servicio de alto margen) | S, W |
| Crédito: "Evalúa tu Crédito Efectibank" y "Evalúa tu Crédito Efectiva" conviven; simulador `/creditsimulator/`; la página de préstamo de motos de Efectibank **no está enlazada desde las fichas** | COMPROBADO | Alto en margen (puente al crédito) | S, W |
| WhatsApp `wa.me/51987654321` parece placeholder; contadores "00HRS 00MIN"; link Mavila con `%20`; alt genéricos "slide" | COMPROBADO | Bajo-medio (leads perdidos si el número es falso) | W |
| 51% del tráfico ya es orgánico; 165 K sesiones/mes; la web es canal de leads (KPI = leads, no venta web) | F1 | — | |

## 4. Efectibank (efectibank.pe) · WordPress + Elementor + Yoast

Detalle completo página por página en `docs/08 §3`. Resumen:

| Hallazgo | Estado | Impacto | Fuente |
|---|---|---|---|
| Título de la home solo "Efectibank"; sin H1 identificable; headings repetidos ("Paga online desde tu app" x2) | COMPROBADO | Medio-alto · CTR en la consulta de marca y en "banco digital" | W, S |
| Sitemap Yoast: 229 páginas, **129 son promociones**, 9 préstamos, 12 seguros, 2 ahorros; `/test/` indexable; "Términos y condiciones María" indexable | COMPROBADO | Medio · dilución; limpiar | S |
| Páginas de préstamo con canonical correcto y `FAQPage`; H1 de marketing ("Tu familia ya tiene casa propia") sin la palabra clave | COMPROBADO | Medio | S |
| Naming inconsistente: "Cuenta de Ahorros Digital" vs "Cuenta de Ahorros Efectiva"; `mailto` a `efectiva.com.pe`; enlaces internos con UTM largos (duplican URLs) | COMPROBADO | Bajo-medio | W |
| Apps: Android **2.6★** (1.02 K reseñas, 500 K+ descargas), iOS **3.1★**; reseñas recientes: se queda en el splash tras el rebrand | COMPROBADO (tiendas de apps) | **Alto**: la calificación frena la instalación desde búsquedas "efectibank app" y la conversión a 100% digital | W |
| Páginas de producto: H1 de eslogan sin palabra clave; sin montos ni TEA (solo PDF); contradicciones (desgravamen incluido/opcional; dos tablas de tasas en depósito); enlaces a `localhost`, SafeLinks y staging `qa2.efectiva.com.pe`; retailers del grupo mencionados sin enlace | COMPROBADO | Alto · conversión y relevancia | W |
| `/solicitar-prestamo/` es un formulario de contacto con callback, no una solicitud online; `/agencias/` es una sola página sin las 176 oficinas; `/blog/` sin artículos | COMPROBADO | Alto · 176 oficinas invisibles; sin contenido | W |
| Negocio: el de mayor margen del grupo (utilidad neta S/ 95.6 M en 2025); quiere ser 100% digital; **ningún dato de solicitudes de crédito por canal** | M25, A1 | — | |

## 5. Skullcandy (skullcandy.com.pe), Coldex (coldex.pe), Diners/BanBif

- Skullcandy: página `/service-unavailable` con título "503 Service Unavailable" indexable y en sitemap; landings de EFE dentro del dominio; `<title>` de la home en inglés; 148 URLs. Negocio: < S/ 40 K/mes, margen ~42%, conversión 0.6% (COMPROBADO/F1).
- Coldex: WordPress B2B, "vende poco"; no revisado a fondo (A2).
- Diners Club Mall / BanBif Mall: tráfico que llega por el banco, no por Google; Diners -27% y sesiones -24% en T3; cualquier cambio de canonical frente a Juntoz debe cuidar al socio (S, F2).

## 6. Transversal

| Tema | Estado |
|---|---|
| **Search Console**: el equipo SEO no tiene acceso a ninguna propiedad | SIN DATO (bloqueo principal) |
| **GA4**: existe por marca; sin exportes de orgánico por página de entrada para el equipo SEO | SIN DATO |
| **Google Business Profile**: sin acceso; sin maestro oficial de tiendas/oficinas/talleres | SIN DATO |
| **Herramientas**: sin Keyword Planner (lo da la cuenta de Google Ads), sin rastreador (Screaming Frog) | SIN DATO |
| **Apps Conecta** (EFE, LC, Juntoz) con instalador y CR ~1%: sin datos de instalaciones, retención ni venta por app | SIN DATO |
| Fecha oficial del Cyber Wow de noviembre | 2–5 nov 2026 (prensa; confirmado en las landings de Hiraoka, Falabella y Sodimac el 20-oct, `docs/10`) |
