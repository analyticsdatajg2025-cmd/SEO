# Landing BCP en Juntoz · administrable desde Google Sheets

El diseño es el de la landing BCP original (mismo HTML y CSS, encapsulado en `#bcp-landing`, sin JavaScript). Lo que cambia por campaña se edita en el Google Sheet. Después se genera el HTML final y se pega en Magento.

```
Google Sheet ──(generador.py)──> vista previa local ──> publicado/bcp-landing.html ──(copiar y pegar)──> Magento CMS
```

| Archivo | Para qué |
|---|---|
| `plantilla.html` | Diseño de la landing con campos `data-field` y variables. No se publica tal cual. |
| `generador.py` | Lee el Sheet, valida, genera la vista previa y el HTML final, y guarda respaldos. |
| `tests/` | Pruebas: `python3 -m unittest discover -s tests` |
| `salida/` | Vista previa y plantilla .xlsx (no se suben al repo). |
| `publicado/bcp-landing.html` | Última versión publicable. |
| `respaldos/` | Versión anterior y diff de cada publicación (no se suben al repo). |

## 1. Preparar (una sola vez)

1. `pip install -r requirements.txt`
2. Crear la plantilla: `python3 generador.py plantilla` → genera `salida/BCP_Google_Sheets_Plantilla.xlsx`.
3. En el Google Sheet: *Archivo → Importar → Subir* el .xlsx → *Reemplazar hoja de cálculo*. Deben quedar estas pestañas: Instrucciones, Config, Textos, Slides, Productos, Beneficios, Pasos, FAQ y Legales. No hay que renombrar las pestañas ni los encabezados.
4. Configurar el acceso de solo lectura:
   - En Google Cloud, crear una cuenta de servicio, habilitar *Google Sheets API* y descargar su clave JSON.
   - Guardar la clave **fuera del repo**, por ejemplo en `~/.config/juntoz/bcp-sheets.json`. El generador se niega a usar una clave guardada dentro del repo.
   - Compartir el Sheet con el correo de la cuenta de servicio como **Lector**.
   - En la terminal:
     ```
     export BCP_SHEET_ID="<ID que aparece en la URL del Sheet, entre /d/ y /edit>"
     export GOOGLE_APPLICATION_CREDENTIALS="$HOME/.config/juntoz/bcp-sheets.json"
     ```

**Sin credenciales:** descargar el Sheet con *Archivo → Descargar → .xlsx* y agregar `--fuente xlsx --archivo descarga.xlsx` a cada comando.

## 2. Actualizar y publicar

1. Editar el Sheet. En los textos se pueden usar las variables `{banco} {codigo} {porcentaje} {tope} {minimo} {vigencia} {tarjetas} {n_pasos}`. `**texto**` pone el texto en negrita; en el título del slide, lo pinta de azul.
2. Vista previa: `python3 generador.py previsualizar` y abrir `salida/bcp-landing.preview.html` en el navegador.
   - Arriba aparecen los errores y avisos.
   - Lo que falta se marca en amarillo.
   - Al pasar el mouse sobre un texto se ve de qué celda sale.
3. Publicar: `python3 generador.py publicar --verificar-urls`
   - Si hay errores, no genera nada y lista los errores.
   - Si todo está bien, escribe `publicado/bcp-landing.html` y guarda la versión anterior en `respaldos/`, junto con un `.diff` de los cambios.
4. Pegar en Magento:
   - Abrir *Contenido → Elementos → Páginas* (o *Bloques*) y entrar a la landing BCP.
   - Reemplazar todo el contenido por el de `publicado/bcp-landing.html`. Con Page Builder, usar un elemento *HTML Code*.
   - Guardar.
   - Limpiar la caché en *Sistema → Gestión de caché*.
   - Revisar la URL en vivo en celular y en escritorio.
5. Para volver a la versión anterior: pegar en Magento el archivo de `respaldos/` que corresponda.

**Merchant Center no se actualiza solo.** Esta landing es HTML estático en Magento. Merchant Center no la recibe de este proceso; solo rastrea la URL. Los cambios aparecen cuando Magento sirve la versión nueva y Google vuelve a rastrear la página. Los precios y promociones de los productos del feed se cambian en el feed, no aquí.

## 3. Qué bloquea la publicación

- **Datos de campaña:** falta un dato obligatorio de Config (código, %, tope, mínimo, fechas, tarjetas) o un texto obligatorio.
- **Fechas:** la promoción ya venció, o la fecha de fin es anterior a la de inicio.
- **Legales:**
  - `legales_aprobados` no está en SI.
  - Falta quién aprobó o la fecha de aprobación.
  - La pestaña Legales está vacía.
  - Los legales se publican **tal cual** (una fila por párrafo): sin variables, sin formato y sin resumir.
- **Enlaces e imágenes:**
  - No son https, son de un dominio que no está en `dominios_enlaces` / `dominios_imagenes`, o apuntan a un ancla que no existe.
  - Con `--verificar-urls`: no responden, o la imagen no devuelve una imagen.
- **Filas:** `visible` distinto de SI/NO, `orden` que no es un número entero, no queda ningún slide o producto visible.
- **Marcadores sin completar** (`[XX]`, `[CÓDIGO]`, `TODO`, `PENDIENTE`, lorem ipsum) o variables desconocidas.
- **Controles sobre el HTML final:** contiene JavaScript, `data-field`, CSS fuera de `#bcp-landing`, algo que parece una credencial, o no tiene exactamente un H1.

Avisos que no bloquean:
- Un campo opcional vacío oculta su elemento.
- Una sección sin filas visibles no se muestra.
- Un color vacío usa el color por defecto.
- Los legales no mencionan el código, el porcentaje, el tope o el mínimo de Config.
