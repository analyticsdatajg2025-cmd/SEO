"""Auditoría SEO pública de un sitio Magento del grupo a partir de su sitemap.

Solo lectura. Para cada URL del sitemap revisa: código de respuesta, tipo de
página (producto, categoría, CMS, blog), título, meta descripción, H1,
canonical, robots, datos estructurados, disponibilidad del producto y si el
título delata otra tienda (EFE, La Curacao, Motocorp) o una página de prueba.

Uso:
    python3 herramientas/auditar_sitio.py https://skullcandy.com.pe [salida.json]

La salida JSON va fuera del repo (datos/ está en .gitignore). Es la pieza
"Leer / Detectar" del agente de docs/10.
"""
import sys, os, re, json, html, collections, urllib.request, urllib.error
import concurrent.futures as cf

UA = {"User-Agent": "Mozilla/5.0 (compatible; seo-audit)"}
OTRAS_TIENDAS = r"Tiendas EFE|La Curacao|Motocorp|Financiera Efectiva|efe\.com\.pe"
PRUEBA = r"test|prueba|temp|ejemplo|demo|\d{4,}|final"


class SinRedireccion(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


_op = urllib.request.build_opener(SinRedireccion)


def get(url, seguir=True):
    abrir = urllib.request.urlopen if seguir else _op.open
    try:
        r = abrir(urllib.request.Request(url, headers=UA), timeout=40)
        return r.status, "", r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Location", ""), ""
    except Exception as e:
        return 0, str(e)[:80], ""


def primero(patron, texto):
    m = re.search(patron, texto or "", re.I | re.S)
    return m.group(1) if m else None


def limpiar(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def urls_sitemap(sitio):
    _, _, robots = get(f"{sitio}/robots.txt")
    mapas = re.findall(r"Sitemap\s*:\s*(\S+)", robots, re.I) or [f"{sitio}/sitemap.xml"]
    urls = []
    for m in mapas:
        _, _, x = get(m)
        hijos = re.findall(r"<loc>([^<]+\.xml)</loc>", x)
        for hoja in hijos or [m]:
            _, _, y = get(hoja) if hijos else (0, "", x)
            urls += re.findall(r"<loc>([^<]+)</loc>", y)
    return list(dict.fromkeys(urls)), robots


def auditar(url):
    st, loc, h = get(url, seguir=False)
    cuerpo = primero(r'<body[^>]*class="([^"]*)"', h) or ""
    tipo = ("producto" if "catalog-product-view" in cuerpo else
            "categoria" if "catalog-category-view" in cuerpo else
            "blog" if "mpblog" in cuerpo else
            "cms" if "cms-" in cuerpo else "otro")
    titulo = limpiar(primero(r"<title>(.*?)</title>", h))
    ruta = re.sub(r"^https?://[^/]+/?", "", url)
    disp = primero(r'"availability"\s*:\s*"[^"]*?(InStock|OutOfStock|PreOrder)', h)
    return {
        "url": url, "status": st, "redirige_a": loc, "tipo": tipo, "titulo": titulo,
        "meta": limpiar(primero(r'<meta name="description" content="(.*?)"', h)),
        "robots": primero(r'<meta name="robots" content="(.*?)"', h),
        "canonical": primero(r'<link\s+rel="canonical"\s+href="(.*?)"', h),
        "h1": [limpiar(x) for x in re.findall(r"<h1[^>]*>(.*?)</h1>", h, re.I | re.S)],
        "schema": sorted(set(re.findall(r'"@type"\s*:\s*"([A-Za-z]+)"', h))),
        "disponibilidad": disp,
        "otra_tienda": bool(re.search(OTRAS_TIENDAS, titulo, re.I)),
        "parece_prueba": tipo in ("cms", "otro") and bool(re.search(PRUEBA, ruta + " " + titulo, re.I)),
    }


def resumen(sitio, res, robots):
    ok = [r for r in res if r["status"] == 200]
    C = collections.Counter
    meta_top = C(r["meta"] for r in ok).most_common(1)
    host = re.sub(r"^https?://", "", sitio)
    filas = [
        ("URLs en el sitemap", len(res)),
        ("Responden distinto de 200", len(res) - len(ok)),
        ("Por tipo", dict(C(r["tipo"] for r in res))),
        ("Título de otra tienda del grupo", sum(r["otra_tienda"] for r in ok)),
        ("Parecen páginas de prueba", sum(r["parece_prueba"] for r in ok)),
        ("Canonical hacia otro dominio", sum(1 for r in ok if r["canonical"] and host not in r["canonical"])),
        ("Meta descripción repetida (la más común)", meta_top[0][1] if meta_top else 0),
        ("Sin H1", sum(len(r["h1"]) == 0 for r in ok)),
        ("Más de un H1", sum(len(r["h1"]) > 1 for r in ok)),
        ("Productos agotados en el sitemap", sum(r["disponibilidad"] == "OutOfStock" for r in ok)),
        ("Títulos duplicados", sum(v for v in C(r["titulo"] for r in ok).values() if v > 1)),
        ("robots.txt con 'Sitemap :' (espacio)", bool(re.search(r"Sitemap\s+:", robots))),
    ]
    for k, v in filas:
        print(f"{k:45} {v}")
    malas = [r for r in ok if r["otra_tienda"] or r["parece_prueba"]] + [r for r in res if r["status"] != 200]
    if malas:
        print("\nPáginas a revisar (otra tienda, prueba o error):")
        for r in malas:
            print(f"  {r['status']}  {r['url']}  | {r['titulo'][:60]}")


if __name__ == "__main__":
    sitio = sys.argv[1].rstrip("/")
    salida = sys.argv[2] if len(sys.argv) > 2 else "datos/auditoria-" + re.sub(r"\W+", "-", sitio.split("//")[-1]) + ".json"
    urls, robots = urls_sitemap(sitio)
    with cf.ThreadPoolExecutor(6) as ex:
        res = list(ex.map(auditar, urls))
    resumen(sitio, res, robots)
    os.makedirs(os.path.dirname(salida) or ".", exist_ok=True)
    json.dump(res, open(salida, "w"), ensure_ascii=False, indent=1)
    print(f"\nDetalle por URL: {salida}")
