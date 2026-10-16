# 04 · Plan de acciones SEO · 90 días (17 oct 2026 → 15 ene 2027)

Última revisión: 16 oct 2026. **Propuesta para evaluar con Elias.** Las acciones de la sesión "SEO" (plan Cyber) están integradas como insumo; no se dan por aprobadas.

Convenciones: **Neto** = estimación de ganancia neta incremental en 12 meses, con el supuesto escrito al lado; `SIN DATO` cuando no se puede estimar sin la información de `docs/06`. Esfuerzo en días-persona (K = Kevin, C = Carolina, E = Elias). Ventanas: **Cyber Wow** (~2-5 nov, congelar cambios 72 h antes), **Navidad** (dic), **calor/El Niño** (nov-feb).

## 0. Lo que hace que el resultado sea "altísimo" o no
Con margen de producto ~10%, vender más por orgánico da dinero neto modesto en 90 días. Lo que puede ser grande rápido es: (1) **dejar de pagar pauta por búsquedas de marca** (neto al 100%), (2) **originar crédito** desde las páginas con intención (margen financiero), (3) **llegar sanos a Cyber Wow y Navidad**, donde un día vende 4x. Los tres dependen de datos que hoy no tenemos (términos de búsqueda de Ads, crédito por canal, GSC). **Primera semana = conseguir accesos y línea base.**

## 1. Semana 0-1 · Accesos, línea base y congelamiento (sin esto nada se puede medir)

| # | Acción | Quién | Esfuerzo | Neto | Depende de |
|---|---|---|---|---|---|
| 1.1 | Acceso **Search Console** (usuario completo) a LC, EFE, Juntoz, Diners, BanBif, Motocorp, Skullcandy, Efectibank, Coldex | E → K | 0.5 | habilita todo | TI / dueños de propiedades |
| 1.2 | **GA4** lector o exporte: orgánico por página de entrada y por día, 2025-2026, con días Cyber marcados; conversiones y venta | E → K | 1 | línea base | Martech |
| 1.3 | **Reporte de términos de búsqueda de Google Ads** (Search + PMax, por marca) ene-sep 2026: cuánta inversión va a consultas con "efe", "curacao", "juntoz", "motocorp", "efectibank" | E (cuenta Ads) → K | 1 | insumo de 2.1 | Paid |
| 1.4 | Exporte de **Google Business Profile** (todas las fichas) + maestro oficial de tiendas/oficinas/talleres con dirección, horario, teléfono | E → C | 1 | insumo de 4.x | Operaciones |
| 1.5 | Línea base por grupo de URL (landings Cyber, categorías clave, top 200 PDP, home) en GSC y GA4; registro de cambios (fecha, URL, antes/después, responsable) | K + C | 2 | medición | 1.1, 1.2 |
| 1.6 | Rastreo acotado (landings, categorías, top PDP) con Screaming Frog o script propio; cruce sitemap ↔ feed (17 K SKU vs 99 K URLs) | K | 2 | diagnóstico | — |
| 1.7 | Fecha oficial de Cyber Wow (IAB) y lista de URLs que usará Paid (no tocar ni redirigir) | E | 0.2 | evita roturas | Paid |

## 2. Conecta (La Curacao + Tiendas EFE) · 50% del esfuerzo

| # | Acción | Quién | Esfuerzo | Neto (estimación) | Ventana |
|---|---|---|---|---|---|
| 2.1 | **Pauta de marca vs orgánico**: con 1.3, medir cuánto de Search/PMax son consultas de marca que el orgánico ya gana en posición 1; proponer prueba controlada (excluir marca en PMax / negativar en Search en una marca o región 2 semanas) y medir venta total | K + E + Paid | 3 | **S/ 240-900 K/año** si 15-35% de ~S/ 280 K/mes de pauta Google es marca y se recupera la mitad por orgánico. HIPÓTESIS fuerte: validar con 1.3 | Después de Cyber (no tocar pauta en el evento) |
| 2.2 | **Landings Cyber limpias** (EFE y LC): canonical de `/cyber-days` en LC; títulos sin fechas pasadas; H1 visible; quitar HTML completo incrustado; una URL fija por evento y redirigir/retirar las repetidas **solo** si GSC muestra que no reciben impresiones | C (CMS) + K (GSC) | 2 | Protege ~25% de la venta web del año (Cyber). No cuantificable aparte | Antes del 30-oct |
| 2.3 | **Canonical en Tiendas EFE** (todo el sitio): inspeccionar 20 URLs en GSC; si Google elige variantes, activar canonical de Magento en staging y pasar a producción después de Cyber | K + TI | 3 | Protege el orgánico (+26%, S/ 7.6 M/año) | Staging antes, producción después de Cyber |
| 2.4 | **Páginas de EFE dentro de Skullcandy y Motocorp**: revisar asignación de páginas CMS por store view en Magento; dejar cada página en su tienda; 301 o noindex en las ajenas | K + TI | 1 | Higiene; evita duplicados entre dominios | Antes de Cyber |
| 2.5 | **Categorías de calor / El Niño** en LC y EFE: ventiladores, aire acondicionado, refrigeradoras, congeladoras, bombas de agua: título, H1, texto de categoría (150-300 palabras útiles), enlaces desde home y guías "cómo elegir"; verificar stock con Comercial | C (contenido) + K (schema) + Comercial | 4 | **S/ 15-60 K/año** neto (HIPÓTESIS: +S/ 0.3-1.2 M de venta web orgánica en la temporada, ×0.5 neta ×10%) | Publicar antes del 15-nov |
| 2.6 | **Datos estructurados** de producto (Product/Offer/AggregateRating cuando haya reseñas) y breadcrumbs en LC y EFE; revisar que precio y stock estén en el JSON-LD (Motocorp ya los tiene en la misma plataforma: replicar) | K + TI | 3 | CTR en fichas (rich results); sin dato de base | Después de Cyber |
| 2.7 | **Puente al crédito en la ficha**: texto de cuotas ("desde S/ X al mes con Efectibank") y enlace rastreable a la página de préstamo electro; corregir enlaces a `efectiva.com.pe` → `efectibank.pe` en las 3 webs | C + K + Efectibank | 2 | SIN DATO (depende del margen financiero y % de venta financiada) | Noviembre |
| 2.8 | Sitemap: depurar URLs sin stock/descontinuadas (cruce con feed y con `GITHUB_OBSOLETOS_CONECTA`); corregir `Sitemap :` en robots; enviar sitemaps en GSC | K + TI | 2 | Rastreo; sin dato de base | Después de Cyber |
| 2.9 | Calidad de fichas top 200 por venta (descripciones con errores, títulos triplicados) con el equipo de contenido | C + Contenido | 3 | Conversión; sin dato | Dic-ene |
| 2.10 | **La Curacao al 20% orgánico** (escenario S/ +5 M/año de venta web ≈ **S/ 250 K/año neto**): plan de 6 meses copiando lo que funciona en EFE; en 90 días solo se siembra (2.2-2.9) y se mide | K + C | continuo | Escenario, no proyección | — |

## 3. Efectibank · 15%

| # | Acción | Quién | Esfuerzo | Neto | Ventana |
|---|---|---|---|---|---|
| 3.1 | Título y H1 de la home y de las páginas de préstamo con la consulta ("Préstamo para electrodomésticos", "Préstamo para motos", "Banco digital"); FAQ reales; limpiar `/test/`, términos duplicados, 129 promociones (noindex a las vencidas) | C (WordPress/Yoast) | 2 | SIN DATO (pedir: solicitudes por canal, valor y margen por crédito) | Noviembre |
| 3.2 | **ASO de la app** (2.6★ Android, 3.1★ iOS): responder reseñas, ficha con palabras clave ("banco digital", "préstamo", "Yape/Plin"), capturas; escalar a Producto el bug del splash (sin arreglo técnico no sube la nota) | C + Producto app | 2 | Instalaciones desde búsqueda "efectibank app"; sin dato | Continuo |
| 3.3 | Enlaces desde Motocorp (fichas de motos → préstamo motos) y desde LC/EFE (fichas electro → préstamo electro) con texto de cuotas; medir clics y solicitudes por página de origen | K + Efectibank | 1 | **Potencialmente el mayor neto por visita** del grupo; SIN DATO | Noviembre |
| 3.4 | Páginas de **agencias** (`/agencias/`): una URL por oficina con NAP y horario; GBP de cada oficina | C | 3 | Local; sin dato | Dic-ene |

## 4. Motocorp · 15%

| # | Acción | Quién | Esfuerzo | Neto | Ventana |
|---|---|---|---|---|---|
| 4.1 | **SEO local**: página por tienda y por taller (22+), con NAP, horario, servicios, mapa, `AutoDealer`/`AutoRepair` schema; GBP de cada punto (categoría, fotos, reseñas, horario); corregir "Workshops" y redirección | C (GBP) + K (páginas) + TI | 5 | Leads y servicio de taller (alto margen). SIN DATO de leads | Nov-dic |
| 4.2 | H1 en home y categorías; meta description de fichas con beneficio (no el legal); WhatsApp real en el botón; contadores vencidos fuera | C | 1 | Leads; sin dato | Noviembre |
| 4.3 | Fichas con "Financia en 36 cuotas con Efectibank" y enlace al préstamo de motos + simulador (3.3) | C + K | 1 | Ver 3.3 | Noviembre |
| 4.4 | Contenido estacional: "moto para delivery", "qué moto comprar con S/ X al mes", mantenimiento post-lluvia (El Niño) | C | 2 | Leads | Dic-ene |

## 5. Juntoz y malls · 15% (depende del equipo Next.js)

| # | Acción | Quién | Esfuerzo | Neto | Ventana |
|---|---|---|---|---|---|
| 5.1 | **Sitemap** (categorías, landings, fichas con stock) y `Sitemap:` en robots; enviar en GSC | K + Plataforma | 2 (+dev) | Tráfico orgánico sin cupón: brecha de 17% en sesiones (meta). SIN DATO por canal | Antes de Cyber si dev puede; si no, después |
| 5.2 | **Canonical** por dominio y decisión sobre las fichas duplicadas en Juntoz/Diners/BanBif (canonical a Juntoz salvo acuerdo con socios); corregir doble barra de BanBif | K + Plataforma + E | 2 (+dev) | Protege a Diners (-27%) y a Juntoz | Después de Cyber |
| 5.3 | `Product` JSON-LD en fichas; título "Producto – Marca \| Juntoz" (vendedor al final); H1 en home | K + Plataforma | 2 (+dev) | CTR; sin dato | Dic |
| 5.4 | Landing Cyber y página de cupones con título/H1/descripción propios; inventario de páginas de cupones bancarios con impresiones (GSC) y pedidos; enlazarlas si rinden | C | 1 | Venta con cupón ya es 65%: no empujar más cupón, sí tráfico de marca | Antes de Cyber |

## 6. Higiene (Skullcandy, Coldex, Diners/BanBif) · 5%
- Skullcandy: noindex y fuera del sitemap `/service-unavailable`; sacar landings de EFE (2.4); título de la home en español. (C, 0.5 día)
- Coldex: revisión básica (robots, sitemap, títulos) cuando haya tiempo; es B2B y vende poco. (C, 1 día, enero)
- Diners/BanBif: no tocar indexación antes de hablar con los socios (5.2).

## 7. Apps Conecta (EFE, LC, Juntoz) con instalador · transversal
- Hoy el instalador convierte ~1%. Acciones SEO/ASO baratas: `Smart App Banner` (iOS) y `manifest.json` + "Add to Home Screen" bien configurados (hoy `/manifest.json` da 404 en EFE), deep links desde fichas a la app, enlaces a las tiendas de apps desde el footer con texto, fichas de Play/App Store con capturas y palabras clave. (K + C, 2 días). Neto: SIN DATO (pedir venta por app y retención).

## 8. Resumen de dinero neto estimable hoy (12 meses, con supuestos)

| Palanca | Rango | Confianza |
|---|---|---|
| Ahorro de pauta de marca (Conecta) | S/ 240-900 K | Baja hasta ver 1.3 |
| Categorías de calor / El Niño (Conecta) | S/ 15-60 K | Media |
| La Curacao al 20% orgánico (escenario a 6-12 meses) | ~S/ 250 K | Baja |
| Crédito originado (Efectibank) | SIN DATO (puede ser la mayor) | — |
| Leads y taller (Motocorp) | SIN DATO | — |
| Juntoz tráfico orgánico | SIN DATO | — |

Lo honesto: **con lo que hay hoy se puede justificar S/ 0.3-1.2 M/año netos**; que sea "altísimo" depende de Efectibank y de la pauta de marca, y para eso hacen falta los datos de `docs/06`.

## 9. Indicadores (semanal, Kevin; ejecutivo mensual, Elias)
- GSC: clics, impresiones, CTR y posición por grupo de URL (landings, categorías clave, PDP top, tiendas, préstamos).
- GA4: sesiones, conversiones e ingresos orgánicos por página de entrada; venta orgánica / venta web.
- Ads: inversión en términos de marca y su tendencia (2.1).
- Efectibank: solicitudes de crédito por página de origen (3.3).
- Motocorp: leads (formulario + WhatsApp) por canal y por tienda.
- GBP: llamadas, rutas, clics a web por tienda.
- Apps: instalaciones por fuente, calificación promedio.
- Salud técnica: 4xx/5xx en landings y categorías (monitor diario), URLs indexadas vs sitemap.
