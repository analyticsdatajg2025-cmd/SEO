-- r07 · Salud del flujo: último día en la exportación cruda y en los resúmenes. Si se separan, falló la consulta programada.
SELECT
  @marca AS marca,
  (SELECT MAX(data_date) FROM `__PROYECTO__.seo.v_gsc_sitio`
     WHERE marca = @marca AND data_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 15 DAY)) AS ultimo_dia_export,
  (SELECT MAX(fecha) FROM `__PROYECTO__.seo.url_dia`
     WHERE marca = @marca AND fecha >= DATE_SUB(CURRENT_DATE(), INTERVAL 15 DAY)) AS ultimo_dia_url_dia,
  (SELECT MAX(fecha) FROM `__PROYECTO__.seo.grupo_dia`
     WHERE marca = @marca AND fecha >= DATE_SUB(CURRENT_DATE(), INTERVAL 15 DAY)) AS ultimo_dia_grupo_dia,
  (SELECT MIN(fecha) FROM `__PROYECTO__.seo.url_dia` WHERE marca = @marca) AS primer_dia_historial,
  (SELECT COUNT(*) FROM `__PROYECTO__.seo.url_grupo` WHERE marca = @marca) AS urls_conocidas;
