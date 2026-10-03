"""Phase 1: per-turn Usage, streamed include_usage, trace stamps."""
import sys
import types
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core import llm, trace
from core.usage import Usage


def test_usage_sums_two_calls_and_keeps_gears():
    usage = Usage()
    usage.add(model="a", gear="t1", prompt=100, completion=20, cache_hit=0, cache_miss=100, ms=1.2)
    usage.add(model="a", gear="f0", prompt=50, completion=10, cache_hit=40, cache_miss=10, ms=0.4)
    totals = usage.totals()
    assert totals["llm_calls"] == 2
    assert totals["prompt_tokens"] == 150
    assert totals["completion_tokens"] == 30
    assert totals["cache_hit_tokens"] == 40
    assert [c["gear"] for c in totals["calls"]] == ["t1", "f0"]


def test_missing_sdk_usage_still_counts_the_call():
    usage = Usage()
    usage.add_sdk("f0", "deepseek-v4-flash", None, 3.0)
    totals = usage.totals()
    assert totals["llm_calls"] == 1
    assert totals["prompt_tokens"] == 0
    assert totals["calls"][0]["prompt"] is None


def test_stream_kwargs_request_usage():
    cfg = llm.GEARS["t1"]
    kwargs = llm.stream_create_kwargs(cfg, [{"role": "user", "content": "q"}], stream=True)
    assert kwargs["stream_options"] == {"include_usage": True}
    plain = llm.stream_create_kwargs(cfg, [{"role": "user", "content": "q"}], stream=False)
    assert "stream_options" not in plain


def test_usage_chunk_with_empty_choices_is_recorded():
    chunk = types.SimpleNamespace(
        choices=[],
        usage=types.SimpleNamespace(
            prompt_tokens=11, completion_tokens=4, total_tokens=15,
            prompt_cache_hit_tokens=8, prompt_cache_miss_tokens=3,
        ),
    )
    usage = Usage()
    out = list(llm._logged_stream("f0", iter([chunk]), usage, "m"))
    assert out == [chunk]
    assert usage.totals()["prompt_tokens"] == 11
    assert usage.totals()["completion_tokens"] == 4
    assert usage.totals()["llm_calls"] == 1


def test_trace_line_has_git_sha_and_prefix_hash(tmp_path, monkeypatch):
    monkeypatch.setattr(trace, "TRACE_PATH", tmp_path / "trace.jsonl")
    monkeypatch.setattr(trace, "GIT_SHA", "abc123")
    trace.note_prefix_hash("105", "deadbeef")
    trace.log_event("105", "q", event="answer", subject=None)
    line = (tmp_path / "trace.jsonl").read_text().strip()
    assert '"git_sha": "abc123"' in line
    assert '"prefix_hash": "deadbeef"' in line


def test_trace_line_accepts_latency_and_ttft(tmp_path, monkeypatch):
    monkeypatch.setattr(trace, "TRACE_PATH", tmp_path / "trace.jsonl")
    trace.log_event("105", "q", event="answer", latency_ms=1200, ttft_ms=340)
    line = (tmp_path / "trace.jsonl").read_text().strip()
    assert '"latency_ms": 1200' in line
    assert '"ttft_ms": 340' in line


def test_complete_non_stream_records_usage():
    usage = Usage()

    def _create(**kwargs):
        assert "stream_options" not in kwargs
        return types.SimpleNamespace(
            choices=[types.SimpleNamespace(message=types.SimpleNamespace(content="ok"))],
            usage=types.SimpleNamespace(
                prompt_tokens=7, completion_tokens=1, total_tokens=8,
                prompt_cache_hit_tokens=0, prompt_cache_miss_tokens=7,
            ),
        )

    with patch.object(llm._client.chat.completions, "create", side_effect=_create):
        llm.complete([{"role": "user", "content": "hi"}], gear="f0", usage_acc=usage)
    assert usage.totals()["prompt_tokens"] == 7
    assert usage.totals()["calls"][0]["gear"] == "f0"
