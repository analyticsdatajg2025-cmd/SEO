# ESTADO · SEO Grupo EFE

## Objetivo
Un solo repo con todo el conocimiento SEO del grupo, orientado a **más ganancia neta para los accionistas en menos de 3 meses, solo con SEO**. Equipo: Kevin (sr.) y Carolina (practicante). Dueño: Elias.

## Hecho
- 2026-10-16: repo creado y unificado. Fuentes consolidadas: fichas de negocio por retail y por sitio (16-oct), dos audios de Elias (modelo de negocio), cifras del grupo (`MKT-SISTEMA`), definiciones de métricas (`dashboard-martech-efe`), catálogos de los repos de feeds, revisión pública de 9 sitios (aquí y en la sesión "SEO"), plan SEO Cyber de la sesión "SEO" (como insumo), listas de apps en Play/App Store, pronóstico ENFEN de El Niño.
- 2026-10-16: docs 01-07, `CLAUDE.md`, `LEEME.md`, grafo `grafo/ecosistema-seo.html`.
- 2026-10-16: requerimiento trasladado a la sesión "SEO" (`session_01Wmsu7Y3z7NFsmPgQchK5fU`) pidiendo que devuelva la data que tenga; pendiente su respuesta.

- 2026-10-16 (v2): incorporadas las consideraciones de Elias: Efectibank como prioridad 360 (`docs/08`, con cifras públicas de la Memoria 2025 y PCR jun-26), plata neta por negocio con los márgenes dados y margen de mercado para Efectibank (`docs/03 §1b`), roadmap por mes con horas, dependencias, bloqueos y resultados observables (`docs/04`), capacidad real del equipo (Josh Kevin, Carol, Rolando y Ronald, Claude Pro), herramientas sin licencias y su impacto operativo, ventanas de riesgo Cyber y plazos de indexación (`docs/09`), restricciones de los malls (`docs/02 §2`). Sin porcentajes definitivos de dedicación ni promesas de ingresos.

- 2026-10-16 (v3): corregidas las bases de la tabla de plata neta (solo web vs empresa completa; Motocorp por debajo de LC y EFE en total), Efectibank marcado como negocio que sí vende en digital (cuentas y créditos vía pauta), y nuevos pedidos B13 (venta de piso por marca) y B14 (pauta digital de Efectibank por objetivo).

- 2026-11-24: **Agente SEO con IA, piloto Skullcandy** (`docs/10`). Elias: periodo de exploración; acceso admin a GSC y GA4; el equipo puede tocar blog, fichas y textos de categorías; la home y lo visible no; aprueba Kevin; respetar el plan de `docs/04`. Auditoría pública de skullcandy.com.pe con `herramientas/auditar_sitio.py`: 143 URLs en el sitemap, ~65 ajenas o de prueba. De paso, auditoría del blog de La Curacao (105 artículos, fuera del sitemap; `docs/02 §1`).

- 2026-11-24 (2): decisiones de Elias para el agente: **3-4 blogs por semana**, 4-5 (o diario) en las semanas previas a Cyber; **cero invención** (todo con dato y fuente); blogs pensados para Google y para búsquedas con IA; ver y editar en un panel. Agregados a `docs/10`: ritmo con arranque gradual, regla de cero invención (§5b), plantilla de blog SEO + IA (§5c), panel + tarea programada como recomendación (§6), cómo hacer los exportes (§8b) y qué medir antes y después (§9).

- 2026-11-25: **panel del agente publicado** (privado): https://claude.ai/artifact/Aq9rmVL6sMC4iNPuRScyTw (fuente `panel/agente-seo-skullcandy.html`). Pestañas: blogs nuevos, ajustes y técnico, calendario, medición; editor con vista previa en Google, chequeo automático, fuentes, aprobar/pedir cambios/rechazar y copiar HTML para Magento. Cargados los tickets S1-S9 (58 páginas ajenas claras + 8 dudosas) y la línea base parcial. Falta: compartirlo con Kevin, los exportes de GSC/GA4 y programar el ciclo semanal.

- 2026-11-25 (2): requisitos para que el agente lea GSC/GA4 sin descargas (BigQuery) y publique en Magento con un "go" (token de integración con permisos mínimos, solo store view Skullcandy, staging, caché): `docs/10 §10`, pregunta AG7. Hoy el agente no tiene acceso a GSC, GA4 ni Magento.

- 2026-11-25 (3): objetivo final del agente y decisiones de Elias (`docs/10 §11`): autonomía por niveles (automático para títulos/metas/FAQ/fechas de campaña; aprobación de Kevin para blogs, textos largos y técnico); investigación de demanda global; sin herramientas de pago pero solo data real; calendario comercial con ~1 mes de aviso. Panel: pestaña Radar y nivel por propuesta.

- 2026-11-25 (4): comparación con el año pasado en radar, territorios y medición (importante, no determinante); **campo de batalla** en el Radar (mapa demanda × posición con cuadrantes Atacar/Defender/Explorar/Asegurado, 8 territorios iniciales sin cifras); pasos para que el agente lea GSC y GA4 solo vía BigQuery (`docs/10 §12`). Falta el ID del proyecto de Google Cloud.

## Pendiente (orden)
0. **Acceso directo a datos** (`docs/10 §12`): proyecto de Google Cloud + exportación de GSC y GA4 a BigQuery + permiso al conector; una sola vez, exportes históricos para el año pasado.
0b. **Piloto agente Skullcandy** (`docs/10 §7-8`): Elias sube los exportes de GSC y GA4 (paso a paso en `docs/10 §8b`); armar el panel y la tarea programada semanal (`docs/10 §6`); Kevin valida ritmo; ticket TI S1-S4/S8; lote 1 de títulos y metas. Preguntas AG1-AG6 en `docs/06 §D`.
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
`CLAUDE.md` (reglas) · `docs/01` (cifras) · `docs/02` (diagnóstico) · `docs/03` (pesos) · `docs/04` (plan) · `docs/05` (El Niño) · `docs/06` (faltante y preguntas) · `docs/07` (inventario de repos) · `docs/10` (agente SEO con IA, piloto Skullcandy) · `herramientas/auditar_sitio.py` · `grafo/ecosistema-seo.html` (grafo).
