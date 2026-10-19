-- r02 · Clics e impresiones por tipo de consulta (marca / no marca / anonimizada), últimas 8 semanas. Búsqueda web.
-- Lo que crece en "no_marca" es demanda nueva que gana el SEO; "marca" la trae la marca y la pauta.
SELECT
  DATE_TRUNC(fecha, ISOWEEK) AS semana,
  tipo_consulta,
  SUM(clics) AS clics,
  SUM(impresiones) AS impresiones,
  ROUND(100 * SAFE_DIVIDE(SUM(clics), SUM(impresiones)), 2) AS ctr_pct,
  ROUND(SAFE_DIVIDE(SUM(suma_posicion), SUM(impresiones)) + 1, 1) AS posicion
FROM `__PROYECTO__.seo.sitio_dia`
WHERE marca = @marca AND tipo_busqueda = 'WEB'
  AND fecha >= DATE_SUB(DATE_TRUNC(CURRENT_DATE(), ISOWEEK), INTERVAL 8 WEEK)
GROUP BY 1, 2
ORDER BY semana DESC, tipo_consulta;
