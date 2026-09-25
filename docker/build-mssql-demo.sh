#!/usr/bin/env bash
# Build olives-mssql-demo:latest — SQL Server 2022 with Olives_BO restored + chatbot_ro wall.
# Run from repo root. Requires Docker, python3.13 + pymssql on the host, and the .bak on disk.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

SA_PW="${MSSQL_SA_PASSWORD:-OlivesDemo_SA_2026!}"
BUILD_PORT="${MSSQL_BUILD_PORT:-14399}"
BAK_ROOT="$ROOT/data/db-snapshots"
# 105 multi-company snapshot — matches CHATBOT_CLIENT=105 / local run.sh (not morec single-company).
DEFAULT_BAK="$BAK_ROOT/backup test/105/olives_bo.bak"
BAK_FILE="${MSSQL_BAK_FILE:-$DEFAULT_BAK}"
IMAGE="${MSSQL_DEMO_IMAGE:-olives-mssql-demo:latest}"

if [[ ! -f "$BAK_FILE" ]]; then
  echo "ERROR: missing $BAK_FILE"
  echo "Place the Olives_BO.bak under data/db-snapshots/backup test/morec/ before building."
  exit 1
fi

echo "==> Starting temporary SQL Server for restore (port $BUILD_PORT)…"
docker rm -f olives-mssql-build >/dev/null 2>&1 || true
docker run -d --name olives-mssql-build \
  -e ACCEPT_EULA=Y \
  -e MSSQL_SA_PASSWORD="$SA_PW" \
  -e MSSQL_PID=Developer \
  -p "${BUILD_PORT}:1433" \
  -v "$BAK_ROOT:/snapshots:ro" \
  mcr.microsoft.com/mssql/server:2022-latest

cleanup() {
  docker rm -f olives-mssql-build >/dev/null 2>&1 || true
}
trap cleanup EXIT

export DB_HOST=127.0.0.1 DB_PORT="$BUILD_PORT" DB_SA_USER=sa DB_SA_PASSWORD="$SA_PW"
export MSSQL_WAIT_SECONDS=600
python3.13 docker/wait-mssql.py

echo "==> Restoring Olives_BO from .bak (this may take several minutes)…"
python3.13 setup/01_db_up.py --mode native --db-name Olives_BO --bak "$BAK_FILE"

echo "==> Applying chatbot_ro login + t. tenant views…"
python3.13 setup/03_apply_db_sql.py --db-name Olives_BO

echo "==> Committing image $IMAGE …"
docker commit olives-mssql-build "$IMAGE"

echo ""
echo "Built $IMAGE"
echo "  SA password (demo only): $SA_PW"
echo "  chatbot_ro password:     $(cat work/ro_password.txt)"
echo "  Save: docker save $IMAGE -o docker/out/olives-mssql-demo.tar"
