-- 21 · Reasignar grupos a TODAS las URLs y recalcular los resúmenes.
-- Correr a mano después de cambiar reglas (01_config_*.sql) o de cargar historial con la API.
-- Más caro que el diario: lee todo url_dia y `semanas_consultas` semanas de la tabla cruda.

DECLARE semanas_consultas INT64 DEFAULT 16;
DECLARE semana_desde DATE DEFAULT DATE_SUB(DATE_TRUNC(CURRENT_DATE(), ISOWEEK), INTERVAL semanas_consultas WEEK);

BEGIN TRANSACTION;

DELETE FROM `__PROYECTO__.seo.url_grupo` WHERE TRUE;
INSERT INTO `__PROYECTO__.seo.url_grupo`
WITH todas AS (
  SELECT DISTINCT marca, url FROM `__PROYECTO__.seo.url_dia`
),
normalizadas AS (
  SELECT
    marca, url,
    LOWER(REGEXP_EXTRACT(url, r'^https?://([^/?#]+)')) AS host,
    CONCAT(RTRIM(LOWER(COALESCE(REGEXP_EXTRACT(url, r'^https?://[^/?#]+([^?#]*)'), '')), '/'), '/') AS ruta
  FROM todas
),
con_regla AS (
  SELECT
    n.marca, n.url, n.host, n.ruta,
    ARRAY_AGG(STRUCT(r.grupo, r.subgrupo) ORDER BY r.prioridad LIMIT 1)[OFFSET(0)] AS regla
  FROM normalizadas n
  LEFT JOIN `__PROYECTO__.seo.reglas_grupo_url` r
    ON r.marca = n.marca AND REGEXP_CONTAINS(n.ruta, r.regex_ruta)
  GROUP BY 1, 2, 3, 4
)
SELECT
  c.marca, c.url, c.host, c.ruta,
  IF(COALESCE(c.host, '') = m.dominio, COALESCE(c.regla.grupo, 'otros'), 'otro_host'),
  IF(COALESCE(c.host, '') = m.dominio, COALESCE(c.regla.subgrupo, 'sin_regla'), COALESCE(c.host, 'sin_host')),
  CURRENT_TIMESTAMP()
FROM con_regla c
JOIN `__PROYECTO__.seo.marcas` m USING (marca);

DELETE FROM `__PROYECTO__.seo.grupo_dia` WHERE TRUE;
INSERT INTO `__PROYECTO__.seo.grupo_dia`
SELECT
  u.fecha, u.marca,
  COALESCE(g.grupo, 'sin_asignar'), COALESCE(g.subgrupo, 'sin_asignar'),
  u.dispositivo, u.tipo_busqueda, u.es_peru,
  SUM(u.clics), SUM(u.impresiones), SUM(u.suma_posicion),
  COUNT(DISTINCT IF(u.impresiones > 0, u.url, NULL))
FROM `__PROYECTO__.seo.url_dia` u
LEFT JOIN `__PROYECTO__.seo.url_grupo` g ON g.marca = u.marca AND g.url = u.url
GROUP BY 1, 2, 3, 4, 5, 6, 7;

DELETE FROM `__PROYECTO__.seo.consulta_grupo_semana` WHERE semana >= semana_desde;
INSERT INTO `__PROYECTO__.seo.consulta_grupo_semana`
SELECT
  DATE_TRUNC(t.data_date, ISOWEEK), t.marca,
  COALESCE(g.grupo, 'sin_asignar'), LOWER(t.query),
  IF(REGEXP_CONTAINS(LOWER(t.query), m.regex_consulta_marca), 'marca', 'no_marca'),
  SUM(t.clicks), SUM(t.impressions), SUM(t.sum_position)
FROM `__PROYECTO__.seo.v_gsc_url` t
JOIN `__PROYECTO__.seo.marcas` m USING (marca)
LEFT JOIN `__PROYECTO__.seo.url_grupo` g ON g.marca = t.marca AND g.url = t.url
WHERE t.data_date >= semana_desde
  AND t.search_type = 'WEB'
  AND NOT t.is_anonymized_query
  AND t.query IS NOT NULL
GROUP BY 1, 2, 3, 4, 5;

COMMIT TRANSACTION;
