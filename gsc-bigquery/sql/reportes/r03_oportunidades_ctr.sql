-- r03 · URLs en posición 4-15 con muchas impresiones (últimos 28 días): las más cerca de ganar clics
-- con título, meta descripción o contenido. Ajustar el umbral de impresiones al tamaño del sitio.
WITH ultima AS (
  SELECT MAX(fecha) AS f FROM `__PROYECTO__.seo.url_dia`
  WHERE marca = @marca AND fecha >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
)
SELECT
  g.grupo, u.url,
  SUM(u.impresiones) AS impresiones,
  SUM(u.clics) AS clics,
  ROUND(100 * SAFE_DIVIDE(SUM(u.clics), SUM(u.impresiones)), 2) AS ctr_pct,
  ROUND(SAFE_DIVIDE(SUM(u.suma_posicion), SUM(u.impresiones)) + 1, 1) AS posicion
FROM `__PROYECTO__.seo.url_dia` u
CROSS JOIN ultima
LEFT JOIN `__PROYECTO__.seo.url_grupo` g ON g.marca = u.marca AND g.url = u.url
WHERE u.marca = @marca AND u.tipo_busqueda = 'WEB'
  AND u.fecha >= DATE_SUB(CURRENT_DATE(), INTERVAL 60 DAY)
  AND u.fecha > DATE_SUB(ultima.f, INTERVAL 28 DAY)
GROUP BY 1, 2
HAVING SUM(u.impresiones) >= 100
  AND SAFE_DIVIDE(SUM(u.suma_posicion), SUM(u.impresiones)) + 1 BETWEEN 4 AND 15
ORDER BY impresiones DESC
LIMIT 30;
