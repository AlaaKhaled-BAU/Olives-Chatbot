"""Thin client -> DeepSeek (direct; OmniRoute removed 2026-08).

NO key here (golden rule 3) -- API keys live in the gitignored .env
and are read from the environment at call time. Override endpoint with
CHATBOT_LLM_BASE_URL + CHATBOT_LLM_API_KEY (defaults: DeepSeek host and
DEEPSEEK_API_KEY). Non-DeepSeek hosts use CHATBOT_MODEL_FAST (default
composer-2.5) on every gear with thinking disabled.

Everything DeepSeek-specific about a request is captured in one GEARS table
so the agent picks a "gear" (model x thinking x effort x timeout) instead of
a raw model name:

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
from urllib.parse import urlparse

from dotenv import load_dotenv
import openai
from openai import OpenAI

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

FAST_MODEL = os.environ.get("CHATBOT_MODEL_FAST", "deepseek-v4-flash")
HEAVY_MODEL = os.environ.get("CHATBOT_MODEL_HEAVY", "deepseek-v4-pro")

_DEEPSEEK_HOSTS = frozenset({"api.deepseek.com", "deepseek.com"})


def llm_base_url() -> str:
    return os.environ.get("CHATBOT_LLM_BASE_URL", "https://api.deepseek.com").rstrip("/")


def _is_deepseek_host(base_url: str) -> bool:
    host = (urlparse(base_url).hostname or "").lower()
    return host in _DEEPSEEK_HOSTS or host.endswith(".deepseek.com")


def alternate_provider() -> bool:
    """OpenAI-compatible endpoint that is not DeepSeek (e.g. Composer battery)."""
    return not _is_deepseek_host(llm_base_url())


def llm_api_key() -> str:
    return os.environ.get("CHATBOT_LLM_API_KEY") or os.environ.get("DEEPSEEK_API_KEY", "")


def _alternate_fast_model() -> str:
    return os.environ.get("CHATBOT_MODEL_FAST", "composer-2.5")


_BASE_URL = llm_base_url()
_CLIENT_TIMEOUT = float(os.environ.get("CHATBOT_LLM_TIMEOUT", "60"))
_client = OpenAI(
    base_url=_BASE_URL,
    api_key=llm_api_key() or "missing-key",
    timeout=_CLIENT_TIMEOUT,
    max_retries=0,
)

_GEARS_DEEPSEEK: dict[str, dict] = {
    "f0": {"model": FAST_MODEL, "thinking": False, "effort": None, "timeout": 30},
    "t1": {"model": FAST_MODEL, "thinking": True, "effort": "low", "timeout": 60},
    "t2": {"model": FAST_MODEL, "thinking": True, "effort": "high", "timeout": 90},
    "p": {"model": HEAVY_MODEL, "thinking": True, "effort": "high", "timeout": 300},
}

GEARS: dict[str, dict] = dict(_GEARS_DEEPSEEK)


def resolve_gear(gear: str) -> dict:
    """Per-request gear config; non-DeepSeek hosts force one fast model, no thinking."""
    base = _GEARS_DEEPSEEK[gear]
    if not alternate_provider():
        return base
    model = _alternate_fast_model()
    return {**base, "model": model, "thinking": False, "effort": None}


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
    if not llm_api_key():
        return False
    try:
        list(_client.with_options(timeout=timeout).models.list())
        return True
    except Exception:  # noqa: BLE001 - health probe must never raise
        return False


def stream_create_kwargs(cfg: dict, messages, *, tools=None, response_format=None,
                         user_id=None, stream: bool = False) -> dict:
    """kwargs for chat.completions.create. Streamed calls request a final
    usage chunk. That chunk has usage set and choices empty — callers must
    not index choices[0] on it."""
    extra_body: dict = {}
    if not alternate_provider():
        extra_body["thinking"] = {"type": "enabled" if cfg["thinking"] else "disabled"}
        if cfg["thinking"] and cfg["effort"]:
            extra_body["reasoning_effort"] = cfg["effort"]
    if user_id:
        extra_body["user_id"] = user_id
    kwargs: dict = {
        "model": cfg["model"],
        "messages": messages,
        "stream": stream,
    }
    if extra_body:
        kwargs["extra_body"] = extra_body
    if stream:
        kwargs["stream_options"] = {"include_usage": True}
    if tools is not None:
        kwargs["tools"] = tools
    if response_format is not None:
        kwargs["response_format"] = response_format
    return kwargs


def complete(messages, gear: str = "t1", *, tools=None, stream=False,
             response_format=None, user_id=None, usage_acc=None):
    """One completion in the requested gear. Returns the raw SDK response
    (streaming iterator when stream=True). Raises ProviderUnavailableError
    for unreachable-provider conditions instead of hanging or leaking."""
    if not llm_api_key():
        raise RuntimeError(
            "CHATBOT_LLM_API_KEY / DEEPSEEK_API_KEY is not set — add it to .env"
        )
    cfg = resolve_gear(gear)
    async_gear = gear == "p"
    kwargs = stream_create_kwargs(
        cfg, messages, tools=tools, response_format=response_format,
        user_id=user_id, stream=stream,
    )

    max_retries = 3 if async_gear else 1
    last_error: Exception | None = None
    for attempt in range(max_retries + 1):
        t0 = time.monotonic()
        try:
            resp = _client.chat.completions.create(**kwargs)
            if stream:
                return _logged_stream(gear, resp, usage_acc, cfg["model"])
            elapsed = time.monotonic() - t0
            sdk_usage = getattr(resp, "usage", None)
            _log_usage(gear, sdk_usage, elapsed)
            if usage_acc is not None:
                usage_acc.add_sdk(gear, cfg["model"], sdk_usage, elapsed)
            return resp
        except openai.RateLimitError as e:
            last_error = e
        except openai.AuthenticationError as e:
            if alternate_provider():
                raise RuntimeError(
                    "CHATBOT_LLM_API_KEY was rejected — fix the key in .env"
                ) from e
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


def _logged_stream(gear: str, stream_iter, usage_acc=None, model: str = ""):
    """Pass-through. The final usage chunk has choices empty and usage set.
    Do not read choices[0] here. agent._stream_turn already skips empty choices."""
    usage = None
    t0 = time.monotonic()
    for chunk in stream_iter:
        u = getattr(chunk, "usage", None)
        if u is not None and getattr(u, "total_tokens", None):
            usage = u
        yield chunk
    elapsed = time.monotonic() - t0
    _log_usage(gear, usage, elapsed)
    if usage_acc is not None:
        usage_acc.add_sdk(gear, model, usage, elapsed)
