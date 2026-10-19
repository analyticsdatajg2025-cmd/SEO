-- r05 · Reparto de impresiones y clics por grupo y subgrupo (últimos 28 días). Muestra dónde está la visibilidad
-- y cuánto se va a promociones, pruebas u otros hosts.
WITH ultima AS (
  SELECT MAX(fecha) AS f FROM `__PROYECTO__.seo.grupo_dia`
  WHERE marca = @marca AND fecha >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
)
SELECT
  grupo, subgrupo,
  SUM(clics) AS clics,
  SUM(impresiones) AS impresiones,
  ROUND(100 * SAFE_DIVIDE(SUM(impresiones), SUM(SUM(impresiones)) OVER ()), 1) AS pct_impresiones,
  ROUND(100 * SAFE_DIVIDE(SUM(clics), SUM(SUM(clics)) OVER ()), 1) AS pct_clics,
  ROUND(SAFE_DIVIDE(SUM(suma_posicion), SUM(impresiones)) + 1, 1) AS posicion
FROM `__PROYECTO__.seo.grupo_dia`, ultima
WHERE marca = @marca AND tipo_busqueda = 'WEB'
  AND fecha >= DATE_SUB(CURRENT_DATE(), INTERVAL 60 DAY)
  AND fecha > DATE_SUB(ultima.f, INTERVAL 28 DAY)
GROUP BY 1, 2
ORDER BY impresiones DESC;
