# ESTADO · SEO Grupo EFE

## Objetivo
Un solo repo con todo el conocimiento SEO del grupo, orientado a **más ganancia neta para los accionistas en menos de 3 meses, solo con SEO**. Equipo: Kevin (sr.) y Carolina (practicante). Dueño: Elias.

## Hecho
- 2026-10-16: repo creado y unificado. Fuentes consolidadas: fichas de negocio por retail y por sitio (16-oct), dos audios de Elias (modelo de negocio), cifras del grupo (`MKT-SISTEMA`), definiciones de métricas (`dashboard-martech-efe`), catálogos de los repos de feeds, revisión pública de 9 sitios (aquí y en la sesión "SEO"), plan SEO Cyber de la sesión "SEO" (como insumo), listas de apps en Play/App Store, pronóstico ENFEN de El Niño.
- 2026-10-16: docs 01-07, `CLAUDE.md`, `LEEME.md`, grafo `grafo/ecosistema-seo.html`.
- 2026-10-16: requerimiento trasladado a la sesión "SEO" (`session_01Wmsu7Y3z7NFsmPgQchK5fU`) pidiendo que devuelva la data que tenga; pendiente su respuesta.

- 2026-10-16 (v2): incorporadas las consideraciones de Elias: Efectibank como prioridad 360 (`docs/08`, con cifras públicas de la Memoria 2025 y PCR jun-26), plata neta por negocio con los márgenes dados y margen de mercado para Efectibank (`docs/03 §1b`), roadmap por mes con horas, dependencias, bloqueos y resultados observables (`docs/04`), capacidad real del equipo (Josh Kevin, Carol, Rolando y Ronald, Claude Pro), herramientas sin licencias y su impacto operativo, ventanas de riesgo Cyber y plazos de indexación (`docs/09`), restricciones de los malls (`docs/02 §2`). Sin porcentajes definitivos de dedicación ni promesas de ingresos.

- 2026-10-16 (v3): corregidas las bases de la tabla de plata neta (solo web vs empresa completa; Motocorp por debajo de LC y EFE en total), Efectibank marcado como negocio que sí vende en digital (cuentas y créditos vía pauta), y nuevos pedidos B13 (venta de piso por marca) y B14 (pauta digital de Efectibank por objetivo).

- 2026-10-19: **auditoría SEO de Efectibank** como dashboard `auditoria-seo-efectibank.html` (rastreo propio de 274 URLs, Lighthouse móvil en 9 páginas, benchmark con tasas SBS y webs de 11 competidores, keywords sin volumen, SEO vs pauta con calculadora vacía, priorización A01-A18, roadmap 30-60-90, dependencias). Resumen de hallazgos nuevos en `docs/08 §7`. No se modificó la web.

- 2026-10-19: landing del sorteo Cyberweek de La Curacao ajustada (`landings/sorteo-cyberweek.html`): tipografía H1 30 / H2 22 / H3 18 / texto 14 px, "¿Cómo participar?" en 3 pasos con íconos junto al formulario, contenedor del formulario más compacto y JS de la landing corregido (dejaba invisible la sección de pasos). **Script de HubSpot intacto** (verificado byte a byte); el formulario se dibuja en iframe, así que su interior solo se ajusta desde el editor de HubSpot.

- 2026-10-19 (v2): landing del sorteo: fotos de premios (TV y moto JETTOR GP 125 desde mcprod.efe.com.pe), "un televisor por día / una moto por semana", fechas de motos (jueves 5 y 12 nov.), legales estructurados y justificados con "Mostrar más", enlace de la landing en el lugar del marcador y teléfono clicable; carrusel automático sin botón de pausa. HubSpot intacto.

- 2026-10-19 (v3): landing renombrada a `landings/sorteo-cyberweek.html` (URL final `lacuracao.pe/sorteo-cyberweek` en canonical, og:url y legales); enlace de combos a la categoría con filtro de precio; "¿Cómo participar?" sin Efectibank, con calendario de sorteos y "Ten en cuenta", a la misma altura que el formulario.

- 2026-10-19 (v4): versión Tiendas EFE de la landing (`landings/sorteo-cyberweek-efe.html`): dominio efe.com.pe (misma URL `/sorteo-cyberweek`), formulario HubSpot de EFE (formId d9029fe2…), colores de marca EFE (azul #0071CE, azul oscuro #00328C, celeste, blanco; #FCB75D solo como acento sutil, sin amarillo), marca La Curacao → Tiendas EFE en textos, SEO y legales (texto del .odt Rev. 01, validar con Legal). Imágenes y enlaces de categorías verificados en efe.com.pe.

- 2026-10-19 (v5): `landings/seccion-ganadores-ruleta.html`: ruleta con regla de un ganador por sorteo (diario); sin campos de N.° de premios, suplentes ni eliminar duplicados (cada línea es una participación); el anuncio dice "¡Felicidades!" sin nombrar el premio.

- 2026-10-19 (v6): `dashboard-seo-cyber.html`: panel con las 16 tareas principales (de `docs/04`, ESTADO y auditoría) y cruce con GSC por CSV para Cyber 2026 vs 2025 (nov: 2–5 vs 3–6; jul: 13–16 vs 14–17; abr: 20–23 vs 7–10; fuentes de prensa, IAB sin confirmar nov-2026). **Urgente**: exportar a Drive el GSC de Cyber julio 2025 antes del ~14-nov (retención de 16 meses).

- 2026-10-20: `dashboard-atribucion-canales.html`: el tablero de atribución y canales (construido como módulo `dc-canales` en MKT-SISTEMA, PR #39) empaquetado en un solo HTML descargable. Funciona sin servidor: se suben los CSV exportados de GA4 (sesiones, eventos, primera interacción, basado en datos), Search Console (Fechas y Consultas), pauta y sistemas propios; todo queda en el navegador, con respaldo descargable. Marcas precargadas: Tiendas EFE, La Curacao y Efectibank (editables); referidos Conecta, Malls y MTC por `utm_source`. Probado en Chrome con CSV de prueba (no datos reales). Pendiente: cargar los exports reales de GA4 y GSC.

## Pendiente (orden)
0. **Elias**: revisar `auditoria-seo-efectibank.html` y decidir si se presentan A01-A06 a Marketing y Legal de Efectibank esta semana (higiene + tasas; no dependen de Cyber).
1. **Elias**: responder las preguntas de `docs/06`, dar los accesos A1-A8 y pedir a Efectibank los datos EF1-EF9 (`docs/08 §5`). Sin GSC y Ads por término no se confirma ni se mide nada.
1b. **Elias**: entregar las cifras verificadas de agosto 2026 vs PY y el registro de cambios SEO (B11) para la referencia histórica; decidir el presupuesto de herramientas (`docs/09 §2b`).
2. **Evaluar con Elias** los pesos (`docs/03`) y el plan (`docs/04`): qué entra antes de Cyber Wow (congelar 72 h antes, ~30-oct) y qué después.
3. Guardar en Drive (no en el repo) las fichas `.docx`, audios y `analisis-marcas-seo.html` de la sesión "SEO"; enlazarlos en `docs/01`.
4. Kevin: línea base GSC/GA4 por grupo de URL; rastreo acotado; cruce sitemap ↔ feed.
5. Carolina: inventario de landings Cyber y cupones; exporte GBP + maestro de tiendas; reseñas de apps.
6. Decidir qué hacer con los repos vacíos (SEO-LOCAL, SEO-Landing, BI-REPO, Contenido-Repo) y con el PR #38 "panel SEO" de MKT-SISTEMA.

## Decisiones / cuidado con
- Este repo usa **nombres reales** (privado). `MKT-SISTEMA` no los permite: no copiar texto de aquí hacia allá sin convertir a fichas.
- Las cifras de `docs/01` son redondeadas y con fuente; las estimaciones de dinero en `docs/04` llevan su supuesto al lado. **No presentar estimaciones como proyecciones.**
- No tocar pauta ni redirigir URLs durante Cyber Wow; cambios de configuración de Magento (canonical) solo con staging y plan de reversión.
- `SEO-repo-efe` no es un repo de SEO: es el feed de catálogo de EFE para Meta/TikTok en producción. No tocarlo.

## Archivos clave
`CLAUDE.md` (reglas) · `docs/01` (cifras) · `docs/02` (diagnóstico) · `docs/03` (pesos) · `docs/04` (plan) · `docs/05` (El Niño) · `docs/06` (faltante y preguntas) · `docs/07` (inventario de repos) · `grafo/ecosistema-seo.html` (grafo).
