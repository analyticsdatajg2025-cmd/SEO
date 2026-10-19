-- 00 · Dataset y tablas del modelo SEO (una sola vez; es idempotente).
-- __PROYECTO__ y __UBICACION__ los reemplaza scripts/desplegar.sh.
-- La ubicación debe ser la MISMA que eligió GSC para la exportación (si no, BigQuery no puede cruzarlas).

CREATE SCHEMA IF NOT EXISTS `__PROYECTO__.seo`
OPTIONS (location = '__UBICACION__', description = 'Modelo SEO Grupo EFE: resúmenes de GSC por marca');

-- Una fila por marca (sitio). Agregar LC, EFE, Juntoz aquí cuando se activen.
CREATE TABLE IF NOT EXISTS `__PROYECTO__.seo.marcas` (
  marca STRING NOT NULL,                 -- efectibank, lacuracao, efe, juntoz...
  dataset_gsc STRING NOT NULL,           -- dataset de la exportación de GSC (searchconsole_<marca>)
  dominio STRING NOT NULL,               -- host principal; otros hosts caen en grupo 'otro_host'
  regex_consulta_marca STRING NOT NULL,  -- RE2 sobre la consulta en minúsculas
  activa BOOL NOT NULL
);

-- Reglas de grupos de URL. Gana la de menor prioridad que coincida con la ruta normalizada
-- (minúsculas, sin ?query ni #fragmento, terminada en '/').
CREATE TABLE IF NOT EXISTS `__PROYECTO__.seo.reglas_grupo_url` (
  marca STRING NOT NULL,
  prioridad INT64 NOT NULL,
  grupo STRING NOT NULL,
  subgrupo STRING NOT NULL,
  regex_ruta STRING NOT NULL,
  nota STRING
);

-- URL → grupo. Se llena solo con URLs nuevas cada día; se reconstruye con 21_reasignar_grupos.sql.
CREATE TABLE IF NOT EXISTS `__PROYECTO__.seo.url_grupo` (
  marca STRING NOT NULL,
  url STRING NOT NULL,
  host STRING,
  ruta STRING,
  grupo STRING NOT NULL,
  subgrupo STRING NOT NULL,
  asignado_en TIMESTAMP NOT NULL
)
CLUSTER BY marca, url;

-- Por URL y día, sin la dimensión consulta (mucho más chica que la tabla cruda).
-- suma_posicion es base 0, como en la exportación: posición media = suma_posicion / impresiones + 1.
CREATE TABLE IF NOT EXISTS `__PROYECTO__.seo.url_dia` (
  fecha DATE NOT NULL,
  marca STRING NOT NULL,
  url STRING NOT NULL,
  dispositivo STRING,
  tipo_busqueda STRING,
  es_peru BOOL,
  clics INT64,
  impresiones INT64,
  suma_posicion FLOAT64,
  fuente STRING                          -- 'export' (BigQuery) o 'api' (carga de historial)
)
PARTITION BY fecha
CLUSTER BY marca, url;

-- Totales del sitio por día (agregado por propiedad), separados en consultas de marca / no marca / anonimizadas.
CREATE TABLE IF NOT EXISTS `__PROYECTO__.seo.sitio_dia` (
  fecha DATE NOT NULL,
  marca STRING NOT NULL,
  dispositivo STRING,
  tipo_busqueda STRING,
  es_peru BOOL,
  tipo_consulta STRING,                  -- marca / no_marca / anonimizada
  clics INT64,
  impresiones INT64,
  suma_posicion FLOAT64,
  fuente STRING
)
PARTITION BY fecha
CLUSTER BY marca;

-- Lo que lee el dashboard: grupo de URL por día.
CREATE TABLE IF NOT EXISTS `__PROYECTO__.seo.grupo_dia` (
  fecha DATE NOT NULL,
  marca STRING NOT NULL,
  grupo STRING,
  subgrupo STRING,
  dispositivo STRING,
  tipo_busqueda STRING,
  es_peru BOOL,
  clics INT64,
  impresiones INT64,
  suma_posicion FLOAT64,
  urls_con_impresion INT64
)
PARTITION BY fecha
CLUSTER BY marca, grupo;

-- Consultas por grupo y semana ISO (lunes). Solo búsqueda web y consultas no anonimizadas.
CREATE TABLE IF NOT EXISTS `__PROYECTO__.seo.consulta_grupo_semana` (
  semana DATE NOT NULL,
  marca STRING NOT NULL,
  grupo STRING,
  consulta STRING,
  tipo_consulta STRING,
  clics INT64,
  impresiones INT64,
  suma_posicion FLOAT64
)
PARTITION BY semana
CLUSTER BY marca, grupo;
