# 12 · PDL «Crédito en electrodomésticos» en La Curacao

Fecha: 20-oct-2026. Archivo: `landings/pdl-credito-electrodomesticos-lc.html` (vista previa con el bloque listo para Magento).

## Qué es
Una página de listado (PDL) dentro de La Curacao con el mismo patrón que `/curacao/oferta-web-celulares.html`, para la búsqueda de compra en cuotas de electrodomésticos y para enlazar al Préstamo Electro de Efectibank (crédito del grupo: `docs/08`). URL propuesta: `https://www.lacuracao.pe/curacao/credito-electrodomesticos.html` (**hoy no existe**: crear la categoría antes de publicar).

## Cómo se eligieron los productos
- **Ventas:** Yandex Metrica de lacuracao.pe (`cyber-dashboard/historico.json`, top 100 productos por día), 2026-08-20 a 2026-10-18: ingresos gross y unidades por SKU, último clic significativo. **No es GA4**: en los repos no hay GA4 de La Curacao (`docs/07`). `COMPROBADO` como fuente; las cifras por SKU van en el Excel de trabajo, no en el repo.
- **Catálogo:** feed de Facebook de la tienda descargado el 20-oct-2026 (precio regular, oferta, stock, foto, URL).
- **Reglas:** electrodomésticos por nombre (línea blanca, cocina, TV y audio, climatización, pequeños electro; fuera celulares, cómputo, menaje, muebles, motos); en stock; precio de venta desde S/ 300 (lo que conviene financiar); 2 o más unidades en 60 días; orden por ingresos; los 60 primeros.
- **Resultado:** 60 productos (Línea blanca 32, TV y audio 16, Cocina 10, Climatización 1, Pequeños electro 1); 21 desde S/ 1,500. Suman S/ 714,565 de ingresos gross en los 60 días (Yandex).
- **Limitación:** Yandex guarda solo el top 100 diario; un producto con pocas ventas diarias puede quedar fuera aunque sume en el mes. Repetir con GA4 (ítem × ingresos) cuando haya acceso.

## Qué trae la página
- Title, description, canonical, Open Graph, H1 «Crédito en electrodomésticos», texto de entrada, migas, FAQ y schema `CollectionPage` + `ItemList` + `BreadcrumbList` + `FAQPage`.
- Banda de crédito con enlace al Préstamo Electro de Efectibank con UTM (`utm_source=lacuracao&utm_medium=referral&utm_campaign=pdl-credito-electrodomesticos&utm_content=pdl`): es otro dominio, así que la UTM sí corresponde.
- Filtros: Todos, Más vendidos (12 con más unidades), Desde S/ 1,500, y por categoría; orden por recomendados (ingresos), más vendidos y precio. Los productos están en el HTML (sin depender de JS para que Google los lea).
- Estilos encapsulados en `#lc-pdl-credito`; no tocan header ni footer.

## Para publicar (Magento)
1. Crear la categoría `credito-electrodomesticos` bajo `/curacao/` con título, meta y H1 de este archivo.
2. Asignar los SKU en el orden de la hoja «Para Magento» del Excel (posición = orden recomendado), o pegar el bloque como contenido de CMS.
3. Precios y stock: en Magento los pone la categoría en vivo; en la vista previa son del 20-oct-2026.
4. **Validar con Comercial y Legal** el texto del crédito (Efectibank, módulos en tienda, «simula tu cuota») y el legal.
5. Enlazar la PDL desde la home y desde las fichas de línea blanca y TV, y pedir indexación en Search Console.
6. Revisar la lista cada mes con los datos nuevos (y antes de Cyber).

## Hallazgo de paso
La página modelo `/curacao/oferta-web-celulares.html` no tiene etiqueta canonical y usa la meta description genérica del sitio (`COMPROBADO`, 20-oct-2026).
