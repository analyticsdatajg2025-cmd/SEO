# 04 · Roadmap SEO 360 · 90 días (17 oct 2026 → 15 ene 2027)

Última revisión: 16 oct 2026 (v3: 360 con Efectibank primero, por mes, con horas, dependencias, bloqueos y resultados observables). **Propuesta para evaluar con Elias.** Etiquetas: `CONFIRMADO` · `HIPÓTESIS` · `ESTIMACIÓN` (con supuesto escrito; no es compromiso) · `SIN DATO`.

Equipo: **Josh Kevin (SEO Senior, "JK")**, **Carol (asistente SEO, "C")**, **Rolando y Ronald (Contenidos, "RR")**, apoyo de **Claude Pro** para análisis, borradores, especificaciones y scripts. Capacidad y reservas en `docs/09` (JK ~24-28 h/semana netas; C ~25-35; RR por confirmar). Nadie dedicado a una sola marca.

## 0. La tesis 360 en tres líneas
1. **El margen del grupo está en el crédito**: una venta financiada deja 25-55% más neto que la misma venta sin crédito; una moto financiada, hasta el doble (`docs/08`). El SEO se mide en ventas **y en créditos originados**.
2. **Lo urgente es Cyber** (2-5 nov, prensa) y **lo importante es Efectibank**; las dos corren en paralelo porque usan recursos distintos (Cyber = CMS Magento + GSC; Efectibank = WordPress + datos + Legal).
3. **Si El Niño es fuerte**, el despacho falla y la demanda se desplaza: el retiro en tienda, las oficinas de crédito dentro de las tiendas y el crédito de reposición son la defensa. Por eso las páginas de tienda/oficina y el puente al crédito no se postergan a 2027.

## 1. Mes 1 · 17 oct → 15 nov · "Llegar sanos a Cyber y arrancar Efectibank"

Ventanas: cambios de CMS hasta el **30 oct**; congelamiento SEO 72 h antes de Cyber Wow; durante el evento solo monitoreo e incidencias críticas. Nada estructural (`docs/09 §3`).

| # | Acción | Quién · horas (`ESTIMACIÓN`) | Depende de | Bloqueo | Resultado observable al cierre del mes |
|---|---|---|---|---|---|
| 1.1 | **Accesos**: GSC (9 propiedades), GA4 lector, reporte de términos de Ads, exporte GBP + maestro de tiendas/oficinas, admin WordPress de Efectibank (lectura), contacto plataforma Juntoz | Elias 2 h · JK 4 h | TI, Paid, Operaciones, Efectibank | Sin GSC no se confirma nada | Lista de accesos con fecha de entrega; línea base creada |
| 1.2 | **Línea base y registro de cambios**: grupos de URL en GSC (landings Cyber, categorías clave, top 200 PDP, préstamos, tiendas), segmento orgánico en GA4, hoja de cambios (fecha, URL, antes/después, responsable) | JK 8 h · C 6 h | 1.1 | — | Línea base ene-sep 26 y Cyber jul-26 documentada |
| 1.3 | **Landings Cyber limpias (LC y EFE)**: canonical de `/cyber-days` (LC), títulos sin fechas pasadas, H1 visible, retirar HTML incrustado, una URL por evento (sin redirigir nada activo en pauta), enlaces desde home a 5-8 categorías con stock | C 8 h (CMS) · JK 4 h (revisión) · Marketing 4 h · Comercial 1 h | Lista de URLs de Paid (1.5); categorías con stock | Marketing sin tiempo de CMS | Antes del 30-oct: landings con título/H1 correctos, inspección en GSC "indexada, canonical = declarado" |
| 1.4 | **Monitoreo Cyber**: script diario (Claude + JK) de códigos de respuesta, canonical, `noindex` y sitemap accesible en ~300 URLs clave; alerta por correo | JK 4 h setup · 0.5 h/día en el evento | — | — | 0 incidencias sin detectar en <24 h durante Cyber |
| 1.5 | **Congelamiento y coordinación con Paid**: lista de URLs en anuncios; fecha oficial IAB; no tocar pauta de marca en el evento | JK 2 h · Paid 1 h | Paid | — | Lista firmada; congelamiento desde el 30-oct |
| 1.6 | **Diagnóstico (no cambio) del canonical en EFE**: inspección de 20 URLs en GSC; especificación para TI con plan de reversión | JK 6 h | 1.1 | Sin GSC se difiere | Spec lista para la semana post-Cyber |
| 1.7 | **Páginas de EFE dentro de Skullcandy/Motocorp**: inventario (script) y pedido a Marketing/TI de reasignar store views o `noindex` | JK 3 h (Claude lista URLs) | Admin Magento | — | Lista de URLs cruzadas y ticket abierto |
| 1.8 | **Efectibank · auditoría inicial** (`docs/08 §3`): rastreo de las 229 páginas (SF gratuito), mapa de intenciones (préstamo efectivo/electro/motos, ahorro, plazo, oficinas), SERP de competencia a mano, errores: `localhost`, SafeLinks, staging en formulario, tablas de tasas contradictorias, `/test/`, 129 promociones | JK 16 h (Claude: cruce de sitemap, borradores) | 1.1 (GSC/GA4 de Efectibank) | Sin GSC: solo externa | Informe de auditoría con hallazgos `COMPROBADO`/`HIPÓTESIS` y lista de correcciones priorizadas |
| 1.9 | **Efectibank · pedido de datos EF1-EF9** (`docs/08 §5`) y reunión con Comercial/BI/Legal (mostrar TEA y cuota en página; sección blog; páginas por oficina) | Elias 2 h · JK 3 h | Efectibank | Decisión de Legal sobre TEA | Respuestas EF1-EF9 o fecha comprometida |
| 1.10 | **Efectibank · correcciones de higiene y producto (WordPress)**: enlaces rotos, nombres únicos, títulos y H1 con producto + beneficio en las 4 páginas que venden (efectivo, electro, motos, ahorro) + depósito; FAQ con schema; noindex a promociones vencidas y `/test/` | C 10 h (con supervisión) · JK 4 h · Marketing Efectibank 4 h · Legal 2 h | 1.8, 1.9 | Admin WordPress | Páginas corregidas y reinspeccionadas en GSC |
| 1.11 | **Juntoz · lo que el CMS permita antes de Cyber**: título/H1/descripción de la landing Cyber y cupones; inventario de páginas de cupones bancarios; especificación de sitemap + canonical + Product schema para el equipo de plataforma | C 4 h · JK 6 h | CMS Juntoz (en implementación) | **CMS sin funciones**: solo spec | Spec entregada; cambios de CMS si se habilitan |
| 1.12 | **SEO local · arranque**: exporte GBP, cruce con maestro, corrección de horarios de Cyber/Navidad y datos básicos en las 30 tiendas con más venta (LC/EFE) y las oficinas Efectibank dentro de ellas | C 30 h · JK 3 h | 1.1 (GBP, maestro) | Sin exporte no arranca | 30 fichas corregidas; informe de duplicados y fichas sin dueño |
| 1.13 | **Reserva de solicitudes de Marketing** (landings de campaña y sorteos con el prompt de MKT-SISTEMA, cupones Juntoz-bancos, referidos) | JK 8-12 h/semana · RR según pedido | Marketing | Si excede, se recorta roadmap con Elias | Lista única de pedidos con prioridad |
| 1.14 | **Pauta de marca · análisis** (sin tocar nada): con el reporte de términos, cuantificar consultas de marca en Search/PMax por marca y diseñar la prueba post-Cyber | JK 6 h (Claude: cruce) | 1.1 (Ads) | Paid no entrega el reporte | Cifra de inversión en marca por mes y diseño de prueba |

**Horas mes 1 (`ESTIMACIÓN`)**: JK ~70 h roadmap + 32-48 h de solicitudes de Marketing + ~10 h monitoreo/reporte ≈ **110-130 h** (capacidad ~100-115 h/mes): **ligeramente por encima**; lo que cede si falta tiempo: 1.14 y parte de 1.8 pasan a la semana 1 del mes 2. C ~60 h (capacidad 100-140): holgura para absorber 1.10 y 1.12. RR: 0-8 h (solo pedidos de Marketing).

**Qué se podrá decir el 15-nov** (observable, no promesa): landings Cyber sanas en GSC; incidencias del evento registradas; auditoría de Efectibank entregada con correcciones de higiene hechas; 30 fichas GBP corregidas; línea base lista; cifra de pauta de marca (si Paid entrega). **No** se podrá atribuir venta al SEO todavía.

## 2. Mes 2 · 16 nov → 15 dic · "Después de Cyber: estructura y el puente al crédito; Navidad en local"

Ventana: cambios estructurales con evaluación de riesgo escrita; Cyber Days de noviembre (fecha `SIN DATO`) obliga a repetir el congelamiento si cae aquí. Navidad: no tocar plantillas de ficha después del 10-dic.

| # | Acción | Quién · horas | Depende de | Bloqueo | Resultado observable |
|---|---|---|---|---|---|
| 2.1 | **Puente al crédito en las fichas (E1)**: bloque "desde S/ X al mes con Efectibank" + enlace rastreable a `prestamo-electro`/`prestamo-motos` con producto y monto prellenados; corregir `efectiva.com.pe` → `efectibank.pe` en las 3 webs; medir clics y solicitudes por página de origen | JK 8 h spec+QA · TI Magento 16-24 h · Efectibank 6 h (regla de cuota, URL) · Legal 2 h | 1.9 (regla de cuota, Legal), TI | **TI sin ventana**: alternativa de CMS (bloque estático por categoría) con menos alcance | Bloque en producción en una categoría piloto → todas; solicitudes con origen "PDP" medibles |
| 2.2 | **Canonical en todo EFE** (y revisión en LC): staging → muestra de 50 URLs → producción; monitoreo 4 semanas | JK 12 h · TI 16-32 h | 1.6, TI | TI | Canonical declarado = elegido en la muestra; sin caída de impresiones en grupos de URL |
| 2.3 | **Páginas cruzadas EFE↔Skullcandy/Motocorp** y **503 indexable de Skullcandy**: aplicar | TI/Marketing 4-8 h · JK 2 h | 1.7 | — | URLs fuera del índice o en su tienda |
| 2.4 | **Pauta de marca · prueba controlada**: exclusión de marca en PMax / negativas en Search en una marca (EFE) o región, 2 semanas, midiendo venta total (orgánico + pagado), no solo pagada | JK 8 h · Paid 8 h · Elias decisión | 1.14; decisión de Paid | Paid no acepta la prueba | Resultado de la prueba: ahorro real y efecto en venta total (`ESTIMACIÓN` previa: S/ 20-75 K/mes si 15-35% de la pauta Google es marca; **a validar**) |
| 2.5 | **Categorías de calor / El Niño (LC y EFE)**: ventiladores, aire acondicionado, refrigeración, congeladoras, bombas de agua: títulos, H1, texto útil, guías "cómo elegir", enlaces desde home; verificar stock con Comercial | RR 20-30 h · C 6 h · JK 4 h · Comercial 2 h | Contenidos, stock | Sin RR, lo hace C con borradores de Claude (menos piezas) | Publicadas antes del 1-dic; impresiones/clics por grupo "calor" en GSC |
| 2.6 | **Efectibank · páginas de préstamo que respondan la búsqueda (E2)**: monto, plazo, TEA desde-hasta, cuota ejemplo, requisitos reales, proceso paso a paso con EFE/LC/Motocorp enlazados; landings por intención si Marketing/Legal aprueban ("préstamo con DNI y recibo", "préstamo para moto 0% inicial") | JK 8 h · C 8 h · RR 10-16 h · Legal 4 h · Marketing Efectibank 6 h | 1.9, 1.10 | Legal (TEA visible) | Páginas publicadas e indexadas; consultas nuevas en GSC |
| 2.7 | **Efectibank · ahorro y depósito digital (E3)**: corregir contradicciones, H1 con TREA, un CTA, FAQ schema, página comparativa honesta | C 6 h · JK 3 h · Marketing Efectibank 3 h | 1.10 | — | Páginas corregidas; impresiones en consultas "cuenta de ahorros / depósito a plazo" |
| 2.8 | **Efectibank · sección blog: arquitectura y plantilla** (E6; sin tráfico esperado en el trimestre): categorías por intención (crédito, ahorro, educación), plantilla con CTA y FAQ, calendario de 8 piezas para dic-feb | JK 6 h · TI/Marketing Efectibank 16-24 h · RR 4 h | 1.9 | TI de Efectibank | Sección publicada vacía o con 2 piezas; sitemap enviado |
| 2.9 | **SEO local · Navidad**: horarios especiales en todas las fichas con más venta (LC, EFE, Motocorp, oficinas Efectibank), fotos, categorías, respuestas a reseñas; **spec de página por tienda/oficina** para TI (Magento y WordPress) | C 40 h · JK 6 h | GBP, maestro | — | Fichas al día antes del 10-dic; spec entregada |
| 2.10 | **Juntoz y malls**: lo que el CMS/plataforma habilite de 1.11 (sitemap, canonical, Product schema); corregir doble barra de BanBif; decisión con socios sobre canonical entre dominios (Elias) | JK 8 h · Plataforma 40-80 h | 1.11, CMS | **CMS/desarrollo** | Sitemap en GSC si se publica; si no, decisión documentada |
| 2.11 | **Motocorp**: H1, meta de fichas sin legal, WhatsApp real, contadores vencidos; **crédito en la ficha** (2.1) y enlace a talleres | C 6 h · JK 3 h · Marketing Motocorp 4 h | CMS | — | Cambios en producción; leads por origen si Motocorp los mide (B3) |
| 2.12 | **Sitemaps y robots (Conecta)**: corregir `Sitemap :`; depurar URLs sin stock/descontinuadas (cruce feed ↔ sitemap ↔ `GITHUB_OBSOLETOS_CONECTA`); reenviar en GSC | JK 10 h (Claude: cruce) · TI 8-16 h | TI | TI | Sitemap de ~17-20 K URLs vivas; % indexado en GSC |
| 2.13 | Reserva de Marketing y monitoreo | JK 8-12 h/semana + 2-3 h/semana | — | — | — |

**Horas mes 2**: JK ~85 h roadmap + 32-48 h Marketing + 10 h ≈ **125-145 h**: **por encima de la capacidad**. Lo que se recorta primero si Elias no amplía capacidad: 2.12 (sitemaps) y 2.10 (Juntoz, que igual depende de terceros) pasan a enero; 2.8 (blog) se limita a la plantilla. C ~70 h (ok). RR 34-50 h (**depende de disponibilidad**: sin RR, 2.5 y 2.6 se hacen con borradores de Claude revisados por JK y Legal).

**Qué se podrá decir el 15-dic**: Cyber medido contra la línea base por grupo de URL; resultado de la prueba de pauta de marca (si se hizo) con ahorro real; puente al crédito en producción (al menos piloto) con primeras solicitudes de origen PDP; Efectibank con páginas de préstamo y ahorro corregidas e indexadas; GBP al día para Navidad; canonical de EFE en curso. **Primeras cifras atribuibles**: ahorro de pauta (si hubo prueba) y solicitudes desde fichas. Venta orgánica: solo comparación contra línea base, sin reclamar causalidad.

## 3. Mes 3 · 16 dic → 15 ene · "Defensa El Niño, medición y lo que depende de TI"

Ventana: Navidad y Año Nuevo (no tocar plantillas hasta el 2-ene); enero = cambios de más alcance; calor récord y posibles lluvias en el norte.

| # | Acción | Quién · horas | Depende de | Bloqueo | Resultado observable |
|---|---|---|---|---|---|
| 3.1 | **Páginas por tienda y por oficina (E4 + local Conecta/Motocorp)**: plantilla y primeras 30-50 páginas (tiendas con más venta y zonas de El Niño: Piura, La Libertad, Lambayeque, San Martín), con retiro en tienda, horario, oficina de crédito, `Store`/`LocalBusiness`/`FinancialService` schema; enlazadas desde el localizador | JK 10 h · C 20 h · TI Magento/WordPress 24-48 h | 2.9 spec, maestro, TI | TI | Páginas indexadas; consultas "tienda/préstamo + ciudad" en GSC |
| 3.2 | **Páginas de estado por zona** (temporales, `noindex`): despachos y tiendas abiertas en el norte si El Niño golpea; enlazadas desde fichas y GBP (cierres temporales) | C 6 h · JK 2 h · Logística 2 h | Mapa de zonas (B8) | Logística | Publicadas solo si hay evento |
| 3.3 | **Crédito de reposición (Efectibank + El Niño)**: si Riesgos lanza producto de emergencia/reposición, landing + enlace desde fichas de refrigeradoras, lavadoras, colchones, motos | JK 4 h · RR 6 h · Efectibank | Decisión de Riesgos | Riesgos | Landing publicada si hay producto |
| 3.4 | **Datos estructurados en LC/EFE (Product/Offer/Breadcrumb)** y **Product JSON-LD en Juntoz** (si plataforma puede) | JK 8 h · TI 16-32 h · Plataforma | TI, 2.2 terminado | TI | Resultados enriquecidos en GSC |
| 3.5 | **Pauta de marca · escalar** lo que la prueba validó (si se validó) | JK 4 h · Paid | 2.4 | Decisión | Ahorro mensual registrado |
| 3.6 | **Efectibank · blog: primeras 4-8 piezas** (E6) y **ASO** (reseñas, ficha, capturas; escalar bug del splash) | RR 16-24 h · C 8 h · JK 4 h · Producto app | 2.8, Producto | Contenidos | Piezas indexadas; **sin tráfico relevante esperado aún** |
| 3.7 | **Juntoz**: cierre de lo pendiente (sitemap/canonical/schema) o decisión de aplazar con fecha | JK 6 h · Plataforma | 2.10 | CMS | — |
| 3.8 | **Reporte ejecutivo de 90 días** a gerencia: tres números verificables (ahorro de pauta medido, solicitudes de crédito con origen web/PDP, venta orgánica vs línea base) + lo bloqueado y por quién | JK 8 h · Elias | Todo lo anterior | — | Presentado el 15-ene |
| 3.9 | Reserva de Marketing y monitoreo | JK 8-12 h/semana + 2-3 h/semana | — | — | — |

**Horas mes 3**: JK ~50 h roadmap + 32-48 h Marketing + 10 h ≈ **90-110 h** (dentro de capacidad, considerando feriados). C ~35-50 h. RR 22-30 h.

**Qué se podrá decir el 15-ene**: canonical EFE con 4 semanas de monitoreo; páginas de tienda/oficina en producción (primeras); puente al crédito con dos meses de datos; prueba de pauta con resultado; Efectibank con base técnica y de producto sana, blog arrancado; comparación de ventas orgánicas Cyber/Navidad 2026 vs 2025 por grupo de URL, con las fechas de cambios marcadas.

## 4. Lo que NO entra en 90 días (y por qué)
- Migración de URLs no amigables de los malls y cambios de arquitectura: requieren CMS/desarrollo y una ventana sin campañas.
- Tráfico y crédito desde el blog de Efectibank: publicación ≠ indexación ≠ posicionamiento ≠ conversión; se mide en 2027.
- Rastreo completo de 99 K URLs y benchmarking de competencia: sin licencias se hace por muestras (`docs/09 §2b`).
- Cualquier cifra de venta o utilidad "generada por SEO": solo se reporta lo medible contra línea base y con registro de cambios.

## 5. Dependencias (resumen)
| Área | Qué necesita el plan | Cuándo |
|---|---|---|
| **TI / Magento** | Admin lectura; ventana post-Cyber para canonical EFE, páginas cruzadas, sitemaps; plantilla de ficha (puente al crédito, schema); plantilla de página por tienda | Semana 1 (accesos); 16-nov en adelante |
| **Marketing (CMS)** | Landings Cyber, categorías de calor, bloque de crédito si TI no llega, Motocorp | Antes del 30-oct y dic |
| **Contenidos (Rolando/Ronald)** | Categorías de calor, páginas de préstamo, blog Efectibank | Nov-ene, 6-10 h/semana |
| **Negocio / Comercial** | Categorías con stock para Cyber y calor; plan de stock El Niño; URLs de pauta | Semana 1 |
| **Paid** | Reporte de términos; prueba de exclusión de marca | Semana 1; después de Cyber |
| **Efectibank (Comercial, BI, Legal, Marketing, TI, Riesgos, Producto)** | EF1-EF9; aprobación de TEA y cuota visibles; admin WordPress; regla de cuota para el puente; app | Semana 1-3 |
| **Operaciones** | Exporte GBP; maestro de tiendas/oficinas/talleres | Semana 1 |
| **Plataforma Juntoz** | Sitemap, canonical, schema; CMS editable | Cuando esté disponible |
| **Elias** | Accesos, decisiones (prueba de pauta, canonical entre malls, prioridad de desarrollo, presupuesto de herramientas), gerencia | Continuo |

## 6. Bloqueos técnicos y presupuestarios
| Bloqueo | Efecto | Salida |
|---|---|---|
| Sin GSC/GA4 | No se confirma indexación ni se mide | Escalar en semana 1; mientras, HTML público y fichas |
| Sin Semrush/Screaming Frog (licencias personales retiradas) | Diagnóstico por muestras, sin competencia ni posiciones frescas en Cyber | Presupuestar con casos de uso (`docs/09 §2b`); no asumir que el equipo las pague |
| CMS de Juntoz/malls en implementación | Solo spec y lo mínimo | Decisión de plataforma |
| TI sin ventana | Canonical, sitemaps, puente al crédito y páginas por tienda se retrasan | Pedir ventana post-Cyber ahora |
| Legal de Efectibank sobre TEA/cuotas en página | Sin cifras, las páginas de préstamo siguen genéricas | Reunión en semana 1 (1.9) |
| Contenidos sin disponibilidad | Menos piezas de calor y préstamo | Borradores con Claude revisados por JK |

## 7. Riesgos comerciales y técnicos
Ver `docs/09 §5`. Los tres que más pesan en este roadmap: tocar estructura cerca de Cyber (mitigación: congelamiento y solo CMS), redirigir URLs de pauta (lista de Paid), y atribuir al SEO efectos de precio, stock, pauta o clima (línea base, grupos de control, fechas marcadas).

## 8. Indicadores (semanal JK; mensual a Elias; 90 días a gerencia)
| Indicador | Fuente | Para qué |
|---|---|---|
| Clics, impresiones, CTR, posición por grupo de URL (landings, categorías, PDP top, tiendas/oficinas, préstamos, ahorro) | GSC | Efecto de cada cambio vs línea base y vs grupo de control |
| Sesiones, conversiones e ingresos orgánicos por página de entrada; venta orgánica / venta web | GA4 | Venta orgánica sin reclamar causalidad |
| Inversión en términos de marca (Search/PMax) y venta total durante la prueba | Google Ads + GA4 | Ahorro real |
| **Solicitudes y aprobaciones de crédito por página de origen** (PDP, préstamo, oficina) y canal | Efectibank BI | La métrica 360 nueva |
| Participación de venta financiada (online y total) | Efectibank BI + Conecta | +pp de crédito |
| Depósitos digitales abiertos desde web/orgánico | Efectibank BI | E3 |
| Leads Motocorp por canal y por tienda | Motocorp | E1/local |
| Llamadas, rutas, clics a web por ficha | GBP | Local |
| Instalaciones por fuente y calificación de apps | Consolas | ASO |
| 4xx/5xx en URLs clave; URLs indexadas vs sitemap; canonical declarado = elegido | Script + GSC | Salud |
| Agosto 2026 vs agosto 2025 (PY) y Cyber jul-26 vs jul-25 por canal | Fichas/GA4 (**cifras verificadas**) | Referencia histórica: se separa crecimiento comercial (stock, precio, pauta) de lo atribuible a cambios SEO con registro de fecha |
