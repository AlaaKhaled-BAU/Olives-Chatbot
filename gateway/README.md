# Gateway

Key custody lives here ONLY (PLAN.md golden rule 4). `core/` and `api/` never
see `LLM_API_KEY` or `GEMINI_KEY` -- they call `http://localhost:4000` with no key.

## Run

```
cp gateway/.env.example gateway/.env   # paste LLM_API_KEY (Claude); GEMINI_KEY is the fallback
set -a && source gateway/.env && set +a
litellm --config gateway/litellm.config.yaml --port 4000
```

Claude (`chatbot`, primary) and Gemini (`chatbot`, fallback) share one model
alias -- `core/llm.py` only ever asks for `"chatbot"`. On primary outage
(bad/missing key, rate limit, etc.) LiteLLM retries the fallback
automatically. Cache is in-memory for pilot (`cache_params.type: local`);
swap to `type: redis` (`docker run -p 6379:6379 redis`) when HA matters.

## Verify it's working

```
curl -s -i -X POST http://localhost:4000/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"chatbot","messages":[{"role":"user","content":"hi"}]}'
```

A repeat of the exact same request should come back with an
`x-litellm-cache-key` header and a near-zero `x-litellm-response-duration-ms`
-- that's the cache hit.
