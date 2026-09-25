"""Thin client -> DeepSeek (direct; OmniRoute removed 2026-08).

NO key here (golden rule 3) -- DEEPSEEK_API_KEY lives in the gitignored .env
and is read from the environment at call time. Everything DeepSeek-specific
about a request is captured in one GEARS table so the agent picks a "gear"
(model x thinking x effort x timeout) instead of a raw model name:

  f0 = flash, thinking OFF      doc answers / envelope / fast-count emission
  t1 = flash, think low         standard NL2SQL lookups
  t2 = flash, think high        multi-hop joins / compound questions
  p  = pro,   think high (ASYNC ONLY -- never in the interactive path)

DeepSeek API contracts honored here (verified against api-docs 2026-08-22):
- Thinking mode is ON by default at effort=high; we always pass an explicit
  toggle so gears are deterministic.
- `temperature`/`top_p` are silently ignored in thinking mode -> never relied on.
- With tools + thinking, every subsequent request must echo the assistant's
  reasoning_content or the API returns HTTP 400 (threaded in core/agent.py).
- KV cache: automatic disk prefix cache billed at hit/miss rates; usage fields
  prompt_cache_hit_tokens/prompt_cache_miss_tokens logged per call.
- user_id: [a-zA-Z0-9_-]+ only; passed via extra_body for per-user cache and
  scheduling isolation.
- Streaming sends ": keep-alive" SSE comments during long inference; the OpenAI
  SDK drops comment lines, so api/server.py synthesizes its own heartbeats.

Retry policy (review finding #15): SDK retries disabled (max_retries=0); this
module owns exactly one retry layer. Interactive gears fail fast into
ProviderUnavailableError; async gear p may retry transient failures.
"""
import os
from pathlib import Path
import random
import time

from dotenv import load_dotenv
import openai
from openai import OpenAI

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

FAST_MODEL = os.environ.get("CHATBOT_MODEL_FAST", "deepseek-v4-flash")
HEAVY_MODEL = os.environ.get("CHATBOT_MODEL_HEAVY", "deepseek-v4-pro")

_client = OpenAI(
    base_url="https://api.deepseek.com",
    api_key=os.environ.get("DEEPSEEK_API_KEY", "missing-key"),
    timeout=60.0,
    max_retries=0,
)

GEARS: dict[str, dict] = {
    "f0": {"model": FAST_MODEL, "thinking": False, "effort": None, "timeout": 30},
    "t1": {"model": FAST_MODEL, "thinking": True, "effort": "low", "timeout": 60},
    "t2": {"model": FAST_MODEL, "thinking": True, "effort": "high", "timeout": 90},
    "p": {"model": HEAVY_MODEL, "thinking": True, "effort": "high", "timeout": 300},
}

# Shown to end users when the provider is unreachable — never leak raw HTTP text.
PROVIDER_UNAVAILABLE_AR = (
    "عذراً، خدمة الذكاء الاصطناعي غير متاحة مؤقتاً. يرجى المحاولة بعد قليل."
)

# Back-compat alias for older imports/tests.
GATEWAY_UNAVAILABLE_AR = PROVIDER_UNAVAILABLE_AR


class ProviderUnavailableError(Exception):
    """Provider unreachable / 5xx / timeout — surface PROVIDER_UNAVAILABLE_AR."""


class GatewayUnavailableError(ProviderUnavailableError):
    """Back-compat alias (old name) — do not use in new code."""


def _log_usage(gear: str, usage, elapsed_s: float) -> None:
    if usage is None:
        return
    hit = getattr(usage, "prompt_cache_hit_tokens", None)
    miss = getattr(usage, "prompt_cache_miss_tokens", None)
    print(
        f"[llm] gear={gear} model={getattr(usage, 'model', '?')} "
        f"in={getattr(usage, 'prompt_tokens', '?')} out={getattr(usage, 'completion_tokens', '?')} "
        f"cache_hit={hit} cache_miss={miss} {elapsed_s:.1f}s",
        flush=True,
    )


def provider_health(timeout: float = 5.0) -> bool:
    """GET /models with the account key — cheap liveness probe for /health."""
    if not os.environ.get("DEEPSEEK_API_KEY"):
        return False
    try:
        list(_client.with_options(timeout=timeout).models.list())
        return True
    except Exception:  # noqa: BLE001 - health probe must never raise
        return False


def complete(messages, gear: str = "t1", *, tools=None, stream=False,
             response_format=None, user_id=None):
    """One completion in the requested gear. Returns the raw SDK response
    (streaming iterator when stream=True). Raises ProviderUnavailableError
    for unreachable-provider conditions instead of hanging or leaking."""
    if not os.environ.get("DEEPSEEK_API_KEY"):
        raise RuntimeError("DEEPSEEK_API_KEY is not set — add it to .env")
    cfg = GEARS[gear]
    async_gear = gear == "p"
    extra_body: dict = {"thinking": {"type": "enabled" if cfg["thinking"] else "disabled"}}
    if cfg["thinking"] and cfg["effort"]:
        extra_body["reasoning_effort"] = cfg["effort"]
    if user_id:
        extra_body["user_id"] = user_id

    kwargs: dict = {
        "model": cfg["model"],
        "messages": messages,
        "stream": stream,
        "extra_body": extra_body,
    }
    if tools is not None:
        kwargs["tools"] = tools
    if response_format is not None:
        kwargs["response_format"] = response_format

    max_retries = 3 if async_gear else 1
    last_error: Exception | None = None
    for attempt in range(max_retries + 1):
        t0 = time.monotonic()
        try:
            resp = _client.chat.completions.create(**kwargs)
            if stream:
                return _logged_stream(gear, resp)
            _log_usage(gear, getattr(resp, "usage", None), time.monotonic() - t0)
            return resp
        except openai.RateLimitError as e:
            last_error = e
        except openai.AuthenticationError as e:
            raise RuntimeError(
                "DEEPSEEK_API_KEY was rejected — fix the key in .env"
            ) from e
        except (openai.APIConnectionError, openai.APITimeoutError) as e:
            if not async_gear:
                raise ProviderUnavailableError(PROVIDER_UNAVAILABLE_AR) from e
            last_error = e
        except openai.APIStatusError as e:
            status = getattr(getattr(e, "response", None), "status_code", None)
            if not async_gear or status is None or status < 500:
                raise ProviderUnavailableError(PROVIDER_UNAVAILABLE_AR) from e
            last_error = e
        if attempt < max_retries:
            time.sleep(min(random.uniform(1.0, 3.0) * (attempt + 1), 15.0))
    raise ProviderUnavailableError(PROVIDER_UNAVAILABLE_AR) from last_error


def _logged_stream(gear: str, stream_iter):
    """Pass-through generator that captures usage from the final chunk when
    the provider includes it, then logs once at stream end."""
    usage = None
    t0 = time.monotonic()
    for chunk in stream_iter:
        u = getattr(chunk, "usage", None)
        if u is not None and getattr(u, "total_tokens", None):
            usage = u
        yield chunk
    _log_usage(gear, usage, time.monotonic() - t0)
