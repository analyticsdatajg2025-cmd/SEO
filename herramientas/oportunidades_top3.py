#!/usr/bin/env python3
"""
Oportunidades SEO no-brand: URLs en posición 5-10 que valen más si pasan al top 3.

Cruza Search Console (obligatorio), GA4 y Yandex Webmaster (opcionales) para
lacuracao.pe (sirve para efe.com.pe cambiando --marca y --dominio).

Uso:
  python3 herramientas/oportunidades_top3.py \
      --gsc datos/gsc_query_page.csv \
      [--gsc-prev datos/gsc_query_page_PY.csv] \
      [--ga4 datos/ga4_landing_organico.csv] \
      [--yandex datos/yandex_queries.csv] \
      [--out datos/salida]

Los archivos van en datos/ (bloqueado por .gitignore). Nunca subir exportes.

Entradas (CSV o XLSX; acepta nombres de columna en español o inglés):
  GSC   : consulta + página + clics + impresiones + posición (Search Analytics
          API, Looker Studio o "Search Analytics for Sheets"). El exporte de la
          interfaz por "Páginas" sin consulta también se acepta, pero entonces
          NO se puede separar marca de no-marca y el informe lo advierte.
  GA4   : página de destino + sesiones + ingresos (+ transacciones), ya
          filtrado a "Organic Search" (Adquisición de tráfico / Exploración).
  Yandex: consulta (y/o página) + impresiones + clics + posición media.

Reglas (no inventa cifras):
  - CTR objetivo del top 3 = CTR real del propio sitio en posiciones 1-3,
    no-brand, por tipo de página. Si no hay muestra suficiente se marca
    SIN DATO, salvo que se pase --ctr-top3 explícito (queda en el informe).
  - Venta extra = clics extra x ingreso orgánico por sesión de esa URL en GA4
    (si la URL no está en GA4, el promedio de su tipo). Supuesto: 1 clic ≈ 1
    sesión. Es un ESCENARIO, no una proyección.
"""
import argparse, os, re, sys
from urllib.parse import urlparse
import pandas as pd

MARCA_DEF = r"curacao|curaca|curazao|curacau|cura[cs]ao|lacura|la cura|\bcuracao\b|\blc\b"
DOMINIO_DEF = "lacuracao.pe"
# Departamentos (nivel 1) de lacuracao.pe vistos en el sitemap el 24-nov-2026.
DEPARTAMENTOS = {
    "tecnologia", "electrohogar", "hogar", "muebles", "dormitorio", "deporte", "infantil",
    "salud", "mejoramiento-del-hogar", "motos", "moda-y-belleza", "moda-hombre",
    "multiservicios", "supermercados", "mascotas", "estilo-de-vida",
    "equipamiento-gastronomico", "libreria", "farmacia", "negocios-e-industria",
    "bebe-y-juguetes", "motocorp", "bundles", "remate-total", "promocionales",
    "moda-infantil", "xo", "tecnolog-a", "marcas",
}

ALIAS = {
    "query": ["query", "consulta", "consultas", "top queries", "consultas principales", "keyword", "search query", "запрос"],
    "page": ["page", "página", "pagina", "url", "landing page", "top pages", "páginas principales",
             "página de destino", "pagina de destino", "landing page + query string",
             "página de destino + cadena de consulta"],
    "clicks": ["clicks", "clics", "clic", "клики"],
    "impressions": ["impressions", "impresiones", "показы", "shows"],
    "position": ["position", "posición", "posicion", "posición media", "average position",
                 "avg position", "pos", "средняя позиция"],
    "sessions": ["sessions", "sesiones"],
    "revenue": ["revenue", "ingresos", "total revenue", "ingresos totales", "purchase revenue",
                "ingresos por compras"],
    "transactions": ["transactions", "transacciones", "purchases", "compras", "ecommerce purchases",
                     "compras de comercio electrónico"],
}


def leer(ruta):
    if ruta.lower().endswith((".xlsx", ".xls")):
        df = pd.read_excel(ruta)
    else:
        df = pd.read_csv(ruta, sep=None, engine="python", encoding="utf-8-sig")
    mapa = {}
    for c in df.columns:
        k = str(c).strip().lower()
        for std, al in ALIAS.items():
            if k in al and std not in mapa.values():
                mapa[c] = std
                break
    df = df.rename(columns=mapa)
    for c in ("clicks", "impressions", "position", "sessions", "revenue", "transactions"):
        if c in df.columns and df[c].dtype == object:
            df[c] = pd.to_numeric(df[c].astype(str).str.replace(r"[^\d.,-]", "", regex=True)
                                  .str.replace(",", "", regex=False), errors="coerce")
    return df


def ruta_de(u):
    u = str(u).strip()
    p = urlparse(u if "://" in u else "https://x" + (u if u.startswith("/") else "/" + u))
    return (p.path or "/").lower().rstrip("/") or "/"


def tipo_de(ruta):
    if ruta == "/":
        return "home"
    partes = [x for x in ruta.strip("/").split("/") if x]
    if partes[0] in ("curacao",):
        return "marca"
    if partes[0] == "catalog":
        return "categoria"  # URL técnica de Magento; su canonical decide
    if not ruta.endswith(".html"):
        return "otra"
    if len(partes) == 1:
        slug = partes[0][:-5]
        return "categoria" if slug in DEPARTAMENTOS else "producto"
    if len(partes) == 2:
        return "categoria"
    return "subcategoria"


def ponderar(g):
    imp = g["impressions"].sum()
    return pd.Series({
        "clics": g["clicks"].sum(),
        "impresiones": imp,
        "posicion": (g["position"] * g["impressions"]).sum() / imp if imp else None,
    })


def ctr_top3(df_q, minimo):
    """CTR real no-brand en posiciones 1-3 por tipo, con muestra mínima de impresiones."""
    t = df_q[df_q["position"] <= 3.5]
    out = {}
    for tipo, g in t.groupby("tipo"):
        if g["impressions"].sum() >= minimo:
            out[tipo] = g["clicks"].sum() / g["impressions"].sum()
    if t["impressions"].sum() >= minimo:
        out["_sitio"] = t["clicks"].sum() / t["impressions"].sum()
    return out


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--gsc", required=True)
    a.add_argument("--gsc-prev")
    a.add_argument("--ga4")
    a.add_argument("--yandex")
    a.add_argument("--marca", default=MARCA_DEF)
    a.add_argument("--pos-min", type=float, default=4.5)
    a.add_argument("--pos-max", type=float, default=10.5)
    a.add_argument("--min-impr", type=int, default=200, help="impresiones mínimas por URL")
    a.add_argument("--min-muestra-ctr", type=int, default=2000)
    a.add_argument("--ctr-top3", type=float, help="CTR objetivo manual (0-1); queda declarado")
    a.add_argument("--top", type=int, default=7)
    a.add_argument("--out", default="datos/salida")
    o = a.parse_args()
    os.makedirs(o.out, exist_ok=True)
    rx = re.compile(o.marca, re.I)
    avisos = []

    g = leer(o.gsc)
    falta = {"page", "clicks", "impressions", "position"} - set(g.columns)
    if falta:
        sys.exit(f"GSC: faltan columnas {falta}. Columnas leídas: {list(g.columns)}")
    g["ruta"] = g["page"].map(ruta_de)
    g["tipo"] = g["ruta"].map(tipo_de)
    con_query = "query" in g.columns
    if con_query:
        g["marca"] = g["query"].astype(str).map(lambda q: bool(rx.search(q)))
    else:
        g["marca"] = False
        avisos.append("GSC sin columna de consulta: no se pudo separar marca de no-marca; "
                      "las cifras incluyen búsquedas de marca.")

    # 1. Resumen marca vs no-marca
    res = g.groupby("marca").apply(ponderar).rename(index={True: "marca", False: "no-marca"})
    res["ctr"] = res["clics"] / res["impresiones"]

    nb = g[~g["marca"]].copy()
    por_tipo = nb.groupby("tipo").apply(ponderar)
    por_tipo["ctr"] = por_tipo["clics"] / por_tipo["impresiones"]

    # 2. CTR objetivo top 3 (propio)
    # Sin consulta, se calcula a nivel de URL (incluye marca: queda en avisos).
    objetivos = ctr_top3(nb, o.min_muestra_ctr)
    if o.ctr_top3 is not None:
        avisos.append(f"CTR objetivo manual {o.ctr_top3:.1%} para todos los tipos (pasado por --ctr-top3).")

    def obj(tipo):
        if o.ctr_top3 is not None:
            return o.ctr_top3
        return objetivos.get(tipo, objetivos.get("_sitio"))

    # 3. Por URL
    url = nb.groupby(["ruta", "tipo"]).apply(ponderar).reset_index()
    url["ctr"] = url["clics"] / url["impresiones"]

    if con_query:
        # consulta no-brand principal en 5-10 por URL (la que hay que empujar)
        q = nb[(nb["position"] >= o.pos_min) & (nb["position"] <= o.pos_max)]
        q = q.sort_values("impressions", ascending=False).drop_duplicates("ruta")
        url = url.merge(q[["ruta", "query", "impressions", "position"]]
                        .rename(columns={"query": "consulta_clave", "impressions": "impr_consulta",
                                         "position": "pos_consulta"}), on="ruta", how="left")

    # 4. GA4: ingreso orgánico por sesión
    if o.ga4:
        ga = leer(o.ga4)
        if not {"page", "sessions", "revenue"} <= set(ga.columns):
            sys.exit(f"GA4: se necesitan página de destino, sesiones e ingresos. Leídas: {list(ga.columns)}")
        ga["ruta"] = ga["page"].map(lambda u: ruta_de(str(u).split("?")[0]))
        agg = {"sessions": "sum", "revenue": "sum"}
        if "transactions" in ga.columns:
            agg["transactions"] = "sum"
        ga = ga.groupby("ruta").agg(agg).reset_index()
        ga["tipo"] = ga["ruta"].map(tipo_de)
        ga["ing_x_sesion"] = ga["revenue"] / ga["sessions"].where(ga["sessions"] > 0)
        prom_tipo = (ga.groupby("tipo")["revenue"].sum() / ga.groupby("tipo")["sessions"].sum()).to_dict()
        cols = ["ruta", "sessions", "revenue", "ing_x_sesion"] + (["transactions"] if "transactions" in ga.columns else [])
        url = url.merge(ga[cols].rename(columns={"sessions": "ga4_sesiones", "revenue": "ga4_ingresos",
                                                 "transactions": "ga4_transacciones"}), on="ruta", how="left")
        url["ing_x_sesion_usado"] = url["ing_x_sesion"].fillna(url["tipo"].map(prom_tipo))
        tot_t = ga.groupby("tipo")[["sessions", "revenue"]].sum()
        por_tipo = por_tipo.join(tot_t.rename(columns={"sessions": "ga4_sesiones", "revenue": "ga4_ingresos"}))
        avisos.append("GA4: ingresos de sesiones orgánicas por página de destino (incluye marca: GA4 no ve la consulta).")
    else:
        avisos.append("Sin GA4: no se calcula venta, solo clics.")

    # 5. Yandex
    if o.yandex:
        y = leer(o.yandex)
        if "query" in y.columns:
            y = y[~y["query"].astype(str).map(lambda s: bool(rx.search(s)))]
        if "page" in y.columns:
            y["ruta"] = y["page"].map(ruta_de)
            ya = y.groupby("ruta").apply(ponderar).reset_index()
            url = url.merge(ya.rename(columns={"clics": "yx_clics", "impresiones": "yx_impr",
                                               "posicion": "yx_pos"}), on="ruta", how="left")
        elif "query" in y.columns and "consulta_clave" in url.columns:
            yq = y.groupby(y["query"].str.lower()).apply(ponderar).reset_index()
            url["_k"] = url["consulta_clave"].str.lower()
            url = url.merge(yq.rename(columns={"query": "_k", "clics": "yx_clics", "impresiones": "yx_impr",
                                               "posicion": "yx_pos"}), on="_k", how="left").drop(columns="_k")
        yt = y.groupby(lambda _: "yandex").apply(ponderar)
        avisos.append(f"Yandex no-brand total: {int(yt['impresiones'].iloc[0]):,} impr., "
                      f"{int(yt['clics'].iloc[0]):,} clics (referencia; en Perú pesa poco).")

    # 6. Oportunidades 5-10 → top 3
    op = url[(url["posicion"] >= o.pos_min) & (url["posicion"] <= o.pos_max)
             & (url["impresiones"] >= o.min_impr)].copy()
    op["ctr_obj_top3"] = op["tipo"].map(obj)
    op["clics_extra"] = (op["impresiones"] * (op["ctr_obj_top3"] - op["ctr"])).clip(lower=0)
    if "ing_x_sesion_usado" in op.columns:
        op["venta_extra_S/"] = op["clics_extra"] * op["ing_x_sesion_usado"]
        orden = "venta_extra_S/"
    else:
        orden = "clics_extra"
    op = op.sort_values([orden, "impresiones"], ascending=False, na_position="last")

    # 7. Comparación con periodo previo
    if o.gsc_prev:
        p = leer(o.gsc_prev)
        p["ruta"] = p["page"].map(ruta_de)
        if "query" in p.columns:
            p = p[~p["query"].astype(str).map(lambda s: bool(rx.search(s)))]
        pp = p.groupby("ruta").apply(ponderar).reset_index()
        op = op.merge(pp.rename(columns={"clics": "clics_prev", "impresiones": "impr_prev",
                                         "posicion": "pos_prev"}), on="ruta", how="left")

    url.to_csv(os.path.join(o.out, "urls_no_brand.csv"), index=False)
    op.to_csv(os.path.join(o.out, "oportunidades_top3.csv"), index=False)

    # 8. Informe
    L = ["# Oportunidades SEO no-brand · posición 5-10 → top 3", ""]
    L += ["## Marca vs no-marca (GSC)", "", "| | Clics | Impresiones | CTR | Posición |", "|---|---|---|---|---|"]
    for k, r in res.iterrows():
        L.append(f"| {k} | {r.clics:,.0f} | {r.impresiones:,.0f} | {r.ctr:.2%} | {r.posicion:.1f} |")
    L += ["", "## No-marca por tipo de página", ""]
    cab = "| Tipo | Clics | Impresiones | CTR | Posición | CTR obj. top 3 |" + (" Sesiones GA4 | Ingresos GA4 |" if o.ga4 else "")
    L += [cab, "|" + "---|" * (cab.count("|") - 1)]
    for t, r in por_tipo.sort_values("impresiones", ascending=False).iterrows():
        ob = obj(t)
        fila = f"| {t} | {r.clics:,.0f} | {r.impresiones:,.0f} | {r.ctr:.2%} | {r.posicion:.1f} | {('%.1f%%' % (ob*100)) if ob else 'SIN DATO'} |"
        if o.ga4:
            fila += f" {r.get('ga4_sesiones', 0) or 0:,.0f} | S/ {r.get('ga4_ingresos', 0) or 0:,.0f} |"
        L.append(fila)
    for t in ("categoria", "subcategoria", "producto"):
        s = op[op["tipo"] == t].head(o.top)
        L += ["", f"## Top {o.top} · {t}", ""]
        if s.empty:
            L.append("Sin URLs en posición 5-10 con impresiones suficientes.")
            continue
        h = "| URL | Consulta clave | Impr. | Clics | CTR | Pos. | CTR top 3 | Clics extra |"
        if "venta_extra_S/" in s.columns:
            h += " Ingreso/sesión | Venta extra (escenario) |"
        if "yx_impr" in s.columns:
            h += " Yandex impr/pos |"
        L += [h, "|" + "---|" * (h.count("|") - 1)]
        for _, r in s.iterrows():
            ob = r["ctr_obj_top3"]
            f = (f"| `{r.ruta}` | {r.get('consulta_clave', '') if pd.notna(r.get('consulta_clave')) else '—'} | "
                 f"{r.impresiones:,.0f} | {r.clics:,.0f} | {r.ctr:.2%} | {r.posicion:.1f} | "
                 f"{('%.1f%%' % (ob*100)) if pd.notna(ob) else 'SIN DATO'} | "
                 f"{r.clics_extra:,.0f} |" if pd.notna(ob) else
                 f"| `{r.ruta}` | — | {r.impresiones:,.0f} | {r.clics:,.0f} | {r.ctr:.2%} | {r.posicion:.1f} | SIN DATO | — |")
            if "venta_extra_S/" in s.columns:
                ing = r.get("ing_x_sesion_usado")
                ve = r.get("venta_extra_S/")
                f += f" {('S/ %.2f' % ing) if pd.notna(ing) else 'SIN DATO'} | {('S/ {:,.0f}'.format(ve)) if pd.notna(ve) else 'SIN DATO'} |"
            if "yx_impr" in s.columns:
                f += f" {r.yx_impr:,.0f} / {r.yx_pos:.1f} |" if pd.notna(r.get("yx_impr")) else " — |"
            L.append(f)
    L += ["", "## Supuestos y avisos", ""] + [f"- {x}" for x in avisos] + [
        f"- Rango de oportunidad: posición media {o.pos_min}-{o.pos_max}, mínimo {o.min_impr} impresiones no-brand por URL.",
        "- CTR objetivo = CTR propio no-brand en posiciones 1-3 (muestra mínima "
        f"{o.min_muestra_ctr:,} impr.). No es una curva genérica.",
        "- 'Venta extra' es un escenario: impresiones actuales x (CTR top 3 − CTR actual) x ingreso por sesión.",
        f"- Regex de marca: `{o.marca}`.",
    ]
    with open(os.path.join(o.out, "informe_oportunidades.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
