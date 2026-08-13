"""S2: core/llm.py must have an explicit request timeout and a capped
retry backoff -- a genuinely hung gateway must not block a worker thread
indefinitely, and a retry storm must not sleep for a full 72s."""
import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import openai

from core import llm


def test_client_has_an_explicit_timeout():
    assert llm._client.timeout == 30.0


def test_retry_backoff_is_capped(monkeypatch):
    sleeps = []
    monkeypatch.setattr(llm.time, "sleep", lambda s: sleeps.append(s))
    with patch.object(llm._client.chat.completions, "create",
                       side_effect=openai.RateLimitError("rate limited", response=_fake_response(), body=None)):
        try:
            llm.complete([{"role": "user", "content": "hi"}])
            assert False, "expected the final RateLimitError to propagate"
        except openai.RateLimitError:
            pass

    assert sleeps == [5, 10, 15], sleeps
    assert sum(sleeps) < 72, "must be a real reduction from the old 12+24+36=72s worst case"


def _fake_response():
    import types
    return types.SimpleNamespace(status_code=429, headers={}, request=types.SimpleNamespace())
