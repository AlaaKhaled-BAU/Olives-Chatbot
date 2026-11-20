# Trace and Grounding Principles Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Record every model call and tool call as its own trace span, grade that path in unit tests, and stop three silent failure modes (ungrounded numbers, ambiguous salesman names, how-to answers with no guide excerpt) without adding LangChain, LangGraph, LangSmith, Langfuse, LangFlow, or LangExtract.

**Architecture:** `core/trace.py` grows a span line beside the existing one-line-per-turn event. `core/grounding.py` is a pure module for number checks, the how-to refusal sentence, and the salesman-name question. `core/agent.py` calls those functions and stamps `trace_id` on the done event. `api/server.py` copies that id, the route flags, and the tool names onto the session turn so `/feedback` can log them. `evals/score_path.py` scores a list of spans with no network and no database.

**Tech Stack:** Python 3.13 (`py -3.13` on Windows), FastAPI, existing `core/trace.py` JSONL, pytest. No new packages.

## Global Constraints

- Python 3.13 only (`py -3.13 -m pytest …`); never `python3`.
- Never use SA or IIS `cds` from the running app — only `chatbot_ro` + `t.` views + `SESSION_CONTEXT` (AGENTS.md rule 2).
- One SQL path: `core/sql.py` + `core/gate.py`. Do not bypass the gate.
- After query results enter model context, no more tool calls (AGENTS.md rule 9). The tool list stays frozen for the whole turn so the DeepSeek prefix cache is not broken. Do not start changing `_active_tools` mid-turn.
- Cache keys include client + CompanyID.
- Never return procedure bodies.
- No new third-party dependency. Do not import langchain, langgraph, langsmith, langfuse, or langextract.
- Unit tests only in Tasks 1–7. Do not call DeepSeek. Do not run `evals/run_golden_session.py` or `evals/run_evals.py` inside a task.
- Do not add a word list whose only justification is one golden question. Name detection keys off the SQL the tool already ran (`t.SalesPersons` plus `LIKE` plus `Name`), not off a phrase from the golden set.
- On PowerShell, run the `git commit` heredocs from Git Bash. Never `git add -i`. Never `--no-verify`.

## Evidence this plan is answering

Measured 10 Nov 2026, client 105. Files: `evals/golden_session_105_results_20261110T170202Z.json`, `evals/heldout_105_results_20261110T165901Z.json`.

| Set | Questions | First pass | Final grader | Asked again | p50 | Off-peak USD / q | Peak USD / q | Model calls / q |
|---|---|---|---|---|---|---|---|---|
| Golden | 6 | 5/6 (83%) | 6/6 | 5/6 (`best_rep_visits` flipped) | 12,239 ms | 0.00854 | 0.01707 | 3.67 |
| Held-out | 8 | 8/8 | 8/8 | not run | 12,308 ms | 0.01082 | 0.02164 | 3.38 |

`last_month_summary` passed the answer check and still logged a `run_select` grain error. That is the path-score target: a green answer with a red path.

9 Nov plan finding, still the reason spans exist: about 86% of that session's spend was 10 calls re-sending 33k–65k uncached tokens, and one tool error could not be named because only the finished turn was logged. The tool list is now frozen (`tests/test_agent.py::test_query_budget_closes_after_max_queries_real_queries`), so do not "fix" cache by changing tools mid-turn. Spans measure whether gear changes and the final-contract call still miss the cache. They do not promise to recover that 86%.

Already done, do not rebuild: `_run_tool` returns `budget_spent` and does not execute query number 5 (`test_parallel_tool_calls_cannot_exceed_query_budget`). This plan only stops the progress label from saying "running query 5 of 4".

## File structure

- `core/trace.py` — append `log_span`. Owns the JSONL line shape. Does not know about tools.
- `core/grounding.py` — pure functions. No SQL, no LLM, no trace.
- `core/agent.py` — opens one `trace_id` per `ask_stream`, writes spans, applies grounding, name ask, and how-to refusal. Puts `trace_id`, `path`, and `tool_names` on the done event.
- `core/sessions.py` — copies those three fields onto the transcript row.
- `api/server.py` — copies them onto `last_turn` and into both feedback log lines.
- `evals/score_path.py` — pure path grade over span dicts.
- Tests live next to the behavior: `tests/test_trace_usage.py`, `tests/test_grounding.py`, `tests/test_agent.py`, `tests/test_feedback.py`, `tests/test_score_path.py`.

---

### Task 1: Span lines

**Files:**
- Modify: `core/trace.py`
- Test: `tests/test_trace_usage.py`

**Interfaces:**
- Consumes: existing `log_event(client, question, event, subject=None, **fields)` and `TRACE_PATH`.
- Produces: `log_span(client: str, trace_id: str, span_id: str, parent_id: str | None, name: str, **fields) -> None`. Writes one JSON object per call with `"kind": "span"`. `log_event` is unchanged; callers pass `trace_id` through `**fields`.

- [ ] **Step 1: Write the failing test**

Append to `tests/test_trace_usage.py`:

```python
def test_log_span_is_its_own_line(tmp_path, monkeypatch):
    monkeypatch.setattr(trace, "TRACE_PATH", tmp_path / "trace.jsonl")
    monkeypatch.setattr(trace, "GIT_SHA", "abc123")
    trace.log_span(
        "105", "trace1", "span1", None, "llm",
        gear="t1", ms=1200, cache_hit_tokens=10, cache_miss_tokens=90,
    )
    trace.log_event("105", "كم المبيعات؟", event="answer", trace_id="trace1")
    lines = (tmp_path / "trace.jsonl").read_text().splitlines()
    assert len(lines) == 2
    span = json.loads(lines[0])
    turn = json.loads(lines[1])
    assert span["kind"] == "span"
    assert span["trace_id"] == "trace1"
    assert span["span_id"] == "span1"
    assert span["parent_id"] is None
    assert span["name"] == "llm"
    assert span["gear"] == "t1"
    assert span["git_sha"] == "abc123"
    assert "question" not in span
    assert turn["trace_id"] == "trace1"
    assert turn["event"] == "answer"
```

Add `import json` to that file if it is not already imported.

- [ ] **Step 2: Run the test to verify it fails**

Run: `py -3.13 -m pytest -q tests/test_trace_usage.py::test_log_span_is_its_own_line -v`

Expected: FAIL with `AttributeError: module 'core.trace' has no attribute 'log_span'`

- [ ] **Step 3: Write the minimal implementation**

In `core/trace.py`, add this function after `log_event`:

```python
def log_span(client: str, trace_id: str, span_id: str, parent_id: str | None,
             name: str, **fields) -> None:
    """One JSONL line for a single model call or tool call.

    The turn summary stays on log_event. A span has no question text, so a
    leaked trace file does not grow a second copy of the user prompt.
    """
    TRACE_PATH.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "kind": "span",
        "ts": time.time(),
        "client": client,
        "trace_id": trace_id,
        "span_id": span_id,
        "parent_id": parent_id,
        "name": name,
        "git_sha": GIT_SHA,
        **fields,
    }
    with TRACE_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, default=str) + "\n")
```

Also open the turn line with `encoding="utf-8"` in `log_event` so Arabic questions survive on Windows. Change only the `open` call:

```python
    with TRACE_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, default=str) + "\n")
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `py -3.13 -m pytest -q tests/test_trace_usage.py -v`

Expected: PASS, including the existing usage tests.

- [ ] **Step 5: Commit**

```bash
git add core/trace.py tests/test_trace_usage.py
git commit -m "$(cat <<'EOF'
feat: write a trace span as its own JSONL line

EOF
)"
```

---

### Task 2: The agent writes a span per call

**Files:**
- Modify: `core/agent.py` (`_step_label`, `ask_stream`)
- Test: `tests/test_agent.py`

**Interfaces:**
- Consumes: `trace.log_span` from Task 1. `Usage.calls` entries have `gear`, `ms`, `cache_hit`, `cache_miss`, `prompt`, `completion`.
- Produces: every `ask_stream` done event includes `trace_id: str`, `path: str`, `tool_names: list[str]`. Spans use `name` of `llm`, `tool`, `plan_cache`, or `final_contract`. Tool spans include `tool`, `ms`, `status` (`ok`, `error`, or `budget_spent`), and `sql_hash` (12 hex chars) when the call had SQL. `prompt_file_hashes() -> dict[str, str]` returns 12-hex sha256 prefixes for `prompts/system.md`, `prompts/join_playbook.md`, and `prompts/analyst.md` when the file exists. The turn `log_event` includes `trace_id` and `prompt_hashes`.

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_agent.py`:

```python
def test_step_label_is_silent_once_the_query_budget_is_spent():
    state = {"queries": ["q"] * agent.MAX_QUERIES}
    assert agent._step_label("run_select", {"sql": "SELECT 1 FROM t.Items"}, state) is None
    assert agent._step_label("run_metric", {"metric": "sales"}, state) is None
    assert agent._step_label("run_report", {"name": "Rpt_Sales"}, state) is None


def test_prompt_file_hashes_are_12_hex_and_cover_system():
    hashes = agent.prompt_file_hashes()
    assert "system.md" in hashes
    assert len(hashes["system.md"]) == 12
    int(hashes["system.md"], 16)


def test_ask_writes_llm_and_tool_spans(monkeypatch, tmp_path):
    monkeypatch.setattr(trace, "TRACE_PATH", tmp_path / "trace.jsonl")
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    calls = [
        _resp(_msg(tool_calls=[_tool_call("c1", "analyze", '{"operation":"difference","before":1,"after":2}')])),
        _resp(_msg(content="الفرق 1.")),
    ]
    with patch.object(agent.llm, "complete", side_effect=calls):
        result = agent.ask("morec", "ما الفرق؟", conversation={"CompanyID": 1})
    assert result["trace_id"]
    assert result["path"]
    assert result["tool_names"] == ["analyze"]
    lines = [json.loads(line) for line in (tmp_path / "trace.jsonl").read_text(encoding="utf-8").splitlines()]
    spans = [row for row in lines if row.get("kind") == "span"]
    names = [row["name"] for row in spans]
    assert "llm" in names
    tool_spans = [row for row in spans if row["name"] == "tool"]
    assert tool_spans[0]["tool"] == "analyze"
    assert tool_spans[0]["status"] == "ok"
    assert tool_spans[0]["trace_id"] == result["trace_id"]
    turns = [row for row in lines if row.get("event") == "answer"]
    assert turns[-1]["trace_id"] == result["trace_id"]
    assert "system.md" in turns[-1]["prompt_hashes"]
```

`_resp`, `_msg`, `_tool_call`, `trace`, and `memory` are already used in `tests/test_agent.py`. Add `import json` if missing.

- [ ] **Step 2: Run the tests to verify they fail**

Run: `py -3.13 -m pytest -q tests/test_agent.py::test_step_label_is_silent_once_the_query_budget_is_spent tests/test_agent.py::test_prompt_file_hashes_are_12_hex_and_cover_system tests/test_agent.py::test_ask_writes_llm_and_tool_spans -v`

Expected: FAIL. `_step_label` still returns `"running query 5 of 4"`. `prompt_file_hashes` does not exist. The done event has no `trace_id`.

- [ ] **Step 3: Write the minimal implementation**

Add near the other module-level helpers in `core/agent.py`:

```python
def prompt_file_hashes() -> dict[str, str]:
    out: dict[str, str] = {}
    for name in ("system.md", "join_playbook.md", "analyst.md"):
        path = BASE_DIR / "prompts" / name
        if path.exists():
            out[name] = hashlib.sha256(path.read_bytes()).hexdigest()[:12]
    return out


def _sql_hash(sql: str | None) -> str | None:
    text = (sql or "").strip()
    if not text:
        return None
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def _new_span_id() -> str:
    return hashlib.sha256(os.urandom(16)).hexdigest()[:16]
```

`hashlib` and `os` are already imported.

In `_step_label`, before the `run_select` / `run_metric` / `run_report` return, add:

```python
    if name in ("run_select", "run_metric", "run_report"):
        if name == "run_select" and "information_schema" in args.get("sql", "").lower():
            return "searching schema"
        n = len(state["queries"]) + 1
        if n > MAX_QUERIES:
            return None
        return f"running query {n} of {MAX_QUERIES}"
```

Replace the existing branch that returns `f"running query {len(state['queries']) + 1} of {MAX_QUERIES}"` with the block above. Leave the information_schema case first so a probe is still "searching schema".

Inside `ask_stream`, immediately after `usage_acc = Usage()`:

```python
    trace_id = _new_span_id()
    prompt_hashes = prompt_file_hashes()
```

Helper, defined inside `ask_stream` next to `_turn_trace`, so it closes over `client`, `trace_id`, and `usage_acc`:

```python
    def _log_new_llm_spans(before: int, parent: str) -> None:
        for call in usage_acc.calls[before:]:
            trace.log_span(
                client, trace_id, _new_span_id(), parent, "llm",
                gear=call.get("gear"), ms=call.get("ms"),
                prompt_tokens=call.get("prompt"),
                completion_tokens=call.get("completion"),
                cache_hit_tokens=call.get("cache_hit"),
                cache_miss_tokens=call.get("cache_miss"),
            )
```

On the plan-cache hit path, just before `trace.record_cache_hit(client)`:

```python
            trace.log_span(client, trace_id, _new_span_id(), None, "plan_cache",
                           queries=len(queries))
            _log_new_llm_spans(0, trace_id)
```

Add `trace_id=trace_id` and `prompt_hashes=prompt_hashes` to that path's `trace.log_event(...)`. Add the same three keys to the cache-hit `yield {"type": "done", ...}`: `trace_id`, `path` = `_path_flags(question, client)`, `tool_names` = `[]`.

In `_turn_trace`, add `trace_id=trace_id` and `prompt_hashes=prompt_hashes` to the `trace.log_event` call.

Initialize in the `state` dict: `"trace_id": trace_id`, `"tool_names": []`.

In the model loop, capture the usage length before `_stream_turn` and log after the message is assembled:

```python
        usage_before = len(usage_acc.calls)
        msg = None
        for event in _stream_turn(...):
            ...
        _log_new_llm_spans(usage_before, trace_id)
```

Inside the `for tc in tool_calls` loop, after `result` is known (the `except` / `finally` block already records `ms`):

```python
            status = "ok"
            if isinstance(result, dict) and result.get("status") == "budget_spent":
                status = "budget_spent"
            elif isinstance(result, dict) and result.get("error"):
                status = "error"
            sql_text = None
            if isinstance(result, dict):
                sql_text = result.get("sql")
            if sql_text is None and name == "run_select":
                sql_text = args.get("sql")
            state["tool_names"].append(name)
            trace.log_span(
                client, trace_id, _new_span_id(), trace_id, "tool",
                tool=name, ms=ms, status=status, sql_hash=_sql_hash(sql_text),
            )
```

`ms` is assigned in the existing `finally`. Read it after that `finally`, so the append sits after the `try`/`except`/`finally`, not inside `finally`.

In `_build_envelope`, the `_final_contract` call is the extra `f0` completion. It already receives `usage_acc` via `state["_usage"]`. Do not log it inside `_build_envelope` (that function has no `trace_id`). After each `envelope = _build_envelope(...)` in the non-cache path, if `usage_acc.calls` grew, those new calls are the contract. Log them with `name="final_contract"` by slicing `usage_acc.calls` from a length captured just before `_build_envelope`. Use span name `final_contract`, not `llm`, so a reader can see the cosmetic call on its own.

On every non-cache `yield {"type": "done", ...}` add:

```python
           "trace_id": trace_id,
           "path": state.get("_path_flags"),
           "tool_names": list(state.get("tool_names") or []),
```

There are two such yields (evidence path and the later path). Add the keys to both.

- [ ] **Step 4: Run the tests to verify they pass**

Run: `py -3.13 -m pytest -q tests/test_agent.py::test_step_label_is_silent_once_the_query_budget_is_spent tests/test_agent.py::test_prompt_file_hashes_are_12_hex_and_cover_system tests/test_agent.py::test_ask_writes_llm_and_tool_spans tests/test_agent.py::test_step_label_is_generic_never_the_sql_or_object_name tests/test_trace_usage.py -v`

Expected: PASS. The old step-label test still sees "running query 1 of 4" and "running query 2 of 4".

- [ ] **Step 5: Commit**

```bash
git add core/agent.py tests/test_agent.py
git commit -m "$(cat <<'EOF'
feat: span each model call and tool call on the turn trace

EOF
)"
```

---

### Task 3: Numbers in the answer must come from the rows

**Files:**
- Create: `core/grounding.py`
- Modify: `core/agent.py` (`_evidence_confidence`)
- Test: `tests/test_grounding.py`

**Interfaces:**
- Consumes: nothing from Tasks 1–2.
- Produces:
  - `numbers_in(text: str) -> set[str]` — western and Arabic-Indic digits, commas removed, trailing zeros on a decimal stripped.
  - `figures_outside_rows(answer: str, rows: list | None, question: str = "") -> list[str]` — sorted numbers that are in the answer, not in the question, not a 4-digit year from 1990 through 2100, and not in the row values.
  - `grounded_confidence(answer: str | None, rows, tool_errors: list, question: str) -> str` — `low` when there are no rows and no doc reason to be medium; `medium` when `tool_errors` is non-empty or `figures_outside_rows` is non-empty; `high` when rows exist and every checked figure is in the rows.

- [ ] **Step 1: Write the failing test**

Create `tests/test_grounding.py`:

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.grounding import figures_outside_rows, grounded_confidence, numbers_in


def test_comma_amount_matches_plain_amount():
    assert numbers_in("15,355.23") == {"15355.23"}


def test_arabic_indic_digits_match_western():
    assert numbers_in("٤ زيارات") == {"4"}


def test_wrong_total_is_outside_the_rows():
    rows = [{"Name": "محمد مصطفى جميل", "Net": 15355.23}]
    outside = figures_outside_rows("المجموع 17,158.83", rows, question="أفضل مندوب")
    assert outside == ["17158.83"]


def test_year_in_the_question_is_not_an_ungrounded_figure():
    rows = [{"Net": 100}]
    outside = figures_outside_rows("في 2026 كان الرقم 100", rows, question="مبيعات 2026")
    assert outside == []


def test_confidence_is_medium_when_a_figure_is_not_in_the_rows():
    rows = [{"Net": 100}]
    assert grounded_confidence("الصافي 100 والفرق 9", rows, [], "كم؟") == "medium"


def test_confidence_is_high_when_every_figure_is_in_the_rows():
    rows = [{"Net": 100, "Invoices": 4}]
    assert grounded_confidence("الصافي 100 من 4 فواتير", rows, [], "كم؟") == "high"


def test_confidence_is_medium_when_a_tool_errored_even_if_rows_match():
    rows = [{"Net": 100}]
    assert grounded_confidence("الصافي 100", rows, [{"tool": "run_select"}], "كم؟") == "medium"


def test_confidence_is_low_with_no_rows_and_no_errors():
    assert grounded_confidence("لا أرقام", None, [], "كم؟") == "low"
```

The Arabic-Indic assertion allows the comma test to stay the money test. `١٥٬٣٥٥٫٢٣` uses an Arabic thousands separator and decimal; if `numbers_in` does not yet map `٬` and `٫`, the first test's second clause still passes via the western comma. The Arabic-Indic test `٤` must pass on its own.

- [ ] **Step 2: Run the test to verify it fails**

Run: `py -3.13 -m pytest -q tests/test_grounding.py -v`

Expected: FAIL with `ModuleNotFoundError: No module named 'core.grounding'`

- [ ] **Step 3: Write the minimal implementation**

Create `core/grounding.py`:

```python
"""Pure checks on answer text. No database and no model calls."""
from __future__ import annotations

import re

_AR_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
_NUM_RE = re.compile(r"\d+(?:[.,]\d+)*")


def _norm_token(token: str) -> str:
    text = token.replace(",", "").replace("،", "")
    if text.count(".") > 1:
        text = text.replace(".", "")
    elif "." in text:
        text = text.rstrip("0").rstrip(".")
    return text


def numbers_in(text: str) -> set[str]:
    raw = (text or "").translate(_AR_DIGITS)
    found: set[str] = set()
    for match in _NUM_RE.finditer(raw):
        token = _norm_token(match.group(0))
        if token:
            found.add(token)
    return found


def _is_calendar_year(token: str) -> bool:
    if len(token) != 4 or not token.isdigit():
        return False
    year = int(token)
    return 1990 <= year <= 2100


def numbers_in_rows(rows) -> set[str]:
    found: set[str] = set()
    if not isinstance(rows, list):
        return found
    for row in rows:
        if isinstance(row, dict):
            for value in row.values():
                found |= numbers_in("" if value is None else str(value))
        else:
            found |= numbers_in("" if row is None else str(row))
    return found


def figures_outside_rows(answer: str, rows, question: str = "") -> list[str]:
    allowed = numbers_in(question) | numbers_in_rows(rows)
    outside = []
    for token in sorted(numbers_in(answer)):
        if token in allowed or _is_calendar_year(token):
            continue
        outside.append(token)
    return outside


def grounded_confidence(answer: str | None, rows, tool_errors: list, question: str) -> str:
    if tool_errors:
        return "medium"
    has_rows = isinstance(rows, list) and len(rows) > 0
    if not has_rows:
        return "low"
    if figures_outside_rows(answer or "", rows, question):
        return "medium"
    return "high"
```

In `core/agent.py`, import `grounding` in the existing `from . import ...` line.

Replace `_evidence_confidence`:

```python
def _evidence_confidence(state: dict, question: str = "", final_text: str | None = None) -> str:
    if state.get("doc_source_pairs") and not state.get("queries"):
        return "medium"
    return grounding.grounded_confidence(
        final_text, state.get("last_rows"), state.get("tool_errors") or [], question,
    )
```

In `_build_envelope`, change the confidence assignment to:

```python
        out["confidence"] = _evidence_confidence(state, question, final_text)
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `py -3.13 -m pytest -q tests/test_grounding.py tests/test_agent.py::test_build_envelope_skips_followups_when_there_is_no_final_text -v`

Expected: PASS. If an existing envelope test asserts `confidence == "high"` for rows whose prose figures were never checked, update that assertion to the new rule in the same commit. Do not weaken `figures_outside_rows` to keep the old test.

- [ ] **Step 5: Commit**

```bash
git add core/grounding.py core/agent.py tests/test_grounding.py tests/test_agent.py
git commit -m "$(cat <<'EOF'
feat: drop confidence when an answer figure is not in the rows

EOF
)"
```

---

### Task 4: Code asks when a salesman name matches zero or many rows

**Files:**
- Modify: `core/grounding.py`
- Modify: `core/agent.py` (`_run_tool`, the tool loop in `ask_stream`)
- Test: `tests/test_grounding.py`, `tests/test_agent.py`

**Interfaces:**
- Consumes: `grounding` from Task 3.
- Produces: `salesman_name_ask(rows: list | None) -> str | None`. Returns `None` when there is exactly one row, or when the rows have no `Name`/`name` field (so a normal aggregate is not interrupted). Returns an Arabic question when there are 0 rows, or 2 or more rows that each have a name. `_run_tool` sets `state["forced_ask"]` only when the SQL contains `salespersons`, `like`, and `name` (case-insensitive) and `salesman_name_ask` returns a string. After the tool batch, `ask_stream` yields `needs_ask` with that string and returns. No further model call.

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_grounding.py`:

```python
from core.grounding import salesman_name_ask


def test_one_salesman_row_does_not_ask():
    assert salesman_name_ask([{"ID": 4, "Name": "محمد مصطفى جميل"}]) is None


def test_zero_salesman_rows_ask():
    text = salesman_name_ask([])
    assert text is not None
    assert "مندوب" in text


def test_two_salesman_rows_list_both_names():
    text = salesman_name_ask([
        {"ID": 1, "Name": "محمد مصطفى جميل"},
        {"ID": 2, "Name": "محمد حسن العفيفي"},
    ])
    assert "محمد مصطفى جميل" in text
    assert "محمد حسن العفيفي" in text


def test_rows_without_a_name_column_do_not_ask():
    assert salesman_name_ask([{"Net": 10}, {"Net": 20}]) is None
```

Append to `tests/test_agent.py`:

```python
def test_salesman_name_lookup_with_two_rows_sets_forced_ask():
    state = {"queries": [], "question": "زيارات محمد", "last_rows": None}
    rows = [{"ID": 1, "Name": "محمد أ"}, {"ID": 2, "Name": "محمد ب"}]
    with patch.object(agent.sql, "run_select", return_value=rows):
        agent._run_tool(
            "run_select",
            {"sql": "SELECT ID, Name FROM t.SalesPersons WHERE Name LIKE N'%محمد%'"},
            {}, {}, [], 1, "morec", state,
        )
    assert state["forced_ask"]
    assert "محمد أ" in state["forced_ask"]
    assert "محمد ب" in state["forced_ask"]


def test_sales_aggregate_does_not_set_forced_ask():
    state = {"queries": [], "question": "كم المبيعات", "last_rows": None}
    with patch.object(agent.sql, "run_select", return_value=[{"Net": 10}, {"Net": 20}]):
        agent._run_tool(
            "run_select",
            {"sql": "SELECT SUM(Net) AS Net FROM t.TransactionsHeaders"},
            {}, {}, [], 1, "morec", state,
        )
    assert "forced_ask" not in state
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `py -3.13 -m pytest -q tests/test_grounding.py::test_two_salesman_rows_list_both_names tests/test_agent.py::test_salesman_name_lookup_with_two_rows_sets_forced_ask -v`

Expected: FAIL with `ImportError` for `salesman_name_ask`, then `KeyError` or missing `forced_ask` once the import exists. Run both files again after the import is added if the first failure hides the second.

- [ ] **Step 3: Write the minimal implementation**

Append to `core/grounding.py`:

```python
def _row_name(row: dict) -> str:
    for key, value in row.items():
        if str(key).lower() == "name" and value not in (None, ""):
            return str(value)
    return ""


def salesman_name_ask(rows: list | None) -> str | None:
    if rows is None:
        return None
    if len(rows) == 0:
        return "لم أجد مندوباً بهذا الاسم. اكتب الاسم كما يظهر في قائمة المناديب."
    if len(rows) == 1:
        return None
    names = []
    for row in rows:
        if not isinstance(row, dict):
            return None
        name = _row_name(row)
        if not name:
            return None
        names.append(name)
        if len(names) == 8:
            break
    listed = "، ".join(names)
    return f"أكثر من مندوب يطابق هذا الاسم: {listed}. أيهم تقصد؟"
```

In `_run_tool`, after a business `run_select` has appended to `state["queries"]` and `result` is the row list (before `_after_business_sql` replaces it), add:

```python
        if (
            "salespersons" in sql_text.lower()
            and "like" in sql_text.lower()
            and "name" in sql_text.lower()
        ):
            ask = grounding.salesman_name_ask(result if isinstance(result, list) else None)
            if ask:
                state["forced_ask"] = ask
```

Use the raw list from `sql.run_select`, not the capped dict from `_after_business_sql`.

In `ask_stream`, after the `for tc in tool_calls` loop finishes and before the budget-warning block:

```python
        if state.get("forced_ask"):
            _turn_trace("needs_ask", param="salesman_name")
            _record_latency()
            yield {
                "type": "done", "answer": None, "needs_ask": state["forced_ask"],
                "trace_id": trace_id, "path": state.get("_path_flags"),
                "tool_names": list(state.get("tool_names") or []),
            }
            return
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `py -3.13 -m pytest -q tests/test_grounding.py tests/test_agent.py::test_salesman_name_lookup_with_two_rows_sets_forced_ask tests/test_agent.py::test_sales_aggregate_does_not_set_forced_ask tests/test_agent.py::test_query_budget_closes_after_max_queries_real_queries -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add core/grounding.py core/agent.py tests/test_grounding.py tests/test_agent.py
git commit -m "$(cat <<'EOF'
feat: ask in code when a salesman name matches zero or many rows

EOF
)"
```

---

### Task 5: A how-to with no excerpt uses a fixed refusal

**Files:**
- Modify: `core/grounding.py`
- Modify: `core/agent.py` (both places that assign the final answer before `_build_envelope`)
- Test: `tests/test_grounding.py`, `tests/test_agent.py`

**Interfaces:**
- Consumes: `state["howto_path"]` and `state["doc_source_pairs"]`.
- Produces: `HOWTO_MISS_AR = "لا يوجد في دليل المستخدم ما يغطي هذا."` and `howto_answer(howto: bool, excerpts: list, draft: str | None) -> str | None`. When `howto` is true and `excerpts` is empty, the return is `HOWTO_MISS_AR`. Otherwise the return is `draft`.

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_grounding.py`:

```python
from core.grounding import HOWTO_MISS_AR, howto_answer


def test_howto_with_no_excerpt_is_the_fixed_sentence():
    assert howto_answer(True, [], "اضغط الزر الأزرق ثم احفظ") == HOWTO_MISS_AR


def test_howto_with_an_excerpt_keeps_the_draft():
    draft = "من الدليل: خيار 157."
    assert howto_answer(True, [("guide.md", "خيارات")], draft) == draft


def test_non_howto_keeps_the_draft_even_with_no_excerpt():
    draft = "الصافي 100"
    assert howto_answer(False, [], draft) == draft
```

Append to `tests/test_agent.py`:

```python
def test_howto_turn_with_empty_docs_does_not_keep_model_prose(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    monkeypatch.setattr(trace, "TRACE_PATH", tmp_path / "trace.jsonl")
    calls = [
        _resp(_msg(tool_calls=[_tool_call("c1", "search_docs", '{"query":"زر غير موجود"}')])),
        _resp(_msg(content="اضغط الزر السري في أعلى الشاشة.")),
    ]
    with patch.object(agent.llm, "complete", side_effect=calls), \
         patch.object(agent, "_search_docs", return_value=[]):
        result = agent.ask("morec", "كيف أغيّر كلمة المرور؟", conversation={"CompanyID": 1})
    assert result["answer"] == agent.grounding.HOWTO_MISS_AR
```

`_is_howto_path` must be true for that question. It matches `كيف` plus a change verb via `_HOWTO_ACTION_RE` (`أغيّر` contains `غيّر` / the pattern `غير`). If this test fails because the router returns false, change the question to `"كيف أغير كلمة المرور؟"` (without the hyphen on ي), which matches `_HOWTO_ACTION_RE`. Do not add a new regex for "كلمة المرور".

- [ ] **Step 2: Run the tests to verify they fail**

Run: `py -3.13 -m pytest -q tests/test_grounding.py::test_howto_with_no_excerpt_is_the_fixed_sentence tests/test_agent.py::test_howto_turn_with_empty_docs_does_not_keep_model_prose -v`

Expected: FAIL. The import of `HOWTO_MISS_AR` fails first. After it exists, `ask` still returns the model sentence.

- [ ] **Step 3: Write the minimal implementation**

Append to `core/grounding.py`:

```python
HOWTO_MISS_AR = "لا يوجد في دليل المستخدم ما يغطي هذا."


def howto_answer(howto: bool, excerpts: list, draft: str | None) -> str | None:
    if howto and not excerpts:
        return HOWTO_MISS_AR
    return draft
```

In `ask_stream`, at both sites that have just finished `_resolve_final_text` / `_apply_count_backstop` and are about to call `_build_envelope`, set:

```python
        final_text = grounding.howto_answer(
            bool(state.get("howto_path")),
            state.get("doc_source_pairs") or [],
            final_text,
        )
```

Do this only on the non-cache path. A plan-cache replay is SQL, not a how-to.

- [ ] **Step 4: Run the tests to verify they pass**

Run: `py -3.13 -m pytest -q tests/test_grounding.py tests/test_agent.py::test_howto_turn_with_empty_docs_does_not_keep_model_prose tests/test_agent.py::test_search_docs_tool_never_counts_against_the_budget -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add core/grounding.py core/agent.py tests/test_grounding.py tests/test_agent.py
git commit -m "$(cat <<'EOF'
feat: refuse a how-to answer when no guide excerpt was retrieved

EOF
)"
```

---

### Task 6: Thumbs-down carries the trace id and the route

**Files:**
- Modify: `core/sessions.py` (`record_session_turn`)
- Modify: `api/server.py` (`last_turn`, the `turn_id` lookup, both `trace.log_event` calls in `feedback`)
- Test: `tests/test_feedback.py`

**Interfaces:**
- Consumes: done-event keys `trace_id`, `path`, `tool_names` from Task 2.
- Produces: transcript rows and `last_turn` store those three keys. `feedback_negative` and a new `feedback_positive` log line include `trace_id`, `path`, and `tool_names`. Thumbs-up still promotes SQL only after `gate.validate`. Thumbs-down still deletes the plan and stores the negative query.

- [ ] **Step 1: Write the failing test**

Append to `tests/test_feedback.py`:

```python
def test_thumbs_down_logs_trace_route_and_tools(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    monkeypatch.setattr(server.trace, "TRACE_PATH", tmp_path / "trace.jsonl")
    with patch.object(server.agent, "ask_stream", return_value=[{
        "type": "done", "answer": "There is 1 company.", "needs_ask": None,
        "answer_sql": "SELECT COUNT(*) FROM t.Companies",
        "cache_key": "key-for-route1",
        "trace_id": "trace-route-1",
        "path": "fc1,ht0,rp0,an0",
        "tool_names": ["run_metric"],
    }]):
        resp = client.post("/ask", json={"question": "how many companies?", "session_id": "route1"},
                            headers={"X-Session-Id": "route1"})
        assert resp.status_code == 200
        list(resp.iter_lines())
    resp = client.post("/feedback", json={"session_id": "route1", "helpful": False, "reason": "wrong"},
                        headers={"X-Session-Id": "route1"})
    assert resp.status_code == 200
    lines = [
        __import__("json").loads(line)
        for line in (tmp_path / "trace.jsonl").read_text(encoding="utf-8").splitlines()
    ]
    negative = [row for row in lines if row.get("event") == "feedback_negative"]
    assert len(negative) == 1
    assert negative[0]["trace_id"] == "trace-route-1"
    assert negative[0]["path"] == "fc1,ht0,rp0,an0"
    assert negative[0]["tool_names"] == ["run_metric"]
    assert negative[0]["reason"] == "wrong"
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `py -3.13 -m pytest -q tests/test_feedback.py::test_thumbs_down_logs_trace_route_and_tools -v`

Expected: FAIL. The log line has no `trace_id` (`KeyError`).

- [ ] **Step 3: Write the minimal implementation**

In `record_session_turn`, add three keys to the transcript dict:

```python
        "trace_id": result.get("trace_id"),
        "path": result.get("path"),
        "tool_names": list(result.get("tool_names") or []),
```

In `api/server.py`, extend `last_turn`:

```python
                session["last_turn"] = {
                    "client": client,
                    "company_id": cid,
                    "question": req.question,
                    "answer_sql": result.get("answer_sql"),
                    "cache_key": result.get("cache_key"),
                    "turn_id": turn_id,
                    "trace_id": result.get("trace_id"),
                    "path": result.get("path"),
                    "tool_names": list(result.get("tool_names") or []),
                }
```

In the `turn_id` lookup inside `feedback`, add the same three keys from `row`:

```python
                turn = {
                    "client": row.get("client") or client,
                    "company_id": row.get("company_id"),
                    "question": row["q"],
                    "answer_sql": row.get("sql"),
                    "cache_key": row.get("cache_key"),
                    "trace_id": row.get("trace_id"),
                    "path": row.get("path"),
                    "tool_names": list(row.get("tool_names") or []),
                }
```

Replace the two `trace.log_event` calls in `feedback` with helpers that always pass the route fields.

On invalid SQL (the existing `feedback_invalid_sql` line), add the same three fields plus keep the event name.

On successful thumbs-up, after `promote_verified_query`, add:

```python
                trace.log_event(
                    client, turn["question"], event="feedback_positive", subject=subject,
                    trace_id=turn.get("trace_id"), path=turn.get("path"),
                    tool_names=turn.get("tool_names") or [],
                )
```

On thumbs-down, change the existing call to:

```python
        trace.log_event(
            client, turn["question"], event="feedback_negative", subject=subject,
            trace_id=turn.get("trace_id"), path=turn.get("path"),
            tool_names=turn.get("tool_names") or [], reason=req.reason,
        )
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `py -3.13 -m pytest -q tests/test_feedback.py -v`

Expected: PASS, including the older promote and 404 tests.

- [ ] **Step 5: Commit**

```bash
git add core/sessions.py api/server.py tests/test_feedback.py
git commit -m "$(cat <<'EOF'
feat: attach trace id and route flags to feedback

EOF
)"
```

---

### Task 7: Score the path without calling the model

**Files:**
- Create: `evals/score_path.py`
- Test: `tests/test_score_path.py`

**Interfaces:**
- Consumes: span dicts from Task 2. A tool span has `name == "tool"`, `tool`, and `status`.
- Produces: `score_path(spans: list[dict], *, max_queries: int = 4) -> dict` with keys `tool_names: list[str]`, `tool_error_count: int`, `business_queries: int`, `over_budget: bool`, `first_business_tool: str | None`, `gears: list[str]`, `path_ok: bool`. `path_ok` is false when any tool span has `status == "error"`, when business tools (`run_select`, `run_metric`, `run_report`) exceed `max_queries`, or when more than one distinct `gear` appears on `name == "llm"` spans. `budget_spent` is not an error. This function does not read files and does not open a network connection.

- [ ] **Step 1: Write the failing test**

Create `tests/test_score_path.py`:

```python
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from evals.score_path import score_path


def test_clean_metric_path_is_ok():
    spans = [
        {"kind": "span", "name": "llm", "gear": "t1"},
        {"kind": "span", "name": "tool", "tool": "run_metric", "status": "ok"},
        {"kind": "span", "name": "llm", "gear": "t1"},
    ]
    scored = score_path(spans)
    assert scored["path_ok"] is True
    assert scored["first_business_tool"] == "run_metric"
    assert scored["tool_error_count"] == 0
    assert scored["gears"] == ["t1"]


def test_grain_error_then_a_good_answer_is_not_a_clean_path():
    """Shape of golden last_month_summary on 10 Nov 2026: the answer passed,
    and run_select had already been rejected for invoice grain."""
    spans = [
        {"kind": "span", "name": "llm", "gear": "t1"},
        {"kind": "span", "name": "tool", "tool": "run_select", "status": "error"},
        {"kind": "span", "name": "llm", "gear": "t2"},
        {"kind": "span", "name": "tool", "tool": "run_metric", "status": "ok"},
    ]
    scored = score_path(spans)
    assert scored["path_ok"] is False
    assert scored["tool_error_count"] == 1
    assert scored["first_business_tool"] == "run_select"
    assert scored["gears"] == ["t1", "t2"]


def test_budget_spent_is_not_an_error_and_does_not_count_as_a_query():
    spans = [
        {"kind": "span", "name": "tool", "tool": "run_select", "status": "ok"},
        {"kind": "span", "name": "tool", "tool": "run_select", "status": "budget_spent"},
    ]
    scored = score_path(spans, max_queries=4)
    assert scored["business_queries"] == 1
    assert scored["over_budget"] is False
    assert scored["path_ok"] is True


def test_five_business_tools_are_over_budget():
    spans = [
        {"kind": "span", "name": "tool", "tool": "run_select", "status": "ok"}
        for _ in range(5)
    ]
    scored = score_path(spans, max_queries=4)
    assert scored["over_budget"] is True
    assert scored["path_ok"] is False
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `py -3.13 -m pytest -q tests/test_score_path.py -v`

Expected: FAIL with `ModuleNotFoundError: No module named 'evals.score_path'`

- [ ] **Step 3: Write the minimal implementation**

Create `evals/score_path.py`:

```python
"""Grade a turn from span dicts. No model, no database, no trace file."""
from __future__ import annotations

_BUSINESS = frozenset({"run_select", "run_metric", "run_report"})


def score_path(spans: list[dict], *, max_queries: int = 4) -> dict:
    tool_names: list[str] = []
    errors = 0
    business = 0
    first: str | None = None
    gears: list[str] = []
    for span in spans or []:
        if span.get("name") == "llm":
            gear = span.get("gear")
            if gear and gear not in gears:
                gears.append(gear)
        if span.get("name") != "tool":
            continue
        tool = span.get("tool") or ""
        tool_names.append(tool)
        status = span.get("status")
        if status == "error":
            errors += 1
        if tool in _BUSINESS and status == "ok":
            business += 1
            if first is None:
                first = tool
    over = business > max_queries
    gear_changed = len(gears) > 1
    return {
        "tool_names": tool_names,
        "tool_error_count": errors,
        "business_queries": business,
        "over_budget": over,
        "first_business_tool": first,
        "gears": gears,
        "path_ok": errors == 0 and not over and not gear_changed,
    }
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `py -3.13 -m pytest -q tests/test_score_path.py tests/test_trace_usage.py tests/test_grounding.py tests/test_feedback.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add evals/score_path.py tests/test_score_path.py
git commit -m "$(cat <<'EOF'
feat: score a turn path from spans without calling the model

EOF
)"
```

---

## What this plan deliberately does not do

- Install LangChain, LangGraph, LangSmith, Langfuse, LangFlow, or LangExtract.
- Retrieve a different schema per question. The full `t.` schema stays in the stable prefix.
- Add embeddings. Docs stay on FTS5 until a counted set of how-to misses exists.
- Approve SQL before it runs. p50 is already 12.2 seconds.
- Store graph checkpoints or resume a cancelled turn.
- Rebuild the query-budget stop. It already returns `budget_spent`.
- Run the live golden or held-out suites. One case on the golden six is 17 points. One case on the held-out eight is 12.5 points. A live run is an owner checkpoint after Task 7, with the command `py -3.13 evals/run_golden_session.py`, and it is not part of the task commits above.

## Drawbacks the implementer must not "fix" by expanding scope

- Trace file grows from 1 line per turn to about 1 turn line plus 1 line per model call and per tool. At 3.67 model calls and a couple of tools, expect roughly 6 lines per question, about 6× the current file. Spans omit the question text on purpose.
- `grounded_confidence` ignores 4-digit years and any number that already appears in the question. A wrong year the user did not type can still look grounded. A rounded number the rows do not contain (`15.4` vs `15.36`) correctly lowers confidence; do not add a tolerance in this plan.
- `salesman_name_ask` fires only on `SalesPersons` + `LIKE` + `Name`. A lookup written with `=` or a different column will not interrupt. That is the bound. Do not scan every result set for Arabic names.
- `howto_answer` replaces the whole draft when the how-to route retrieved nothing. A mixed question that the router classified as how-to will not get a SQL answer on that turn. The router already returns false when the question has a count or a metric. Do not special-case one screen.
- `path_ok` is false when the gear changes, including a justified t1→t2 escalation. That is the signal, not a bug. Do not make `path_ok` follow the answer grade.
- `score_path` is not wired into `run_golden_session.py` in this plan. Wiring it into a paid run is a later change after these tests are green.

## Self-review

Spec coverage: span log (Tasks 1–2), path grade (Task 7), number audit (Task 3), code-level name interrupt (Task 4), how-to cite-or-refuse (Task 5), feedback joined to route (Task 6). Libraries stay out (Global Constraints and the "does not do" section). The 10 Nov counts are in the evidence table. The already-shipped budget stop is named so Task 2 does not rebuild it.

Placeholder scan: every task has a failing test, a command, the implementation, and a commit. No step says "handle edge cases" without code.

Type consistency: `log_span(client, trace_id, span_id, parent_id, name, **fields)`, `prompt_file_hashes()`, `figures_outside_rows`, `grounded_confidence`, `salesman_name_ask`, `howto_answer`, `HOWTO_MISS_AR`, `score_path`, done-event keys `trace_id` / `path` / `tool_names`. Task 6 reads the keys Task 2 writes. Task 7 reads the span `name` / `tool` / `status` / `gear` fields Task 2 writes.
