# 09 · Capacidad del equipo, herramientas disponibles y riesgos de cambio (Cyber)

Última revisión: 16 oct 2026. Base para que `docs/04` sea ejecutable y no un deseo.

## 1. Capacidad real del equipo (supuestos a validar con Elias)

| Rol | Persona | Horas/semana | Lo que consume fuera del roadmap | Horas netas/semana para el roadmap | 90 días (~12 semanas) |
|---|---|---|---|---|---|
| SEO Senior | **Josh Kevin Seminario**: estrategia multimarca, auditoría técnica, análisis competitivo, keywords, optimización ecommerce, analítica, priorización y validación | 40 `SUPUESTO` | Solicitudes operativas y coordinaciones con Marketing, RR. SS., Paid, Contenidos y TI: **30-40%** `SUPUESTO` | **24-28** | **~290-340 h** |
| Asistente SEO | **Carol**: Google Business Profile, fichas, sedes, seguimiento operativo. **No se amarra a SEO local**: con supervisión puede ejecutar metadatos en CMS, inventarios de URLs, ASO, QA de implementaciones y reportes | 30-40 `SUPUESTO` | Supervisión del Senior (resta ~2 h/semana al Senior); reportes | **25-35** | **~300-420 h** |
| Equipo de Contenidos | **Rolando y Ronald**: PDL, PDP, blogs y landings según disponibilidad | `SIN DATO` | Otras áreas | **por confirmar**: el plan asume 6-10 h/semana para SEO | ~70-120 h `SUPUESTO` |
| Claude (cuenta Pro) | Apoyo del equipo: cruces de datos, borradores de contenido y metadatos, especificaciones para TI, scripts de chequeo masivo (códigos de respuesta, títulos, canonical), revisión de muestras de HTML, resúmenes de informes | según uso | — | Multiplica horas del Senior y del Asistente en análisis y redacción; **no reemplaza Semrush, Screaming Frog ni la validación técnica humana** | — |
| TI / Magento | externo | `SIN DATO` | Backlog propio | por ticket; sin ventana confirmada antes de Cyber | — |
| Plataforma Juntoz (Next.js) | externo | `SIN DATO` | CMS en implementación | por ticket | — |
| Marketing (CMS) | externo | — | Campañas | cambios de títulos/landings bajo pedido | — |

Reglas de reparto que se proponen:
- **Reserva fija del Senior para solicitudes de Marketing: 8-12 h/semana** (landings comerciales, sorteos, cupones Juntoz con bancos, páginas de referidos). Si el volumen real es mayor, se recorta del roadmap, no al revés sin decisión de Elias.
- **Reserva de monitoreo y reporte: 2-3 h/semana** del Senior.
- Ninguna marca tiene dedicación exclusiva. El Asistente trabaja un frente a la vez (GBP) con supervisión semanal.

## 2. Herramientas y accesos: qué se puede diagnosticar hoy

Hasta hace poco el SEO Senior usaba **licencias personales** de Semrush y Screaming Frog (incluso en campañas Cyber) para auditar a escala, investigar keywords, analizar competencia, priorizar URLs comerciales y medir antes/después. Ya no están disponibles y la empresa no financia equivalentes. **El plan no asume que el equipo vuelva a pagarlas de su bolsillo.** Sin logs de servidor, APIs ni entornos de desarrollo confirmados.

| Diagnóstico | Con qué (gratis o ya disponible) | Alcance | Limitación |
|---|---|---|---|
| Indexación, canonical elegido, consultas, CTR, sitemaps enviados, errores de rastreo | **Google Search Console** (pendiente de acceso, A1) | Completo por propiedad | Sin acceso = nada de esto |
| Tráfico orgánico, páginas de entrada, conversiones, ingresos | **GA4** (pendiente, A2) | Completo | Sin acceso = solo las fichas |
| Volumen de búsqueda | **Keyword Planner** (gratis con la cuenta de Google Ads, A3) + consultas reales de GSC | Suficiente para priorizar | Rangos, no cifras exactas, si la cuenta no invierte en esa campaña |
| Términos de marca pagados | Reporte de términos de búsqueda de Google Ads (A3) | Completo | Depende de Paid |
| Rastreo técnico | **Screaming Frog versión gratuita (500 URLs)** por muestra: home, landings, 50 categorías, 200 fichas; o **script propio** (Python, `requests` + parser) sobre el sitemap para códigos de respuesta, canonical, título, H1, noindex | Muestra representativa y chequeos masivos simples | No reemplaza un rastreo completo de 99 K URLs con render JS; Juntoz (Next.js) requiere render para ver el DOM final |
| Datos estructurados | **Prueba de resultados enriquecidos** de Google, Schema Validator | Por URL | Manual |
| Velocidad / Core Web Vitals | **PageSpeed Insights** y el informe CWV de GSC | Por URL / por grupo | Sin acceso a GSC, solo por URL |
| Fichas de tiendas | **Google Business Profile** (A4) + Google Maps | Completo | Sin acceso = solo lo visible |
| Backlinks | GSC (enlaces) y Bing Webmaster Tools (gratis) | Básico | Sin herramienta de pago, sin competencia |
| Competencia / cuota de mercado SEO | — | — | **Requiere presupuesto** (Semrush/Ahrefs/Similarweb) |
| Rastreo masivo con render JS y logs | — | — | **Requiere presupuesto** (SF licencia ~US$ 259/año) **o apoyo de TI** (logs, acceso a staging) |

Claude puede ayudar a cruzar datos, redactar especificaciones y revisar muestras de HTML; **no reemplaza un rastreador de miles de URLs ni la validación técnica humana**.

### 2b. Impacto operativo de contar o no con herramientas especializadas (sin asumir ingresos)

| Tarea | Con Semrush + Screaming Frog (licencia) | Sin ellas (hoy) | Caso de uso concreto en este plan |
|---|---|---|---|
| Rastreo completo de LC y EFE (~99 K URLs c/u), Juntoz (42 K SKU con render JS) | 1 corrida por sitio, horas; detecta canonical, duplicados, 4xx/5xx, títulos, profundidad, huérfanas | Muestras de 500 URLs (SF gratuito) o script propio sin render; Juntoz no se puede ver bien | 2.3, 2.8, 5.1-5.3: hoy se diagnostica por muestra y GSC; el riesgo de dejar errores sin ver sube |
| Keyword research con volumen y dificultad | Volúmenes, tendencias, SERP features, clusters en horas | Keyword Planner (rangos si la cuenta no invierte), GSC (solo lo que ya rankea), SERP a mano | 2.5 (calor), E2/E3 (préstamos, ahorro): se prioriza sin volumen fiable |
| Competencia (quién gana tráfico, con qué páginas, gap de keywords) | Estimación de tráfico y gap por dominio | No disponible; solo SERP manual de muestras | E2 (bancos, cajas, comparadores), Cyber (Falabella, Ripley, Oechsle): se pierde la vista del rival |
| Monitoreo durante Cyber (posiciones diarias, errores nuevos) | Alertas y rastreos programados | GSC con 2-3 días de retraso + script diario de códigos de respuesta | 2.2 y monitoreo del evento: se detecta más tarde |
| Medición antes/después de cada optimización | Posiciones por keyword y URL en el tiempo | GSC por grupo de URL (suficiente para clics/impresiones, no para posiciones por keyword frescas) | Indicadores de `docs/04`: medible pero más grueso |
| Backlinks y autoridad | Perfil de enlaces y comparables | GSC (propios) y Bing WT | Secundario en 90 días |
| Costo de referencia | Semrush Pro ~US$ 140/mes; Screaming Frog ~US$ 259/año | — | Comparar con horas: un rastreo completo manual de 99 K URLs no es viable; el costo anual es menor que una semana del Senior |

Conclusión operativa: sin herramientas, **el equipo puede ejecutar el plan de 90 días** (CMS, GBP, GSC, muestras, especificaciones), pero con **menos profundidad, más lentitud y más riesgo de no ver errores a escala**, sobre todo en Juntoz y en el monitoreo de Cyber. La recomendación es presupuestar Screaming Frog (rastreo a escala, caso 2.3/2.8/5.x) y una herramienta de keywords/competencia (caso E2/E3 y Cyber), justificadas por casos de uso, **sin atribuirles ingresos**.

## 3. Ventanas de riesgo: antes, durante y después de Cyber

Calendario: Cyber Wow (prensa: 2-5 nov; confirmar con IAB), Cyber Days de noviembre (fecha `SIN DATO`), Navidad, Año Nuevo. Un día Cyber vende ~4x un día normal; Cyber pesa ~25% de la venta web anual (`CONFIRMADO`, fichas).

### Qué cambios son de qué tipo

| Tipo de cambio | Riesgo | Reversión | Cuándo |
|---|---|---|---|
| Títulos, descripciones, H1, texto de categoría, enlaces internos (CMS) | Bajo | Minutos | Antes (hasta 72 h antes) y después |
| Canonical puntual en una landing (CMS) | Bajo-medio | Minutos | Antes, con inspección en GSC |
| Fichas de GBP (horarios, fotos, categorías) | Bajo | Inmediata | Siempre |
| **Canonical en todo el sitio** (configuración Magento) | Alto: afecta ~99 K URLs; Google tarda semanas en reprocesar | Config revertible, pero el reprocesamiento no es inmediato | **Después de Cyber**, con staging, muestra en GSC y monitoreo |
| **Sitemaps** (depurar, regenerar), **robots.txt** | Medio-alto: un error quita URLs del rastreo | Rápida en archivo, lenta en efecto | Después de Cyber; corrección del `Sitemap :` puede ir antes si TI confirma que es trivial |
| **Redirecciones / migración de URLs** (unificar landings Cyber, URLs no amigables de malls) | Alto: pérdida de señales si se hace mal; rompe enlaces de pauta | Parcial | **Después de Cyber**, nunca sobre URLs activas en pauta |
| Plantillas (datos estructurados, breadcrumbs, títulos de ficha) | Medio: afecta todas las fichas | Despliegue | Después de Cyber, con prueba en una categoría |
| Arquitectura / categorías nuevas | Alto | Difícil | Enero en adelante |

### Antes de Cyber (ahora → 72 h antes)
- Riesgo de tocar estructura: Google puede estar **reprocesando** justo en el pico; una regresión no se detecta a tiempo. **Solo cambios de CMS reversibles** y diagnóstico.
- Preparación de páginas comerciales: metadatos limpios, enlaces desde home a categorías con stock, URLs de pauta confirmadas y con respuesta 200.
- Congelamiento SEO 72 h antes del evento (y hasta el cierre de Cyber Days si son consecutivos).

### Durante Cyber
- **Nada estructural.** Monitoreo diario de códigos de respuesta de landings y categorías clave, sitemap accesible, sin `noindex` accidental.
- Incidencias críticas (landing caída, canonical que saca la landing del índice, redirección rota de pauta): intervención urgente con registro y responsable.
- No tocar pauta de marca en el evento.

### Después de Cyber (desde el cierre de Cyber Days → enero)
- Cambios estructurales **con evaluación de riesgo escrita**: qué cambia, URLs afectadas, prueba en staging o en una muestra, responsable, fecha, cómo se revierte, qué se monitorea y durante cuánto tiempo.
- Orden sugerido: canonical EFE → páginas cruzadas → sitemaps y robots → datos estructurados → unificación de URLs de evento → malls (cuando el CMS lo permita).
- Navidad y Año Nuevo también son ventanas de alta demanda: los cambios de más alcance van a **enero**.

## 4. Plazos orientativos de efecto (con incertidumbre)

No hay plazos exactos; esto es lo que la experiencia general y la documentación de Google permiten decir. Se mide con GSC (Inspección de URL, informe de indexación, rendimiento).

| Etapa | Qué significa | Orden de magnitud | Incertidumbre |
|---|---|---|---|
| Publicación | El cambio está en producción | Día 0 | — |
| Descubrimiento | Google encuentra la URL (sitemap, enlaces internos, solicitud de indexación) | Horas a días en páginas enlazadas desde home; días a semanas en páginas profundas | Alta en sitios con 99 K URLs: el presupuesto de rastreo se reparte |
| Rastreo | Googlebot descarga la página | Páginas populares: días; cola larga: semanas | Depende de la salud del sitio |
| Indexación | La página entra al índice con el canonical elegido | Días a semanas; **cambios de canonical masivos: semanas a meses** en reprocesarse | Alta |
| Posicionamiento | La página compite y sube | Consultas de marca y landings de evento: días a semanas. Consultas genéricas competidas (financieras, "aire acondicionado"): **meses** | Muy alta; depende de competencia y autoridad |
| Conversión | Ventas, solicitudes, leads atribuibles | Después del posicionamiento y según demanda estacional | Depende de stock, precio, pauta |

Consecuencias prácticas: lo que se publica **hoy** puede llegar sano a Cyber Wow si son metadatos de páginas ya indexadas; una sección nueva (blog de Efectibank) publicada en noviembre **no** genera tráfico relevante en su primer mes; los cambios estructurales de después de Cyber se evalúan en enero-febrero, no en diciembre.

## 5. Riesgos (comerciales y técnicos)

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Un cambio estructural antes o durante Cyber desindexa o degrada landings/categorías | Media si se hace; nula si no se hace | Muy alto (ventas del evento) | Congelamiento; solo CMS; registro; monitoreo diario |
| Redirigir una URL que Paid usa | Media | Alto | Lista de URLs de pauta (1.7); no redirigir en Cyber |
| TI sin ventana para canonical/sitemaps hasta 2027 | Alta | Medio (se pierde el efecto en diciembre) | Pedir ventana ahora para la semana posterior a Cyber Days |
| Accesos a GSC/GA4 no llegan | Media | Alto (sin medición, sin confirmación de hallazgos) | Escalar con Elias en la semana 0; mientras, trabajar con fichas y HTML público |
| Capacidad del Senior absorbida por solicitudes de Marketing | Alta | Medio | Reserva explícita de horas; lista única de pedidos con prioridad de Elias |
| Malls sin CMS editable en 90 días | Alta | Medio | Solo diagnóstico y especificación; no prometer landings |
| Efectibank: datos no llegan o blog sin recursos de Contenidos | Media | Medio (estratégico, no urgente) | Auditoría técnica primero; contenido cuando haya capacidad |
| Falta de rastreador de pago: hallazgos basados en muestras | Alta | Medio | Muestras representativas + GSC; pedir presupuesto SF si el volumen lo justifica |
| El Niño corta despachos en el norte | Media-alta (`docs/05`) | Alto comercial | SEO local y "retiro en tienda" listos antes de enero |
| Atribuir al SEO efectos de precio, stock, pauta o clima | Alta | Credibilidad del área | Línea base, grupos de control de URLs, fechas marcadas |
