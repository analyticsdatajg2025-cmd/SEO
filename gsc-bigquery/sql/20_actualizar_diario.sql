-- 20 · Actualización diaria (consulta programada en BigQuery; no usa Claude ni tokens).
-- Reprocesa los últimos `dias` días para absorber datos que GSC publica con retraso.
-- Solo lee particiones recientes de las tablas crudas: el costo crece con los días reprocesados, no con el historial.

DECLARE dias INT64 DEFAULT 5;
DECLARE desde DATE DEFAULT DATE_SUB(CURRENT_DATE(), INTERVAL dias DAY);
DECLARE semana_desde DATE DEFAULT DATE_TRUNC(desde, ISOWEEK);
-- Umbral de impresiones para guardar una consulta por grupo y semana. 1 = todo (sirve para Efectibank);
-- subirlo (p. ej. a 5) en sitios de 100 K URLs si la tabla crece demasiado.
DECLARE min_impresiones_consulta INT64 DEFAULT 1;

BEGIN TRANSACTION;

-- 1. Por URL y día
DELETE FROM `__PROYECTO__.seo.url_dia` WHERE fecha >= desde;
INSERT INTO `__PROYECTO__.seo.url_dia`
SELECT
  data_date, marca, url, device, search_type, country = 'per',
  SUM(clicks), SUM(impressions), SUM(sum_position), 'export'
FROM `__PROYECTO__.seo.v_gsc_url`
WHERE data_date >= desde
GROUP BY 1, 2, 3, 4, 5, 6;

-- 2. Totales del sitio con marca / no marca
DELETE FROM `__PROYECTO__.seo.sitio_dia` WHERE fecha >= desde;
INSERT INTO `__PROYECTO__.seo.sitio_dia`
SELECT
  s.data_date, s.marca, s.device, s.search_type, s.country = 'per',
  CASE
    WHEN s.is_anonymized_query OR s.query IS NULL THEN 'anonimizada'
    WHEN REGEXP_CONTAINS(LOWER(s.query), m.regex_consulta_marca) THEN 'marca'
    ELSE 'no_marca'
  END,
  SUM(s.clicks), SUM(s.impressions), SUM(s.sum_top_position), 'export'
FROM `__PROYECTO__.seo.v_gsc_sitio` s
JOIN `__PROYECTO__.seo.marcas` m USING (marca)
WHERE s.data_date >= desde
GROUP BY 1, 2, 3, 4, 5, 6;

-- 3. Grupo para las URLs que aparecen por primera vez
INSERT INTO `__PROYECTO__.seo.url_grupo`
WITH nuevas AS (
  SELECT DISTINCT u.marca, u.url
  FROM `__PROYECTO__.seo.url_dia` u
  LEFT JOIN `__PROYECTO__.seo.url_grupo` g ON g.marca = u.marca AND g.url = u.url
  WHERE u.fecha >= desde AND g.url IS NULL
),
normalizadas AS (
  SELECT
    marca, url,
    LOWER(REGEXP_EXTRACT(url, r'^https?://([^/?#]+)')) AS host,
    CONCAT(RTRIM(LOWER(COALESCE(REGEXP_EXTRACT(url, r'^https?://[^/?#]+([^?#]*)'), '')), '/'), '/') AS ruta
  FROM nuevas
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

-- 4. Grupo por día (lo que lee el dashboard)
DELETE FROM `__PROYECTO__.seo.grupo_dia` WHERE fecha >= desde;
INSERT INTO `__PROYECTO__.seo.grupo_dia`
SELECT
  u.fecha, u.marca,
  COALESCE(g.grupo, 'sin_asignar'), COALESCE(g.subgrupo, 'sin_asignar'),
  u.dispositivo, u.tipo_busqueda, u.es_peru,
  SUM(u.clics), SUM(u.impresiones), SUM(u.suma_posicion),
  COUNT(DISTINCT IF(u.impresiones > 0, u.url, NULL))
FROM `__PROYECTO__.seo.url_dia` u
LEFT JOIN `__PROYECTO__.seo.url_grupo` g ON g.marca = u.marca AND g.url = u.url
WHERE u.fecha >= desde
GROUP BY 1, 2, 3, 4, 5, 6, 7;

-- 5. Consultas por grupo y semana (semanas tocadas por la ventana)
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
GROUP BY 1, 2, 3, 4, 5
HAVING SUM(t.impressions) >= min_impresiones_consulta;

COMMIT TRANSACTION;
