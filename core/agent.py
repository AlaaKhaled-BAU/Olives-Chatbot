"""The agent loop (PLAN.md Phase 6). Check the plan cache and verified-query
few-shots before asking the model to plan from scratch, then generate SQL
against the t. views; golden rule 6 -- once query results are in the
model's context, no more tool calls are even offered, so the next turn
must be the final answer.

FIXPLAN M6 (2026-07-25): the dedicated run_proc tool was removed --
chatbot_ro has no EXECUTE grant on any procedure (confirmed live), so it
always errored and just burned a turn. catalog/allowed_proc_names are
still very much in use: gate.validate() still allow-lists any EXEC a model
embeds directly in run_select's SQL text (denied at the DB permission
layer regardless, same as before), and introspect_schema still looks up
procedure parameters from the catalog."""
import argparse
import hashlib
import json
import re
import time
from pathlib import Path

from . import catalog, config, docs, gate, llm, memory, params, sql, trace

BASE_DIR = Path(__file__).resolve().parent.parent
# Live-tested at 6: a model that doesn't already know this schema's exact
# naming (it isn't a standard one -- guesses like "OSFA_SalesmenAuthorization"
# are reasonable-sounding but wrong) burns several turns on introspect_schema
# guesses before switching to a broader INFORMATION_SCHEMA LIKE search. That's
# the right recovery strategy, it just needs more room to get there.
MAX_TURNS = 12
MODEL_ALIAS = "chatbot"  # the one name the gateway maps to Claude/Gemini
# C4: replaces the old binary "results_in_context" latch. That made period-
# over-period comparison, drill-down, and verification-against-a-second-
# query structurally impossible -- exactly what a "data master" (vs a
# single-SQL-runner) needs to do. INFORMATION_SCHEMA probes and analyze
# calls are free (don't count here) -- only real business queries do.
# Deliberately not tuned further yet ("land the budget, measure, then
# tune") and MAX_TURNS is deliberately NOT raised in this same change.
MAX_QUERIES = 4

# C6a: row-count cap, not a byte-slice. json.dumps(...)[:8000] can cut mid-
# token, handing the model MALFORMED JSON with no signal it was ever cut --
# exactly the condition that produces a confident wrong total. 50 rows of
# ordinary relational data comfortably fits any reasonable context budget
# without needing a second byte-level safety net on top.
_ROW_DISPLAY_CAP = 50

# C7: the real DeepSeek failure mode (_looks_like_malformed_tool_syntax)
# always starts with this exact marker. Content is buffered (never
# forwarded) until enough of it has arrived to rule the marker out --
# a couple of characters, imperceptible -- so a garbled turn never leaks
# partial special-token text to the client before it's discarded and retried.
_MALFORMED_SENTINEL = "<｜"

_STEP_LABELS = {"introspect_schema": "searching schema", "analyze": "analyzing", "search_docs": "searching documentation"}


def _step_label(name: str, args: dict, state: dict) -> str | None:
    """Human-readable progress label for a tool about to run. Deliberately
    generic -- never the table/column/proc name or SQL text (C7: 'show
    that a query is running, never its text -- that leaks schema shape and,
    through it, other clients' branch structure'). None for ask_user, which
    ends the turn immediately with nothing to narrate a wait for."""
    if name == "run_select":
        if "information_schema" not in args.get("sql", "").lower():
            return f"running query {len(state['queries']) + 1} of {MAX_QUERIES}"
        return "searching schema"  # a metadata probe, same user-facing activity as introspect_schema
    return _STEP_LABELS.get(name)


def _stream_turn(messages, tools):
    """Runs one LLM completion with stream=True. Yields {"type":
    "answer_chunk", "text": ...} live as content tokens arrive (C7: 'stream
    the final answer token-by-token'). Tool-call deltas are reconstructed
    silently from fragments and NEVER yielded (C7: 'do not stream tool-call
    arguments... to the client UI'). The turn's reconstructed message dict
    -- same shape as msg.model_dump() would produce, trimmed to the fields
    the caller actually uses -- is yielded last as {"type": "_turn_done",
    "message": ...}; the caller filters this event out, it never reaches
    api/server.py."""
    stream = llm.complete(messages, tools=tools, stream=True)
    buffer = ""
    forwarding = False
    tool_calls = {}
    for chunk in stream:
        delta = chunk.choices[0].delta
        if delta.content:
            if forwarding:
                yield {"type": "answer_chunk", "text": delta.content}
                buffer += delta.content
            else:
                buffer += delta.content
                if _MALFORMED_SENTINEL not in buffer and len(buffer) >= len(_MALFORMED_SENTINEL):
                    forwarding = True
                    yield {"type": "answer_chunk", "text": buffer}
        if delta.tool_calls:
            for tcd in delta.tool_calls:
                slot = tool_calls.setdefault(
                    tcd.index, {"id": None, "type": "function", "function": {"name": "", "arguments": ""}})
                if tcd.id:
                    slot["id"] = tcd.id
                if tcd.function and tcd.function.name:
                    slot["function"]["name"] += tcd.function.name
                if tcd.function and tcd.function.arguments:
                    slot["function"]["arguments"] += tcd.function.arguments
    if not forwarding and buffer and _MALFORMED_SENTINEL not in buffer:
        yield {"type": "answer_chunk", "text": buffer}  # short response, never crossed the buffering threshold
    message = {"role": "assistant", "content": buffer or None}
    if tool_calls:
        message["tool_calls"] = [tool_calls[i] for i in sorted(tool_calls)]
    yield {"type": "_turn_done", "message": message}


def _cap_for_context(result):
    """result is whatever sql.run_select() returned -- a list of row dicts
    (or occasionally a non-list for an edge-case query shape; passed
    through unchanged if so, nothing to cap). total_rows_returned is
    len(result) as ACTUALLY RETURNED, which is itself already capped at
    gate.DEFAULT_ROW_CAP (200, injected as TOP N by the gate) -- so when
    it equals 200 exactly, it's a floor on the true match count, not a
    proven total. The note says this explicitly rather than implying an
    exact count the tool can't actually back up."""
    if not isinstance(result, list) or len(result) <= _ROW_DISPLAY_CAP:
        return result
    return {
        "rows": result[:_ROW_DISPLAY_CAP],
        "shown": _ROW_DISPLAY_CAP,
        "total_rows_returned": len(result),
        "note": (f"Only the first {_ROW_DISPLAY_CAP} of {len(result)} returned rows are shown "
                 f"above. Never infer a count/sum/average from this partial list -- if you need "
                 f"one, write a dedicated aggregate query (COUNT/SUM/AVG) instead."),
    }

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "introspect_schema",
            "description": (
                "Look up columns for a table, or parameters for an allow-listed "
                "procedure, by name (case-insensitive)."
            ),
            "parameters": {
                "type": "object",
                "properties": {"name": {"type": "string"}},
                "required": ["name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "run_select",
            "description": "Run exactly one read-only SELECT against the t. (tenant-scoped) views.",
            "parameters": {
                "type": "object",
                "properties": {"sql": {"type": "string"}},
                "required": ["sql"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "ask_user",
            "description": "Ask the user a clarifying question when a required value can't be resolved any other way.",
            "parameters": {
                "type": "object",
                "properties": {"question": {"type": "string"}},
                "required": ["question"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "analyze",
            "description": (
                "Compute an exact derived value (percent change, difference, or ratio) from two "
                "numbers already in your context -- e.g. comparing this month's total against "
                "last month's. Does not touch the database and never counts against the query "
                "budget. Use this instead of doing the arithmetic yourself in prose -- it's exact, "
                "prose arithmetic isn't guaranteed to be."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {"type": "string", "enum": ["percent_change", "difference", "ratio"]},
                    "before": {"type": "number"},
                    "after": {"type": "number"},
                },
                "required": ["operation", "before", "after"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_docs",
            "description": (
                "Search the Olives user/system documentation for how a feature, screen, or system "
                "option works -- conceptual/how-to questions, not this client's own numbers. Returns "
                "the best-matching excerpts with their source. Never counts against the query budget."
            ),
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
        },
    },
]


def _schema_cache(client: str):
    return json.loads((config.work_dir(client) / "schema_cache.json").read_text())


def _schema_version(cache: dict) -> str:
    """C3: short content hash of the shapes a cached plan actually depends
    on (table/column names+types, proc signatures) -- baked into the
    plan_cache key so a schema change (renamed column, dropped table)
    can't get silently matched by a query issued before it. Deliberately
    excludes profile_probe/has_tenant_view/nullable_companyid_rows: those
    change on every refresh.py run for reasons unrelated to whether a
    cached SQL plan is still valid, and would invalidate the whole cache
    on every run for no benefit."""
    payload = json.dumps({"tables": cache.get("tables", {}), "procs": cache.get("procs", {})}, sort_keys=True)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def _system_prompt(client: str) -> str:
    return (BASE_DIR / "prompts" / "system.md").read_text().replace("{{CLIENT}}", client)


def _introspect(cache, catalog_procs, name: str):
    low = name.strip().lower()
    # C0: has_tenant_view is None on a pre-C0 schema_cache.json (never refuse
    # anything for a stale cache -- the t. wall itself is the real security
    # boundary regardless, this is a turn-saving UX improvement, not a
    # security control, so degrading to the old permissive behavior is safe).
    # Present but missing this specific table -> genuinely no view, refuse
    # loudly instead of letting the model discover it several turns later
    # via a failed "Invalid object name t.X" query.
    has_view = cache.get("has_tenant_view")
    for table_name, cols in cache["tables"].items():
        if table_name.split(".")[-1].lower() == low:
            if has_view is not None and not has_view.get(table_name, False):
                return {"error": f"{name!r} exists in the schema but has no client-facing "
                                  f"t. view -- not queryable (see db/table_classification.md)"}
            return {"kind": "table", "name": table_name, "columns": cols}
    for proc_name, proc_params in catalog_procs.items():
        if proc_name.split(".")[-1].lower() == low:
            return {"kind": "procedure", "name": proc_name, "params": proc_params}
    return {"error": f"{name!r} not found or not entitled to this client"}


def _looks_like_malformed_tool_syntax(content: str) -> bool:
    """Live-observed failure mode: a few turns into a tool-calling
    conversation, DeepSeek (via the gateway) occasionally emits its raw
    tool-call special tokens as plain text content instead of the
    structured tool_calls field -- msg.tool_calls comes back empty and the
    literal markup (e.g. "<｜｜DSML｜｜tool_calls>") would
    otherwise be accepted as the final answer. Retry rather than surface it.

    C9: was `"tool_calls" in content or "｜" in content` -- the first half
    false-positives on any legitimate answer that discusses the system
    itself (e.g. a user asking "how does this assistant work?" and the
    model's real answer mentioning "tool_calls" in prose). Tightened to the
    actual sentinel plus its leading marker (`<｜`), which is how every
    real occurrence of DeepSeek's special token starts and not a sequence
    ordinary English/Arabic prose would ever produce."""
    if not content:
        return False
    return "<｜" in content


def _analyze(args: dict) -> dict:
    """C4: exact arithmetic the model can offload instead of computing (and
    potentially getting slightly wrong) in prose -- no DB access, doesn't
    touch state at all, so it never counts against MAX_QUERIES."""
    op = args.get("operation")
    try:
        before, after = float(args["before"]), float(args["after"])
    except (KeyError, TypeError, ValueError):
        return {"error": "before/after must both be numbers"}
    if op == "difference":
        return {"result": after - before}
    if op == "ratio":
        if not before:
            return {"error": "before is 0 -- ratio is undefined"}
        return {"result": after / before}
    if op == "percent_change":
        if not before:
            return {"error": "before is 0 -- percent change is undefined"}
        return {"result": (after - before) / before * 100}
    return {"error": f"unknown operation {op!r} -- use percent_change, difference, or ratio"}


def _run_tool(name, args, cache, catalog_procs, allowed_proc_names, company_id, client, state):
    if name == "introspect_schema":
        return _introspect(cache, catalog_procs, args.get("name", ""))
    if name == "analyze":
        return _analyze(args)
    if name == "search_docs":
        # C5: knowledge retrieval, not a business-data query -- same
        # exemption class as INFORMATION_SCHEMA probes and analyze, never
        # counts against MAX_QUERIES.
        results = docs.search(client, args.get("query", ""))
        # C8: citation trail for the answer envelope's "sources" -- kept as
        # display strings only (never re-parsed), same info the tool result
        # itself already carries.
        state["doc_sources"].extend(f"{r['source']} › {r['heading']}" for r in results)
        return {"results": results}
    if name == "run_select":
        result = sql.run_select(args["sql"], company_id, client, allowed_procs=allowed_proc_names)
        # Models sometimes explore the schema via INFORMATION_SCHEMA through
        # run_select instead of introspect_schema -- that's metadata, not a
        # business query, so it's free (doesn't count against MAX_QUERIES,
        # C4) same as it previously didn't flip the old results_in_context
        # latch. C3: only a real business query is appended to
        # state["queries"] -- the old code tracked "last_sql"
        # unconditionally, so a metadata probe issued after the real query
        # (e.g. re-checking a column name for a follow-up) would silently
        # become the thing cached/promoted instead of the actual answer.
        if "information_schema" not in args["sql"].lower():
            state["queries"].append(args["sql"])
            # C8: candidate table/chart data for the answer envelope, never
            # re-asked of the model (it already has these numbers; making
            # it retype them into a table structure risks a transcription
            # mismatch with the prose answer). The MOST SUBSTANTIVE result
            # wins, not simply the last one -- live-observed real bug: a
            # multi-row breakdown query followed by an incidental "what's
            # today's date" lookup (also a real business query by this
            # tool's own definition) let the 1-row date check silently
            # clobber the actual breakdown data as "the" table.
            if isinstance(result, list) and (state["last_rows"] is None or len(result) > len(state["last_rows"])):
                state["last_rows"] = result
        return result
    return {"error": f"unknown tool {name}"}


# C8: table display cap. Same idea as _ROW_DISPLAY_CAP (the model's OWN
# context cap in _cap_for_context) but independent -- the UI table can
# reasonably show more rows than are worth spending model-context tokens
# on, and the two caps changing together for unrelated reasons would be a
# coincidence, not a real coupling.
_TABLE_ROW_CAP = 100

_SOURCE_TABLE_RE = re.compile(r"\bt\.(\w+)", re.IGNORECASE)


def _build_table(rows: list | None) -> dict | None:
    """C8: {columns, rows} from the most substantive business query's OWN
    result rows -- never re-derived from the model's prose, so it can't
    drift from what was actually returned. None when there's nothing worth
    showing: no business query ran, it returned zero rows, or it's a
    single scalar (1 row, 1 column -- e.g. a COUNT(*) or a date lookup),
    which only repeats a number the prose answer already states."""
    if not rows or (len(rows) == 1 and len(rows[0]) <= 1):
        return None
    columns = list(rows[0].keys())
    return {"columns": columns, "rows": [[row.get(c) for c in columns] for row in rows[:_TABLE_ROW_CAP]]}


_TIME_LIKE_COLUMN_RE = re.compile(r"month|date|day|year|week", re.IGNORECASE)


def _build_chart(table: dict | None) -> dict | None:
    """C8: a heuristic, not a model judgment call -- deliberately cheap
    ('the differentiator, and cheap once C4 and C6a land'). Offers a chart
    only for the shape it's unambiguous for: exactly one label column and
    one numeric column, few enough rows to be readable. Any other shape
    (single value, wide result, non-numeric second column) yields no chart
    rather than a misleading one. "line" only when the label column reads
    as a time series (its own header says so) -- a bar is the safer
    default otherwise, since an arbitrary label axis has no implied order
    a connecting line would honestly represent."""
    if not table or len(table["columns"]) != 2 or not (1 < len(table["rows"]) <= 20):
        return None
    label, value = table["rows"][0]
    if not (isinstance(value, (int, float)) and not isinstance(value, bool) and not isinstance(label, (int, float))):
        return None
    kind = "line" if _TIME_LIKE_COLUMN_RE.search(table["columns"][0]) else "bar"
    return {"kind": kind, "x": table["columns"][0], "y": table["columns"][1]}


def _build_sources(queries: list, doc_sources: list) -> list:
    """C8: 'always cite' -- table names come straight from the SQL actually
    run (every client-facing table this project has is queried as
    `t.TableName`, confirmed throughout this codebase), never a second
    guess at what the model "meant" to query. Doc sources were already
    recorded verbatim by _run_tool's search_docs branch."""
    tables = sorted(set(m.group(1) for q in queries for m in _SOURCE_TABLE_RE.finditer(q)))
    return tables + doc_sources


def _suggest_followups(question: str, answer: str) -> list:
    """C8: 2-3 model-proposed next questions -- the one envelope piece that
    genuinely needs judgment, not mechanically derivable from data already
    in hand ('this is what turns a query box into an analyst'). A small,
    non-streamed, best-effort extra call: never blocks or breaks the real
    answer if it errors or the model doesn't cooperate."""
    try:
        resp = llm.complete([
            {"role": "system", "content": (
                "Suggest 2-3 short, natural follow-up questions a business user might ask next, given "
                "this question and answer. Reply with ONLY a JSON array of strings, nothing else."
            )},
            {"role": "user", "content": f"Question: {question}\nAnswer: {answer}"},
        ])
        text = (resp.choices[0].message.content or "[]").strip()
        if text.startswith("```"):
            text = text.strip("`").removeprefix("json").strip()
        items = json.loads(text)
        return [str(x) for x in items][:3] if isinstance(items, list) else []
    except Exception:  # noqa: BLE001 - cosmetic extra, must never break the real answer
        return []


def _build_envelope(question: str, final_text: str, state: dict) -> dict:
    """C8: assembles the structured pieces the plan asks /ask to return
    alongside the prose answer. Everything except followups is derived
    from data this turn already produced -- never a second, potentially
    inconsistent ask to the model for numbers/names it already gave."""
    table = _build_table(state["last_rows"])
    return {
        "table": table,
        "chart": _build_chart(table),
        "sources": _build_sources(state["queries"], state["doc_sources"]),
        "followups": _suggest_followups(question, final_text) if final_text else [],
    }


def ask_stream(client: str, question: str, conversation: dict = None, role: str = "manager",
               subject: str | None = None):
    """Generator form of ask() (C7). Yields progress/content events as they
    happen:
      {"type": "step", "step": str}          -- e.g. "searching schema"
      {"type": "answer_chunk", "text": str}  -- live text of the final answer
      {"type": "done", answer, needs_ask, answer_sql, cache_key}  -- exactly
        once, last, same shape ask() has always returned (plus "type").
    `subject` (FIXPLAN M4): a short caller-identity hash for the audit trail,
    threaded through to every trace.log_event call below. Optional so direct
    CLI/test callers (no HTTP auth layer) don't need to fabricate one."""
    start = time.monotonic()

    def _record_latency():
        trace.observe_latency(client, time.monotonic() - start)

    conversation = conversation or {}
    client_config = config.load_client(client)
    name_aliases = client_config.get("name_aliases", [client])

    cache = _schema_cache(client)
    catalog_procs = catalog.for_client(client, name_aliases)
    allowed_proc_names = list(catalog_procs.keys())

    profile = params.discover_profile(client)
    company_id = params.resolve("CompanyID", conversation, profile)
    if company_id in (params.NEEDS_ASK, params.MULTI):
        trace.log_event(client, question, event="needs_ask", subject=subject, param="CompanyID")
        _record_latency()
        # C6c: list the REAL options when known, so the reply can be
        # validated against them instead of api/server.py having to guess
        # at a bare number in free text (the fixed bug: "how many invoices
        # in 2024" was previously silently accepted as CompanyID=2024).
        companies = profile.get("_companies") or []
        if companies:
            options = "، ".join(f"{c['name']} ({c['id']})" for c in companies)
            msg = f"Which company should I look at? Options: {options}"
        else:
            msg = "Which company should I look at?"
        yield {"type": "done", "answer": None, "needs_ask": msg}
        return

    # C3: schema_version in the key means a plan cached against an older
    # schema shape (renamed column, dropped table) can never be matched by
    # a query issued after a refresh -- different version, different key,
    # a clean miss instead of a wrong hit.
    schema_version = _schema_version(cache)
    key = memory.cache_key(client, company_id, role, MODEL_ALIAS, question, schema_version)
    cached_plan = memory.get_plan(key)
    if cached_plan:
        try:
            # C4a: plan_cache now stores an ORDERED LIST of queries (one
            # turn can be several, C4) -- re-run each in order and hand the
            # combined result set to the model, not just the last one.
            # cached_plan.get("sql") handles a plan written before this
            # change (single-string shape) without crashing.
            queries = cached_plan.get("queries") or ([cached_plan["sql"]] if cached_plan.get("sql") else [])
            raw_results = [sql.run_select(q, company_id, client, allowed_procs=allowed_proc_names) for q in queries]
            results = [_cap_for_context(r) for r in raw_results]
            messages = [
                {"role": "system", "content": _system_prompt(client)},
                {"role": "user", "content": question},
                {
                    "role": "user",
                    "content": f"Query results (in order): {json.dumps(results, default=str)}\n\n"
                    "Answer the question from these results only.",
                },
            ]
            answer = None
            for event in _stream_turn(messages, None):
                if event["type"] == "_turn_done":
                    answer = event["message"]["content"]
                else:
                    yield event
            trace.record_cache_hit(client)
            trace.log_event(client, question, event="answer", subject=subject, company_id=company_id, source="plan_cache")
            _record_latency()
            # C3: cache_key/answer_sql returned so /feedback can act on THIS
            # turn without recomputing anything or trusting client input --
            # a cache hit is still only plan_cache (cheap-to-regenerate), not
            # a promotion, so a thumbs-up here goes through the same
            # explicit promote_verified_query path as a full turn would.
            # answer_sql stays a single joined string (never re-executed,
            # only ever shown as few-shot display text) even though the
            # underlying cache now stores the real list.
            # C8: the most substantive result wins, not simply the last one
            # -- same reasoning as _run_tool's own tracking (a smaller,
            # later query must not clobber a genuinely bigger earlier one).
            last_rows = max((r for r in raw_results if isinstance(r, list)), key=len, default=None)
            envelope = _build_envelope(question, answer, {"queries": queries, "last_rows": last_rows, "doc_sources": []})
            yield {"type": "done", "answer": answer, "needs_ask": None,
                   "answer_sql": "; ".join(queries), "cache_key": key, **envelope}
            return
        except gate.GateError:
            pass  # cached plan no longer validates -- fall through to a full turn

    messages = [{"role": "system", "content": _system_prompt(client)}]
    shots = memory.few_shots(client, limit=3)
    if shots:
        examples = "\n".join(f'- "{s["question"]}" -> `{s["proc_or_sql"]}`' for s in shots)
        messages.append({
            "role": "system",
            "content": f"Previously-verified query patterns for this client:\n{examples}",
        })
    messages.append({"role": "user", "content": question})

    # C4: "queries" replaces the old single answer_sql/results_in_context
    # latch -- an ordered list of every real business query run this turn,
    # so a second query can be compared against the first (period-over-
    # period, drill-down, verification). INFORMATION_SCHEMA probes and
    # analyze calls never append here, so they stay free.
    # C8: last_rows/doc_sources feed the answer envelope (table/chart/
    # sources) -- see _run_tool and _build_envelope.
    state = {"queries": [], "warned_last_query": False, "last_rows": None, "doc_sources": []}
    final_text = None

    for _ in range(MAX_TURNS):
        tools = None if len(state["queries"]) >= MAX_QUERIES else TOOLS
        msg = None
        for event in _stream_turn(messages, tools):
            if event["type"] == "_turn_done":
                msg = event["message"]
            else:
                yield event
        tool_calls = msg.get("tool_calls")

        if not tool_calls and _looks_like_malformed_tool_syntax(msg.get("content")):
            continue  # drop this turn, don't add it to messages, try again

        messages.append(msg)

        if not tool_calls:
            final_text = msg.get("content")
            break

        for tc in tool_calls:
            name = tc["function"]["name"]
            try:
                args = json.loads(tc["function"]["arguments"] or "{}")
            except json.JSONDecodeError:
                args = {}

            if name == "ask_user":
                trace.log_event(client, question, event="needs_ask", subject=subject, param=args.get("question"))
                _record_latency()
                yield {"type": "done", "answer": None, "needs_ask": args.get("question")}
                return

            step = _step_label(name, args, state)
            if step:
                yield {"type": "step", "step": step}

            try:
                result = _run_tool(name, args, cache, catalog_procs, allowed_proc_names, company_id, client, state)
            except gate.GateError as e:
                trace.record_gate_rejection(client)
                result = {"error": str(e)}
            except Exception as e:  # noqa: BLE001 - a tool error goes back to the model, not a crash
                result = {"error": str(e)}

            messages.append({
                "role": "tool",
                "tool_call_id": tc["id"],
                "content": json.dumps(_cap_for_context(result), default=str),
            })

        # C4: once the budget is spent, tools=None on the NEXT llm.complete
        # call already makes a further tool call impossible (the same
        # golden-rule-6 mechanism as before, just parameterized by a
        # counter instead of a boolean) -- this is an additional nudge so
        # the model produces a real final answer instead of trying (and
        # failing) to call another tool. Injected once, not on every
        # remaining loop iteration.
        if len(state["queries"]) >= MAX_QUERIES and not state["warned_last_query"]:
            messages.append({"role": "system", "content": "This is your last query. Answer from what you have."})
            state["warned_last_query"] = True

    if final_text is None:
        final_text = "I can't answer that confidently from the available data."
        trace.log_event(client, question, event="refused", subject=subject)
        envelope = {"table": None, "chart": None, "sources": [], "followups": []}
    else:
        trace.log_event(client, question, event="answer", subject=subject, company_id=company_id)
        # C3: plan_cache may still be written automatically (cheap to
        # regenerate, schema_version already guards against a stale-shape
        # hit) -- verified_queries is NEVER written here. Promotion only
        # happens on an explicit signal: a user thumbs-up (api/server.py's
        # /feedback) or a passing eval case (evals/run_evals.py, C3a).
        # C4a: stores the real ORDERED LIST (not a joined string) -- each
        # entry must independently pass gate.validate() again on replay,
        # which a joined multi-statement string never could.
        if state["queries"]:
            memory.set_plan(key, client, {"queries": state["queries"]})
        envelope = _build_envelope(question, final_text, state)

    _record_latency()
    # answer_sql stays a single joined string for external consumers
    # (api/server.py's /feedback, evals/run_evals.py's C3a promotion) --
    # never re-executed, only ever displayed as few-shot text, so joining
    # multiple statements here is safe even though gate.py would reject
    # them joined (plan_cache keeps the real separable list instead, above).
    yield {"type": "done", "answer": final_text, "needs_ask": None,
           "answer_sql": "; ".join(state["queries"]) if state["queries"] else None, "cache_key": key, **envelope}


def ask(client: str, question: str, conversation: dict = None, role: str = "manager", subject: str | None = None) -> dict:
    """Returns {"answer": str|None, "needs_ask": str|None} -- exactly one is
    set. Thin wrapper over ask_stream() (C7) for callers that only want the
    final result (CLI, tests) without consuming progress/streaming events."""
    for event in ask_stream(client, question, conversation, role, subject):
        if event["type"] == "done":
            return {k: v for k, v in event.items() if k != "type"}
    raise RuntimeError("ask_stream() ended without a 'done' event")  # unreachable


def _main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--client", required=True)
    parser.add_argument("question")
    args = parser.parse_args()

    result = ask(args.client, args.question)
    print(result["needs_ask"] if result["needs_ask"] else result["answer"])


if __name__ == "__main__":
    _main()
