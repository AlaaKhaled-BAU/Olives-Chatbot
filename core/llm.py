"""Thin client -> the gateway. NO key here (PLAN.md golden rule 4) -- core/
reaches the LLM only through the gateway's base_url. LiteLLM (or OmniRoute)
holds the real key behind GATEWAY_URL.

S2 (2026-07-26): the OpenAI client had no timeout at all -- a genuinely
hung gateway (not a fast HTTP-level rate-limit/auth error, an actual
network hang) would block a worker thread indefinitely, with nothing in
this file able to time it out. 30s matches the precedent
gateway/litellm.config.yaml's own comment already establishes ("a client-
facing timeout should stay generous (20-30s), matching... core/sql.py's
own 30s pymssql timeout") -- not a new arbitrary number. Retry sleep was
also uncapped in practice (12+24+36=72s worst case across 3 retries,
purely in time.sleep, before even counting request time) -- reduced since
this is documented as "just a thin client-side safety net" for a BRIEF
gateway hiccup, not a full retry strategy (the real fallback/retry logic
lives server-side in the gateway, see the docstring below).

Deliberately NOT done here: emitting a progress signal before each retry.
That needs the actual SSE progress-frame mechanism C7 (Phase 10) builds --
today's /ask only ever sends one frame at the end, so there is nothing yet
for a mid-retry signal to feed into. Land it with C7, not as a half-built
piece here."""
import os
import time

import openai
from openai import OpenAI

_client = OpenAI(
    base_url=os.environ.get("GATEWAY_URL", "http://localhost:4000"),
    api_key=os.environ.get("GATEWAY_API_KEY", "not-needed"),
    timeout=30.0,
)

MODEL = os.environ.get("CHATBOT_MODEL", "auto/best-coding")


def complete(messages, retries: int = 3, **kwargs):
    """Retries on rate limits and auth errors with backoff. Primary/fallback
    routing itself happens server-side in the gateway (FIXPLAN M2: distinct
    model_name deployments + router_settings.fallbacks keyed on "chatbot" --
    see gateway/litellm.config.yaml's comment for why that specific shape is
    the only one of three tested that doesn't leak raw errors). This retry
    is just a thin client-side safety net for a RateLimitError/
    AuthenticationError that gets through anyway (e.g. the gateway itself
    briefly unreachable) -- the gateway's own fallback already covers a dead
    model deployment."""
    last_error = None
    for attempt in range(retries + 1):
        try:
            return _client.chat.completions.create(model=MODEL, messages=messages, **kwargs)
        except (openai.RateLimitError, openai.AuthenticationError) as e:
            last_error = e
            if attempt < retries:
                time.sleep(min(5 * (attempt + 1), 15))
    raise last_error
