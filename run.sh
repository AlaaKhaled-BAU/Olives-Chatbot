#!/bin/bash
# Starts everything the Olives chatbot needs: the shared SQL Server container,
# the LiteLLM gateway, and the chatbot API server -- then opens the browser.
# Ctrl+C (or closing this terminal) stops the gateway and server.
set -e
export PATH="$HOME/.local/bin:$PATH"
cd "$(dirname "$0")"

echo "Starting SQL Server container (drift-tool-mssql, shared with the drift tool)..."
docker start drift-tool-mssql >/dev/null 2>&1 || echo "  (couldn't start it -- check 'docker ps -a')"

echo "Starting LiteLLM gateway on :4000..."
( set -a && source gateway/.env && set +a && exec litellm --config gateway/litellm.config.yaml --port 4000 ) &
GATEWAY_PID=$!
trap 'kill $GATEWAY_PID $SERVER_PID 2>/dev/null' EXIT

sleep 3

echo "Starting chatbot API server on :8100..."
( set -a && source .env && set +a && exec python3.13 -m uvicorn api.server:app --host 0.0.0.0 --port 8100 ) &
SERVER_PID=$!

sleep 2
xdg-open http://localhost:8100 >/dev/null 2>&1 &

echo ""
echo "Olives Chatbot running at http://localhost:8100"
echo "You'll need one of the access tokens from client-chatbot/.env to log in."
echo "Press Ctrl+C to stop."
wait
