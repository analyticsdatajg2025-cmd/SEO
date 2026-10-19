#!/usr/bin/env python3
"""Carga una vez el historial de GSC (hasta 16 meses) vía API en seo.url_dia y seo.sitio_dia.

La exportación a BigQuery solo guarda desde el día en que se activa; esto rellena lo anterior.
Corre fuera de Claude (no gasta tokens). Después: scripts/desplegar.sh correr 21.

Uso:
  pip install -r scripts/requirements.txt
  GOOGLE_APPLICATION_CREDENTIALS=<ruta-clave.json> python3 scripts/cargar_historial_api.py \
      --proyecto <id-proyecto-gcp> --marca efectibank --propiedad sc-domain:efectibank.pe \
      --desde 2025-06-01 --hasta 2026-10-20

La cuenta de servicio debe estar agregada como usuario (restringido basta) en la propiedad de GSC
y tener permiso de edición en el dataset `seo`. --hasta debe ser el día ANTERIOR al primer día exportado.

Límites conocidos de la API: 25 K filas por pedido (se pagina) y un tope diario de filas por
propiedad y tipo de búsqueda; en sitios de 100 K URLs puede cortar la cola larga. Para Efectibank no aplica.
La API omite las consultas anonimizadas: se reconstruyen como diferencia entre el total y la suma por consulta.
"""
import argparse
import datetime as dt
import re
import time
from collections import defaultdict

from google.cloud import bigquery
from googleapiclient.discovery import build
import google.auth

TIPOS = {"web": "WEB", "image": "IMAGE", "video": "VIDEO", "news": "NEWS"}
FILAS_POR_PEDIDO = 25000


def consultar(gsc, propiedad, dia, dimensiones, tipo):
    """Todas las filas de un día para las dimensiones dadas (pagina de 25 K en 25 K)."""
    filas, inicio = [], 0
    while True:
        cuerpo = {
            "startDate": dia, "endDate": dia, "dimensions": dimensiones, "type": tipo,
            "rowLimit": FILAS_POR_PEDIDO, "startRow": inicio, "dataState": "final",
        }
        for intento in range(5):
            try:
                r = gsc.searchanalytics().query(siteUrl=propiedad, body=cuerpo).execute()
                break
            except Exception:  # cuota o error transitorio: esperar y reintentar
                if intento == 4:
                    raise
                time.sleep(2 ** (intento + 1))
        lote = r.get("rows", [])
        filas.extend(lote)
        if len(lote) < FILAS_POR_PEDIDO:
            return filas
        inicio += FILAS_POR_PEDIDO


def suma_pos(fila):
    # La exportación guarda la posición en base 0 sumada por impresión; la API da el promedio en base 1.
    return max(fila["position"] - 1, 0) * fila["impressions"]


def filas_dia(gsc, propiedad, dia, tipo_api, marca, regex_marca):
    tipo = TIPOS[tipo_api]
    url_dia, sitio_dia = [], []

    for f in consultar(gsc, propiedad, dia, ["page", "device", "country"], tipo_api):
        pagina, disp, pais = f["keys"]
        url_dia.append({
            "fecha": dia, "marca": marca, "url": pagina, "dispositivo": disp, "tipo_busqueda": tipo,
            "es_peru": pais == "per", "clics": int(f["clicks"]), "impresiones": int(f["impressions"]),
            "suma_posicion": suma_pos(f), "fuente": "api",
        })

    # Totales por propiedad (sin consulta) y por consulta: la diferencia son las anonimizadas.
    totales = {tuple(f["keys"]): f for f in consultar(gsc, propiedad, dia, ["device", "country"], tipo_api)}
    acumulado = defaultdict(lambda: defaultdict(lambda: [0, 0, 0.0]))  # (disp, pais) -> tipo_consulta -> [c, i, p]
    for f in consultar(gsc, propiedad, dia, ["query", "device", "country"], tipo_api):
        consulta, disp, pais = f["keys"]
        tipo_c = "marca" if regex_marca.search(consulta.lower()) else "no_marca"
        a = acumulado[(disp, pais)][tipo_c]
        a[0] += int(f["clicks"]); a[1] += int(f["impressions"]); a[2] += suma_pos(f)

    for (disp, pais), t in totales.items():
        partes = acumulado[(disp, pais)]
        resto = [int(t["clicks"]), int(t["impressions"]), suma_pos(t)]
        for v in partes.values():
            resto = [resto[0] - v[0], resto[1] - v[1], resto[2] - v[2]]
        partes["anonimizada"] = [max(resto[0], 0), max(resto[1], 0), max(resto[2], 0.0)]

    # Por pais se agrega a es_peru antes de guardar, para que coincida con la tabla.
    agregado = defaultdict(lambda: [0, 0, 0.0])
    for (disp, pais), partes in acumulado.items():
        for tipo_c, v in partes.items():
            a = agregado[(disp, pais == "per", tipo_c)]
            a[0] += v[0]; a[1] += v[1]; a[2] += v[2]
    for (disp, es_peru, tipo_c), v in agregado.items():
        if v[1] == 0 and v[0] == 0:
            continue
        sitio_dia.append({
            "fecha": dia, "marca": marca, "dispositivo": disp, "tipo_busqueda": tipo, "es_peru": es_peru,
            "tipo_consulta": tipo_c, "clics": v[0], "impresiones": v[1], "suma_posicion": v[2], "fuente": "api",
        })
    return url_dia, sitio_dia


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--proyecto", required=True)
    p.add_argument("--marca", required=True)
    p.add_argument("--propiedad", required=True, help="sc-domain:dominio.pe o https://www.dominio.pe/")
    p.add_argument("--desde", required=True, type=dt.date.fromisoformat)
    p.add_argument("--hasta", required=True, type=dt.date.fromisoformat)
    p.add_argument("--tipos", default="web", help="web,image,video,news (por defecto: web)")
    p.add_argument("--ubicacion", default="US")
    a = p.parse_args()

    cred, _ = google.auth.default(scopes=[
        "https://www.googleapis.com/auth/webmasters.readonly",
        "https://www.googleapis.com/auth/bigquery",
    ])
    gsc = build("searchconsole", "v1", credentials=cred, cache_discovery=False)
    bq = bigquery.Client(project=a.proyecto, credentials=cred, location=a.ubicacion)

    fila = list(bq.query(
        f"SELECT regex_consulta_marca FROM `{a.proyecto}.seo.marcas` WHERE marca = @m",
        job_config=bigquery.QueryJobConfig(query_parameters=[bigquery.ScalarQueryParameter("m", "STRING", a.marca)]),
    ).result())
    if not fila:
        raise SystemExit(f"La marca {a.marca} no está en seo.marcas: correr antes desplegar.sh tablas")
    regex_marca = re.compile(fila[0].regex_consulta_marca)

    # Idempotente: borra lo cargado antes por la API en el mismo rango.
    for tabla in ("url_dia", "sitio_dia"):
        bq.query(
            f"DELETE FROM `{a.proyecto}.seo.{tabla}` WHERE marca = @m AND fuente = 'api' AND fecha BETWEEN @d AND @h",
            job_config=bigquery.QueryJobConfig(query_parameters=[
                bigquery.ScalarQueryParameter("m", "STRING", a.marca),
                bigquery.ScalarQueryParameter("d", "DATE", a.desde),
                bigquery.ScalarQueryParameter("h", "DATE", a.hasta),
            ]),
        ).result()

    configs = {
        tabla: bigquery.LoadJobConfig(
            schema=bq.get_table(f"{a.proyecto}.seo.{tabla}").schema,
            write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        )
        for tabla in ("url_dia", "sitio_dia")
    }
    pendientes = {"url_dia": [], "sitio_dia": []}

    def guardar():
        # Un job de carga por tabla cada ~30 días: lejos del tope diario de cargas por tabla.
        for tabla, filas in pendientes.items():
            if filas:
                bq.load_table_from_json(filas, f"{a.proyecto}.seo.{tabla}", job_config=configs[tabla]).result()
            filas.clear()

    tipos = [t.strip() for t in a.tipos.split(",") if t.strip()]
    dia = a.desde
    while dia <= a.hasta:
        for t in tipos:
            u, s = filas_dia(gsc, a.propiedad, dia.isoformat(), t, a.marca, regex_marca)
            pendientes["url_dia"] += u
            pendientes["sitio_dia"] += s
        print(f"{dia}: {len(pendientes['url_dia'])} filas url_dia en espera")
        if dia.day == 1 or dia == a.hasta:
            guardar()
        dia += dt.timedelta(days=1)


if __name__ == "__main__":
    main()
