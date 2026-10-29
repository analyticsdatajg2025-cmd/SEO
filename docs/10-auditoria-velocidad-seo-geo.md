# 10 · Auditoría de velocidad, SEO y GEO por tienda

Medición: **29 oct 2026**. Dashboard: [Salud web de tiendas EFE](https://claude.ai/artifact/QyjQU1iq1wZ1wzFy7Y1KaF) (privado; compartir desde el menú Share).

**Método.** La API de PageSpeed Insights sin clave devolvió 429 (cuota compartida agotada). Se corrió **Lighthouse 12.6.1** (el mismo motor de PSI) con el perfil móvil de PSI, una corrida por URL, en 20 URLs de 9 tiendas, más escritorio en las 9 portadas. Es dato de **laboratorio**: varía ±10 puntos entre corridas y no reemplaza los datos de usuarios reales (CrUX / informe de Core Web Vitals en GSC). HTML y `robots.txt` leídos el mismo día. Etiquetas como en `docs/02`.

## 1. Velocidad (móvil) · COMPROBADO en laboratorio

| Tienda | Portada: rendimiento · LCP · peso | Categoría | Ficha / producto |
|---|---|---|---|
| Tiendas EFE | 29 · 7,0 s · 25,3 MB | 27 · 11,1 s | 21 · 5,4 s |
| La Curacao | 28 · 8,0 s · 16,5 MB | 34 · 4,4 s | 19 · 7,4 s |
| Motocorp | 29 · 12,1 s · 17,5 MB (1.282 peticiones) | 32 · 4,4 s | 29 · 4,8 s |
| Skullcandy | 12 · 15,6 s · 14,4 MB (CLS 0,51) | 56 · 3,7 s | 21 · 8,2 s |
| Juntoz | 35 · 7,0 s · 13,5 MB | — | 46 · 4,4 s |
| Diners Club Mall | 25 · 9,3 s · 10,9 MB | — | — |
| BanBif Mall | 25 · 32,9 s · 11,7 MB | — | — |
| Efectibank | 34 · 5,1 s · 6,0 MB | — | Préstamo motos 39 · 6,6 s; efectivo 40 · 6,6 s |
| Coldex | 27 · 15,9 s · 4,6 MB | — | — |

- **Las 20 páginas móviles están bajo 60**; 19 de 20 bajo 50. Mediana de LCP móvil muy por encima de los 2,5 s que pide Google.
- **Google Tag Manager es el tercero que más bloquea en las 20 páginas** (0,5 a 3,4 s de bloqueo). Siguen HubSpot, Facebook y Clarity en Magento.
- **Imagen principal en carga diferida (lazy)** en 9 de 20 páginas: se pide tarde justo la imagen que define el LCP.
- **Portadas muy pesadas**: 11 a 25 MB en las tiendas y malls; HTML de 1,2 a 1,7 MB en EFE, La Curacao, Diners y BanBif (cientos de imágenes y JSON incrustado).
- Servidor sano en casi todo: respuesta del servidor bajo 0,3 s en EFE, La Curacao, Motocorp, Juntoz, Diners y Efectibank (Magento con Fastly + Brotli). Excepciones: Skullcandy portada y ficha ~0,66 s, BanBif ~0,6 s, Coldex ~1,3 s. El cuello de botella principal es el **front**, no el hosting.
- SEO de Lighthouse 75-100: lo básico pasa; el problema de negocio es la carga.

## 2. SEO en el HTML · COMPROBADO

- **Canonical**: solo la portada de La Curacao lo declara entre las 16 URLs de Magento y Next.js; Efectibank y Coldex sí (Yoast/Rank Math). Confirma `docs/02 §1`.
- **H1**: sin H1 en las portadas de Motocorp, Skullcandy, Juntoz, Diners, BanBif, Efectibank y Coldex; fichas con 2 a 6 H1 (La Curacao 6).
- **Datos estructurados**: Magento ya trae Organization/WebSite en portadas (incluida EFE: **corrige** `docs/02 §1`, que decía "sin JSON-LD") y Product/Offer/Breadcrumb en fichas; **Juntoz y malls, ninguno**. Sin AggregateRating en ninguna ficha.
- Ficha Motocorp sin meta descripción; Skullcandy con títulos de 11-14 caracteres ("Auriculares", "Hesh 360 White") y la misma meta descripción en categoría y ficha.
- Ficha La Curacao con dos `<title>`.

## 3. GEO (buscadores con IA) · COMPROBADO

- Ningún sitio bloquea bots de IA (GPTBot, ClaudeBot, PerplexityBot, Google-Extended): pueden leer y citar.
- **Ninguna Organization tiene `sameAs`** (salvo Coldex): los motores de IA no enlazan la marca con sus redes ni perfiles.
- **Efectibank** no se declara como entidad financiera (solo WebSite; sin Organization ni FinancialService) y la **TEA no aparece en el HTML** de las páginas de préstamo: una IA no puede responder "¿cuánto cobra Efectibank?" desde su web.
- Magento sirve `/llms.txt` vacío con código 200; `robots.txt` con `Sitemap :` (espacio). Malls sin sitemap en robots.

## 4. Acciones propuestas (para evaluar con Elias)

Nada durante el congelamiento de Cyber Wow (30 oct – 5 nov). Sin estimación de ventas hasta tener GSC y CrUX.

| # | Acción | Tiendas | Quién | Cuándo |
|---|---|---|---|---|
| 1 | Imagen principal sin lazy y con `preload`/`fetchpriority=high` | EFE, LC, Motocorp, Skullcandy, BanBif, Coldex | TI Magento / plataformas | Desde 6-nov, con staging |
| 2 | Auditoría de GTM: retirar etiquetas sin uso, diferir chat, mapas de calor y píxeles | Todas | Martech + Paid + TI | Inventario ya; cambios post-Cyber |
| 3 | Portadas más livianas: menos banners/carruseles bajo el primer pantallazo, WebP/AVIF al tamaño mostrado | EFE, Motocorp, LC, Skullcandy, Juntoz, malls | Marketing (CMS) + TI | Post-Cyber |
| 4 | Canonical autorreferente en categorías y fichas | Magento y Juntoz/malls | TI / plataforma | Post-Cyber, con reversión (`docs/04` 1.6) |
| 5 | Un H1 por página | 7 portadas + fichas | Marketing / plataforma | Post-Cyber |
| 6 | Organization con `sameAs`; FinancialService en Efectibank | Todas menos Coldex | SEO spec + TI | Noviembre |
| 7 | Product/Offer/Breadcrumb y sitemap en Juntoz y malls | Juntoz, Diners, BanBif | Plataforma Juntoz | Según CMS (`docs/02 §2`) |
| 8 | Monto, plazo, TEA y requisitos en texto en préstamos | Efectibank | Marketing Efectibank + Legal | Noviembre (`docs/08`) |
| 9 | `Sitemap:` sin espacio; `llms.txt` con contenido o 404 | Magento | TI | Post-Cyber |
| 10 | `alt` en banners y productos | Varias | Marketing (CMS) | Continuo |

## 5. Lo que falta para medir de verdad
- **Clave de API de PageSpeed** (Google Cloud, gratuita) para datos de campo CrUX por URL y origen, y para repetir la medición en forma automática.
- **GSC** (informe de Core Web Vitals por grupo de URL): sin él no se sabe qué ve Google en usuarios reales (`docs/06`, acceso A1).
- Repetir la medición 3 veces por URL tras cada cambio y anotar en el registro de cambios (`docs/04` 1.2).
