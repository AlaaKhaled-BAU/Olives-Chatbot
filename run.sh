#!/bin/bash
# Starts the Olives chatbot API (DeepSeek direct; no gateway since 2026-08).
set -e
export PATH="$HOME/.local/bin:$HOME/.npm-global/bin:$PATH"
cd "$(dirname "$0")"

echo "Using SQL Server at ${DB_HOST:-127.0.0.1}:${DB_PORT:-1433} (set in .env)"

if ! grep -q "^DEEPSEEK_API_KEY=..*" .env 2>/dev/null; then
  echo "ERROR: DEEPSEEK_API_KEY not set in .env"
  exit 1
fi

echo "Starting chatbot API on :8100 (127.0.0.1)..."
( set -a && source .env && set +a && exec python3.13 -m uvicorn api.server:app --host 127.0.0.1 --port 8100 ) &
SERVER_PID=$!
trap 'kill $SERVER_PID 2>/dev/null' EXIT

sleep 2
xdg-open http://localhost:8100 >/dev/null 2>&1 &

echo ""
echo "Olives Chatbot: http://localhost:8100"
echo "Provider: DeepSeek (${CHATBOT_MODEL_FAST:-deepseek-v4-flash} / rescue ${CHATBOT_MODEL_HEAVY:-deepseek-v4-pro})"
echo "Press Ctrl+C to stop the API server."
wait
