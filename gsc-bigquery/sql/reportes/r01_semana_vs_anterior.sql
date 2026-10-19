-- r01 · Última semana completa (lun-dom) vs la anterior, por grupo de URL. Búsqueda web.
WITH ultima AS (
  SELECT DATE_SUB(DATE_TRUNC(DATE_ADD(MAX(fecha), INTERVAL 1 DAY), ISOWEEK), INTERVAL 7 DAY) AS semana
  FROM `__PROYECTO__.seo.grupo_dia`
  WHERE marca = @marca AND fecha >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
),
base AS (
  SELECT
    g.grupo,
    DATE_TRUNC(g.fecha, ISOWEEK) = u.semana AS actual,
    SUM(g.clics) AS clics, SUM(g.impresiones) AS impresiones, SUM(g.suma_posicion) AS suma_posicion
  FROM `__PROYECTO__.seo.grupo_dia` g, ultima u
  WHERE g.marca = @marca AND g.tipo_busqueda = 'WEB'
    AND g.fecha >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
    AND DATE_TRUNC(g.fecha, ISOWEEK) IN (u.semana, DATE_SUB(u.semana, INTERVAL 7 DAY))
  GROUP BY 1, 2
)
SELECT
  (SELECT semana FROM ultima) AS semana,
  grupo,
  SUM(IF(actual, clics, 0)) AS clics,
  SUM(IF(actual, 0, clics)) AS clics_ant,
  ROUND(100 * SAFE_DIVIDE(SUM(IF(actual, clics, 0)) - SUM(IF(actual, 0, clics)), SUM(IF(actual, 0, clics))), 1) AS var_clics_pct,
  SUM(IF(actual, impresiones, 0)) AS impresiones,
  SUM(IF(actual, 0, impresiones)) AS impr_ant,
  ROUND(100 * SAFE_DIVIDE(SUM(IF(actual, clics, 0)), SUM(IF(actual, impresiones, 0))), 2) AS ctr_pct,
  ROUND(SAFE_DIVIDE(SUM(IF(actual, suma_posicion, 0)), SUM(IF(actual, impresiones, 0))) + 1, 1) AS posicion,
  ROUND(SAFE_DIVIDE(SUM(IF(actual, 0, suma_posicion)), SUM(IF(actual, 0, impresiones))) + 1, 1) AS posicion_ant
FROM base
GROUP BY grupo
ORDER BY clics DESC;
