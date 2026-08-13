#!/usr/bin/env bash
# Isolated SQL-Server-MCP test. Proves the DB is reachable ONLY through the MCP,
# in a topology where the chatbot is on a different network than the DB.
#
# Reuses the already-running drift-tool-mssql; the host publish :14330 and the
# in-process pymssql path stay untouched = current setup remains the FALLBACK.
#
# Topology:
#   olives_dbnet  (internal, no host route) : DB  +  MCP
#   olives_appnet (internal, no host route) : MCP +  test-client
#   -> test-client sees the MCP but has NO route to the DB. Only the MCP bridges both.
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"        # client-chatbot/
IMG=olives-sqlmcp:test

echo "[*] build image with deps baked in (needs internet; the isolated nets have none)"
docker build -q -t "$IMG" "$ROOT/sqlmcp" >/dev/null || { echo "[!] build failed"; exit 4; }

echo "[*] nets + attach DB (additive, reversible; fallback untouched)"
docker network create --internal olives_dbnet  2>/dev/null || true
docker network create --internal olives_appnet 2>/dev/null || true
docker network connect olives_dbnet drift-tool-mssql 2>/dev/null || true

echo "[*] start MCP on dbnet (SSE :9000), then add appnet"
docker rm -f olives-sql-mcp >/dev/null 2>&1 || true
docker run -d --name olives-sql-mcp --network olives_dbnet \
  -e DB_HOST=drift-tool-mssql -e DB_PORT=1433 -e MCP_PORT=9000 \
  -e MCP_ALLOWED_HOSTS="olives-sql-mcp:*" \
  -v "$ROOT":/app -w /app "$IMG" \
  python sqlmcp/sql_server.py >/dev/null
docker network connect olives_appnet olives-sql-mcp

echo "[*] wait for MCP to install deps + bind :9000 (up to ~2min)"
UP=0
for _ in $(seq 1 40); do
  if docker run --rm --network olives_appnet "$IMG" \
       python -c 'import socket;socket.create_connection(("olives-sql-mcp",9000),timeout=2)' 2>/dev/null; then
    UP=1; break
  fi
  sleep 3
done
if [ "$UP" != 1 ]; then
  echo "[!] MCP never came up. Last logs:"; docker logs --tail 30 olives-sql-mcp 2>&1
  docker rm -f olives-sql-mcp >/dev/null 2>&1 || true
  exit 3
fi

echo "[*] run the isolation proof on appnet (no DB route)"
docker run --rm --network olives_appnet -v "$ROOT":/app -w /app "$IMG" \
  python sqlmcp/prove_isolation.py
RC=$?

echo "[*] teardown MCP; DB + host:14330 fallback stay up"
docker rm -f olives-sql-mcp >/dev/null 2>&1 || true
# to fully restore the DB's networking too:
#   docker network disconnect olives_dbnet drift-tool-mssql
#   docker network rm olives_dbnet olives_appnet
echo "[*] result exit=$RC  (0 = DB reachable ONLY via MCP, and query worked)"
exit $RC
