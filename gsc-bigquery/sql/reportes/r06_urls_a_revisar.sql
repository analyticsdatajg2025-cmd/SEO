-- r06 · URLs de pruebas, promociones, otros hosts o sin regla que reciben impresiones (últimos 28 días).
-- Candidatas a noindex, redirección o a una regla nueva en 01_config_<marca>.sql.
WITH ultima AS (
  SELECT MAX(fecha) AS f FROM `__PROYECTO__.seo.url_dia`
  WHERE marca = @marca AND fecha >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
)
SELECT
  g.grupo, g.subgrupo, u.url,
  SUM(u.impresiones) AS impresiones,
  SUM(u.clics) AS clics
FROM `__PROYECTO__.seo.url_dia` u
CROSS JOIN ultima
JOIN `__PROYECTO__.seo.url_grupo` g ON g.marca = u.marca AND g.url = u.url
WHERE u.marca = @marca
  AND u.fecha >= DATE_SUB(CURRENT_DATE(), INTERVAL 60 DAY)
  AND u.fecha > DATE_SUB(ultima.f, INTERVAL 28 DAY)
  AND g.grupo IN ('pruebas_basura', 'promociones', 'otro_host', 'otros')
GROUP BY 1, 2, 3
ORDER BY impresiones DESC
LIMIT 40;
