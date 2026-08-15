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
import calendar
import datetime
import hashlib
import json
import re
import time
from pathlib import Path

from . import catalog, config, docs, gate, hot_cache, llm, memory, metrics, params, reports, sql, tenant_pack, trace, vault

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
# P0: search_docs is free vs MAX_QUERIES but still thrashes without its own cap.
MAX_DOC_SEARCHES = 3

_DOCS_ONLY_SCHEMA_TOOLS = frozenset({
    "introspect_schema", "search_schema_notes", "read_schema_note", "get_joins",
})

_FAST_PATH_SKIP_TOOLS = frozenset({
    "search_docs", "search_schema_notes", "read_schema_note", "get_joins",
})

_EXPLAIN_INTENT_RE = re.compile(
    r"كيف|اشرح|explain|how does|how do|what is|what does|ماذا تعني",
    re.IGNORECASE,
)
_COUNT_HINT_RE = re.compile(r"كم|عدد|how many|\bcount\b", re.IGNORECASE)
_MASTER_COUNT_TERMS = (
    "عميل", "عملاء", "زبائن", "زبون", "customer", "customers",
    "مندوب", "مناديب", "مندوبين", "salesperson", "salesman",
    "صنف", "أصناف", "اصناف", "item", "items",
)

_RELATIVE_DATE_PHRASES = (
    "هذا الشهر", "this month", "الشهر الماضي", "هذا العام", "this year", "السنة",
)
_THIS_MONTH_PHRASES = ("هذا الشهر", "this month")
_THIS_YEAR_PHRASES = ("هذا العام", "this year")
_ALL_COMPANIES_PHRASES = ("كل الشركات", "all companies", "لكل الشركات")
_CALENDAR_CONFIRM_RE = re.compile(
    r"(?:^|\s)(?:نعم|احسب|موافق|آخر\s*شهر|آخر\s*قيد|yes|ok|calculate\s+last)(?:\s|$|[؟?.!])",
    re.IGNORECASE,
)
_AR_MONTH_NAMES = (
    "يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو",
    "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر",
)
_EMPTY_FINAL_RETRY_NUDGE = "أجب بالعربية من نتائج الأدوات فقط."

_COUNT_SQL_INTENT_RE = re.compile(
    r"كم|عدد|مجموع|how many|count|\bSELECT\b",
    re.IGNORECASE,
)

# C6a: row-count cap, not a byte-slice. json.dumps(...)[:8000] can cut mid-
# token, handing the model MALFORMED JSON with no signal it was ever cut --
# exactly the condition that produces a confident wrong total. 50 rows of
# ordinary relational data comfortably fits any reasonable context budget
# without needing a second byte-level safety net on top.
_ROW_DISPLAY_CAP = 50

# C7: leaked tool-call markup from several gateways/models. Content is
# buffered (never forwarded) until enough has arrived to rule these out.
_MALFORMED_MARKERS = (
    "<｜",           # DeepSeek DSML
    "<tool_call",    # Kimi/Nemotron XML tool leak
    "<function=",    # alternate XML wrapper
)
_MALFORMED_SENTINEL = _MALFORMED_MARKERS[0]  # kept for tests/comments

_STEP_LABELS = {
    "introspect_schema": "searching schema",
    "analyze": "analyzing",
    "search_docs": "searching documentation",
    "search_schema_notes": "searching schema notes",
    "read_schema_note": "reading schema note",
    "get_joins": "looking up joins",
    "lookup_hot": "loading master data",
    "run_metric": "running metric query",
}


def _step_label(name: str, args: dict, state: dict) -> str | None:
    """Human-readable progress label for a tool about to run. Deliberately
    generic -- never the table/column/proc name or SQL text (C7: 'show
    that a query is running, never its text -- that leaks schema shape and,
    through it, other clients' branch structure'). None for ask_user, which
    ends the turn immediately with nothing to narrate a wait for."""
    if name in ("run_select", "run_metric"):
        if name == "run_select" and "information_schema" in args.get("sql", "").lower():
            return "searching schema"
        return f"running query {len(state['queries']) + 1} of {MAX_QUERIES}"
    return _STEP_LABELS.get(name)


def _looks_like_malformed_tool_syntax(content: str) -> bool:
    """Live-observed failure modes: models occasionally emit raw tool-call
    markup as plain text content instead of the structured tool_calls field
    -- msg.tool_calls comes back empty and the literal markup (e.g.
    "<｜｜DSML｜｜tool_calls>", "<tool_call>…</tool_call>",
    "<function=run_select>") would otherwise be accepted as the final answer.
    Retry rather than surface it.

    C9: was `"tool_calls" in content or "｜" in content` -- tightened to
    actual sentinel prefixes ordinary prose would not produce."""
    if not content:
        return False
    if "<｜" in content:
        return True
    low = content.lower()
    return any(marker in low for marker in _MALFORMED_MARKERS[1:])


def _still_buffering_tool_syntax(buffer: str) -> bool:
    """True while buffer might still grow into leaked tool-call markup."""
    if _looks_like_malformed_tool_syntax(buffer):
        return True
    low = buffer.lower()
    for marker in _MALFORMED_MARKERS:
        m = marker if marker == "<｜" else marker.lower()
        check = buffer if marker == "<｜" else low
        if len(check) < len(m) and m.startswith(check):
            return True
    return False


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
    assembling_tools = False
    tool_calls = {}
    for chunk in stream:
        if not chunk.choices:
            continue
        delta = chunk.choices[0].delta
        if delta.tool_calls:
            assembling_tools = True
        if delta.content:
            buffer += delta.content
            if assembling_tools or _looks_like_malformed_tool_syntax(buffer):
                forwarding = False
            elif forwarding:
                yield {"type": "answer_chunk", "text": delta.content}
            elif not _still_buffering_tool_syntax(buffer):
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
    if not forwarding and not assembling_tools and buffer and not _looks_like_malformed_tool_syntax(buffer):
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
            "description": (
                "Block only when identity or policy is unresolved: multi-company CompanyID, "
                "which of several hot-cache people/items, EXEC/proc body, or كل الشركات. "
                "Do NOT block for grain ambiguity (best salesman, sales vs orders, cash vs credit) — "
                "state one Arabic assumption, run run_metric/run_select, then offer an alternate "
                "('إذا تقصد عدد الفواتير أو زبائن المنطقة، قل.')."
            ),
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
    {
        "type": "function",
        "function": {
            "name": "search_schema_notes",
            "description": (
                "Regex search over vault schema notes (tables, procedures metadata, relations) in Olives_BO. "
                "Never returns procedure bodies. Does not count against query budget."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "pattern": {"type": "string"},
                    "type": {"type": "string", "description": "Optional: table, procedure, or relation"},
                },
                "required": ["pattern"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_schema_note",
            "description": (
                "Read a vault schema note by name or path. Procedures return metadata only (params, tables read) — "
                "never CREATE PROCEDURE text. Does not count against query budget."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "path": {"type": "string"},
                    "type": {"type": "string"},
                },
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_joins",
            "description": (
                "Get FK relation notes and graph dependencies for a BO table name. "
                "Does not count against query budget."
            ),
            "parameters": {
                "type": "object",
                "properties": {"table": {"type": "string"}},
                "required": ["table"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "run_metric",
            "description": (
                "Run a named business metric with the correct grain — prefer over run_select for "
                "net sales, salesperson sales rank, returns, orders, van stock, or "
                "customer-to-salesperson assignment. Counts against the query budget."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "metric": {
                        "type": "string",
                        "description": (
                            "Metric name or alias: net_sales (مبيعات), "
                            "net_sales_by_salesperson (أفضل مندوب / best salesman), "
                            "daily_sales_pack (محصلة يومية / daily sales), "
                            "returns (مرتجعات), orders (طلبات), van_stock (رصيد السيارة), "
                            "cfd_assignment (عملاء المندوب)."
                        ),
                    },
                    "filters": {
                        "type": "object",
                        "properties": {
                            "from_date": {"type": "string", "description": "YYYY-MM-DD"},
                            "to_date": {"type": "string", "description": "YYYY-MM-DD"},
                            "sales_person_id": {"type": "integer"},
                            "undelivered_only": {"type": "boolean"},
                        },
                    },
                },
                "required": ["metric"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "lookup_hot",
            "description": (
                "Load an L1 master snapshot (salespersons, items, routes, companies, etc.). "
                "Never for invoices/orders/receipts/balances. Free — does not count against query budget."
            ),
            "parameters": {
                "type": "object",
                "properties": {"table": {"type": "string"}},
                "required": ["table"],
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


def _has_count_sql_intent(question: str) -> bool:
    """Mixed how-to + count questions keep SQL tools; price-list explainers do not."""
    return bool(_COUNT_SQL_INTENT_RE.search(question))


def _is_fast_count_path(question: str) -> bool:
    """Count-only master or named-metric questions — skip docs/vault latency."""
    q = (question or "").strip()
    if not q or _EXPLAIN_INTENT_RE.search(q):
        return False
    if not _COUNT_HINT_RE.search(q):
        return False
    q_lower = q.lower()
    if metrics.question_mentions_metric(q):
        return True
    return any(term in q_lower for term in _MASTER_COUNT_TERMS)


def _needs_honesty_preamble(question: str) -> bool:
    q = question.lower()
    if any(p.lower() in q for p in _RELATIVE_DATE_PHRASES):
        return True
    return any(p.lower() in q for p in _ALL_COMPANIES_PHRASES)


def _honesty_preamble(client: str, company_id: int) -> str:
    """Deterministic relative-date / all-companies guard — not prompt-only."""
    calendar_today = time.strftime("%Y-%m-%d")
    max_invoice_date = "none"
    max_order_date = "none"
    try:
        rows = sql.run_select(
            "SELECT MAX(TransactionDate) AS d FROM t.TransactionsHeaders",
            company_id, client,
        )
        if rows and rows[0].get("d") is not None:
            max_invoice_date = str(rows[0]["d"])[:10]
    except Exception:  # noqa: BLE001 — fail soft when DB unavailable (tests mock)
        pass
    try:
        rows = sql.run_select(
            "SELECT MAX(OrderDate) AS d FROM t.OrdersHeaders",
            company_id, client,
        )
        if rows and rows[0].get("d") is not None:
            max_order_date = str(rows[0]["d"])[:10]
    except Exception:  # noqa: BLE001
        pass
    return (
        f"Honesty: calendar_today={calendar_today}. "
        f"max_invoice_date={max_invoice_date} (from MAX(TransactionDate)). "
        f"max_order_date={max_order_date}. "
        f"t. views return only CompanyID={company_id}. "
        "If the user asked for all companies, say you only see this company. "
        "If they asked for this month/year and that calendar period has no invoices, "
        "say the calendar period is empty, then offer the last posting period."
    )


def _ar_month_year(d: datetime.date) -> str:
    return f"{_AR_MONTH_NAMES[d.month - 1]} {d.year}"


def _parse_iso_date(value) -> datetime.date | None:
    if value is None:
        return None
    try:
        return datetime.date.fromisoformat(str(value)[:10])
    except (TypeError, ValueError):
        return None


def _fetch_max_invoice_date(client: str, company_id: int) -> datetime.date | None:
    try:
        rows = sql.run_select(
            "SELECT MAX(TransactionDate) AS d FROM t.TransactionsHeaders "
            "WHERE TransactionTypeID = 1 AND ISNULL(IsVoid,0) = 0",
            company_id, client,
        )
        if rows and rows[0].get("d") is not None:
            return _parse_iso_date(rows[0]["d"])
    except Exception:  # noqa: BLE001
        pass
    return None


def _month_bounds(year: int, month: int) -> tuple[datetime.date, datetime.date]:
    first = datetime.date(year, month, 1)
    last = datetime.date(year, month, calendar.monthrange(year, month)[1])
    return first, last


def _asks_this_month(question: str) -> bool:
    q = question.lower()
    return any(p.lower() in q for p in _THIS_MONTH_PHRASES)


def _asks_this_year(question: str) -> bool:
    q = question.lower()
    return any(p.lower() in q for p in _THIS_YEAR_PHRASES)


def _user_confirmed_last_posting(question: str) -> bool:
    return bool(_CALENDAR_CONFIRM_RE.search(question.strip()))


def _calendar_month_has_invoices(client: str, company_id: int, year: int, month: int) -> bool:
    first, last = _month_bounds(year, month)
    try:
        rows = sql.run_select(
            "SELECT TOP 1 1 AS x FROM t.TransactionsHeaders "
            "WHERE TransactionTypeID = 1 AND ISNULL(IsVoid,0) = 0 "
            f"AND TransactionDate >= '{first.isoformat()}' "
            f"AND TransactionDate <= '{last.isoformat()}'",
            company_id, client,
        )
        return bool(rows)
    except Exception:  # noqa: BLE001
        return False


def _empty_calendar_needs_ask(question: str, client: str, company_id: int) -> str | None:
    """Code-side guard: do not compute July as هذا الشهر when calendar month is empty."""
    if any(p.lower() in question.lower() for p in _ALL_COMPANIES_PHRASES):
        return None
    if _user_confirmed_last_posting(question):
        return None
    if not (_asks_this_month(question) or _asks_this_year(question)):
        return None
    today = datetime.date.today()
    max_invoice = _fetch_max_invoice_date(client, company_id)
    if max_invoice is None:
        return None

    if _asks_this_month(question):
        if _calendar_month_has_invoices(client, company_id, today.year, today.month):
            return None
        return (
            f"{_ar_month_year(today)} فارغ. آخر قيد: {_ar_month_year(max_invoice)}. "
            "هل أحسب آخر شهر قيد؟"
        )

    if _asks_this_year(question):
        try:
            rows = sql.run_select(
                "SELECT TOP 1 1 AS x FROM t.TransactionsHeaders "
                "WHERE TransactionTypeID = 1 AND ISNULL(IsVoid,0) = 0 "
                f"AND TransactionDate >= '{today.year}-01-01' "
                f"AND TransactionDate <= '{today.isoformat()}'",
                company_id, client,
            )
            if rows:
                return None
        except Exception:  # noqa: BLE001
            pass
        return (
            f"عام {today.year} فارغ حتى اليوم. آخر قيد: {_ar_month_year(max_invoice)}. "
            "هل أحسب آخر شهر قيد؟"
        )

    return None


def _calendar_confirm_system_note(client: str, company_id: int) -> str | None:
    max_invoice = _fetch_max_invoice_date(client, company_id)
    if max_invoice is None:
        return None
    first, last = _month_bounds(max_invoice.year, max_invoice.month)
    return (
        f"User confirmed last posting month. Use run_metric(net_sales, "
        f"from_date={first.isoformat()}, to_date={last.isoformat()}). "
        "Do not label that period as هذا الشهر or the current calendar month."
    )


def _search_docs(client: str, query: str) -> list:
    """Call docs.search with client locale for Arabic synonym expansion."""
    locale = config.load_client(client).get("locale")
    return docs.search(client, query, locale=locale)


def _dedupe_doc_pairs(pairs: list[tuple[str, str]]) -> list[tuple[str, str]]:
    seen: set[tuple[str, str]] = set()
    out: list[tuple[str, str]] = []
    for pair in pairs:
        if pair not in seen:
            seen.add(pair)
            out.append(pair)
    return out


def _active_tools(state: dict) -> list | None:
    """Filter tool list for query budget, doc-search cap, and docs-only guard."""
    if len(state["queries"]) >= MAX_QUERIES:
        return None
    tools = TOOLS
    if state.get("fast_count"):
        tools = [t for t in tools if t["function"]["name"] not in _FAST_PATH_SKIP_TOOLS]
    if state.get("doc_searches", 0) >= MAX_DOC_SEARCHES:
        tools = [t for t in tools if t["function"]["name"] != "search_docs"]
    if state.get("docs_only"):
        tools = [t for t in tools if t["function"]["name"] not in _DOCS_ONLY_SCHEMA_TOOLS]
    return tools


def _system_prompt(client: str, company_id: int | None = None) -> str:
    base = (BASE_DIR / "prompts" / "system.md").read_text()
    base = base.replace("{{CLIENT}}", client).replace("{{MAX_QUERIES}}", str(MAX_QUERIES))
    playbook = BASE_DIR / "prompts" / "join_playbook.md"
    if playbook.exists():
        base += "\n\n## Join playbook\n" + playbook.read_text()
    if company_id is not None:
        base += "\n\n" + tenant_pack.build(client, company_id)
    return base


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


def _sanitize_final_text(text: str | None) -> str | None:
    if text and _looks_like_malformed_tool_syntax(text):
        return None
    return text


def _is_blank(text: str | None) -> bool:
    return not text or not str(text).strip()


def _has_evidence(state: dict) -> bool:
    rows = state.get("last_rows")
    if isinstance(rows, list) and rows:
        return True
    return bool(state.get("doc_source_pairs"))


def _format_stub_number(val) -> str:
    if isinstance(val, float) and val == int(val):
        return str(int(val))
    return str(val)


def _build_arabic_stub(state: dict) -> str:
    """Deterministic Arabic fallback when the model returns empty after tools."""
    rows = state.get("last_rows")
    if isinstance(rows, list) and rows:
        row = rows[0]
        if len(rows) == 1:
            if len(row) == 1:
                val = next(iter(row.values()))
                if isinstance(val, (int, float)) and not isinstance(val, bool):
                    return f"النتيجة: {_format_stub_number(val)}."
            nums = [
                (k, v) for k, v in row.items()
                if isinstance(v, (int, float)) and not isinstance(v, bool)
            ]
            if nums:
                parts = [f"{k}: {_format_stub_number(v)}" for k, v in nums[:3]]
                return "النتيجة: " + "، ".join(parts) + "."
        return "النتيجة في الجدول أدناه."
    if state.get("doc_source_pairs"):
        return "الإجابة في المصادر أدناه."
    return "تعذر صياغة الإجابة من البيانات المتاحة."


def _retry_empty_final(messages: list) -> str | None:
    """One extra completion with tools=None after successful tools yielded empty content."""
    retry_messages = messages + [{"role": "system", "content": _EMPTY_FINAL_RETRY_NUDGE}]
    try:
        resp = llm.complete(retry_messages, tools=None, stream=False)
        return _sanitize_final_text(resp.choices[0].message.content)
    except Exception:  # noqa: BLE001
        return None


def _resolve_final_text(final_text: str | None, messages: list, state: dict) -> str:
    """Never return whitespace or empty when SQL/docs evidence exists."""
    if not _is_blank(final_text):
        return final_text.strip()
    if not _has_evidence(state):
        return final_text or ""
    retried = _retry_empty_final(messages)
    if not _is_blank(retried):
        return retried.strip()
    return _build_arabic_stub(state)


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
        state["doc_searches"] = state.get("doc_searches", 0) + 1
        results = _search_docs(client, args.get("query", ""))
        for r in results:
            state["doc_source_pairs"].append((r["source"], r.get("heading") or ""))
        state["doc_source_pairs"] = _dedupe_doc_pairs(state["doc_source_pairs"])
        question = state.get("question", "")
        if results and not _has_count_sql_intent(question):
            state["docs_only"] = True
        return {"results": results}
    if name == "search_schema_notes":
        return {"results": vault.search_schema_notes(
            args.get("pattern", ""), type_filter=args.get("type"),
        )}
    if name == "read_schema_note":
        return vault.read_schema_note(
            name=args.get("name"), path=args.get("path"), type_filter=args.get("type"),
        )
    if name == "get_joins":
        return vault.get_joins(args.get("table", ""))
    if name == "lookup_hot":
        result = hot_cache.lookup(args.get("table", ""), company_id, client)
        base = (args.get("table") or "").strip().split(".")[-1]
        sql_text = hot_cache.l1_sql(base, client)
        if sql_text:
            # Record SQL for the done envelope only — does not spend MAX_QUERIES.
            state.setdefault("hot_sql", []).append(sql_text)
        return result
    if name == "run_metric":
        result = metrics.run_metric(
            args.get("metric", ""),
            company_id,
            client,
            allowed_procs=allowed_proc_names,
            filters=args.get("filters"),
        )
        if "error" not in result:
            sql_text = result.get("sql")
            state["queries"].append(sql_text)
            rows = result.get("rows")
            if isinstance(rows, list) and (state["last_rows"] is None or len(rows) > len(state["last_rows"])):
                state["last_rows"] = rows
        return result
    if name == "run_select":
        sql_text = args["sql"]
        if "information_schema" not in sql_text.lower():
            grain_err = gate.invoice_grain_error(sql_text)
            if grain_err:
                return {"error": grain_err}
        result = sql.run_select(sql_text, company_id, client, allowed_procs=allowed_proc_names)
        # Models sometimes explore the schema via INFORMATION_SCHEMA through
        # run_select instead of introspect_schema -- that's metadata, not a
        # business query, so it's free (doesn't count against MAX_QUERIES,
        # C4) same as it previously didn't flip the old results_in_context
        # latch. C3: only a real business query is appended to
        # state["queries"] -- the old code tracked "last_sql"
        # unconditionally, so a metadata probe issued after the real query
        # (e.g. re-checking a column name for a follow-up) would silently
        # become the thing cached/promoted instead of the actual answer.
        if "information_schema" not in sql_text.lower():
            state["queries"].append(sql_text)
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


def _format_doc_sources(doc_source_pairs: list[tuple[str, str]]) -> list[str]:
    formatted = []
    for source, heading in doc_source_pairs:
        formatted.append(f"{source} › {heading}" if heading else source)
    return formatted


def _build_sources(queries: list, doc_source_pairs: list[tuple[str, str]]) -> list:
    """C8: 'always cite' -- table names come straight from the SQL actually
    run (every client-facing table this project has is queried as
    `t.TableName`, confirmed throughout this codebase), never a second
    guess at what the model "meant" to query. Doc sources were already
    recorded verbatim by _run_tool's search_docs branch."""
    tables = sorted(set(m.group(1) for q in queries for m in _SOURCE_TABLE_RE.finditer(q)))
    return tables + _format_doc_sources(doc_source_pairs)


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


def _answer_sql(state: dict) -> str | None:
    parts = list(state.get("queries") or []) + list(state.get("hot_sql") or [])
    return "; ".join(parts) if parts else None


def _build_envelope(question: str, final_text: str, state: dict) -> dict:
    """C8: assembles the structured pieces the plan asks /ask to return
    alongside the prose answer. Everything except followups is derived
    from data this turn already produced -- never a second, potentially
    inconsistent ask to the model for numbers/names it already gave."""
    table = _build_table(state["last_rows"])
    return {
        "table": table,
        "chart": _build_chart(table),
        "sources": _build_sources(state["queries"], state["doc_source_pairs"]),
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
                {"role": "system", "content": _system_prompt(client, company_id)},
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
            last_rows = max((r for r in raw_results if isinstance(r, list)), key=len, default=None)
            cache_state = {
                "queries": queries, "last_rows": last_rows, "doc_source_pairs": [],
            }
            if _is_blank(answer) and _has_evidence(cache_state):
                answer = _resolve_final_text(answer, messages, cache_state)
            elif answer:
                answer = answer.strip()
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
            envelope = _build_envelope(question, answer, cache_state)
            yield {"type": "done", "answer": answer, "needs_ask": None,
                   "answer_sql": "; ".join(queries), "cache_key": key,
                   "doc_search_count": 0, **envelope}
            return
        except gate.GateError:
            pass  # cached plan no longer validates -- fall through to a full turn

    calendar_ask = _empty_calendar_needs_ask(question, client, company_id)
    if calendar_ask:
        trace.log_event(client, question, event="needs_ask", subject=subject, param="calendar_period")
        _record_latency()
        yield {"type": "done", "answer": None, "needs_ask": calendar_ask}
        return

    messages = [{"role": "system", "content": _system_prompt(client, company_id)}]
    shots = memory.few_shots(client, company_id, question, limit=3)
    if shots:
        examples = "\n".join(f'- "{s["question"]}" -> `{s["proc_or_sql"]}`' for s in shots)
        messages.append({
            "role": "system",
            "content": f"Previously-verified query patterns for this client and CompanyID:\n{examples}",
        })
    negatives = memory.negative_shots(client, company_id, question, limit=2)
    if negatives:
        bad = "\n".join(
            f'- "{n["question"]}" FAILED (`{n.get("proc_or_sql") or ""}`) — {n.get("reason") or "avoid this pattern"}'
            for n in negatives
        )
        messages.append({
            "role": "system",
            "content": f"Known bad patterns for this client and CompanyID — do not repeat:\n{bad}",
        })
    report_cards = reports.match_reports(question, client, limit=2)
    if report_cards:
        cards = "\n".join(
            f"- {c['name']}: {c.get('purpose', '')[:200]} | tables: {', '.join(c.get('tables', []))}"
            for c in report_cards
        )
        messages.append({
            "role": "system",
            "content": f"Matching report metadata (write equivalent SELECT on t., never EXEC):\n{cards}",
        })
    # Wave 6 vault cards — deterministic schema memory on every /ask
    fast_count = _is_fast_count_path(question)
    if not fast_count:
        vault_hits = vault.retrieve_cards(question, client, limit=3)
        if vault_hits:
            vault_block = vault.format_retrieved_cards(question, vault_hits)
            messages.append({"role": "system", "content": vault_block})
    if fast_count:
        messages.append({
            "role": "system",
            "content": (
                "Count-only question for a master table or named metric — use run_metric "
                "or run_select directly. Do not call search_docs or vault tools."
            ),
        })
    if _needs_honesty_preamble(question):
        messages.append({"role": "system", "content": _honesty_preamble(client, company_id)})
    if _user_confirmed_last_posting(question):
        confirm_note = _calendar_confirm_system_note(client, company_id)
        if confirm_note:
            messages.append({"role": "system", "content": confirm_note})
    messages.append({"role": "user", "content": question})

    # C4: "queries" replaces the old single answer_sql/results_in_context
    # latch -- an ordered list of every real business query run this turn,
    # so a second query can be compared against the first (period-over-
    # period, drill-down, verification). INFORMATION_SCHEMA probes and
    # analyze calls never append here, so they stay free.
    # C8: last_rows/doc_source_pairs feed the answer envelope (table/chart/
    # sources) -- see _run_tool and _build_envelope.
    state = {
        "queries": [],
        "warned_last_query": False,
        "warned_doc_search_cap": False,
        "last_rows": None,
        "doc_source_pairs": [],
        "doc_searches": 0,
        "docs_only": False,
        "fast_count": fast_count,
        "question": question,
    }
    final_text = None

    for _ in range(MAX_TURNS):
        tools = _active_tools(state)
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
            final_text = _sanitize_final_text(msg.get("content"))
            if not _is_blank(final_text):
                break
            final_text = None
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
        if state.get("doc_searches", 0) >= MAX_DOC_SEARCHES and not state.get("warned_doc_search_cap"):
            messages.append({
                "role": "system",
                "content": (
                    "No more documentation searches. Answer from excerpts already retrieved, "
                    "or say the guides do not cover this (لا يوجد في دليل المستخدم)."
                ),
            })
            state["warned_doc_search_cap"] = True

    if _has_evidence(state):
        final_text = _resolve_final_text(final_text, messages, state)
        trace.log_event(client, question, event="answer", subject=subject, company_id=company_id)
        if state["queries"]:
            memory.set_plan(key, client, {"queries": state["queries"]})
        envelope = _build_envelope(question, final_text, state)
    elif _is_blank(final_text):
        final_text = "I can't answer that confidently from the available data."
        trace.log_event(client, question, event="refused", subject=subject)
        envelope = {"table": None, "chart": None, "sources": [], "followups": [], "doc_search_count": state.get("doc_searches", 0)}
    else:
        final_text = final_text.strip()
        trace.log_event(client, question, event="answer", subject=subject, company_id=company_id)
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
           "answer_sql": _answer_sql(state), "cache_key": key,
           "doc_search_count": state.get("doc_searches", 0), **envelope}


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
