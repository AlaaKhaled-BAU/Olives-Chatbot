"""Phase 6 acceptance, mocked at the LLM boundary -- deterministic and
immune to gateway/quota flakiness (core/llm.complete is the seam). Covers
the orchestration logic in core/agent.py itself: the CompanyID MULTI
short-circuit, tool dispatch, the C4 query-budget gate (up to MAX_QUERIES
real business queries per turn, INFORMATION_SCHEMA/analyze calls always
free), and the refusal path when the model never produces a final answer.

The one live, un-mocked path (an actual "how many companies" question
against the real gateway) is exercised manually -- see the Phase 6 commit
message -- not here, since CI-style runs shouldn't depend on a live LLM
quota."""
import sys
import types
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from core import agent, memory

SCOPE = {"CompanyID": 1}  # bypass multi-company probe in live schema_cache


def _msg(content=None, tool_calls=None):
    """A minimal stand-in for the openai SDK's ChatCompletionMessage."""
    return types.SimpleNamespace(content=content, tool_calls=tool_calls)


def _resp(message):
    """C7: agent.py now always calls llm.complete(..., stream=True), so a
    mocked completion must look like a stream (an iterable of chunks with
    .choices[0].delta), not a single response object. A single chunk
    carrying the WHOLE message reconstructs identically to a real
    multi-chunk stream -- _stream_turn() just accumulates deltas, it
    doesn't care how many pieces they arrive in. Returns a concrete list
    (not a generator) so tests using `return_value=` (reused across
    several .complete() calls) can iterate it more than once."""
    tool_calls = None
    if message.tool_calls:
        tool_calls = [
            types.SimpleNamespace(index=i, id=tc.id,
                                   function=types.SimpleNamespace(name=tc.function.name,
                                                                   arguments=tc.function.arguments))
            for i, tc in enumerate(message.tool_calls)
        ]
    delta = types.SimpleNamespace(content=message.content, tool_calls=tool_calls)
    finish_reason = "tool_calls" if tool_calls else "stop"
    return [types.SimpleNamespace(choices=[types.SimpleNamespace(delta=delta, finish_reason=finish_reason)])]


def _plain_resp(content):
    """Non-streaming response shape for envelope/contract calls
    (_final_contract) — unlike the streamed calls mocked elsewhere in this
    file, which need _resp()'s streaming chunk shape."""
    return types.SimpleNamespace(choices=[types.SimpleNamespace(message=types.SimpleNamespace(content=content))])


def _content_chunk(text):
    """One raw streaming chunk carrying a content delta fragment -- for
    testing _stream_turn's live-forwarding/buffering logic directly with
    REAL multi-chunk fragmentation, unlike _resp()'s one-chunk shortcut."""
    delta = types.SimpleNamespace(content=text, tool_calls=None)
    return types.SimpleNamespace(choices=[types.SimpleNamespace(delta=delta, finish_reason=None)])


def _tool_call_delta_chunk(index, call_id=None, name=None, arguments=None):
    """One raw streaming chunk carrying a tool-call delta FRAGMENT -- id/
    name typically arrive once in the first chunk for a given index, then
    only `arguments` fragments in subsequent chunks (the real gateway shape,
    confirmed live)."""
    fn = types.SimpleNamespace(name=name, arguments=arguments) if (name is not None or arguments is not None) else None
    tcd = types.SimpleNamespace(index=index, id=call_id, function=fn)
    delta = types.SimpleNamespace(content=None, tool_calls=[tcd])
    return types.SimpleNamespace(choices=[types.SimpleNamespace(delta=delta, finish_reason=None)])


def test_step_label_is_generic_never_the_sql_or_object_name():
    """C7: 'show that a query is running, never its text -- that leaks
    schema shape and, through it, other clients' branch structure.'"""
    state = {"queries": [], "warned_last_query": False}
    assert agent._step_label("introspect_schema", {"name": "Companies"}, state) == "searching schema"
    assert agent._step_label("analyze", {}, state) == "analyzing"
    assert agent._step_label("search_docs", {"query": "price list"}, state) == "searching documentation"
    assert agent._step_label("ask_user", {"question": "Which month?"}, state) is None
    assert agent._step_label("run_select", {"sql": "SELECT * FROM t.Customers"}, state) == "running query 1 of 4"
    assert agent._step_label(
        "run_select", {"sql": "SELECT * FROM INFORMATION_SCHEMA.COLUMNS"}, state) == "searching schema", \
        "a metadata probe is the same user-facing activity as introspect_schema, not a counted query"

    state["queries"].append("SELECT 1 FROM t.Y")
    assert agent._step_label("run_select", {"sql": "SELECT * FROM t.Y"}, state) == "running query 2 of 4"


def test_build_table_from_row_dicts():
    rows = [{"Name": "Alpha", "n": 3}, {"Name": "Beta", "n": 7}]
    table = agent._build_table(rows)
    assert table == {"columns": ["Name", "n"], "rows": [["Alpha", 3], ["Beta", 7]]}


def test_build_table_is_none_for_no_rows():
    assert agent._build_table(None) is None
    assert agent._build_table([]) is None


def test_build_table_is_none_for_a_single_scalar():
    """A 1-row/1-column result (COUNT(*), a date lookup, etc.) only repeats
    a number the prose answer already states -- not worth a table."""
    assert agent._build_table([{"n": 33517}]) is None
    assert agent._build_table([{"CurrentDateTime": "2026-07-27"}]) is None


def test_build_table_keeps_a_single_row_with_multiple_columns():
    """1 row is still worth tabulating when it has more than one field --
    e.g. a single customer's name/email/phone lookup."""
    table = agent._build_table([{"Name": "Alpha", "Phone": "123"}])
    assert table == {"columns": ["Name", "Phone"], "rows": [["Alpha", "123"]]}


def test_run_select_unfiltered_transactions_headers_count_returns_grain_error():
    """P0.3: raw header counts without type+void must fail with a metric hint."""
    state = {"queries": [], "last_rows": None, "doc_source_pairs": []}
    with patch.object(agent.sql, "run_select") as mock_run:
        result = agent._run_tool(
            "run_select",
            {"sql": "SELECT COUNT(*) FROM t.TransactionsHeaders"},
            {},
            {},
            [],
            2,
            "105",
            state,
        )
    mock_run.assert_not_called()
    assert "error" in result
    assert "run_metric" in result["error"]


def test_run_tool_tracks_the_most_substantive_result_not_simply_the_last():
    """Live-observed real bug: a multi-row breakdown query followed by an
    incidental 1-row 'what's today's date' lookup (also a real business
    query by run_select's own free-vs-counted rule -- it isn't
    INFORMATION_SCHEMA) must not let the smaller result silently clobber
    the actual breakdown as the answer envelope's table data."""
    state = {"queries": [], "last_rows": None, "doc_source_pairs": []}
    breakdown = [{"Month": "Jan", "n": 10}, {"Month": "Feb", "n": 20}]
    date_check = [{"CurrentDateTime": "2026-07-27"}]
    with patch.object(agent.sql, "run_select", side_effect=[breakdown, date_check]):
        agent._run_tool("run_select", {"sql": "SELECT Month, COUNT(*) AS n FROM t.Orders GROUP BY Month"},
                         {}, {}, [], 1, "morec", state)
        agent._run_tool("run_select", {"sql": "SELECT GETDATE() AS CurrentDateTime"},
                         {}, {}, [], 1, "morec", state)
    assert state["last_rows"] == breakdown, "the bigger, earlier result must win over a smaller, later one"


def test_build_table_caps_at_table_row_cap():
    rows = [{"n": i} for i in range(agent._TABLE_ROW_CAP + 20)]
    table = agent._build_table(rows)
    assert len(table["rows"]) == agent._TABLE_ROW_CAP


def test_build_chart_offers_bar_for_a_non_time_label_column():
    table = {"columns": ["Region", "Total"], "rows": [["East", 100], ["West", 150]]}
    assert agent._build_chart(table) == {"kind": "bar", "x": "Region", "y": "Total"}


def test_build_chart_offers_line_for_a_time_like_label_column():
    table = {"columns": ["Month", "Total"], "rows": [["Jan", 100], ["Feb", 150]]}
    assert agent._build_chart(table) == {"kind": "line", "x": "Month", "y": "Total"}


def test_build_chart_none_for_wrong_shapes():
    assert agent._build_chart(None) is None
    assert agent._build_chart({"columns": ["n"], "rows": [[3]]}) is None, "single value -- nothing to chart"
    assert agent._build_chart({"columns": ["a", "b", "c"], "rows": [[1, 2, 3]]}) is None, "not 2 columns"
    assert agent._build_chart({"columns": ["Month", "Total"], "rows": [["Jan", 100]]}) is None, \
        "only 1 row -- not worth a chart"
    assert agent._build_chart({"columns": ["a", "b"], "rows": [["x", "y"], ["p", "q"]]}) is None, \
        "neither column is numeric"
    assert agent._build_chart({"columns": ["a", "b"], "rows": [[1, 2], [3, 4]]}) is None, \
        "first column is also numeric -- not a clear label/value shape"


def test_build_sources_extracts_table_names_and_keeps_doc_sources():
    queries = ["SELECT COUNT(*) FROM t.Customers", "SELECT * FROM t.Orders o JOIN t.Customers c ON o.id=c.id"]
    doc_source_pairs = [("system_options_guide.md", "Invoicing")]
    sources = agent._build_sources(queries, doc_source_pairs)
    assert sources == ["Customers", "Orders", "system_options_guide.md › Invoicing"], \
        "table names deduped/sorted, doc sources kept verbatim and appended"


def test_build_sources_ignores_information_schema_and_empty_input():
    assert agent._build_sources([], []) == []


def test_final_contract_parses_a_clean_json_object(monkeypatch):
    payload = '{"answer_md": "النتيجة 3", "refusal": false, "confidence": "high", "followups": ["Q1?", "Q2?"]}'
    monkeypatch.setattr(agent.llm, "complete", lambda *a, **k: _plain_resp(payload))
    out = agent._final_contract("q", "a", None)
    assert out["followups"] == ["Q1?", "Q2?"]
    assert out["confidence"] == "high"
    assert out["refusal"] is False


def test_final_contract_caps_followups_at_three():
    payload = '{"followups": ["a", "b", "c", "d", "e"], "confidence": "low", "refusal": true}'
    with patch.object(agent.llm, "complete", return_value=_plain_resp(payload)):
        out = agent._final_contract("q", "a", None)
    assert len(out["followups"]) == 3
    assert out["refusal"] is True


def test_final_contract_rejects_bad_confidence_values():
    payload = '{"followups": [], "confidence": "cosmic"}'
    with patch.object(agent.llm, "complete", return_value=_plain_resp(payload)):
        assert agent._final_contract("q", "a", None)["confidence"] is None


def test_final_contract_never_raises_on_a_bad_reply():
    """Cosmetic enrichment — must degrade to None on non-JSON, non-dict JSON,
    or the LLM call itself failing, never break the real answer."""
    with patch.object(agent.llm, "complete", return_value=_plain_resp("not json at all")):
        assert agent._final_contract("q", "a", None) is None
    with patch.object(agent.llm, "complete", return_value=_plain_resp('{"not": "relevant"}')):
        assert agent._final_contract("q", "a", None)["followups"] == []
    with patch.object(agent.llm, "complete", side_effect=RuntimeError("provider down")):
        assert agent._final_contract("q", "a", None) is None


def test_final_contract_call_carries_no_tools_and_json_mode():
    captured = {}

    def fake_complete(messages, **kwargs):
        captured.update(kwargs)
        return _plain_resp('{"followups": []}')

    with patch.object(agent.llm, "complete", side_effect=fake_complete):
        agent._final_contract("q", "a", "uid123")
    # Golden rule 9 made structural: the final formatting call has NO tools.
    assert "tools" not in captured
    assert captured["response_format"] == {"type": "json_object"}
    assert captured.get("user_id") == "uid123"


def test_build_envelope_skips_followups_when_there_is_no_final_text():
    state = {"queries": [], "last_rows": None, "doc_source_pairs": []}
    with patch.object(agent.llm, "complete") as mock_complete:
        envelope = agent._build_envelope("q", "", state)
    mock_complete.assert_not_called()
    assert envelope == {"table": None, "chart": None, "sources": [], "followups": []}


def test_stream_turn_forwards_content_chunks_live():
    chunks = [_content_chunk("Hel"), _content_chunk("lo "), _content_chunk("world.")]
    with patch.object(agent.llm, "complete", return_value=chunks):
        events = list(agent._stream_turn([], None))
    answer_chunks = [e["text"] for e in events if e["type"] == "answer_chunk"]
    assert "".join(answer_chunks) == "Hello world."
    done = next(e for e in events if e["type"] == "_turn_done")
    assert done["message"]["content"] == "Hello world."
    assert "tool_calls" not in done["message"]


def test_stream_turn_never_forwards_malformed_sentinel_text():
    """C7: the real DeepSeek failure mode must never leak partial special-
    token text to the client before it's recognized and discarded --
    forwarding live token-by-token must not defeat the existing retry
    protection against this failure mode."""
    chunks = [_content_chunk("<｜"), _content_chunk("｜DSML｜｜tool_calls>"), _content_chunk("garbage")]
    with patch.object(agent.llm, "complete", return_value=chunks):
        events = list(agent._stream_turn([], None))
    assert not any(e["type"] == "answer_chunk" for e in events), \
        "a garbled turn must never forward any text to the client"
    done = next(e for e in events if e["type"] == "_turn_done")
    assert agent._looks_like_malformed_tool_syntax(done["message"]["content"])


def test_stream_turn_reconstructs_tool_call_from_fragmented_deltas():
    """Matches the real gateway shape observed live: id+name in the first
    delta for an index, only `arguments` fragments after."""
    chunks = [
        _tool_call_delta_chunk(0, call_id="call_1", name="run_select", arguments=""),
        _tool_call_delta_chunk(0, arguments='{"sql": '),
        _tool_call_delta_chunk(0, arguments='"SELECT 1"}'),
    ]
    with patch.object(agent.llm, "complete", return_value=chunks):
        events = list(agent._stream_turn([], agent.TOOLS))
    assert not any(e["type"] == "answer_chunk" for e in events), "tool-call turns must never forward anything"
    done = next(e for e in events if e["type"] == "_turn_done")
    tc = done["message"]["tool_calls"][0]
    assert tc["id"] == "call_1"
    assert tc["function"]["name"] == "run_select"
    assert tc["function"]["arguments"] == '{"sql": "SELECT 1"}'


def _tool_call(call_id, name, arguments_json):
    fn = types.SimpleNamespace(name=name, arguments=arguments_json)
    return types.SimpleNamespace(id=call_id, function=fn)


def test_multi_company_short_circuits_before_any_llm_call(monkeypatch):
    monkeypatch.setattr(agent.params, "discover_profile", lambda client: {"CompanyID": agent.params.MULTI})
    with patch.object(agent.llm, "complete") as mock_complete:
        result = agent.ask("morec", "how many customers?")
    mock_complete.assert_not_called()
    assert result["needs_ask"]
    assert result["answer"] is None


def test_information_schema_exploration_never_counts_against_the_budget(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    calls = [
        _resp(_msg(tool_calls=[_tool_call(
            "c1", "run_select",
            '{"sql": "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME=\'Customers\'"}',
        )])),
        _resp(_msg(tool_calls=[_tool_call("c2", "run_select", '{"sql": "SELECT COUNT(*) FROM t.Customers"}')])),
        _resp(_msg(content="There are 33517 customers.")),
    ]
    with patch.object(agent.llm, "complete", side_effect=calls) as mock_complete, \
         patch.object(agent.sql, "run_select", return_value=[{"n": 1}]) as mock_run_select, \
         patch.object(agent.tenant_pack, "build", return_value="## Tenant context\nCompanyID: 1"):
        result = agent.ask("morec", "how many customers?", conversation=SCOPE)

    assert result["answer"] == "There are 33517 customers."
    # C4: tools stay offered on BOTH call #2 (the INFORMATION_SCHEMA probe
    # never counts) and call #3 (only 1 of MAX_QUERIES=4 real queries spent
    # so far) -- a single real query no longer closes the loop at all.
    assert mock_complete.call_args_list[1].kwargs["tools"] is not None
    assert mock_complete.call_args_list[2].kwargs["tools"] is not None
    assert mock_run_select.call_count == 2


def test_query_budget_closes_after_max_queries_real_queries(monkeypatch, tmp_path):
    """C4's actual boundary: MAX_QUERIES real business queries are allowed
    (a period-over-period comparison needs at least 2, which the old
    one-query ceiling made structurally impossible) -- the (MAX_QUERIES+1)th
    call must not be offered a tool at all, and a "last query" reminder
    must be injected exactly once."""
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    calls = [_resp(_msg(tool_calls=[_tool_call(f"c{i}", "run_select", f'{{"sql": "SELECT {i}"}}')]))
             for i in range(agent.MAX_QUERIES)]
    calls.append(_resp(_msg(content="Here is the comparison.")))
    with patch.object(agent.llm, "complete", side_effect=calls) as mock_complete, \
         patch.object(agent.sql, "run_select", return_value=[{"n": 1}]):
        result = agent.ask("morec", "compare this month to last month", conversation=SCOPE)

    assert result["answer"] == "Here is the comparison."
    # calls[0..MAX_QUERIES-1] each still had tools offered (budget not yet
    # spent going INTO that call); the final call (index MAX_QUERIES) must
    # have tools withheld.
    for i in range(agent.MAX_QUERIES):
        assert mock_complete.call_args_list[i].kwargs["tools"] is not None, f"call {i} should still offer tools"
    assert mock_complete.call_args_list[agent.MAX_QUERIES].kwargs["tools"] is None
    warnings = [m for m in mock_complete.call_args_list[agent.MAX_QUERIES].args[0]
                if m.get("content") == "This is your last query. Answer from what you have."]
    assert len(warnings) == 1, "the last-query reminder must be injected exactly once"


def test_analyze_tool_never_counts_against_the_budget(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    calls = [
        _resp(_msg(tool_calls=[_tool_call("c1", "run_select", '{"sql": "SELECT COUNT(*) FROM t.Customers"}')])),
        _resp(_msg(tool_calls=[_tool_call(
            "c2", "analyze", '{"operation": "percent_change", "before": 100, "after": 120}')])),
        _resp(_msg(content="Customers grew 20%.")),
    ]
    with patch.object(agent.llm, "complete", side_effect=calls) as mock_complete, \
         patch.object(agent.sql, "run_select", return_value=[{"n": 1}]):
        result = agent.ask("morec", "how much did customers grow?", conversation=SCOPE)

    assert result["answer"] == "Customers grew 20%."
    # only 1 of MAX_QUERIES=4 spent (the analyze call is free) -- tools
    # must still be offered on the turn right after it.
    assert mock_complete.call_args_list[2].kwargs["tools"] is not None


def test_analyze_computes_correctly():
    assert agent._analyze({"operation": "percent_change", "before": 100, "after": 120}) == {"result": 20.0}
    assert agent._analyze({"operation": "difference", "before": 100, "after": 120}) == {"result": 20.0}
    assert agent._analyze({"operation": "ratio", "before": 50, "after": 100}) == {"result": 2.0}
    assert "error" in agent._analyze({"operation": "bogus", "before": 1, "after": 2})
    assert "error" in agent._analyze({"operation": "difference", "before": "not a number", "after": 2})


def test_search_docs_tool_never_counts_against_the_budget(monkeypatch, tmp_path):
    """C5: a docs lookup is knowledge retrieval, not a business-data query
    -- same free-tool class as INFORMATION_SCHEMA probes and analyze."""
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    calls = [
        _resp(_msg(tool_calls=[_tool_call("c1", "run_select", '{"sql": "SELECT COUNT(*) FROM t.Customers"}')])),
        _resp(_msg(tool_calls=[_tool_call("c2", "search_docs", '{"query": "price list"}')])),
        _resp(_msg(content="A price list controls item pricing; you have 33517 customers.")),
    ]
    with patch.object(agent.llm, "complete", side_effect=calls) as mock_complete, \
         patch.object(agent.sql, "run_select", return_value=[{"n": 1}]), \
         patch.object(agent.docs, "search", return_value=[{"source": "guide.md", "heading": "Price Lists", "excerpt": "..."}]) as mock_search:
        result = agent.ask("morec", "what is a price list, and how many customers do I have?", conversation=SCOPE)

    assert result["answer"] == "A price list controls item pricing; you have 33517 customers."
    mock_search.assert_called_once()
    assert mock_search.call_args.args[:2] == ("morec", "price list")
    # only 1 of MAX_QUERIES=4 spent (search_docs is free) -- tools must
    # still be offered on the turn right after it.
    assert mock_complete.call_args_list[2].kwargs["tools"] is not None


def test_real_table_result_feeds_plan_cache_but_never_verified_query(monkeypatch, tmp_path):
    """C3: a successfully-answered question is cheap-to-regenerate-cache
    material (plan_cache), never an unverified promotion to verified_queries
    -- that used to happen unconditionally here, which is exactly the bug
    this fix closes (a confidently wrong answer stored as "verified")."""
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    calls = [
        _resp(_msg(tool_calls=[_tool_call("c1", "run_select", '{"sql": "SELECT COUNT(*) FROM t.Customers"}')])),
        _resp(_msg(content="33517 customers.")),
    ]
    with patch.object(agent.llm, "complete", side_effect=calls), \
         patch.object(agent.sql, "run_select", return_value=[{"n": 33517}]):
        result = agent.ask("morec", "how many customers total?", conversation=SCOPE)

    assert result["answer"] == "33517 customers."
    assert result["answer_sql"] == "SELECT COUNT(*) FROM t.Customers"
    # C4a: plan_cache stores the real ORDERED LIST, not a joined string --
    # each entry must independently pass gate.validate() again on replay.
    assert memory.get_plan(result["cache_key"]) == {"queries": ["SELECT COUNT(*) FROM t.Customers"]}
    assert memory.get_verified_query("morec", 1, "how many customers total?") is None


def test_information_schema_only_turn_never_caches_the_probe_as_the_answer(monkeypatch, tmp_path):
    """C3's actual measured bug (not a hypothetical): the OLD code tracked
    "last_sql" unconditionally, so a turn shaped like "probe the schema via
    INFORMATION_SCHEMA, then answer directly without ever running a real
    business query" stored the METADATA PROBE as the cached/verified
    answer query. A later identical question would then hit that bogus
    cache, re-run the INFORMATION_SCHEMA query, and ask the model to
    answer a business question from a list of column names. Note this
    scenario is the ONLY realistic way answer_sql can end up None on a
    successful turn: golden rule 6 means a REAL business query (which DOES
    flip results_in_context) always forecloses any later tool call in the
    same turn, so a business query can never be "overwritten" by a
    trailing probe in practice -- it can only be preceded by one, or
    replaced entirely by a turn that never issues one at all (this case)."""
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    calls = [
        _resp(_msg(tool_calls=[_tool_call(
            "c1", "run_select",
            '{"sql": "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME=\'Customers\'"}',
        )])),
        _resp(_msg(content="Based on the schema, there should be some customers.")),
    ]
    with patch.object(agent.llm, "complete", side_effect=calls), \
         patch.object(agent.sql, "run_select", return_value=[{"COLUMN_NAME": "ID"}]):
        result = agent.ask("morec", "how many customers total?", conversation=SCOPE)

    assert result["answer_sql"] is None
    assert memory.get_plan(result["cache_key"]) is None, "an info-schema-only turn must cache nothing at all"


def test_refusal_when_no_final_answer_within_turn_budget(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    # every turn keeps calling a tool, never producing a final text answer
    endless = _resp(_msg(tool_calls=[_tool_call("c", "introspect_schema", '{"name": "Customers"}')]))
    with patch.object(agent.llm, "complete", return_value=endless):
        result = agent.ask("morec", "an impossible question", conversation=SCOPE)

    assert result["needs_ask"] is None
    assert "can't answer" in result["answer"].lower()


def test_ask_user_tool_call_returns_needs_ask_immediately(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    resp = _resp(_msg(tool_calls=[_tool_call("c1", "ask_user", '{"question": "Which month?"}')]))
    with patch.object(agent.llm, "complete", return_value=resp):
        result = agent.ask("morec", "how many orders?", conversation=SCOPE)

    assert result["needs_ask"] == "Which month?"
    assert result["answer"] is None


def test_malformed_tool_syntax_is_retried_not_returned_as_answer(monkeypatch, tmp_path):
    """Live-observed DeepSeek/gateway failure mode: raw tool-call special
    tokens leak into content instead of populating tool_calls. Must be
    retried, never handed to the user as the final answer."""
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    garbled = _resp(_msg(content="<｜｜DSML｜｜tool_calls>garbage"))
    clean = _resp(_msg(content="There are 3 companies."))
    # E1: a real final answer also triggers one extra, non-streaming
    # llm.complete() call for the JSON answer contract (_final_contract) --
    # a real 3rd mock item, so this test still proves the number of calls
    # the retry logic itself makes (2) plus the contract call on top.
    followups = _plain_resp('{"followups": [], "confidence": "high", "refusal": false}')
    with patch.object(agent.llm, "complete", side_effect=[garbled, clean, followups]) as mock_complete:
        result = agent.ask("morec", "how many companies?", conversation=SCOPE)

    assert result["answer"] == "There are 3 companies."
    assert mock_complete.call_count == 3


def test_cap_for_context_passes_small_results_through_unchanged():
    small = [{"id": 1}, {"id": 2}]
    assert agent._cap_for_context(small) is small


def test_cap_for_context_caps_large_results_with_an_honest_note():
    """C6a: replaces the old json.dumps(...)[:8000] byte-slice, which could
    cut mid-token and hand the model malformed JSON with no signal it was
    ever truncated -- the exact condition that produces a confident wrong
    total."""
    big = [{"id": i} for i in range(120)]
    capped = agent._cap_for_context(big)
    assert len(capped["rows"]) == agent._ROW_DISPLAY_CAP
    assert capped["total_rows_returned"] == 120
    assert "never infer" in capped["note"].lower()
    # the JSON must actually be valid -- the whole point of the fix
    import json
    json.loads(json.dumps(capped, default=str))


def test_cap_for_context_leaves_non_list_results_alone():
    """introspect_schema/ask_user/error results aren't row lists -- must
    pass through untouched, not get wrapped or corrupted."""
    error = {"error": "something went wrong"}
    assert agent._cap_for_context(error) is error


def test_looks_like_malformed_tool_syntax():
    assert agent._looks_like_malformed_tool_syntax("<｜｜DSML｜｜tool_calls>")
    assert agent._looks_like_malformed_tool_syntax("<tool_call>\n<function=run_select>")
    assert agent._looks_like_malformed_tool_syntax(
        "prose:<tool_call>run_select<arg_key>sql</arg_key></tool_call>")
    assert not agent._looks_like_malformed_tool_syntax("There are 3 companies.")
    assert not agent._looks_like_malformed_tool_syntax("")
    assert not agent._looks_like_malformed_tool_syntax(None)


def test_stream_turn_never_forwards_tool_call_xml():
    chunks = [_content_chunk("<tool_call>"), _content_chunk("<function=run_select>")]
    with patch.object(agent.llm, "complete", return_value=chunks):
        events = list(agent._stream_turn([], None))
    assert not any(e["type"] == "answer_chunk" for e in events)
    done = next(e for e in events if e["type"] == "_turn_done")
    assert agent._looks_like_malformed_tool_syntax(done["message"]["content"])


def test_malformed_tool_call_xml_is_retried_not_returned(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    garbled = _resp(_msg(content="<tool_call>\n<function=run_select>\n<parameter=sql>\nSELECT 1\n"))
    clean = _resp(_msg(content="Top customer is Acme."))
    followups = _plain_resp("[]")
    with patch.object(agent.llm, "complete", side_effect=[garbled, clean, followups]) as mock_complete:
        result = agent.ask("morec", "top customers?", conversation=SCOPE)
    assert result["answer"] == "Top customer is Acme."
    assert mock_complete.call_count == 3


def test_system_prompt_documents_invoice_grain_and_isvoid():
    prompt = agent._system_prompt("105")
    assert "TransactionTypeID" in prompt
    assert "ISNULL(IsVoid" in prompt
    assert "Receipts" in prompt


def test_malformed_tool_syntax_does_not_false_positive_on_prose_mentioning_it():
    """C9: the old check was `"tool_calls" in content or "｜" in content` --
    a legitimate answer that merely discusses tool-calling in English prose
    (no real DeepSeek sentinel) must not be misdiagnosed as garbled and
    endlessly retried."""
    assert not agent._looks_like_malformed_tool_syntax(
        "This assistant works by making tool_calls to the database, then summarizing the results.")


def test_run_proc_tool_not_offered():
    """FIXPLAN M6: chatbot_ro has no EXECUTE grant on any procedure (confirmed
    live -- every run_proc call errors), so the tool is not offered at all
    rather than burning a turn on a call that always fails. Path A (a real
    audited EXECUTE grant) would re-add this deliberately, not by accident."""
    names = {t["function"]["name"] for t in agent.TOOLS}
    assert "run_proc" not in names
    assert names == {
        "introspect_schema", "run_select", "run_metric", "run_report", "ask_user", "analyze", "search_docs",
        "search_schema_notes", "read_schema_note", "get_joins", "lookup_hot",
    }


def test_introspect_refuses_a_table_with_no_tenant_view():
    """C0: a table without a t. view must be refused up front, with a clear
    reason the model can act on -- not silently returned as introspectable
    only to fail several turns later on "Invalid object name t.Users"."""
    cache = {"tables": {"dbo.Users": [{"column": "UserID", "type": "int"}]},
             "has_tenant_view": {"dbo.Users": False}}
    result = agent._introspect(cache, {}, "Users")
    assert "error" in result
    assert "no client-facing" in result["error"]


def test_introspect_allows_a_table_with_a_tenant_view():
    cache = {"tables": {"dbo.Currencies": [{"column": "ID", "type": "int"}]},
             "has_tenant_view": {"dbo.Currencies": True}}
    result = agent._introspect(cache, {}, "Currencies")
    assert result == {"kind": "table", "name": "dbo.Currencies", "columns": [{"column": "ID", "type": "int"}]}


def test_introspect_never_refuses_on_a_pre_c0_cache():
    """has_tenant_view entirely absent (a schema_cache.json from before this
    phase) must never refuse anything -- the t. wall is the real security
    boundary regardless, refusing early is a turn-saving UX improvement
    only. Absence of the key, not an empty dict, is the pre-C0 signal."""
    cache = {"tables": {"dbo.Users": [{"column": "UserID", "type": "int"}]}}
    result = agent._introspect(cache, {}, "Users")
    assert result["kind"] == "table"


def test_dedupe_doc_pairs_preserves_first_seen_order():
    pairs = [("a.md", "H1"), ("b.md", "H2"), ("a.md", "H1"), ("c.md", "H3")]
    assert agent._dedupe_doc_pairs(pairs) == [("a.md", "H1"), ("b.md", "H2"), ("c.md", "H3")]


def test_has_count_sql_intent():
    assert agent._has_count_sql_intent("كم طلب لدينا؟")
    assert agent._has_count_sql_intent("how many invoices")
    assert agent._has_count_sql_intent("SELECT COUNT(*) FROM t.X")
    assert not agent._has_count_sql_intent("ماذا تعني قائمة الأسعار؟")
    assert not agent._has_count_sql_intent("what is the price list")


def test_is_fast_count_path_for_masters_and_metrics():
    assert agent._is_fast_count_path("كم عدد العملاء؟")
    assert agent._is_fast_count_path("how many items")
    assert agent._is_fast_count_path("كم مبيعات اليوم")
    assert not agent._is_fast_count_path("اشرح كيف أعيّن زبائن لمندوب")
    assert not agent._is_fast_count_path("ماذا تعني قائمة الأسعار؟")


def test_fast_count_path_omits_docs_and_vault_tools():
    state = {"queries": [], "fast_count": True, "doc_searches": 0, "docs_only": False}
    names = {t["function"]["name"] for t in agent._active_tools(state)}
    assert "search_docs" not in names
    assert "search_schema_notes" not in names
    assert "run_metric" in names


def test_needs_honesty_preamble():
    assert agent._needs_honesty_preamble("كم مبيعات هذا الشهر؟")
    assert agent._needs_honesty_preamble("sales this month")
    assert agent._needs_honesty_preamble("كم مبيعات كل الشركات؟")
    assert not agent._needs_honesty_preamble("how many customers")


def test_doc_search_cap_omits_search_docs(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    calls = [
        _resp(_msg(tool_calls=[_tool_call(f"c{i}", "search_docs", f'{{"query": "q{i}"}}')]))
        for i in range(agent.MAX_DOC_SEARCHES)
    ]
    calls.append(_resp(_msg(content="Answer from docs.")))
    followups = _plain_resp("[]")
    with patch.object(agent.llm, "complete", side_effect=calls + [followups]) as mock_complete, \
         patch.object(agent.docs, "search", return_value=[{"source": "g.md", "heading": "H", "excerpt": "x"}]):
        result = agent.ask("morec", "how does approval work?", conversation=SCOPE)
    assert result["answer"] == "Answer from docs."
    assert result["doc_search_count"] == agent.MAX_DOC_SEARCHES
    tools_on_fourth = mock_complete.call_args_list[agent.MAX_DOC_SEARCHES].kwargs["tools"]
    names = {t["function"]["name"] for t in tools_on_fourth}
    assert "search_docs" not in names


def test_docs_only_omits_schema_tools(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    calls = [
        _resp(_msg(tool_calls=[_tool_call("c1", "search_docs", '{"query": "price list"}')])),
        _resp(_msg(tool_calls=[_tool_call("c2", "introspect_schema", '{"name": "Items"}')])),
        _resp(_msg(content="Price list explained.")),
    ]
    followups = _plain_resp("[]")
    with patch.object(agent.llm, "complete", side_effect=calls + [followups]) as mock_complete, \
         patch.object(agent.docs, "search", return_value=[{"source": "g.md", "heading": "Price", "excerpt": "..."}]):
        result = agent.ask("morec", "what is a price list?", conversation=SCOPE)
    assert result["answer"] == "Price list explained."
    tools_after_docs = mock_complete.call_args_list[1].kwargs["tools"]
    names = {t["function"]["name"] for t in tools_after_docs}
    assert "introspect_schema" not in names
    assert "search_schema_notes" not in names


def test_docs_only_not_set_when_count_intent(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    calls = [
        _resp(_msg(tool_calls=[_tool_call("c1", "search_docs", '{"query": "price list"}')])),
        _resp(_msg(tool_calls=[_tool_call("c2", "run_select", '{"sql": "SELECT COUNT(*) FROM t.Items"}')])),
        _resp(_msg(content="Price list and count.")),
    ]
    followups = _plain_resp("[]")
    with patch.object(agent.llm, "complete", side_effect=calls + [followups]) as mock_complete, \
         patch.object(agent.docs, "search", return_value=[{"source": "g.md", "heading": "Price", "excerpt": "..."}]), \
         patch.object(agent.sql, "run_select", return_value=[{"n": 5}]):
        agent.ask("morec", "explain price list then كم items", conversation=SCOPE)
    tools_after_docs = mock_complete.call_args_list[1].kwargs["tools"]
    names = {t["function"]["name"] for t in tools_after_docs}
    assert "introspect_schema" in names


def test_honesty_preamble_injected(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    seen = []
    stream_resp = _resp(_msg(content="Contextual answer."))
    followups = _plain_resp("[]")

    def side_effect(messages, **kwargs):
        if kwargs.get("stream"):
            seen.append(messages)
            return stream_resp
        return followups

    with patch.object(agent.llm, "complete", side_effect=side_effect), \
         patch.object(agent.sql, "run_select", return_value=[{"d": "2025-07-15"}]), \
         patch.object(agent, "_empty_calendar_needs_ask", return_value=None):
        agent.ask("morec", "كم مبيعات هذا الشهر؟", conversation=SCOPE)
    honesty = [m for m in seen[0] if m.get("role") == "system" and m.get("content", "").startswith("Honesty:")]
    assert len(honesty) == 1
    assert "calendar_today=" in honesty[0]["content"]
    assert "CompanyID=1" in honesty[0]["content"]


def test_doc_search_count_in_result(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    calls = [
        _resp(_msg(tool_calls=[_tool_call("c1", "search_docs", '{"query": "approval"}')])),
        _resp(_msg(content="Approved via screen 7.1.3.")),
    ]
    followups = _plain_resp("[]")
    with patch.object(agent.llm, "complete", side_effect=calls + [followups]), \
         patch.object(agent.docs, "search", return_value=[{"source": "g.md", "heading": "Approve", "excerpt": "..."}]):
        result = agent.ask("morec", "how to approve orders?", conversation=SCOPE)
    assert result["doc_search_count"] == 1


def test_build_arabic_stub_single_count_row():
    state = {"last_rows": [{"n": 9}], "doc_source_pairs": [], "queries": ["SELECT COUNT(*) AS n FROM t.X"]}
    assert agent._build_arabic_stub(state) == "النتيجة: 9."


def test_build_arabic_stub_multi_numeric_columns():
    state = {"last_rows": [{"total": 432.58, "invoice_count": 2}], "doc_source_pairs": []}
    stub = agent._build_arabic_stub(state)
    assert "432.58" in stub
    assert "invoice_count" in stub


def test_build_arabic_stub_docs_only():
    state = {"last_rows": None, "doc_source_pairs": [("guide.md", "Assign")]}
    assert agent._build_arabic_stub(state) == "الإجابة في المصادر أدناه."


def test_empty_model_answer_after_run_select_uses_arabic_stub(monkeypatch, tmp_path):
    """P0.1: SQL rows but blank model text must never yield an empty answer."""
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    calls = [
        _resp(_msg(tool_calls=[_tool_call("c1", "run_select", '{"sql": "SELECT COUNT(*) AS n FROM t.Customers"}')])),
        _resp(_msg(content="   ")),
    ]
    retry = _plain_resp("   ")
    followups = _plain_resp("[]")
    with patch.object(agent.llm, "complete", side_effect=calls + [retry, followups]), \
         patch.object(agent.sql, "run_select", return_value=[{"n": 9}]):
        result = agent.ask("morec", "كم عدد الزبائن؟", conversation=SCOPE)
    assert result["answer"] == "النتيجة: 9."
    assert result["answer_sql"]


def test_empty_calendar_month_needs_ask_before_tools(monkeypatch, tmp_path):
    """P0.2: هذا الشهر with no invoices in current calendar month → needs_ask."""
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    today = __import__("datetime").date.today()

    def fake_run_select(sql_text, company_id, client, **kwargs):
        if "MAX(TransactionDate)" in sql_text:
            return [{"d": "2025-07-15"}]
        if "TOP 1" in sql_text:
            return []
        raise AssertionError(f"unexpected SQL: {sql_text}")

    with patch.object(agent.llm, "complete") as mock_complete, \
         patch.object(agent.sql, "run_select", side_effect=fake_run_select):
        result = agent.ask("morec", "كم مبيعات هذا الشهر؟", conversation=SCOPE)
    mock_complete.assert_not_called()
    assert result["needs_ask"]
    assert str(today.year) in result["needs_ask"]
    assert "2025" in result["needs_ask"] or "يوليو" in result["needs_ask"]
    assert "هل أحسب" in result["needs_ask"]


def test_calendar_confirm_skips_empty_month_gate(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    calls = [
        _resp(_msg(tool_calls=[_tool_call("c1", "run_metric", '{"metric": "net_sales", "filters": {"from_date": "2025-07-01", "to_date": "2025-07-31"}}')])),
        _resp(_msg(content="مبيعات يوليو 2025: 432.58.")),
    ]
    followups = _plain_resp("[]")

    def fake_run_select(sql_text, company_id, client, **kwargs):
        if "MAX(TransactionDate)" in sql_text:
            return [{"d": "2025-07-15"}]
        return [{"net_sales": 432.58}]

    with patch.object(agent.llm, "complete", side_effect=calls + [followups]), \
         patch.object(agent.sql, "run_select", side_effect=fake_run_select), \
         patch.object(agent.metrics, "run_metric", return_value={
             "rows": [{"net_sales": 432.58}], "sql": "SELECT 1",
         }):
        result = agent.ask("morec", "نعم احسب آخر شهر قيد", conversation=SCOPE)
    assert result["answer"]
    assert result["needs_ask"] is None


def test_docs_only_never_calls_run_select(monkeypatch, tmp_path):
    """Pure how-to questions must not offer or invoke run_select."""
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    calls = [
        _resp(_msg(tool_calls=[_tool_call("c1", "search_docs", '{"query": "assign customers"}')])),
        _resp(_msg(content="Assign via screen 4.8.")),
    ]
    followups = _plain_resp("[]")
    with patch.object(agent.llm, "complete", side_effect=calls + [followups]) as mock_complete, \
         patch.object(agent.docs, "search", return_value=[{"source": "g.md", "heading": "4.8", "excerpt": "..."}]), \
         patch.object(agent.sql, "run_select") as mock_run_select:
        result = agent.ask("morec", "كيف أعيّن زبائن لمندوب؟", conversation=SCOPE)
    assert result["answer"] == "Assign via screen 4.8."
    mock_run_select.assert_not_called()
    tools_after_docs = mock_complete.call_args_list[1].kwargs["tools"]
    names = {t["function"]["name"] for t in tools_after_docs}
    assert "run_select" not in names
    assert "run_metric" not in names


def test_metric_questions_skip_docs(monkeypatch, tmp_path):
    """Count/metric questions must not offer search_docs on the first turn."""
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    calls = [
        _resp(_msg(tool_calls=[_tool_call(
            "c1", "run_metric",
            '{"metric": "net_sales", "filters": {"from_date": "2025-07-01", "to_date": "2025-07-31"}}',
        )])),
        _resp(_msg(content="مبيعات يوليو.")),
    ]
    followups = _plain_resp("[]")
    with patch.object(agent.llm, "complete", side_effect=calls + [followups]) as mock_complete, \
         patch.object(agent.metrics, "run_metric", return_value={"rows": [{"net_sales": 1}], "sql": "SELECT 1"}), \
         patch.object(agent.docs, "search") as mock_search:
        agent.ask("morec", "كم مبيعات يوليو؟", conversation=SCOPE)
    first_tools = mock_complete.call_args_list[0].kwargs["tools"]
    names = {t["function"]["name"] for t in first_tools}
    assert "search_docs" not in names
    mock_search.assert_not_called()


def test_report_questions_use_run_report_not_docs_thrash(monkeypatch, tmp_path):
    """Named report path should call run_report once, not search_docs repeatedly."""
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    calls = [
        _resp(_msg(tool_calls=[_tool_call(
            "c1", "run_report",
            '{"name": "Rpt_SalesmanSalesSummary", "params": {"from_date": "2025-07-01", "to_date": "2025-07-31"}}',
        )])),
        _resp(_msg(content="تقرير مبيعات المندوب جاهز.")),
    ]
    followups = _plain_resp("[]")
    with patch.object(agent.llm, "complete", side_effect=calls + [followups]) as mock_complete, \
         patch.object(agent.reports, "run_report", return_value={
             "report": "Rpt_SalesmanSalesSummary",
             "sql": "SELECT 1",
             "rows": [{"SalesPersonName": "Imad", "gross_amount": 100}],
         }) as mock_run_report, \
         patch.object(agent.docs, "search") as mock_search:
        result = agent.ask("morec", "تقرير مبيعات المندوب لشهر يوليو", conversation=SCOPE)
    assert result["answer"] == "تقرير مبيعات المندوب جاهز."
    assert result.get("report_name") == "Rpt_SalesmanSalesSummary"
    mock_run_report.assert_called_once()
    mock_search.assert_not_called()
    first_tools = mock_complete.call_args_list[0].kwargs["tools"]
    names = {t["function"]["name"] for t in first_tools}
    assert "search_docs" not in names
    assert "run_select" not in names
    assert "run_report" in names


def test_vault_search_cap_increments_and_blocks(monkeypatch, tmp_path):
    """Fourth vault tool call must be refused by omitting vault tools."""
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    calls = [
        _resp(_msg(tool_calls=[_tool_call("c0", "search_schema_notes", '{"pattern": "CFD"}')])),
        _resp(_msg(tool_calls=[_tool_call("c1", "read_schema_note", '{"name": "Customers"}')])),
        _resp(_msg(tool_calls=[_tool_call("c2", "get_joins", '{"table": "Customers"}')])),
    ]
    calls.append(_resp(_msg(content="Joined via CFD.")))
    followups = _plain_resp("[]")
    with patch.object(agent.llm, "complete", side_effect=calls + [followups]) as mock_complete, \
         patch.object(agent.vault, "search_schema_notes", return_value={"results": []}), \
         patch.object(agent.vault, "read_schema_note", return_value={"name": "Customers"}), \
         patch.object(agent.vault, "get_joins", return_value={"joins": []}):
        result = agent.ask("morec", "customers joined to salesperson via CFD", conversation=SCOPE)
    assert result["answer"] == "Joined via CFD."
    tools_on_fourth = mock_complete.call_args_list[agent.MAX_VAULT_SEARCHES].kwargs["tools"]
    names = {t["function"]["name"] for t in tools_on_fourth}
    assert "search_schema_notes" not in names
    assert "get_joins" not in names


def test_run_report_path1_uses_empty_allowlist():
    state = {"queries": [], "last_rows": None, "doc_source_pairs": []}
    with patch.object(agent.reports, "run_report_select", return_value={
        "report": "Rpt_SalesmanSalesSummary", "sql": "SELECT 1", "rows": [],
    }) as mock_select:
        result = agent._run_tool(
            "run_report",
            {"name": "Rpt_SalesmanSalesSummary", "params": {}},
            {}, {}, [], 2, "105", state,
        )
    mock_select.assert_called_once()
    assert mock_select.call_args.kwargs["allowed_procs"] == []
    assert result["sql"] == "SELECT 1"
    assert state["report_name"] == "Rpt_SalesmanSalesSummary"


def test_run_report_path3_not_certified():
    state = {"queries": [], "last_rows": None, "doc_source_pairs": []}
    with patch.object(agent.reports, "build_report_sql", return_value=None), \
         patch.object(agent.reports, "_catalog_card", return_value={"name": "Rpt_Foo", "purpose": "Foo purpose"}):
        result = agent._run_tool(
            "run_report",
            {"name": "Rpt_Foo"},
            {}, {}, [], 2, "105", state,
        )
    assert result["status"] == "not_certified"
    assert "not certified" in result["message"]
    assert result["purpose"] == "Foo purpose"
    assert state["queries"] == []


def test_is_report_path_detects_arabic_alias():
    assert agent._is_report_path("تقرير مبيعات المندوب", "105")


def test_report_path_first_tools_tight_for_sales_and_orders():
    """Report path must offer run_report only — not run_select or search_docs."""
    question = "اعرض تقرير المبيعات والطلبات لمقارنة المناديب"
    assert agent._is_report_path(question, "105")
    state = {
        "queries": [],
        "report_path": True,
        "howto_path": False,
        "fast_count": False,
        "doc_searches": 0,
        "vault_searches": 0,
        "docs_only": False,
        "question": question,
    }
    names = {t["function"]["name"] for t in agent._active_tools(state)}
    assert "run_report" in names
    assert "run_select" not in names
    assert "search_docs" not in names
    assert names <= {"run_report", "ask_user", "analyze"}


def test_report_path_bypasses_poisoned_plan_cache(monkeypatch, tmp_path):
    """Named report questions must not replay plan_cache run_select — use run_report."""
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    question = "اعرض تقرير المبيعات والطلبات لمقارنة المناديب"
    scope = {"CompanyID": 2}
    cache = agent._schema_cache("105")
    key = memory.cache_key("105", 2, "manager", agent.MODEL_ALIAS, question, agent._schema_version(cache))
    poison_sql = "SELECT COUNT(DISTINCT th.TransactionNo) FROM t.TransactionsHeaders th"
    memory.set_plan(key, "105", {"queries": [poison_sql]})

    calls = [
        _resp(_msg(tool_calls=[_tool_call(
            "c1", "run_report",
            '{"name": "Rpt_SalesAndOrders", "params": {}}',
        )])),
        _resp(_msg(content="تقرير المبيعات والطلبات جاهز.")),
    ]
    followups = _plain_resp("[]")
    with patch.object(agent.llm, "complete", side_effect=calls + [followups]) as mock_complete, \
         patch.object(agent.reports, "run_report", return_value={
             "report": "Rpt_SalesAndOrders",
             "sql": "SELECT 1",
             "rows": [{"SalesPersonName": "Imad", "invoice_count": 130}],
         }) as mock_run_report, \
         patch.object(agent.sql, "run_select", side_effect=AssertionError("plan_cache replay must not run")):
        result = agent.ask("105", question, conversation=scope)

    mock_run_report.assert_called_once()
    assert result.get("report_name") == "Rpt_SalesAndOrders"
    assert result["answer"] == "تقرير المبيعات والطلبات جاهز."
    assert memory.get_plan(key) == {"queries": [poison_sql]}
    first_tools = mock_complete.call_args_list[0].kwargs["tools"]
    names = {t["function"]["name"] for t in first_tools}
    assert "run_report" in names
    assert "run_select" not in names


def test_is_howto_path_excludes_counts():
    assert agent._is_howto_path("كيف أعيّن زبائن لمندوب؟", "105")
    assert not agent._is_howto_path("كم عدد العملاء؟", "105")


def test_vault_tool_increments_counter():
    state = {"queries": [], "last_rows": None, "doc_source_pairs": [], "vault_searches": 0}
    with patch.object(agent.vault, "get_joins", return_value={"joins": []}):
        agent._run_tool("get_joins", {"table": "Customers"}, {}, {}, [], 1, "105", state)
    assert state["vault_searches"] == 1
