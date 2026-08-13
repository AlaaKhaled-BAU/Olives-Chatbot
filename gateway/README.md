# Gateway

**Active:** [OmniRoute](https://github.com/diegosouzapw/OmniRoute) on `http://localhost:20128/v1`.

Provider keys (Gemini, OpenRouter, etc.) live in OmniRoute (`omniroute keys list`), not in this repo.
The chatbot app sends `GATEWAY_API_KEY` from the repo-root `.env` when calling OmniRoute.

## Run OmniRoute

```bash
omniroute serve --port 20128
# or daemon: omniroute serve --port 20128 --no-open --daemon
```

Set in repo-root `.env`:

```
GATEWAY_URL=http://localhost:20128/v1
GATEWAY_API_KEY=<your-omniroute-client-key>
CHATBOT_MODEL=auto/best-coding
```

## Verify

```bash
set -a && source ../.env && set +a
curl -s -X POST http://localhost:20128/v1/chat/completions \
  -H "Authorization: Bearer $GATEWAY_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"$CHATBOT_MODEL\",\"messages\":[{\"role\":\"user\",\"content\":\"hi\"}],\"max_tokens\":20}"
```

## LiteLLM (optional fallback)

`litellm.config.yaml` is kept for a self-hosted LiteLLM path. To use it instead:

1. Put provider keys in `gateway/.env` (`GEMINI_KEY`, `DEEPSEEK_KEY`, `MASTER_KEY`)
2. `litellm --config gateway/litellm.config.yaml --port 4000`
3. Point `.env` at `GATEWAY_URL=http://localhost:4000` and `CHATBOT_MODEL=chatbot`
