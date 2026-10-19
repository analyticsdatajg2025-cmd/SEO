-- 01 · Configuración de Efectibank: marca y reglas de grupos de URL.
-- Rutas COMPROBADAS en el sitemap de efectibank.pe (19-oct-2026, 238 URLs; 129 son promociones y campañas).
-- La regex de consultas de marca es HIPÓTESIS: validarla con el reporte r04 apenas haya datos.
-- Para cambiar reglas: editar este archivo, volver a correrlo y luego 21_reasignar_grupos.sql.

MERGE `__PROYECTO__.seo.marcas` m
USING (
  SELECT
    'efectibank' AS marca,
    'searchconsole_efectibank' AS dataset_gsc,
    'www.efectibank.pe' AS dominio,
    -- "efectiva" sola no basta: choca con "tasa efectiva anual".
    r'efect[iy] ?-?ban[ck]|(financiera|banco|caja|app|prestamos?|credito|cuenta) efectiva|^efectiva\b' AS regex_consulta_marca,
    TRUE AS activa
) s
ON m.marca = s.marca
WHEN MATCHED THEN UPDATE SET dataset_gsc = s.dataset_gsc, dominio = s.dominio,
  regex_consulta_marca = s.regex_consulta_marca, activa = s.activa
WHEN NOT MATCHED THEN INSERT ROW;

DELETE FROM `__PROYECTO__.seo.reglas_grupo_url` WHERE marca = 'efectibank';

INSERT INTO `__PROYECTO__.seo.reglas_grupo_url` (marca, prioridad, grupo, subgrupo, regex_ruta, nota)
VALUES
  -- Primero lo que no debería estar indexado (pruebas, duplicados "-2", portadas viejas)
  ('efectibank', 10, 'pruebas_basura', 'pruebas', r'^/(test|prueba|sample-page|hello-world|20261-2|home-nuevo-efectibank|portada-marzo-2023|blog-2|simulador-de-cuotas-2|efectiva-digital-2|campana-kfc-2|category)/', 'Candidatas a noindex/410'),
  ('efectibank', 20, 'home', 'home', r'^/$', NULL),

  -- Préstamos (el dinero: docs/08 §2)
  ('efectibank', 30, 'prestamos', 'efectivo_garantia', r'^/prestamos/prestamo/prestamo-efectivo-con-garantia-liquida/', NULL),
  ('efectibank', 31, 'prestamos', 'efectivo', r'^/prestamos/prestamo/prestamo-efectivo/', NULL),
  ('efectibank', 32, 'prestamos', 'electro', r'^/prestamos/prestamo/prestamo-electro/', NULL),
  ('efectibank', 33, 'prestamos', 'motos', r'^/prestamos/prestamo/prestamo-motos/', NULL),
  ('efectibank', 34, 'prestamos', 'hipotecario_mivivienda', r'^/(prestamos/prestamo/prestamo-hipotecario-mivivienda|adquisicion-de-vivienda-nueva-avn|construccion-sitio-propio)/', 'AVN y construcción: HIPÓTESIS, parecen MiVivienda'),
  ('efectibank', 35, 'prestamos', 'convenios', r'^/prestamos/convenios/', NULL),
  ('efectibank', 36, 'prestamos', 'negocios', r'^/prestamos/negocios/', 'Efectinegocio y proveedor'),
  ('efectibank', 39, 'prestamos', 'otros', r'^/prestamos/', 'Incluye /prestamos/producto-nuevo/'),
  ('efectibank', 40, 'solicitud', 'solicitar_prestamo', r'^/solicitar-prestamo/', 'Formulario: conversión'),
  ('efectibank', 41, 'simulador', 'simulador', r'^/simulador-de-cuotas/', NULL),

  -- Ahorros y pasivos
  ('efectibank', 50, 'ahorros', 'cuenta_ahorros', r'^/ahorros/cuenta-de-ahorros/', NULL),
  ('efectibank', 51, 'ahorros', 'deposito_plazo', r'^/ahorros/deposito-a-plazo/', NULL),
  ('efectibank', 52, 'ahorros', 'banca_preferente', r'^/(banca-preferente|landing-banca-preferente)/', NULL),
  ('efectibank', 53, 'ahorros', 'tarjeta_debito', r'^/tarjeta-debito/', NULL),

  -- Seguros
  ('efectibank', 60, 'seguros', 'vida', r'^/seguros/vida/', NULL),
  ('efectibank', 61, 'seguros', 'salud', r'^/seguros/salud/', NULL),
  ('efectibank', 62, 'seguros', 'patrimonio', r'^/seguros/patrimonio/', NULL),
  ('efectibank', 63, 'seguros', 'hogar', r'^/seguros/hogar/', NULL),
  ('efectibank', 64, 'seguros', 'accidentes', r'^/seguros/accidentes/', NULL),
  ('efectibank', 69, 'seguros', 'general', r'^/(seguros|segurosefectiva)/', NULL),

  -- Local, contenido, campañas
  ('efectibank', 70, 'agencias', 'agencias', r'^/agencias/', 'Hoy 1 sola página para 176 oficinas'),
  ('efectibank', 75, 'blog', 'articulos', r'^/(blog|que-es-[^/]+)/', 'Los artículos viven en la raíz (/que-es-...): HIPÓTESIS para los futuros'),
  ('efectibank', 80, 'promociones', 'promociones', r'^/(promociones-y-campanas|promociones-20[0-9]{2})/', 'Dilución: muchas vencidas'),
  ('efectibank', 81, 'promociones', 'campanas', r'^/campana-[^/]+/', NULL),
  ('efectibank', 85, 'landings', 'landings', r'^/(landing[^/]*|nuevalandingsimplificada|premium|c2f|aliados-efectiva-aliados|alianzas|clientes-aliados|conoce-a-maria)/', 'Landings de pauta y alianzas'),

  -- Servicio, atención, institucional
  ('efectibank', 90, 'servicios', 'pagos_remesas', r'^/(pago-de-servicios|pago-online|canales-de-pago|remesas)/', NULL),
  ('efectibank', 91, 'atencion', 'atencion', r'^/(preguntas-frecuentes|contactanos|procedimiento-de-atencion|derecho-de-arrepentimiento|devolucion-de-comisiones|gracias-devoluciones|actualizacion-de-datos|formulario-no-contactar|equipos-adquiridos-en-cuotas|seguridad|comunicado-[^/]+)/', NULL),
  ('efectibank', 92, 'institucional', 'legal_institucional', r'^/(quienes-somos|transparencia|informacion-al-inversionista|notas-de-prensa|linea-etica|trabaja-con-nosotros|aviso-legal|politica-[^/]+|terminos-[^/]+|tratamiento-de-datos[^/]*|clausulas-grupo-efe)/', NULL),

  ('efectibank', 999, 'otros', 'sin_regla', r'.*', 'Revisar con r06 y crear regla si pesa');
