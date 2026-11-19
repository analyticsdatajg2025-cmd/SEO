#!/usr/bin/env python3
"""Extrae de Google Search Console las consultas diarias de efe.com.pe.

Qué hace
  1. Lee la cuenta de servicio de la variable de entorno
     GOOGLE_APPLICATION_CREDENTIALS_JSON (nunca la imprime ni la guarda).
  2. Lista las propiedades que ve la cuenta (sites.list) y comprueba que la de
     efe.com.pe está. Si no está, se detiene y dice cuáles sí ve.
  3. Llama a searchAnalytics.query (dimensiones date + query, tipo web), día
     por día y paginando con startRow, y escribe un CSV
     date,query,clicks,impressions,position.
  4. Opcional (--html-out): genera el dashboard con los datos incrustados a
     partir de dashboards/kws-diarias-efe.html (solo las consultas principales).

Regla del repo: el CSV y el HTML con datos son exportes de GSC y NO van al
repo. El script se niega a escribirlos dentro del repositorio.

Uso
  python3 scripts/gsc_kws_diarias.py --listar
  python3 scripts/gsc_kws_diarias.py --csv-out /ruta/fuera/del/repo/gsc.csv \
      --html-out /ruta/fuera/del/repo/kws-diarias-efe-datos.html
  python3 scripts/gsc_kws_diarias.py --csv-in /ruta/gsc.csv --html-out /ruta/kws.html

Requiere: google-auth y requests (pip install google-auth requests).
"""
import argparse
import csv
import datetime as dt
import json
import os
import re
import sys
import time
import unicodedata

API = "https://searchconsole.googleapis.com/webmasters/v3"
SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANTILLA = os.path.join(REPO, "dashboards", "kws-diarias-efe.html")
MARCADOR = "/*__GSC_EMBED__*/null"
DOMINIO = "efe.com.pe"
FILAS_POR_PAGINA = 25000


def sesion():
    """Sesión HTTP autenticada.

    - Si la variable trae el JSON de la cuenta de servicio, se firma aquí un token
      con el permiso de solo lectura de Search Console.
    - Si trae un marcador (entornos donde un proxy inyecta la credencial de Google
      en las llamadas a *.googleapis.com), se llama sin token propio.
    """
    try:
        import requests
    except ImportError:
        sys.exit("Falta requests: pip install requests google-auth")
    raw = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_JSON")
    if not raw:
        sys.exit("Falta la variable de entorno GOOGLE_APPLICATION_CREDENTIALS_JSON.")
    try:
        info = json.loads(raw)
    except ValueError:
        info = None
    if isinstance(info, dict) and info.get("private_key"):
        try:
            from google.oauth2 import service_account
            from google.auth.transport.requests import AuthorizedSession
        except ImportError:
            sys.exit("Falta google-auth: pip install google-auth requests")
        cred = service_account.Credentials.from_service_account_info(info, scopes=[SCOPE])
        return AuthorizedSession(cred)
    print("Aviso: la variable no trae el JSON de la cuenta de servicio (marcador); "
          "se usa la credencial que inyecta el proxy del entorno.")
    s = requests.Session()
    s.headers["Authorization"] = "Bearer inyectado-por-el-proxy"  # valor de relleno, el proxy lo reemplaza
    return s


def pedir(s, metodo, url, **kw):
    """Llamada con reintentos ante errores temporales (429 / 5xx / red)."""
    for intento in range(5):
        try:
            r = s.request(metodo, url, timeout=120, **kw)
        except Exception as e:  # red
            if intento == 4:
                sys.exit(f"Error de red llamando a Search Console: {type(e).__name__}: {e}")
            time.sleep(2 ** intento)
            continue
        if r.status_code in (429, 500, 502, 503, 504) and intento < 4:
            time.sleep(2 ** intento)
            continue
        if r.status_code == 403 and "ACCESS_TOKEN_SCOPE_INSUFFICIENT" in r.text:
            sys.exit("ALTO: el token de Google no tiene el permiso (scope) de Search Console "
                     f"({SCOPE}). La red sí llega; falta el permiso en la credencial. "
                     "No se generó ningún dato.")
        if r.status_code != 200:
            sys.exit(f"Search Console respondió {r.status_code}: {r.text[:500]}")
        return r.json()


def listar_propiedades(s):
    return pedir(s, "GET", f"{API}/sites").get("siteEntry", [])


def es_de_efe(url):
    u = url.lower()
    if u.startswith("sc-domain:"):
        return u == f"sc-domain:{DOMINIO}"
    host = re.sub(r"^https?://", "", u).split("/")[0]
    return host == DOMINIO or host.endswith("." + DOMINIO)


def elegir_propiedad(sitios, pedida):
    """Devuelve la propiedad de efe.com.pe a usar, o None si no hay acceso."""
    utiles = [x for x in sitios if x.get("permissionLevel") != "siteUnverifiedUser"]
    urls = [x["siteUrl"] for x in utiles]
    if pedida and pedida in urls and es_de_efe(pedida):
        return pedida
    efe = [u for u in urls if es_de_efe(u)]
    if not efe:
        return None
    # preferencia: propiedad de dominio, luego https://www
    efe.sort(key=lambda u: (not u.startswith("sc-domain:"), "www." not in u, not u.startswith("https")))
    return efe[0]


def extraer(s, sitio, desde, hasta):
    from urllib.parse import quote
    url = f"{API}/sites/{quote(sitio, safe='')}/searchAnalytics/query"
    filas = []
    d = desde
    while d <= hasta:
        dia = d.isoformat()
        inicio = 0
        while True:
            cuerpo = {"startDate": dia, "endDate": dia, "dimensions": ["date", "query"],
                      "type": "web", "rowLimit": FILAS_POR_PAGINA, "startRow": inicio}
            rows = pedir(s, "POST", url, json=cuerpo).get("rows", [])
            for r in rows:
                filas.append((r["keys"][0], r["keys"][1], int(r["clicks"]), int(r["impressions"]), float(r["position"])))
            if len(rows) < FILAS_POR_PAGINA:
                break
            inicio += FILAS_POR_PAGINA
        d += dt.timedelta(days=1)
    return filas


def fuera_del_repo(ruta, que):
    real = os.path.realpath(ruta)
    if real == REPO or real.startswith(REPO + os.sep):
        sys.exit(f"No escribo {que} dentro del repo ({ruta}): los exportes de GSC no se suben. Usa una ruta fuera del repo.")
    os.makedirs(os.path.dirname(real) or ".", exist_ok=True)
    return real


def norm(q):
    q = unicodedata.normalize("NFD", q.lower())
    return "".join(c for c in q if not 0x300 <= ord(c) <= 0x36F).strip()


def agregado_para_html(filas, top, top_dia):
    """Consultas principales: top del periodo + top de cada día, por clics y por impresiones."""
    tot, por_dia = {}, {}
    for fecha, q, c, i, _ in filas:
        k = norm(q)
        t = tot.setdefault(k, [0, 0]); t[0] += c; t[1] += i
        por_dia.setdefault(fecha, []).append((k, c, i))
    elegidas = set()
    for m in (0, 1):
        elegidas.update(sorted(tot, key=lambda k: -tot[k][m])[:top])
        for lst in por_dia.values():
            elegidas.update(k for k, *_ in sorted(lst, key=lambda x: -x[1 + m])[:top_dia])
    dias = sorted(por_dia)
    idx_d = {d: n for n, d in enumerate(dias)}
    consultas, idx_q, rows = [], {}, []
    for fecha, q, c, i, p in filas:
        k = norm(q)
        if k not in elegidas:
            continue
        if k not in idx_q:
            idx_q[k] = len(consultas); consultas.append(q)
        rows.append([idx_d[fecha], idx_q[k], c, i, round(p, 2)])
    return dias, consultas, rows


def generar_html(filas, meta, salida, plantilla, top, top_dia):
    with open(plantilla, encoding="utf-8") as f:
        html = f.read()
    if html.count(MARCADOR) != 1:
        sys.exit(f"La plantilla {plantilla} no tiene el marcador {MARCADOR} (una sola vez).")
    dias, consultas, rows = agregado_para_html(filas, top, top_dia)
    meta = dict(meta, consultas_incrustadas=len(consultas), filas_incrustadas=len(rows))
    datos = json.dumps({"meta": meta, "days": dias, "queries": consultas, "rows": rows},
                       ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    with open(salida, "w", encoding="utf-8") as f:
        f.write(html.replace(MARCADOR, datos))
    return len(consultas), len(rows)


def main():
    ap = argparse.ArgumentParser(description="Consultas diarias de efe.com.pe desde Search Console.")
    ap.add_argument("--site", default=os.environ.get("GSC_SITE_URL"), help="Propiedad de GSC (por defecto, GSC_SITE_URL).")
    ap.add_argument("--days", type=int, default=120, help="Días hacia atrás (por defecto 120).")
    ap.add_argument("--end", help="Fecha final AAAA-MM-DD (por defecto, hoy; GSC entrega hasta donde tenga).")
    ap.add_argument("--csv-out", help="Ruta del CSV, FUERA del repo.")
    ap.add_argument("--html-out", help="Ruta del dashboard con datos incrustados, FUERA del repo.")
    ap.add_argument("--template", default=PLANTILLA, help="Plantilla HTML del dashboard.")
    ap.add_argument("--top", type=int, default=200, help="Consultas top del periodo a incrustar (por clics y por impresiones).")
    ap.add_argument("--top-dia", type=int, default=30, help="Consultas top de cada día a incrustar.")
    ap.add_argument("--csv-in", help="No llamar a la API: leer un CSV ya extraído (mismas columnas) y generar el HTML.")
    ap.add_argument("--listar", action="store_true", help="Solo listar las propiedades accesibles.")
    a = ap.parse_args()

    if a.csv_in:
        if not a.html_out:
            sys.exit("--csv-in necesita --html-out.")
        html_out = fuera_del_repo(a.html_out, "el HTML con datos")
        with open(a.csv_in, encoding="utf-8-sig", newline="") as f:
            filas = [(r["date"], r["query"], int(float(r["clicks"])), int(float(r["impressions"])), float(r["position"]))
                     for r in csv.DictReader(f)]
        if not filas:
            sys.exit("El CSV no tiene filas.")
        fechas = sorted({f[0] for f in filas})
        extraido = dt.date.fromtimestamp(os.path.getmtime(a.csv_in)).isoformat()
        meta = {"propiedad": a.site or "SIN DATO", "desde": fechas[0], "hasta": fechas[-1],
                "extraido": extraido, "filas_extraidas": len(filas), "tipo": "web"}
        nq, nr = generar_html(filas, meta, html_out, a.template, a.top, a.top_dia)
        print(f"HTML: {html_out} ({nq} consultas, {nr} filas día × consulta incrustadas)")
        return

    s = sesion()
    sitios = listar_propiedades(s)
    print(f"Propiedades que ve la cuenta de servicio: {len(sitios)}")
    for x in sorted(sitios, key=lambda x: x["siteUrl"]):
        print(f"  {x['siteUrl']}  ({x.get('permissionLevel')})")
    if a.listar:
        return
    sitio = elegir_propiedad(sitios, a.site)
    if not sitio:
        sys.exit(f"ALTO: la cuenta de servicio no tiene acceso a ninguna propiedad de {DOMINIO}. "
                 "Hay que agregarla como usuario en Search Console. No se generó ningún dato.")
    if a.site and sitio != a.site:
        print(f"Aviso: GSC_SITE_URL/--site no es una propiedad accesible de {DOMINIO}; uso {sitio}")
    if not a.csv_out and not a.html_out:
        sys.exit("Indica --csv-out y/o --html-out (rutas fuera del repo).")
    csv_out = fuera_del_repo(a.csv_out, "el CSV") if a.csv_out else None
    html_out = fuera_del_repo(a.html_out, "el HTML con datos") if a.html_out else None

    hasta = dt.date.fromisoformat(a.end) if a.end else dt.date.today()
    desde = hasta - dt.timedelta(days=a.days - 1)
    print(f"Propiedad: {sitio} · pidiendo {desde} a {hasta} (tipo web, date + query)")
    filas = extraer(s, sitio, desde, hasta)
    if not filas:
        sys.exit("Search Console no devolvió filas para ese rango. No se generó ningún archivo.")
    fechas = sorted({f[0] for f in filas})
    print(f"Filas extraídas: {len(filas)} · días con datos: {len(fechas)} ({fechas[0]} a {fechas[-1]})")

    if csv_out:
        with open(csv_out, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["date", "query", "clicks", "impressions", "position"])
            w.writerows(filas)
        print(f"CSV: {csv_out}")
    if html_out:
        meta = {"propiedad": sitio, "desde": fechas[0], "hasta": fechas[-1],
                "extraido": dt.date.today().isoformat(), "filas_extraidas": len(filas), "tipo": "web"}
        nq, nr = generar_html(filas, meta, html_out, a.template, a.top, a.top_dia)
        print(f"HTML: {html_out} ({nq} consultas, {nr} filas día × consulta incrustadas)")


if __name__ == "__main__":
    main()
