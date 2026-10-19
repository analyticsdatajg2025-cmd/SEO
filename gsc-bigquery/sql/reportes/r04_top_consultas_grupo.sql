-- r04 · Top 10 consultas por grupo en las últimas 4 semanas, marcando si son de marca.
-- Sirve también para validar la regex de marca (seo.marcas): si una consulta de marca sale como no_marca, corregirla.
WITH base AS (
  SELECT
    grupo, consulta, tipo_consulta,
    SUM(clics) AS clics, SUM(impresiones) AS impresiones,
    ROUND(SAFE_DIVIDE(SUM(suma_posicion), SUM(impresiones)) + 1, 1) AS posicion
  FROM `__PROYECTO__.seo.consulta_grupo_semana`
  WHERE marca = @marca
    AND semana >= DATE_SUB(DATE_TRUNC(CURRENT_DATE(), ISOWEEK), INTERVAL 4 WEEK)
  GROUP BY 1, 2, 3
)
SELECT * EXCEPT (n)
FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY grupo ORDER BY impresiones DESC) AS n FROM base
)
WHERE n <= 10
ORDER BY grupo, impresiones DESC;
