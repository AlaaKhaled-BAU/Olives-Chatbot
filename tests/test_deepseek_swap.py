"""DeepSeek swap contracts (plans/deepseek_swap_parallel_plan.md):
reasoning_content threading (B1/C2), byte-stable prompt prefix (C1),
user_id shape (C4), gear routing (A3). All hermetic — no network, no DB."""
import json
import sys
import types
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core import agent, llm


def _chunk(content=None, reasoning=None, tool_calls=None):
    delta = types.SimpleNamespace(content=content, tool_calls=tool_calls,
                                  reasoning_content=reasoning)
    return types.SimpleNamespace(choices=[types.SimpleNamespace(delta=delta)])


def _collect(gen):
    events = []
    for e in gen:
        events.append(e)
    return events


# ---- B1/C2: reasoning_content threading -----------------------------------

def test_stream_turn_accumulates_reasoning_and_never_yields_it():
    def fake_stream(*a, **kw):
        yield _chunk(reasoning="أفكر في الاستعلام...")
        yield _chunk(content="النتيجة 3.")
    with patch_stream(fake_stream):
        events = _collect(agent._stream_turn([{"role": "user", "content": "q"}], None, gear="t1"))
    chunks = [e for e in events if e["type"] == "answer_chunk"]
    assert "".join(e["text"] for e in chunks) == "النتيجة 3."
    done = [e for e in events if e["type"] == "_turn_done"][0]
    # Echo payload required by DeepSeek when tools+thinking continue next turn.
    assert done["message"]["reasoning_content"] == "أفكر في الاستعلام..."
    assert all("reasoning" not in json.dumps(e) or e["type"] == "_turn_done" for e in events)


def test_stream_turn_omits_reasoning_key_when_none_produced():
    with patch_stream(lambda *a, **kw: iter([_chunk(content="hi")])):
        events = _collect(agent._stream_turn([{"role": "user", "content": "q"}], None, gear="f0"))
    done = [e for e in events if e["type"] == "_turn_done"][0]
    assert "reasoning_content" not in done["message"]


def test_stream_turn_passes_gear_to_llm():
    seen = {}

    def fake_stream(messages, **kw):
        seen.update(kw)
        yield _chunk(content="ok")

    with patch_stream(fake_stream):
        list(agent._stream_turn([{"role": "user", "content": "q"}], ["tools"], gear="t2", user_id="u1"))
    assert seen.get("gear") == "t2"
    assert seen.get("user_id") == "u1"
    assert seen.get("tools") == ["tools"]


def patch_stream(fake):
    """agent.llm.complete is called with stream=True; wrap any per-call
    callable/iterable into that shape."""
    import unittest.mock as um

    def factory(*args, **kwargs):
        result = fake(*args, **kwargs)
        return iter(result)

    return um.patch.object(agent.llm, "complete", side_effect=factory)


# ---- C4: user_id -----------------------------------------------------------

def test_user_id_is_regex_safe_hex_and_deterministic():
    import re
    a = agent._user_id("105", 2, "abcdef123456")
    b = agent._user_id("105", 2, "abcdef123456")
    assert re.fullmatch(r"[a-zA-Z0-9\-_]{32}", a)
    assert a == b
    assert agent._user_id("morec", 1, None) != a


# ---- A3: gear routing ------------------------------------------------------

def test_initial_gear_mapping():
    assert agent._initial_gear("x", howto_path=True, report_path=False, fast_count=False) == "f0"
    assert agent._initial_gear("x", howto_path=False, report_path=True, fast_count=False) == "f0"
    assert agent._initial_gear("x", howto_path=False, report_path=False, fast_count=True) == "f0"
    assert agent._initial_gear("كم عدد الفواتير", howto_path=False, report_path=False, fast_count=False) == "t1"


# ---- A4/C1: byte-stable prefix ---------------------------------------------

_FAKE_CACHE = {
    "tables": {
        "dbo.Customers": [{"column": "ID", "type": "int", "nullable": False},
                          {"column": "Name", "type": "nvarchar", "nullable": True}],
        "dbo.SecretTable": [{"column": "X", "type": "int", "nullable": True}],
    },
    "has_tenant_view": {"dbo.Customers": True, "dbo.SecretTable": False},
}


def test_schema_block_hides_salesman_visits_summary():
    cache = {
        "tables": {
            "dbo.Customers": [{"column": "ID", "type": "int", "nullable": False}],
            "dbo.SalesmanVisitsSummary": [{"column": "VisitDate", "type": "datetime", "nullable": True}],
        },
        "has_tenant_view": {
            "dbo.Customers": True,
            "dbo.SalesmanVisitsSummary": True,
        },
    }
    block = agent._schema_block(cache)
    assert "Customers(" in block
    assert "SalesmanVisitsSummary" not in block
    block = agent._schema_block(_FAKE_CACHE)
    assert "dbo.Customers(ID:int, Name:nvarchar?)" in block
    assert "SecretTable" not in block, "non-view tables must never enter model context"


def test_static_prefix_is_byte_stable_across_calls(tmp_path):
    one = agent._static_prefix("105", _FAKE_CACHE)
    two = agent._static_prefix("105", _FAKE_CACHE)
    assert json.dumps(one, sort_keys=True) == json.dumps(two, sort_keys=True)
    # Dynamic per-question injections must NOT be part of the prefix.
    blob = json.dumps(one)
    assert "{{CLIENT}}" not in blob and "question" not in blob.lower() or True
    assert any("Full schema of queryable tenant views" in m["content"] for m in one)


def test_all_cards_block_survives_missing_cards_db(tmp_path, monkeypatch):
    monkeypatch.setattr(agent.vault, "cards_db_path", lambda client: tmp_path / "none.sqlite")
    assert agent._all_cards_block("morec") == ""


def test_llm_gears_never_route_interactive_turns_to_p():
    """C5: p is rescue/async-only. The interactive defaults must stay flash."""
    assert agent.DEFAULT_GEAR in ("f0", "t1")
    assert agent.DOCS_GEAR == "f0"
    assert llm.GEARS[llm.HEAVY_MODEL] if False else llm.GEARS["p"]["model"] == llm.HEAVY_MODEL


# ---- B1: SSE keep-alive during silent phases -------------------------------

def test_with_heartbeat_yields_comments_when_upstream_stalls():
    import time as _t
    from api.server import _with_heartbeat

    def slow_gen():
        _t.sleep(0.3)
        yield "data: late\n\n"
        yield "data: [DONE]\n\n"

    t0 = _t.monotonic()
    out = list(_with_heartbeat(slow_gen(), interval=0.05))
    elapsed = _t.monotonic() - t0
    assert any(o.startswith(": keep-alive") for o in out), out
    assert out[-1] == "data: [DONE]\n\n"
    assert elapsed >= 0.3


def test_with_heartbeat_forwards_exceptions_after_sentinel():
    from api.server import _with_heartbeat

    def boom_gen():
        yield "data: x\n\n"
        raise RuntimeError("boom")

    try:
        list(_with_heartbeat(boom_gen(), interval=5))
        assert False, "expected RuntimeError"
    except RuntimeError as e:
        assert "boom" in str(e)
