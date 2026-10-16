# 06 · Información que falta y preguntas para Elias

Última revisión: 16 oct 2026. Ordenado por lo que más cambia las decisiones.

## A. Accesos (sin esto no se mide ni se confirma nada)
| # | Qué | Para qué | Quién lo da |
|---|---|---|---|
| A1 | **Search Console** usuario completo: lacuracao.pe, efe.com.pe, juntoz.com, dinersclubmall.pe, banbifmall.pe, motocorp.pe, skullcandy.com.pe, efectibank.pe, coldex.pe, mMall | Indexación real, canonical elegido, consultas por URL, sitemaps | TI / dueños de propiedades |
| A2 | **GA4** lector en cada propiedad (o exportes) | Orgánico por página de entrada, conversiones, ingresos, días Cyber | Martech |
| A3 | **Google Ads**: reporte de términos de búsqueda (Search y PMax) por marca, ene-sep 2026; acceso a Keyword Planner | Canibalización de marca; volúmenes de keywords | Paid |
| A4 | **Google Business Profile** (todas las fichas) + maestro oficial de tiendas, oficinas y talleres | SEO local | Operaciones |
| A5 | Admin de **Magento** solo lectura (o un contacto) | Páginas CMS por store view, canonical, sitemap | TI |
| A6 | Contacto del equipo de **plataforma Juntoz (Next.js)** y su backlog | Sitemap, canonical, schema | Juntoz |
| A7 | Consolas de **Google Play y App Store** (lectura) de las apps Efectibank, EFE, LC, Juntoz | ASO, instalaciones por fuente | Producto |
| A8 | Rastreador (Screaming Frog) o permiso para rastrear con script propio | Auditoría técnica | Elias |

## B. Datos de negocio
| # | Qué falta | Por qué importa |
|---|---|---|
| B1 | **Margen real** por marca y categoría (hoy: ~10% dicho en audio; tracker supone 10%) | Convierte venta orgánica en dinero neto; decide pesos |
| B2 | **Efectibank**: lista EF1-EF9 de `docs/08 §5` por responsable (objetivo del canal, rentabilidad por producto, tráfico orgánico y conversiones, solicitudes/aprobaciones/desembolsos por canal y página de origen, estado técnico y accesos, costo de fondeo, app, herramientas, maestro de 176 oficinas); % de la venta de Conecta y Motocorp financiada (Elias: 30-40%) | Es la palanca de mayor margen; el modelo usa margen de mercado hasta tener el real |
| B3 | **Motocorp**: leads por canal (formulario, WhatsApp, llamada), costo por lead, % que cierra en venta, ticket promedio de moto | Define el valor de un lead orgánico y del SEO local |
| B4 | **Juntoz**: venta y sesiones por canal de tráfico (orgánico vs pagado vs cupón); costo de cupones; resultado neto mensual | Hoy solo sabemos que no es rentable y que falta tráfico |
| B5 | **Apps Conecta** (EFE, LC, Juntoz): instalaciones, usuarios activos, venta por app, retención; cómo se mide el "CR 1%" del instalador | Decide si vale esfuerzo ASO |
| B6 | Venta web **por categoría** y **por departamento/tienda de recojo** (LC, EFE) | Prioridad de categorías (calor, El Niño) y de tiendas (local) |
| B7 | Plan comercial de **Cyber Wow noviembre**: categorías, stock, URLs de pauta, fecha oficial | Qué enlazar desde las landings; qué no tocar |
| B8 | Plan de **stock de climatización/frío** nov-feb y zonas con despacho suspendido en escenario El Niño extraordinario | Contenido estacional y páginas de estado |
| B9 | Resto del audio sobre Efectibank (se cortó al 3:25) y marcas de motos además de Jettor y Honda | Contexto |
| B10 | Qué es "Mafrem Mall" / mMall y su dominio | Inventario |
| B11 | **Resultados de agosto 2026 vs agosto 2025 (PY)** por marca y canal, con las optimizaciones SEO implementadas y sus fechas (registro de cambios del área) | Referencia histórica de la contribución del SEO: separar crecimiento comercial de lo atribuible; **solo cifras verificadas** |
| B12 | Volumen real de solicitudes de Marketing al SEO Senior (landings, sorteos, cupones, referidos) por mes | Dimensionar la reserva de horas de `docs/09` |
| B13 | **Venta de piso por marca** (LC, EFE, Motocorp) 2025-2026, % financiada con Efectibank, ticket de piso, y venta de Motocorp actual (la pública es de 2022) | Hoy solo hay data web: la tabla de plata neta por empresa completa es estimación |
| B14 | **Efectibank digital**: inversión en pauta por objetivo (apertura de cuentas, crédito), costo por cuenta y por crédito aprobado, y cuántas aperturas/solicitudes llegan por orgánico | El SEO compite con esa pauta: el ahorro por reemplazar pauta de marca y de producto es neto al 100% |

## C. Preguntas para Elias (responder en una línea cada una)
1. ¿El objetivo de 3 meses se mide en **ganancia neta** del grupo o en venta web orgánica? Si es neto, ¿aceptamos que la palanca principal sea **dejar de pagar pauta de marca** (eso toca el presupuesto de Paid)?
2. ¿Podemos hacer la **prueba de exclusión de marca** en PMax/Search después de Cyber, en una marca (EFE) o región, 2 semanas, midiendo venta total y no solo venta pagada?
3. ¿Efectibank entra en el alcance del equipo SEO (Kevin/Carolina) o tiene su propio equipo de marketing? ¿Podemos enlazar desde las fichas de LC/EFE/Motocorp a sus páginas de préstamo con texto de cuotas?
4. ¿Qué margen financiero promedio deja un crédito de electro y uno de moto? Con una cifra aproximada ya se puede priorizar.
5. ¿Hay desarrollo disponible en **Magento (Conecta)** y en **Next.js (Juntoz)** antes de Cyber, o solo cambios de CMS? ¿Quién aprueba cambios de configuración (canonical, sitemap)?
6. ¿Se pueden crear **páginas por tienda** (LC, EFE, Motocorp) y por agencia (Efectibank)? ¿Existe un maestro de tiendas con dirección, horario y teléfono?
7. ¿Diners y BanBif aceptarían que sus fichas apunten con canonical a Juntoz, o cada mall debe rankear por su cuenta? ¿Hay un contrato que lo condicione?
8. ¿Los repos vacíos SEO-LOCAL, SEO-Landing, BI-REPO y Contenido-Repo se archivan o se absorben aquí?
9. ¿Las fichas `.docx`, los audios y el `analisis-marcas-seo.html` de la sesión "SEO" se guardan en Drive para enlazarlos desde este repo?
10. ¿Qué entregable quiere gerencia a 90 días: tres números (ahorro de pauta, venta orgánica, créditos originados) o algo distinto?
11. ¿Las apps de EFE/LC/Juntoz son webviews de la web (misma URL) o tienen contenido propio? ¿Quién las mantiene?
12. ¿Cuál es la fuente oficial de la venta "neta" (tracker vs Magento vs SAP) y de la venta en tienda atribuible a la web (60% de recojo)?
