# ESTADO · SEO Grupo EFE

## Objetivo
Un solo repo con todo el conocimiento SEO del grupo, orientado a **más ganancia neta para los accionistas en menos de 3 meses, solo con SEO**. Equipo: Kevin (sr.) y Carolina (practicante). Dueño: Elias.

## Hecho
- 2026-10-16: repo creado y unificado. Fuentes consolidadas: fichas de negocio por retail y por sitio (16-oct), dos audios de Elias (modelo de negocio), cifras del grupo (`MKT-SISTEMA`), definiciones de métricas (`dashboard-martech-efe`), catálogos de los repos de feeds, revisión pública de 9 sitios (aquí y en la sesión "SEO"), plan SEO Cyber de la sesión "SEO" (como insumo), listas de apps en Play/App Store, pronóstico ENFEN de El Niño.
- 2026-10-16: docs 01-07, `CLAUDE.md`, `LEEME.md`, grafo `grafo/ecosistema-seo.html`.
- 2026-10-16: requerimiento trasladado a la sesión "SEO" (`session_01Wmsu7Y3z7NFsmPgQchK5fU`) pidiendo que devuelva la data que tenga; pendiente su respuesta.

- 2026-10-16 (v2): incorporadas las consideraciones de Elias: Efectibank como prioridad 360 (`docs/08`, con cifras públicas de la Memoria 2025 y PCR jun-26), plata neta por negocio con los márgenes dados y margen de mercado para Efectibank (`docs/03 §1b`), roadmap por mes con horas, dependencias, bloqueos y resultados observables (`docs/04`), capacidad real del equipo (Josh Kevin, Carol, Rolando y Ronald, Claude Pro), herramientas sin licencias y su impacto operativo, ventanas de riesgo Cyber y plazos de indexación (`docs/09`), restricciones de los malls (`docs/02 §2`). Sin porcentajes definitivos de dedicación ni promesas de ingresos.

- 2026-10-16 (v3): corregidas las bases de la tabla de plata neta (solo web vs empresa completa; Motocorp por debajo de LC y EFE en total), Efectibank marcado como negocio que sí vende en digital (cuentas y créditos vía pauta), y nuevos pedidos B13 (venta de piso por marca) y B14 (pauta digital de Efectibank por objetivo).

- 2026-10-23: `dashboard/puntaje-seo.html`: puntaje SEO 0-100 por marca (Efectibank, La Curacao, Tiendas EFE, Juntoz, Motocorp) con rúbrica de 5 dimensiones sobre el diagnóstico de `docs/02` (criterio, `HIPÓTESIS`), selector de mes, historial de tráfico orgánico, keywords y autoridad (hoy `SIN DATO` salvo el promedio derivado de F1) y línea de historia. Puntajes oct-26: Motocorp 65, EFE 39, Efectibank 38, LC 36, Juntoz 23.

## Pendiente (orden)
1. **Elias**: responder las preguntas de `docs/06`, dar los accesos A1-A8 y pedir a Efectibank los datos EF1-EF9 (`docs/08 §5`). Sin GSC y Ads por término no se confirma ni se mide nada.
1b. **Elias**: entregar las cifras verificadas de agosto 2026 vs PY y el registro de cambios SEO (B11) para la referencia histórica; decidir el presupuesto de herramientas (`docs/09 §2b`).
2. **Evaluar con Elias** los pesos (`docs/03`) y el plan (`docs/04`): qué entra antes de Cyber Wow (congelar 72 h antes, ~30-oct) y qué después.
3. Guardar en Drive (no en el repo) las fichas `.docx`, audios y `analisis-marcas-seo.html` de la sesión "SEO"; enlazarlos en `docs/01`.
4. Kevin: línea base GSC/GA4 por grupo de URL; rastreo acotado; cruce sitemap ↔ feed.
5. Carolina: inventario de landings Cyber y cupones; exporte GBP + maestro de tiendas; reseñas de apps.
5b. Kevin/Carol: cargar cada mes en `dashboard/puntaje-seo.html` (clics GSC, consultas con clic, DR de Ahrefs gratis) y repetir el puntaje en noviembre, después del Cyber Wow.
6. Decidir qué hacer con los repos vacíos (SEO-LOCAL, SEO-Landing, BI-REPO, Contenido-Repo) y con el PR #38 "panel SEO" de MKT-SISTEMA.

## Decisiones / cuidado con
- Este repo usa **nombres reales** (privado). `MKT-SISTEMA` no los permite: no copiar texto de aquí hacia allá sin convertir a fichas.
- Las cifras de `docs/01` son redondeadas y con fuente; las estimaciones de dinero en `docs/04` llevan su supuesto al lado. **No presentar estimaciones como proyecciones.**
- No tocar pauta ni redirigir URLs durante Cyber Wow; cambios de configuración de Magento (canonical) solo con staging y plan de reversión.
- `SEO-repo-efe` no es un repo de SEO: es el feed de catálogo de EFE para Meta/TikTok en producción. No tocarlo.

## Archivos clave
`CLAUDE.md` (reglas) · `docs/01` (cifras) · `docs/02` (diagnóstico) · `docs/03` (pesos) · `docs/04` (plan) · `docs/05` (El Niño) · `docs/06` (faltante y preguntas) · `docs/07` (inventario de repos) · `grafo/ecosistema-seo.html` (grafo).
