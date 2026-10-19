#!/usr/bin/env bash
# Corre un reporte de sql/reportes/ y devuelve pocas filas resumidas (pensado para leer rápido, o para Claude).
# Uso: PROYECTO=<id-proyecto-gcp> scripts/reporte.sh r01 [marca]      # marca por defecto: efectibank
#      scripts/reporte.sh lista
# Credencial: la de gcloud/bq activa, o la variable GOOGLE_APPLICATION_CREDENTIALS_JSON
# (cuenta de servicio de SOLO LECTURA guardada en la configuración del entorno, nunca en el repo).
set -euo pipefail

DIR="$(cd "$(dirname "$0")/.." && pwd)"
if [[ "${1:-}" == "lista" || -z "${1:-}" ]]; then
  for f in "$DIR"/sql/reportes/*.sql; do printf '%-28s %s\n' "$(basename "$f" .sql)" "$(head -1 "$f" | sed 's/^-- //')"; done
  exit 0
fi

: "${PROYECTO:?Definir PROYECTO (id del proyecto de Google Cloud)}"
UBICACION="${UBICACION:-US}"
MARCA="${2:-efectibank}"
TOPE_BYTES="${TOPE_BYTES:-5000000000}"   # 5 GB: un reporte sobre resúmenes lee mucho menos
archivo="$(ls "$DIR"/sql/reportes/"$1"*.sql 2>/dev/null | head -1)"
[[ -n "$archivo" ]] || { echo "No existe el reporte $1 (ver: $0 lista)"; exit 1; }

if [[ -n "${GOOGLE_APPLICATION_CREDENTIALS_JSON:-}" ]]; then
  clave="$(mktemp)"; chmod 600 "$clave"
  trap 'rm -f "$clave"' EXIT
  printf '%s' "$GOOGLE_APPLICATION_CREDENTIALS_JSON" > "$clave"
  gcloud auth activate-service-account --key-file="$clave" --quiet >/dev/null 2>&1
fi

bq query --project_id="$PROYECTO" --location="$UBICACION" --use_legacy_sql=false \
  --maximum_bytes_billed="$TOPE_BYTES" --max_rows=100 --format=pretty \
  --parameter="marca:STRING:${MARCA}" \
  "$(sed "s/__PROYECTO__/${PROYECTO}/g" "$archivo")"
