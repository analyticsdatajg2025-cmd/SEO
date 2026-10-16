# 03 · Pesos por negocio y modelo de ganancia neta

Última revisión: 16 oct 2026. **Propuesta para evaluar con Elias**, no decisión.

## 1. Cómo convierte el SEO en dinero neto (fórmula)

Para cada negocio, en un período:

```
Δ Ganancia neta = Δ venta neta orgánica × margen de producto
                + ahorro de pauta (búsquedas de marca que el orgánico ya gana y se dejan de pagar)
                + Δ créditos originados × margen financiero (Efectibank)
                + Δ leads × tasa de cierre × ticket × margen (Motocorp)
                − costo incremental (cero si es el mismo equipo)
```

Lo que sabemos de cada término (fuentes en `docs/01`):

| Término | La Curacao | Tiendas EFE | Juntoz | Motocorp | Efectibank |
|---|---|---|---|---|---|
| Venta orgánica base / año | S/ 7 M (web total GA4) | S/ 7.6 M (12 meses) | SIN DATO (web pura S/ 14 M, canal de tráfico sin desglose) | web S/ 260 K (leads, no venta) | SIN DATO |
| Venta neta ≈ venta total × | ~0.5 | ~0.55 | 1 (ya es neta) | — | — |
| Margen | ~10% | ~10% | comisión 7.1% | ~8% + crédito | financiero, alto, SIN DATO |
| Pauta Google / mes (Search + PMax + Shopping) | ~S/ 150–180 K (HIPÓTESIS: 60–70% de S/ 255 K) | ~S/ 110–130 K (HIPÓTESIS) | parte de S/ 173 K | n.d. | SIN DATO |
| Señal de canibalización de marca | Search 27% de la venta, PMax 22% | **Search -31%, PMax +64%** | — | — | — |

**Consecuencia del modelo**: con margen de producto ~10%, cada S/ 1 M de venta web orgánica adicional vale ~S/ 50 K netos (la mitad es venta neta). En cambio, **cada sol de pauta de marca que el orgánico reemplaza vale S/ 1 neto**, y cada crédito originado vale el margen financiero completo. Por eso, en 90 días, el dinero neto está en este orden:

1. **Dejar de pagar por lo que el orgánico ya gana** (Conecta, luego Juntoz).
2. **Llevar al crédito** desde las páginas con más intención (Motocorp y electro → Efectibank).
3. **Vender más por orgánico** en los picos (Cyber Wow, Navidad, calor/El Niño).
4. **SEO local**: 60% de los pedidos online se recogen en tienda; el teléfono/rutas de GBP cierran en piso con ticket 2.5x el de la web.

## 2. Pesos propuestos (esfuerzo del equipo en 90 días)

| Negocio | Peso | Por qué | Dinero neto que mueve (ver `docs/04`) |
|---|---|---|---|
| **La Curacao** | **30%** | Mayor venta web (S/ 60 M) y la brecha más grande: orgánico 12% vs 23% en EFE con la misma plataforma; Cyber 2026 -20%; errores comprobados (canonical, landings) | Venta orgánica en Cyber/Navidad + ahorro de pauta de marca |
| **Tiendas EFE** | **20%** | Orgánico crece +26% y es el 2° canal: proteger (canonical en todo el sitio) y cobrar la canibalización Search→PMax | Ahorro de pauta (el mayor neto rápido) |
| **Efectibank** | **15%** | Mayor margen del grupo; quiere ser 100% digital; app con 2.6★; home con título vacío; puente desde fichas de electro y motos roto | Créditos originados (sin dato; pedir) |
| **Motocorp** | **15%** | Ticket altísimo, poca competencia, 51% orgánico; 22+ tiendas y talleres sin páginas; cierra con crédito Efectibank (doble margen) | Leads y servicio de taller; local |
| **Juntoz + malls** | **15%** | Única vía rentable de crecer (comisión 7.1%, pauta y cupones no rinden); brecha de tráfico (83% de meta); base técnica muy débil (sin sitemap, sin canonical, sin schema) | Tráfico orgánico sin cupón; depende de desarrollo Next.js |
| **Skullcandy, Coldex, Diners, BanBif** | **5%** | Limpiezas baratas (páginas de EFE en Skullcandy, 503 indexable); Diners/BanBif llegan por el banco | Higiene; proteger a los socios |

Transversales dentro de los pesos: **SEO local / GBP** (LC, EFE, Motocorp, agencias Efectibank), **ASO** de las apps, **medición** (GSC + GA4 + línea base).

## 3. Cómo se recalculan los pesos
Cuando lleguen los datos de `docs/06` (sobre todo GSC, Ads por término, crédito por canal, leads de Motocorp), se recalcula con la fórmula de arriba por negocio y se reparte el esfuerzo proporcional al **dinero neto esperado ÷ esfuerzo**, con un piso de 5% para higiene. Hasta entonces, estos pesos son el mejor juicio con lo que hay.

## 4. Reparto sugerido del equipo
- **Kevin (técnico)**: canonical, sitemaps, datos estructurados, GSC, cruces feed↔sitemap↔stock, scripts de monitoreo, coordinación con TI/Magento y con el equipo Next.js de Juntoz, análisis de términos de búsqueda de Ads.
- **Carolina (operativo)**: metadatos en CMS (títulos, descripciones, H1), inventario de landings, fichas de Google Business Profile (horarios, fotos, categorías, duplicados), reseñas y textos de las apps (ASO), briefs de contenido estacional, registro de cambios.
- **Elias**: accesos, decisiones de negocio (categorías a empujar, pauta de marca, prioridad de desarrollo), presentación a gerencia.
