# CLAUDE.md · Repo SEO · Grupo EFE

Guía para Claude Code (y para cualquier persona) que trabaje en este repo. Leerla completa antes de tocar nada.

## Qué es este repo
Repositorio **único de SEO** del Grupo EFE. Consolida todo el conocimiento SEO que estaba repartido en otras sesiones y repos: cifras de negocio, diagnóstico de los sitios, pesos por negocio, plan de acciones y lo que falta. **Objetivo del área SEO: hacer ganar más dinero neto a los accionistas, solo con acciones SEO, con resultados visibles en menos de 3 meses.**

Equipo SEO: **Josh Kevin Seminario** (SEO Senior: estrategia multimarca, auditoría técnica, competencia, keywords, ecommerce, analítica), **Carol** (asistente SEO: GBP, fichas, sedes y operación; con supervisión ejecuta CMS, inventarios, ASO y QA), **Rolando y Ronald** (Contenidos, según disponibilidad). Apoyo: cuenta Claude Pro. Dueño: Elias Figueroa (Head of Martech). Nadie está amarrado a un solo tipo de SEO ni a una sola marca.

## Cómo trabajar
- Español, directo, sin jerga innecesaria. Pocas cifras, bien elegidas.
- **Nunca inventar cifras.** Toda cifra lleva fuente y fecha (`docs/01-negocios-y-cifras.md`). Lo que no se sabe se marca `SIN DATO`; lo que se infiere, `HIPÓTESIS`; lo visto en el HTML de un sitio, `COMPROBADO`.
- **Las decisiones de otras sesiones son insumo, no decisiones.** El plan SEO Cyber de la sesión "SEO" (artifact `KqSryvCVBMkrnRj2GDxMqf`) está copiado en `docs/02-diagnostico-seo.md` como hallazgos; las acciones se evalúan con Elias en `docs/04-plan-acciones-90-dias.md`.
- **No subir datos crudos**: Excel, CSV, docx con fichas, audios, exportes de GA4/GSC, listas de clientes. Van en Drive y se enlazan. El `.gitignore` los bloquea; no forzar con `-f`.
- **Sin credenciales** en código, docs, commits ni respuestas (tokens, IDs de cuenta, claves de GSC/GA4).
- Este repo es **privado** y usa nombres reales de marcas y personas por decisión del dueño. El repo `MKT-SISTEMA` tiene una ley de privacidad con fichas (`zqa2zq`...); **no copiar de aquí hacia allá** sin convertir nombres.
- Un cambio por commit, mensaje descriptivo. Al terminar una tarea: actualizar `ESTADO.md` y, si cambió algo, el doc correspondiente.

## Mapa del repo
| Archivo | Para qué |
|---|---|
| `ESTADO.md` | En qué va el trabajo: hecho, pendiente, decisiones, preguntas abiertas. **Leer segundo.** |
| `LEEME.md` | Guía para personas (Kevin, Carolina, gerencia). |
| `docs/01-negocios-y-cifras.md` | Negocios del grupo, ventas, canales, márgenes, activos digitales. Con fuente y fecha. |
| `docs/02-diagnostico-seo.md` | Hallazgos SEO por sitio (técnico, contenido, local, apps). |
| `docs/03-pesos-y-prioridades.md` | Modelo de ganancia neta y pesos por negocio. |
| `docs/04-plan-acciones-90-dias.md` | Acciones rápidas estimadas, responsables, indicadores. **A evaluar con Elias.** |
| `docs/05-fenomeno-el-nino-2027.md` | Escenarios de El Niño y su efecto en demanda, despacho y SEO. |
| `docs/06-informacion-faltante-y-preguntas.md` | Qué falta por tema y las preguntas para Elias. |
| `docs/07-inventario-repos-y-sistemas.md` | Huella de los otros repos y sistemas (qué son, dónde viven, qué los rompe). |
| `docs/08-efectibank-360.md` | Efectibank: cifras públicas, margen de mercado, auditoría de su web, palancas SEO en plata neta, datos que faltan por responsable, tiempos. |
| `docs/09-capacidad-herramientas-y-riesgos.md` | Capacidad real del equipo (horas), herramientas disponibles y su impacto operativo, ventanas de riesgo Cyber, plazos de rastreo e indexación. |
| `landings/bcp/` | Landing BCP en Juntoz administrable desde Google Sheets: plantilla, generador, pruebas. Ver su `README.md`. |
| `grafo/ecosistema-seo.html` | Grafo visual del ecosistema: negocios, activos, datos, sistemas, acciones. Abrir en el navegador. |

## Reglas de negocio que no se tocan sin preguntar
- Venta web "total" = ingresos GA4; "venta neta" = confirmada en el tracker (aprox. la mitad en La Curacao y EFE). Ver `docs/01`.
- Márgenes para el modelo (`docs/03 §1b`): producto físico ~10% (Elias; tracker supone 10%); Motocorp ~8%; Skullcandy ~42%; Juntoz comisión 7.1%; Diners 8.6%; **Efectibank: margen de mercado S/ 25-35 netos por S/ 1,000 prestados (motos S/ 50-70), real S/ 45-55** (`docs/08 §2`). 30-40% de la venta de Conecta y Motocorp se financia con Efectibank (Elias).
- **No asignar porcentajes definitivos de dedicación ni prometer incrementos de ventas o utilidad** sin validar capacidad, datos y necesidades comerciales. Las estimaciones llevan su supuesto al lado.
- Días Cyber: ~4x un día normal; pesan ~25% de la venta web del año.

## Comandos
No hay build. El grafo es un HTML sin dependencias: `python3 -m http.server` en `grafo/` o abrir el archivo directo.

## Al terminar una tarea
1. `ESTADO.md` actualizado (hecho / pendiente / decisiones).
2. Cifras nuevas → `docs/01` con fuente y fecha.
3. Commit pequeño y descriptivo.
