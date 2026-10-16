# CLAUDE.md · Repo SEO · Grupo EFE

Guía para Claude Code (y para cualquier persona) que trabaje en este repo. Leerla completa antes de tocar nada.

## Qué es este repo
Repositorio **único de SEO** del Grupo EFE. Consolida todo el conocimiento SEO que estaba repartido en otras sesiones y repos: cifras de negocio, diagnóstico de los sitios, pesos por negocio, plan de acciones y lo que falta. **Objetivo del área SEO: hacer ganar más dinero neto a los accionistas, solo con acciones SEO, con resultados visibles en menos de 3 meses.**

Equipo SEO: **Kevin** (analista sr., perfil ingeniero de sistemas) y **Carolina** (practicante, perfil operativo). Dueño: Elias Figueroa (Head of Martech).

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
| `grafo/ecosistema-seo.html` | Grafo visual del ecosistema: negocios, activos, datos, sistemas, acciones. Abrir en el navegador. |

## Reglas de negocio que no se tocan sin preguntar
- Venta web "total" = ingresos GA4; "venta neta" = confirmada en el tracker (aprox. la mitad en La Curacao y EFE). Ver `docs/01`.
- Margen de producto físico: ~10% (dicho por Elias en audio; el tracker usa 10% supuesto). Skullcandy ~42% (tracker). Juntoz: comisión 7.1%; Diners 8.6%. Efectibank: margen financiero, sin dato.
- Días Cyber: ~4x un día normal; pesan ~25% de la venta web del año.

## Comandos
No hay build. El grafo es un HTML sin dependencias: `python3 -m http.server` en `grafo/` o abrir el archivo directo.

## Al terminar una tarea
1. `ESTADO.md` actualizado (hecho / pendiente / decisiones).
2. Cifras nuevas → `docs/01` con fuente y fecha.
3. Commit pequeño y descriptivo.
