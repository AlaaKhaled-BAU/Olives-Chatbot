#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
IMAGE="${CHATBOT_IMAGE:-olives-chatbot:latest}"
docker build -t "$IMAGE" -f Dockerfile .
echo "Built $IMAGE"
mkdir -p docker/out
docker save "$IMAGE" -o docker/out/olives-chatbot.tar
ls -lh docker/out/olives-chatbot.tar
