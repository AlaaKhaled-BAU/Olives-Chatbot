#!/usr/bin/env bash
# Dev-only: run chatbot in Docker against the *exact* local mssql data dir (bind mount).
# Same DB files as `run.sh` → 127.0.0.1:1433 on host.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MSSQL_DATA="${MSSQL_DATA:-/media/alaa/data/mssql-data}"
SNAPSHOTS="${SQL_SNAPSHOTS:-/media/alaa/data/olives/data/db-snapshots}"

if [[ ! -d "$MSSQL_DATA" ]]; then
  echo "ERROR: MSSQL_DATA not found: $MSSQL_DATA"
  exit 1
fi

export MSSQL_DATA SNAPSHOTS
envsubst '${MSSQL_DATA} ${SNAPSHOTS}' < "$ROOT/docker/compose.local-parity.template.yml" \
  > "$ROOT/docker-compose.local-parity.yml"
echo "Wrote docker-compose.local-parity.yml"
echo "  mssql data: $MSSQL_DATA"
echo "Run: docker compose -f docker-compose.local-parity.yml up"
