#!/usr/bin/env python3
"""Genera el dashboard de Search Console de Efectibank con datos reales.

Qué hace
  1. Lee la cuenta de servicio: --clave ruta/a/la-clave.json o la variable
     GOOGLE_APPLICATION_CREDENTIALS_JSON (nunca la imprime ni la guarda).
  2. Lista las propiedades que ve la cuenta y elige la de efectibank.pe
     (prefiere la de dominio). Si no está, se detiene y dice cuáles sí ve.
  3. Pide a la API de Search Console (tipo web):
       - la serie diaria de los últimos 16 meses (dimensión date);
       - para 7, 28, 90 y 365 días, y para el período anterior del mismo largo:
         consultas, páginas, dispositivos y países.
  4. Incrusta todo en dashboards/gsc-efectibank.html (marcador
     /*__GSC_EMBED__*/null) y escribe el HTML con datos FUERA del repo.

El dashboard separa marca / no marca y agrupa las URLs (préstamos, ahorros,
seguros, agencias...) en el navegador, con las reglas de gsc-bigquery
(sitemap del 19-oct-2026). Así la regla se puede ajustar sin volver a extraer.

Regla del repo: el HTML con datos es un exporte de GSC y NO va al repo.

Uso
  python3 scripts/gsc_efectibank.py --listar --clave ~/claves/gsc.json
  python3 scripts/gsc_efectibank.py --clave ~/claves/gsc.json --html-out ~/gsc-efectibank.html

Requiere: google-auth y requests (pip install google-auth requests).
"""
import argparse
import datetime as dt
import json
import os
import re
import sys
import time
from urllib.parse import quote

API = "https://searchconsole.googleapis.com/webmasters/v3"
SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANTILLA = os.path.join(REPO, "dashboards", "gsc-efectibank.html")
MARCADOR = "/*__GSC_EMBED__*/null"
DOMINIO = "efectibank.pe"
RANGOS = (7, 28, 90, 365)
FILAS_POR_PAGINA = 25000
MAX_CONSULTAS = 5000  # por período; las más chicas no cambian la lectura y pesan en el HTML


def sesion(ruta_clave):
    try:
        from google.oauth2 import service_account
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        sys.exit("Falta google-auth: pip install google-auth requests")
    if ruta_clave:
        with open(os.path.expanduser(ruta_clave), encoding="utf-8") as f:
            info = json.load(f)
    else:
        raw = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_JSON")
        if not raw:
            sys.exit("Falta la clave: usa --clave ruta.json o la variable GOOGLE_APPLICATION_CREDENTIALS_JSON.")
        try:
            info = json.loads(raw)
        except ValueError:
            info = None
    if not isinstance(info, dict) or not info.get("private_key"):
        sys.exit("La clave no es el JSON de una cuenta de servicio (falta private_key).")
    cred = service_account.Credentials.from_service_account_info(info, scopes=[SCOPE])
    return AuthorizedSession(cred)


def pedir(s, metodo, url, **kw):
    """Llamada con reintentos ante errores temporales (429 / 5xx / red)."""
    for intento in range(5):
        try:
            r = s.request(metodo, url, timeout=120, **kw)
        except Exception as e:
            if intento == 4:
                sys.exit(f"Error de red llamando a Search Console: {type(e).__name__}: {e}")
            time.sleep(2 ** intento)
            continue
        if r.status_code in (429, 500, 502, 503, 504) and intento < 4:
            time.sleep(2 ** intento)
            continue
        if r.status_code != 200:
            sys.exit(f"Search Console respondió {r.status_code}: {r.text[:500]}")
        return r.json()


def es_de_efectibank(url):
    u = url.lower()
    if u.startswith("sc-domain:"):
        return u == f"sc-domain:{DOMINIO}"
    host = re.sub(r"^https?://", "", u).split("/")[0]
    return host == DOMINIO or host.endswith("." + DOMINIO)


def elegir_propiedad(sitios, pedida):
    urls = [x["siteUrl"] for x in sitios if x.get("permissionLevel") != "siteUnverifiedUser"]
    if pedida:
        return pedida if pedida in urls else None
    propias = [u for u in urls if es_de_efectibank(u)]
    propias.sort(key=lambda u: (not u.startswith("sc-domain:"), "www." not in u, not u.startswith("https")))
    return propias[0] if propias else None


def consulta(s, sitio, desde, hasta, dimensiones, tope=None):
    url = f"{API}/sites/{quote(sitio, safe='')}/searchAnalytics/query"
    filas, inicio = [], 0
    while True:
        cuerpo = {"startDate": desde.isoformat(), "endDate": hasta.isoformat(), "dimensions": dimensiones,
                  "type": "web", "rowLimit": FILAS_POR_PAGINA, "startRow": inicio}
        rows = pedir(s, "POST", url, json=cuerpo).get("rows", [])
        filas.extend(rows)
        if len(rows) < FILAS_POR_PAGINA or (tope and len(filas) >= tope):
            break
        inicio += FILAS_POR_PAGINA
    return filas[:tope] if tope else filas


def fila(r, clave=True):
    f = {"clics": int(r["clicks"]), "impresiones": int(r["impressions"]),
         "ctr": round(r["ctr"], 4), "posicion": round(r["position"], 1)}
    return {"clave": r["keys"][0], **f} if clave else f


def tablas(s, sitio, desde, hasta):
    return {
        "desde": desde.isoformat(), "hasta": hasta.isoformat(),
        "consultas": [fila(r) for r in consulta(s, sitio, desde, hasta, ["query"], MAX_CONSULTAS)],
        "paginas": [fila(r) for r in consulta(s, sitio, desde, hasta, ["page"])],
        "dispositivos": [fila(r) for r in consulta(s, sitio, desde, hasta, ["device"])],
        "paises": [fila(r) for r in consulta(s, sitio, desde, hasta, ["country"])],
    }


def fuera_del_repo(ruta):
    real = os.path.realpath(os.path.expanduser(ruta))
    if real == REPO or real.startswith(REPO + os.sep):
        sys.exit(f"No escribo el HTML con datos dentro del repo ({ruta}): los exportes de GSC no se suben.")
    os.makedirs(os.path.dirname(real) or ".", exist_ok=True)
    return real


def main():
    ap = argparse.ArgumentParser(description="Dashboard de Search Console de Efectibank.")
    ap.add_argument("--clave", help="JSON de la cuenta de servicio (si no, GOOGLE_APPLICATION_CREDENTIALS_JSON).")
    ap.add_argument("--site", help="Propiedad exacta de GSC (por defecto se detecta la de efectibank.pe).")
    ap.add_argument("--html-out", help="Ruta del dashboard con datos, FUERA del repo.")
    ap.add_argument("--json-out", help="Opcional: los mismos datos en JSON (para cargarlos con el botón del dashboard).")
    ap.add_argument("--template", default=PLANTILLA)
    ap.add_argument("--listar", action="store_true", help="Solo listar las propiedades accesibles.")
    a = ap.parse_args()

    s = sesion(a.clave)
    sitios = pedir(s, "GET", f"{API}/sites").get("siteEntry", [])
    print(f"Propiedades que ve la cuenta de servicio: {len(sitios)}")
    for x in sorted(sitios, key=lambda x: x["siteUrl"]):
        print(f"  {x['siteUrl']}  ({x.get('permissionLevel')})")
    if a.listar:
        return
    sitio = elegir_propiedad(sitios, a.site)
    if not sitio:
        sys.exit(f"ALTO: la cuenta de servicio no ve {a.site or 'ninguna propiedad de ' + DOMINIO}. "
                 "Agrégala como usuario en Search Console. No se generó ningún dato.")
    if not a.html_out and not a.json_out:
        sys.exit("Indica --html-out y/o --json-out (rutas fuera del repo).")
    html_out = fuera_del_repo(a.html_out) if a.html_out else None
    json_out = fuera_del_repo(a.json_out) if a.json_out else None

    # GSC guarda 16 meses; los últimos ~2 días suelen venir incompletos y se descartan.
    hoy = dt.date.today()
    diario = [dict(fecha=r["keys"][0], **fila(r, False))
              for r in consulta(s, sitio, hoy - dt.timedelta(days=486), hoy, ["date"])]
    diario.sort(key=lambda f: f["fecha"])
    if len(diario) > 2:
        diario = diario[:-2]
    if not diario:
        sys.exit("Search Console no devolvió filas. No se generó ningún archivo.")
    fin = dt.date.fromisoformat(diario[-1]["fecha"])
    print(f"Propiedad: {sitio} · serie diaria {diario[0]['fecha']} a {fin} ({len(diario)} días)")

    datos = {"sitio": sitio, "generado": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
             "diario": diario, "tablas": {}}
    for n in RANGOS:
        desde = fin - dt.timedelta(days=n - 1)
        if desde < dt.date.fromisoformat(diario[0]["fecha"]):
            continue
        actual = tablas(s, sitio, desde, fin)
        ini_prev = desde - dt.timedelta(days=n)
        if ini_prev >= dt.date.fromisoformat(diario[0]["fecha"]):
            actual["previo"] = tablas(s, sitio, ini_prev, desde - dt.timedelta(days=1))
        datos["tablas"][str(n)] = actual
        print(f"  {n} días: {len(actual['consultas'])} consultas, {len(actual['paginas'])} páginas")

    texto = json.dumps(datos, ensure_ascii=False, separators=(",", ":"))
    if json_out:
        with open(json_out, "w", encoding="utf-8") as f:
            f.write(texto)
        print(f"JSON: {json_out}")
    if html_out:
        with open(a.template, encoding="utf-8") as f:
            html = f.read()
        if html.count(MARCADOR) != 1:
            sys.exit(f"La plantilla {a.template} no tiene el marcador {MARCADOR} (una sola vez).")
        with open(html_out, "w", encoding="utf-8") as f:
            f.write(html.replace(MARCADOR, texto.replace("</", "<\\/")))
        print(f"HTML: {html_out}")


if __name__ == "__main__":
    main()
