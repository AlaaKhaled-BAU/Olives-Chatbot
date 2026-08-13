#!/bin/bash
# Starts the Olives chatbot stack: SQL Server (optional), OmniRoute gateway check, API.
set -e
export PATH="$HOME/.local/bin:$HOME/.npm-global/bin:$PATH"
cd "$(dirname "$0")"

echo "Checking SQL Server container (drift-tool-mssql)..."
docker start drift-tool-mssql >/dev/null 2>&1 || echo "  (not running — skip if using remote SQL)"

if curl -sf http://localhost:20128/v1/models >/dev/null 2>&1; then
  echo "OmniRoute gateway OK on :20128"
else
  echo "Starting OmniRoute on :20128..."
  omniroute serve --port 20128 --no-open --daemon 2>/dev/null || true
  sleep 2
  curl -sf http://localhost:20128/v1/models >/dev/null || {
    echo "ERROR: OmniRoute not reachable. Run: omniroute serve --port 20128"
    exit 1
  }
fi

echo "Starting chatbot API on :8100..."
( set -a && source .env && set +a && exec python3.13 -m uvicorn api.server:app --host 0.0.0.0 --port 8100 ) &
SERVER_PID=$!
trap 'kill $SERVER_PID 2>/dev/null' EXIT

sleep 2
xdg-open http://localhost:8100 >/dev/null 2>&1 &

echo ""
echo "Olives Chatbot: http://localhost:8100"
echo "Gateway: $GATEWAY_URL (set in .env)"
echo "Press Ctrl+C to stop the API server."
wait
