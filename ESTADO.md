# ESTADO · SEO Grupo EFE

## Objetivo
Un solo repo con todo el conocimiento SEO del grupo, orientado a **más ganancia neta para los accionistas en menos de 3 meses, solo con SEO**. Equipo: Kevin (sr.) y Carolina (practicante). Dueño: Elias.

## Hecho
- 2026-10-16: repo creado y unificado. Fuentes consolidadas: fichas de negocio por retail y por sitio (16-oct), dos audios de Elias (modelo de negocio), cifras del grupo (`MKT-SISTEMA`), definiciones de métricas (`dashboard-martech-efe`), catálogos de los repos de feeds, revisión pública de 9 sitios (aquí y en la sesión "SEO"), plan SEO Cyber de la sesión "SEO" (como insumo), listas de apps en Play/App Store, pronóstico ENFEN de El Niño.
- 2026-10-16: docs 01-07, `CLAUDE.md`, `LEEME.md`, grafo `grafo/ecosistema-seo.html`.
- 2026-10-16: requerimiento trasladado a la sesión "SEO" (`session_01Wmsu7Y3z7NFsmPgQchK5fU`) pidiendo que devuelva la data que tenga; pendiente su respuesta.

- 2026-10-16 (v2): incorporadas las consideraciones de Elias: Efectibank como prioridad 360 (`docs/08`, con cifras públicas de la Memoria 2025 y PCR jun-26), plata neta por negocio con los márgenes dados y margen de mercado para Efectibank (`docs/03 §1b`), roadmap por mes con horas, dependencias, bloqueos y resultados observables (`docs/04`), capacidad real del equipo (Josh Kevin, Carol, Rolando y Ronald, Claude Pro), herramientas sin licencias y su impacto operativo, ventanas de riesgo Cyber y plazos de indexación (`docs/09`), restricciones de los malls (`docs/02 §2`). Sin porcentajes definitivos de dedicación ni promesas de ingresos.

- 2026-10-16 (v3): corregidas las bases de la tabla de plata neta (solo web vs empresa completa; Motocorp por debajo de LC y EFE en total), Efectibank marcado como negocio que sí vende en digital (cuentas y créditos vía pauta), y nuevos pedidos B13 (venta de piso por marca) y B14 (pauta digital de Efectibank por objetivo).

- 2026-10-20: análisis de competencia Cyber Wow 2026 (`docs/10`): Hiraoka, Falabella y Sodimac usan una URL fija por evento con canonical, enlace permanente en footer/menú, FAQ y bloques por categoría que enlazan a las PLP de siempre; Falabella y Sodimac tienen `aggregateRating` e insignias de despacho por producto. Ripley bloquea bots (Cloudflare): SIN DATO. Fechas confirmadas: 2 al 5 de noviembre.

- 2026-10-20: benchmarking Cyber de Hiraoka, Carsa, Tottus, Falabella y Ripley (bloqueado) y plan de 3 acciones (`docs/11`). Hallazgo propio: las landings `/cyber-wow` de EFE y LC tienen el title sin año y H2 con fechas de julio; EFE sin canonical; el blog repite los mismos artículos en ambos dominios.

## Pendiente (orden)
1. **Elias**: responder las preguntas de `docs/06`, dar los accesos A1-A8 y pedir a Efectibank los datos EF1-EF9 (`docs/08 §5`). Sin GSC y Ads por término no se confirma ni se mide nada.
1b. **Elias**: entregar las cifras verificadas de agosto 2026 vs PY y el registro de cambios SEO (B11) para la referencia histórica; decidir el presupuesto de herramientas (`docs/09 §2b`).
2. **Evaluar con Elias** los pesos (`docs/03`) y el plan (`docs/04`): qué entra antes de Cyber Wow (congelar 72 h antes, ~30-oct) y qué después.
3. Guardar en Drive (no en el repo) las fichas `.docx`, audios y `analisis-marcas-seo.html` de la sesión "SEO"; enlazarlos en `docs/01`.
4. Kevin: línea base GSC/GA4 por grupo de URL; rastreo acotado; cruce sitemap ↔ feed.
5. Carolina: inventario de landings Cyber y cupones; exporte GBP + maestro de tiendas; reseñas de apps.
5b. Validar con la jefatura el plan de `docs/11 §2` (metadatos, blog, landings) y corregir antes del 30-oct el año y los textos de julio en `/cyber-wow` de EFE y LC. Evaluar con Elias las acciones de `docs/10 §5` que entran antes del congelamiento (~30-oct). Carol: abrir Ripley en navegador y completar `docs/10`. Kevin: repetir la revisión de competencia el 2-nov y el 6-nov, y la misma revisión para EFE y LC.
6. Decidir qué hacer con los repos vacíos (SEO-LOCAL, SEO-Landing, BI-REPO, Contenido-Repo) y con el PR #38 "panel SEO" de MKT-SISTEMA.

## Decisiones / cuidado con
- Este repo usa **nombres reales** (privado). `MKT-SISTEMA` no los permite: no copiar texto de aquí hacia allá sin convertir a fichas.
- Las cifras de `docs/01` son redondeadas y con fuente; las estimaciones de dinero en `docs/04` llevan su supuesto al lado. **No presentar estimaciones como proyecciones.**
- No tocar pauta ni redirigir URLs durante Cyber Wow; cambios de configuración de Magento (canonical) solo con staging y plan de reversión.
- `SEO-repo-efe` no es un repo de SEO: es el feed de catálogo de EFE para Meta/TikTok en producción. No tocarlo.

## Archivos clave
`CLAUDE.md` (reglas) · `docs/01` (cifras) · `docs/02` (diagnóstico) · `docs/03` (pesos) · `docs/04` (plan) · `docs/05` (El Niño) · `docs/06` (faltante y preguntas) · `docs/07` (inventario de repos) · `docs/10` (competencia Cyber) · `docs/11` (benchmark + 3 acciones) · `grafo/ecosistema-seo.html` (grafo).
