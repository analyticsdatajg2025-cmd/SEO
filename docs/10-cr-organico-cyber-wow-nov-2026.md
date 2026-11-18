# 10 · La Curacao · caída del CR orgánico alrededor de Cyber Wow (12-oct a 15-nov 2026)

Análisis del 18-nov-2026. Fuente: tablero "Canales" (GA4 + Qlik), capturas semanales y exporte del periodo entregados por Elias el 18-nov; gráfico de Términos de búsqueda de Google Ads (todas las campañas). **La hoja de GSC no se pudo abrir (privada): todo lo que depende de GSC queda como `HIPÓTESIS`.** Los archivos crudos no están en el repo.

## 1. Los datos

CR gross = transacciones GA4 / sesiones. Cyber Wow cayó en la semana del 2 al 8-nov.

| Semana | SEO sesiones | SEO trx | SEO CR | SEM sesiones | SEM trx | SEM CR | SEO+SEM sesiones | SEO+SEM trx | SEO+SEM CR |
|---|---|---|---|---|---|---|---|---|---|
| 12-18 oct | 34,884 | 290 | 0.83% | 7,058 | 42 | 0.60% | 41,942 | 332 | 0.79% |
| 19-25 oct | 32,517 | 273 | 0.84% | 8,638 | 35 | 0.41% | 41,155 | 308 | 0.75% |
| 26 oct-1 nov | 32,183 | 217 | 0.67% | 7,460 | 64 | 0.86% | 39,643 | 281 | 0.71% |
| 2-8 nov (Cyber) | 31,543 | 455 | 1.44% | 48,854 | 1,055 | 2.16% | 80,397 | 1,510 | 1.88% |
| 9-15 nov | 24,946 | 99 | 0.40% | 30,044 | 316 | 1.05% | 54,990 | 415 | 0.75% |

Otros canales, CR gross por semana (mismo orden): PMAX 0.71 / 0.62 / 0.50 / 0.97 / 0.67%; Directo 0.45 / 0.42 / 0.34 / 1.30 / 0.35%; Referral 0.92 / 0.92 / 0.61 / 1.44 / 0.89%.

## 2. Lectura

Hay dos caídas distintas.

**a) Semana previa (26-oct a 1-nov): 0.84% → 0.67%.** Cae en todos los canales a la vez (PMAX, Directo, Referral). Es la espera de Cyber: la gente mira y no compra. No es un problema SEO. `HIPÓTESIS` bien sustentada por ser transversal.

**b) Semana posterior (9-15 nov): 0.40%, la mitad de lo normal.** Aquí el orgánico es el único canal que queda muy por debajo de su nivel de octubre; PMAX y Referral volvieron a lo normal. Lo que cambió:

- **SEM no volvió a su nivel**: 30,044 sesiones contra 7-9 mil en octubre (3.5-4x), con CR de 1.05%.
- **Orgánico perdió sesiones y compradores**: 24,946 sesiones (-23% vs el promedio de octubre, 33,195) y 99 transacciones (vs ~260).
- **Sumados, SEO + SEM convierten igual que antes**: 0.75% contra 0.71-0.79% en octubre.
- El gráfico de Ads muestra lo mismo: tras Cyber las impresiones vuelven al nivel de octubre pero los clics quedan más altos (lectura visual, ~13-14 mil/día vs ~10 mil), es decir, sube el CTR. Eso es típico de términos de marca.

**Conclusión (`HIPÓTESIS`, falta GSC y el detalle de términos de Ads):** la búsqueda en Google no convierte peor. Los compradores con intención (sobre todo quien busca la marca) están entrando por el anuncio y no por el resultado orgánico. El orgánico se queda con el tráfico informativo y por eso su CR se ve bajo. El costo real no es venta perdida, es **pagar clics que antes eran gratis**.

**c) Durante Cyber** el orgánico no creció en sesiones (31.5 mil, menos que en octubre) mientras SEM se multiplicó casi por 6 y PMAX por 2.5. La demanda extra de Cyber la captó la pauta. La venta orgánica de esa semana (S/ 1.08 M gross, ticket ~S/ 2,400 vs ~S/ 900 habitual) merece revisión: puede haber pocas órdenes muy grandes.

## 3. Qué falta para confirmarlo

| Dato | De dónde | Qué confirma |
|---|---|---|
| Clics, impresiones y posición de consultas **con marca vs sin marca**, por semana | GSC | Si lo que cayó en orgánico son los clics de marca |
| Términos de búsqueda de Ads por semana, con campaña y costo | Google Ads | Cuánto de SEM post-Cyber es marca y cuánto costó |
| Campañas de Search activas desde el 9-nov (¿quedó prendida una de marca o de "Cyber extendido"?) | Performance | Causa directa |
| Páginas de destino orgánicas del 9-15 nov y su CR | GA4 | Si landings de Cyber vencidas siguen recibiendo tráfico |
| Stock y precio de los productos más visitados tras Cyber | Comercial | Descartar quiebres de stock o subida de precios |

## 4. Otras causas posibles (no descartadas)

- Landings de Cyber que siguen posicionadas con ofertas ya terminadas.
- Quiebres de stock o precios más altos tras Cyber en las fichas con más tráfico orgánico.
- Resaca de demanda: quien iba a comprar ya compró (pero PMAX no la muestra).

## 5. Dato aparte
TikTok Ads: 154,578 sesiones y 6 transacciones en las cinco semanas. No es tema SEO, pero conviene que Performance lo revise (medición o calidad del tráfico).
