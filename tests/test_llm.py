"""DeepSeek direct-client contract (post-OmniRoute): explicit timeouts, no
SDK retry stacking, correct down-detection, per-gear params, user_id shape."""
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import httpx
import openai
import pytest

from core import llm


def _fake_response(status_code=429):
    import types
    return types.SimpleNamespace(status_code=status_code, headers={}, request=types.SimpleNamespace())


def _conn_error():
    return openai.APIConnectionError(request=httpx.Request("POST", "https://api.deepseek.com"))


def _timeout_error():
    return openai.APITimeoutError(request=httpx.Request("POST", "https://api.deepseek.com"))


def test_sdk_retries_disabled():
    assert llm._client.max_retries == 0, "SDK retries must be off — app-level policy owns retrying"


def test_gears_table_shape():
    assert set(llm.GEARS) == {"f0", "t1", "t2", "p"}
    assert llm.GEARS["f0"]["thinking"] is False
    assert all(g["thinking"] for g in llm.GEARS.values() if g is not llm.GEARS["f0"])
    assert llm.GEARS["p"]["model"] == llm.HEAVY_MODEL
    assert llm.GEARS["f0"]["model"] == llm.FAST_MODEL


def test_f0_disables_thinking_explicitly():
    import types as _t
    captured = {}

    def _create(**kwargs):
        captured.update(kwargs)
        usage = _t.SimpleNamespace(prompt_tokens=1, completion_tokens=1,
                                   prompt_cache_hit_tokens=0, prompt_cache_miss_tokens=1)
        return _t.SimpleNamespace(
            choices=[_t.SimpleNamespace(message=_t.SimpleNamespace(content="ok"))], usage=usage)

    with patch.object(llm._client.chat.completions, "create", side_effect=_create):
        llm.complete([{"role": "user", "content": "hi"}], gear="f0")
    eb = captured["extra_body"]
    assert eb["thinking"] == {"type": "disabled"}
    assert "reasoning_effort" not in eb
    assert captured["model"] == llm.FAST_MODEL


def test_t1_sends_low_effort_and_p_uses_heavy():
    seen = []

    def _create(**kwargs):
        seen.append(kwargs)
        import types as _t
        msg = _t.SimpleNamespace(content="ok")
        usage = _t.SimpleNamespace(prompt_tokens=1, completion_tokens=1)
        return _t.SimpleNamespace(choices=[_t.SimpleNamespace(message=msg)], usage=usage)

    with patch.object(llm._client.chat.completions, "create", side_effect=_create):
        llm.complete([{"role": "user", "content": "q"}], gear="t1")
        llm.complete([{"role": "user", "content": "q"}], gear="p")
    assert seen[0]["extra_body"]["thinking"] == {"type": "enabled"}
    assert seen[0]["extra_body"]["reasoning_effort"] == "low"
    assert seen[1]["model"] == llm.HEAVY_MODEL


def test_user_id_lands_in_extra_body():
    captured = {}

    def _create(**kwargs):
        captured.update(kwargs)
        import types as _t
        return _t.SimpleNamespace(
            choices=[_t.SimpleNamespace(message=_t.SimpleNamespace(content="ok"))],
            usage=_t.SimpleNamespace(prompt_tokens=1, completion_tokens=1))

    with patch.object(llm._client.chat.completions, "create", side_effect=_create):
        llm.complete([{"role": "user", "content": "q"}], gear="f0", user_id="abc-123")
    assert captured["extra_body"]["user_id"] == "abc-123"


def test_conn_refused_maps_to_provider_unavailable(monkeypatch):
    sleeps = []
    monkeypatch.setattr(llm.time, "sleep", lambda s: sleeps.append(s))
    with patch.object(llm._client.chat.completions, "create", side_effect=_conn_error()):
        with pytest.raises(llm.ProviderUnavailableError) as ei:
            llm.complete([{"role": "user", "content": "hi"}], gear="t1")
    assert str(ei.value) == llm.PROVIDER_UNAVAILABLE_AR
    assert sleeps == [], "interactive gears fail fast on connection errors"


def test_timeout_maps_to_provider_unavailable(monkeypatch):
    monkeypatch.setattr(llm.time, "sleep", lambda s: None)
    with patch.object(llm._client.chat.completions, "create", side_effect=_timeout_error()):
        with pytest.raises(llm.ProviderUnavailableError):
            llm.complete([{"role": "user", "content": "hi"}], gear="t1")


def test_502_maps_to_provider_unavailable(monkeypatch):
    monkeypatch.setattr(llm.time, "sleep", lambda s: None)
    with patch.object(llm._client.chat.completions, "create",
                      side_effect=openai.APIStatusError("bad gateway", response=_fake_response(502), body=None)):
        with pytest.raises(llm.ProviderUnavailableError):
            llm.complete([{"role": "user", "content": "hi"}], gear="f0")


def test_rate_limit_single_retry_then_unavailable(monkeypatch):
    sleeps = []
    monkeypatch.setattr(llm.time, "sleep", lambda s: sleeps.append(s))
    err = openai.RateLimitError("rate limited", response=_fake_response(429), body=None)
    with patch.object(llm._client.chat.completions, "create", side_effect=[err, err]):
        with pytest.raises(llm.ProviderUnavailableError):
            llm.complete([{"role": "user", "content": "hi"}], gear="t1")
    assert len(sleeps) == 1 and 1.0 <= sleeps[0] <= 3.0, sleeps


def test_async_p_retries_transient_then_raises(monkeypatch):
    sleeps = []
    monkeypatch.setattr(llm.time, "sleep", lambda s: sleeps.append(s))
    def _boom(**kw):
        raise _conn_error()

    with patch.object(llm._client.chat.completions, "create", side_effect=_boom):
        with pytest.raises(llm.ProviderUnavailableError):
            llm.complete([{"role": "user", "content": "batch"}], gear="p")
    assert len(sleeps) == 3, sleeps


def test_auth_error_is_fatal_and_never_retried(monkeypatch):
    sleeps = []
    monkeypatch.setattr(llm.time, "sleep", lambda s: sleeps.append(s))
    err = openai.AuthenticationError("bad key", response=_fake_response(401), body=None)
    with patch.object(llm._client.chat.completions, "create", side_effect=err):
        with pytest.raises(RuntimeError):
            llm.complete([{"role": "user", "content": "hi"}])
    assert sleeps == []


def test_missing_key_fails_fast(monkeypatch):
    monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)
    with pytest.raises(RuntimeError):
        llm.complete([{"role": "user", "content": "hi"}])


def test_old_alias_still_importable():
    assert issubclass(llm.GatewayUnavailableError, llm.ProviderUnavailableError)
