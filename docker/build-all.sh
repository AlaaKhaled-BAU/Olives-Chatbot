#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
mkdir -p docker/out
echo "=== Building chatbot image ==="
bash docker/build-chatbot.sh
echo ""
if docker inspect "${MSSQL_SOURCE_CONTAINER:-mssql}" >/dev/null 2>&1 \
   && [[ "${MSSQL_BUILD_FROM_BAK:-}" != "1" ]]; then
  echo "NOTE: local mssql uses a bind-mounted data dir — commit cannot capture it."
  echo "      Building from 105/olives_bo.bak (same tenant as CHATBOT_CLIENT=105)."
fi
echo "=== Building mssql demo image from 105 olives_bo.bak ==="
bash docker/build-mssql-demo.sh
echo ""
echo "=== Saving mssql demo tar ==="
docker save olives-mssql-demo:latest -o docker/out/olives-mssql-demo.tar
ls -lh docker/out/*.tar
echo ""
echo "Done. Ship docker/out/*.tar + docker-compose*.yml + docker/.env.example to your boss."
