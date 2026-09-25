#!/usr/bin/env bash
# Mirror run.sh guards: same env + same baked work/ artifacts on first start.
set -euo pipefail
cd /app

if [[ -z "${DEEPSEEK_API_KEY:-}" ]]; then
  echo "ERROR: DEEPSEEK_API_KEY is not set (copy docker/.env.example → .env)."
  exit 1
fi

# Docker volume on /app/work hides image layers — seed from baked copy once.
if [[ ! -f /app/work/ro_password.txt ]] || [[ ! -f "/app/work/${CHATBOT_CLIENT:-105}/schema_cache.json" ]]; then
  echo "Seeding /app/work from baked image copy…"
  mkdir -p /app/work
  cp -a /opt/olives-work-baked/. /app/work/
fi

echo "Olives chatbot — CHATBOT_CLIENT=${CHATBOT_CLIENT:-105}"
echo "SQL snapshot: ${DB_HOST:-127.0.0.1}:${DB_PORT:-1433} → clients/${CHATBOT_CLIENT:-105}.yaml (chatbot_ro + work/ro_password.txt)"
echo "Vault notes: $(find obsidian/olives -name '*.md' 2>/dev/null | wc -l) markdown files"
echo "Listening on :8100"

exec python -m uvicorn api.server:app --host 0.0.0.0 --port 8100
