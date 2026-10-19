#!/usr/bin/env bash
# Despliega el modelo SEO en BigQuery y crea la consulta programada diaria.
# Uso:
#   PROYECTO=<id-proyecto-gcp> UBICACION=US scripts/desplegar.sh tablas     # 00 + 01 (antes o después de activar GSC)
#   PROYECTO=<id-proyecto-gcp> UBICACION=US scripts/desplegar.sh vistas     # 02 (cuando ya existan las tablas de la exportación)
#   PROYECTO=<id-proyecto-gcp> UBICACION=US scripts/desplegar.sh programar  # consulta programada diaria con 20
#   PROYECTO=<id-proyecto-gcp> UBICACION=US scripts/desplegar.sh correr 20  # corre a mano un archivo sql/NN_*.sql
# Lo ejecuta una persona con permiso de edición en el proyecto (no la cuenta de solo lectura de los reportes).
set -euo pipefail

: "${PROYECTO:?Definir PROYECTO (id del proyecto de Google Cloud)}"
UBICACION="${UBICACION:-US}"
HORA_UTC="${HORA_UTC:-12:00}"   # 07:00 en Lima; la exportación de GSC suele estar lista antes
TOPE_BYTES="${TOPE_BYTES:-50000000000}"   # 50 GB por consulta: freno ante un error que lea todo
DIR="$(cd "$(dirname "$0")/.." && pwd)"

sql() {  # imprime un archivo SQL con proyecto y ubicación reemplazados
  sed -e "s/__PROYECTO__/${PROYECTO}/g" -e "s/__UBICACION__/${UBICACION}/g" "$1"
}

correr() {
  echo ">> $(basename "$1")"
  bq query --project_id="$PROYECTO" --location="$UBICACION" --use_legacy_sql=false \
    --maximum_bytes_billed="$TOPE_BYTES" --format=none "$(sql "$1")"
}

case "${1:-}" in
  tablas)
    correr "$DIR/sql/00_tablas.sql"
    for f in "$DIR"/sql/01_config_*.sql; do correr "$f"; done
    ;;
  vistas)
    correr "$DIR/sql/02_vistas_gsc.sql"
    ;;
  programar)
    params="$(sql "$DIR/sql/20_actualizar_diario.sql" | python3 -c 'import json,sys; print(json.dumps({"query": sys.stdin.read()}))')"
    bq mk --transfer_config --project_id="$PROYECTO" --location="$UBICACION" \
      --data_source=scheduled_query \
      --display_name="seo_gsc_actualizar_diario" \
      --schedule="every day ${HORA_UTC}" \
      --params="$params"
    ;;
  correr)
    archivo="$(ls "$DIR"/sql/"${2:?Indicar el número, p. ej. 21}"_*.sql | head -1)"
    correr "$archivo"
    ;;
  *)
    sed -n '2,9p' "$0"; exit 1
    ;;
esac
