-- 02 · Vistas que unen las exportaciones de GSC de todas las marcas con una columna `marca`.
-- Al sumar una marca: copiar el bloque comentado, cambiar marca y dataset, y volver a correr este archivo.
-- Siempre filtrar por data_date al consultarlas: las tablas crudas están particionadas por día.

CREATE OR REPLACE VIEW `__PROYECTO__.seo.v_gsc_url` AS
SELECT 'efectibank' AS marca, t.*
FROM `__PROYECTO__.searchconsole_efectibank.searchdata_url_impression` t
-- UNION ALL
-- SELECT 'lacuracao' AS marca, t.* FROM `__PROYECTO__.searchconsole_lacuracao.searchdata_url_impression` t
;

CREATE OR REPLACE VIEW `__PROYECTO__.seo.v_gsc_sitio` AS
SELECT 'efectibank' AS marca, t.*
FROM `__PROYECTO__.searchconsole_efectibank.searchdata_site_impression` t
-- UNION ALL
-- SELECT 'lacuracao' AS marca, t.* FROM `__PROYECTO__.searchconsole_lacuracao.searchdata_site_impression` t
;

CREATE OR REPLACE VIEW `__PROYECTO__.seo.v_gsc_exportlog` AS
SELECT 'efectibank' AS marca, t.*
FROM `__PROYECTO__.searchconsole_efectibank.ExportLog` t
;
