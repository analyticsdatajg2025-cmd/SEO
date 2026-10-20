"""Pruebas del generador. Correr desde landings/bcp:  python3 -m unittest discover -s tests

Los datos de campaña de estas pruebas son ficticios (código PRUEBA15) y solo sirven para probar.
"""
import copy
import datetime as dt
import re
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import generador as g  # noqa: E402

HOY = dt.date(2026, 10, 20)
LEGAL = ("Promoción válida del 21 al 28 de octubre de 2026 con el código PRUEBA15.\n"
         "15% de descuento hasta S/200 desde S/399. Texto «de prueba» & <sin> HTML.")


def fixture():
    cfg = {k: d for k, _, _, d, _ in g.CONFIG}
    cfg.update({"campana": "Prueba", "codigo": "PRUEBA15", "porcentaje": "15", "tope": "200", "minimo": "399",
                "fecha_inicio": "2026-10-21", "fecha_fin": "28/10/2026", "tarjetas": "Tarjetas de crédito y débito BCP",
                "legales_aprobados": "SI", "legales_aprobado_por": "Equipo de prueba", "legales_fecha_aprobacion": "2026-10-19"})
    return {
        "Config": [g.COLUMNAS["Config"]] + [[k, v, ""] for k, v in cfg.items()],
        "Textos": [g.COLUMNAS["Textos"]] + [[k, d, ""] for k, _, d, _ in g.TEXTOS],
        "Slides": [g.COLUMNAS["Slides"]] + copy.deepcopy(g.EJEMPLO["Slides"]),
        "Productos": [g.COLUMNAS["Productos"]] + copy.deepcopy(g.EJEMPLO["Productos"]),
        "Beneficios": [g.COLUMNAS["Beneficios"]] + copy.deepcopy(g.EJEMPLO["Beneficios"]),
        "Pasos": [g.COLUMNAS["Pasos"]] + copy.deepcopy(g.EJEMPLO["Pasos"]),
        "FAQ": [g.COLUMNAS["FAQ"]] + copy.deepcopy(g.EJEMPLO["FAQ"]),
        "Legales": [g.COLUMNAS["Legales"], [1, LEGAL]],
    }


def config(datos, clave, valor):
    for fila in datos["Config"][1:]:
        if fila[0] == clave:
            fila[1] = valor


def final(datos):
    ctx, inf, _ = g.construir(datos, HOY)
    html = g.renderizar(ctx, "final", "prueba")
    g.revisar_final(html, inf)
    return html, inf


class Generador(unittest.TestCase):
    def test_datos_completos_generan_html_publicable(self):
        html, inf = final(fixture())
        self.assertEqual(inf.errores, [])
        self.assertNotIn("<script", html)
        self.assertNotIn("data-field", html)
        self.assertNotIn("onclick", html)
        self.assertEqual(len(re.findall(r"<h1\b", html)), 1)
        self.assertIn("Ahorra hasta <span>15%</span> pagando con tus tarjetas BCP", html)
        self.assertIn("del 21 al 28 de octubre de 2026", html)
        self.assertIn("--bcp-blue:#0030B2", html)
        self.assertEqual(html.count('class="bcp-product"'), 8)
        self.assertIn("PRUEBA15", html)

    def test_legales_se_publican_sin_cambiar_la_redaccion(self):
        html, _ = final(fixture())
        esperado = str(g.escape(LEGAL)).replace("\n", "<br>")
        self.assertIn(esperado, html)

    def test_sin_legales_aprobados_no_se_publica(self):
        d = fixture()
        config(d, "legales_aprobados", "NO")
        _, inf = final(d)
        self.assertTrue(any("legales_aprobados" in e for e in inf.errores))

    def test_campo_obligatorio_vacio_bloquea(self):
        d = fixture()
        config(d, "codigo", "")
        _, inf = final(d)
        self.assertTrue(any("codigo" in e for e in inf.errores))
        self.assertTrue(any("sin completar" in e for e in inf.errores))

    def test_campana_vencida_bloquea(self):
        d = fixture()
        config(d, "fecha_inicio", "2026-09-01")
        config(d, "fecha_fin", "2026-09-30")
        _, inf = final(d)
        self.assertTrue(any("venció" in e for e in inf.errores))

    def test_enlace_fuera_de_dominio_y_ancla_inexistente(self):
        d = fixture()
        d["Productos"][1][6] = "https://otro-sitio.com/p/1"
        d["Slides"][1][7] = "#no-existe"
        _, inf = final(d)
        self.assertTrue(any("otro-sitio.com" in e for e in inf.errores))
        self.assertTrue(any("#no-existe" in e for e in inf.errores))

    def test_url_no_https_y_javascript(self):
        d = fixture()
        d["Productos"][2][4] = "http://juntoz.com/img.jpg"
        d["Productos"][3][6] = "javascript:alert(1)"
        html, inf = final(d)
        self.assertEqual(len([e for e in inf.errores if "https" in e]), 2)
        self.assertNotIn("javascript:", html)

    def test_visibilidad_y_orden(self):
        d = fixture()
        d["Productos"][1][1] = "NO"          # oculta el iPhone
        d["Productos"][8][0] = 0             # Hugo Boss primero
        html, inf = final(d)
        self.assertEqual(inf.errores, [])
        self.assertNotIn("IPHONE 18", html)
        self.assertLess(html.index("Hugo Boss Bottled"), html.index("SAMSUNG S26"))

    def test_opcionales_vacios_no_rompen(self):
        d = fixture()
        d["Slides"][1][3] = ""                        # sin descripción
        d["Slides"][1][8] = d["Slides"][1][9] = ""    # sin segundo botón
        d["Productos"][1][8] = ""                     # sin etiqueta
        d["Pasos"] = [g.COLUMNAS["Pasos"]]            # sin pasos: sección oculta
        html, inf = final(d)
        self.assertEqual(inf.errores, [])
        self.assertNotIn('class="bcp-product__tag"', html)
        self.assertNotIn("bcp-btn--ghost\" href", html)
        self.assertNotIn('id="bcp-como-usar"', html)
        self.assertNotRegex(html, r"<p[^>]*></p>")

    def test_variable_desconocida_y_marcador(self):
        d = fixture()
        d["FAQ"][1][3] = "Usa {cupon}"
        d["Pasos"][1][3] = "Monto [XX]"
        _, inf = final(d)
        self.assertTrue(any("{cupon}" in e for e in inf.errores))
        self.assertTrue(any("[XX]" in e for e in inf.errores))

    def test_negrita_y_escape(self):
        d = fixture()
        d["FAQ"][1][3] = "**Ojo** <b>no</b> pasa"
        html, _ = final(d)
        self.assertIn("<strong>Ojo</strong> &lt;b&gt;no&lt;/b&gt; pasa", html)

    def test_varios_slides_un_solo_h1(self):
        d = fixture()
        d["Slides"].append([2, "SI", "Segundo slide", "", "https://mcprod.efe.com.pe/media/wysiwyg/x.png", "Alt", "Ver", "#bcp-productos", "", ""])
        html, inf = final(d)
        self.assertEqual(inf.errores, [])
        self.assertEqual(len(re.findall(r"<h1\b", html)), 1)
        self.assertIn('<h2 class="bcp-h1">Segundo slide</h2>', html)
        self.assertIn('href="#bcp-slide-2"', html)
        self.assertIn('loading="lazy"', html)

    def test_color_invalido(self):
        d = fixture()
        config(d, "color_principal", "azul")
        _, inf = final(d)
        self.assertTrue(any("color_principal" in e for e in inf.errores))

    def test_css_encapsulado(self):
        html, _ = final(fixture())
        inf = g.Informe()
        g.revisar_final(html.replace("</style>", "body{margin:0}</style>"), inf)
        self.assertTrue(any("body" in e for e in inf.errores))

    def test_preview_tiene_data_field_y_marca_faltantes(self):
        d = fixture()
        config(d, "tope", "")
        ctx, inf, _ = g.construir(d, HOY)
        prev = g.documento_preview(g.renderizar(ctx, "preview", "x"), inf, "prueba", False)
        self.assertIn('data-field="Productos fila 2.nombre"', prev)
        self.assertIn('<mark class="pv-falta">FALTA: Config, tope</mark>', prev)

    def test_registros_con_filas_irregulares(self):
        filas = [["Orden", "Visible", "Título"], ["1", "TRUE"], [], ["2", "no", "x", "extra"]]
        regs = g.a_registros(filas)
        self.assertEqual(len(regs), 2)
        self.assertEqual(regs[0]["titulo"], "")
        self.assertEqual(regs[1]["_fila"], 4)
        self.assertTrue(g.es_visible(regs[0]["visible"]))

    def test_plantilla_xlsx_y_publicacion_con_respaldo(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            plantilla = tmp / "plantilla.xlsx"
            g.crear_plantilla(plantilla)
            base = ["previsualizar", "--fuente", "xlsx", "--archivo", str(plantilla), "--hoy", "2026-10-20",
                    "--salida", str(tmp / "salida")]
            self.assertEqual(g.main(base), 1)  # plantilla sin datos de campaña: no publicable
            self.assertTrue((tmp / "salida" / "bcp-landing.preview.html").exists())

            from openpyxl import Workbook
            wb = Workbook()
            wb.remove(wb.active)
            for nombre, filas in fixture().items():
                ws = wb.create_sheet(nombre)
                for f in filas:
                    ws.append(f)
            datos = tmp / "datos.xlsx"
            wb.save(datos)
            pub = ["publicar", "--fuente", "xlsx", "--archivo", str(datos), "--hoy", "2026-10-20",
                   "--salida", str(tmp / "salida"), "--publicado", str(tmp / "pub"), "--respaldos", str(tmp / "resp")]
            self.assertEqual(g.main(pub), 0)
            self.assertTrue((tmp / "pub" / "bcp-landing.html").exists())
            self.assertEqual(g.main(pub), 0)
            self.assertEqual(len(list((tmp / "resp").glob("*.html"))), 1)


class LecturaSheets(unittest.TestCase):
    def test_lee_pestanas_con_cuenta_de_servicio(self):
        from unittest import mock
        try:
            import google.oauth2.service_account  # noqa: F401
        except ImportError:
            self.skipTest("google-auth no instalado")
        resp = mock.Mock(status_code=200)
        resp.json.return_value = {"valueRanges": [{"values": [["clave", "valor"], ["banco", "BCP"]]}] + [{}] * 7}
        with tempfile.TemporaryDirectory() as tmp, \
                mock.patch("google.oauth2.service_account.Credentials.from_service_account_file") as cred, \
                mock.patch("google.auth.transport.requests.AuthorizedSession") as sesion:
            ruta = Path(tmp) / "cuenta.json"
            ruta.write_text("{}")
            sesion.return_value.get.return_value = resp
            datos = g.leer_sheets("ID_DE_PRUEBA", str(ruta))
            self.assertEqual(cred.call_args.kwargs["scopes"], ["https://www.googleapis.com/auth/spreadsheets.readonly"])
            url = sesion.return_value.get.call_args.args[0]
            self.assertIn("/spreadsheets/ID_DE_PRUEBA/values:batchGet", url)
            self.assertEqual(datos["Config"], [["clave", "valor"], ["banco", "BCP"]])
            self.assertEqual(datos["Legales"], [])

    def test_rechaza_credenciales_dentro_del_repo(self):
        try:
            import google.oauth2.service_account  # noqa: F401
        except ImportError:
            self.skipTest("google-auth no instalado")
        with self.assertRaises(SystemExit):
            g.leer_sheets("ID", str(Path(g.__file__)))


if __name__ == "__main__":
    unittest.main()
