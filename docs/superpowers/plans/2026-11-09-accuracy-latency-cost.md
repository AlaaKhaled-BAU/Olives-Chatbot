# Chatbot Accuracy, Latency and Cost Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix the root causes found in the 2026-11-09 six-question session so answers are more accurate, faster and cheaper — with a measured, per-case guarantee that nothing that was right before becomes wrong.

**Architecture:** Measure first (golden session eval with live reference SQL, plus cost/latency from `work/trace.jsonl`), then ship small single-cause fixes, each behind its own unit test and re-measured against the golden set and the existing eval suites. Behaviour changes whose effect on accuracy is uncertain ship behind an env flag and are flipped only after an A/B run is not worse.

**Tech Stack:** Python 3.13 (`py -3.13` on Windows), FastAPI, sqlglot, pymssql, DeepSeek (`deepseek-flash` via OpenAI SDK), pytest.

## Global Constraints

- Python 3.13 only (`py -3.13 -m pytest …`); never `python3`.
- Never use SA or IIS `cds` from the running app — only `chatbot_ro` + `t.` views + `SESSION_CONTEXT` (AGENTS.md rule 2). **Waived for this branch by the product owner (2026-11-09):** the existing local `cds` runtime override and the `t.` → `dbo.` fallback stay unchanged; no task may add new connection paths or credentials.
- One SQL path: `core/sql.py` + `core/gate.py`. Do not bypass the gate.
- After query results enter model context, no more tool calls (AGENTS.md rule 9).
- Cache keys include client + CompanyID.
- Never return procedure bodies.
- "Better, not worse": a change is merged only if (a) unit tests are green, (b) every golden case that passed at baseline still passes, (c) `evals/run_evals.py` accuracy is ≥ baseline and isolation stays 100%.
- Baseline at plan time: `py -3.13 -m pytest -q tests/test_metrics.py tests/test_gate.py tests/test_agent.py tests/test_thread.py tests/test_llm.py tests/test_trace_usage.py` → **155 passed**.

---

## Investigation findings (why each task exists)

Evidence: `work/manual_eval.json` (answers + SQL), `work/session_trace.json` (per-turn trace), server log `[llm]` lines, read-only replays in `work/review_verify.py`, `work/_replay_q3.py`.

| # | Symptom | Root cause (confirmed unless marked) | Task |
|---|---|---|---|
| 1 | Q1 named the wrong best rep (Hamzawi 17,158.83; truth Jamil 15,355.23) and contradicted Q5 | `run_metric` tool schema says `to_date` is **half-open** (`core/agent.py:769`), but `metrics._invoice_date_filters` / `_order_date_filters` emit `<=` (`core/metrics.py:144,158`). The model correctly passed `to_date=2026-11-01` → Nov 1 included (7 invoices). The `sales` metric uses `<` (`_sales_half_open_dates`), so the same month gives two answers. The wrong SQL is also stored in plan cache. | 3 |
| 2 | Q2/Q3/Q5 appended "count is lines, not invoices" although counts were real header counts | `verify._count_kind_for_select` returns `"lines"` for any COUNT in a SELECT that joins a detail table, even `COUNT(DISTINCT CASE … th.TransactionNo END)` (verified: `count_scopes(build_sales_sql(...))` → `lines`). `_apply_count_backstop` then appends `COUNT_NOTE_USER`. | 4 |
| 3 | Q4 said "9 invoices" (9 lines; 5 headers) and the warning did NOT fire | `_LINES_WORD_RE` matched the word «البنود» inside a pasted SQL comment, so the backstop skipped. SQL was in the answer because `prompts/system.md:210` says "SQL is shown to the user after your answer" and the non-thinking f0 gear echoed it. | 4, 5 |
| 4 | Q4 ran entirely on f0 (no thinking), skipped vault cards | `_is_fast_count_path` fires on «كم» + master term «عميل», so a multi-part analytic question was treated as a count-only lookup (`path=fc1`). | 10 |
| 5 | Q6 (how-to) ran the full SQL agent, 3 calls, 18 s; template follow-ups about tax/period | `_is_howto_path` returns False because `metrics.question_mentions_metric` matches alias «طلبات». Follow-ups come from `thread.card_followups(thread_head)` with a card *inherited* from Q5. | 10, 11 |
| 6 | "running query 5 of 4" | Budget is checked only when building the tool list per model turn (`_active_tools`), but one model turn can emit several parallel tool calls. | 7 |
| 7 | Confidence "high" on wrong Q1, "medium" on correct Q5 | `_final_contract` is an f0 call that sees only question + draft text, no data. It also adds one serial LLM call (2.6–5.2 s) after the answer, and its follow-ups are discarded whenever a thread card exists. | 11 |
| 8 | ~86 % of spend came from 10 calls that re-sent 33k–65k uncached tokens | DeepSeek prefix cache breaks right after the first system message (~6.8k tokens = 24,827 chars of system.md+playbook) whenever the **tool list changes** between calls (`_active_tools` drops `recall_turns` after rows, drops `search_docs` at cap, returns `None` at query cap), and resets to 0 when the **gear/thinking mode changes** (t1→t2 escalation in Q3; f0 start in Q4). Every big miss in the log lines up with one of these. | 8, 9 |
| 9 | Q3 said it "couldn't extract" the list although its last query returned exactly the right 10 rows | All four Q3 statements pass the gate and run today (replayed). A different tool call errored (it triggered t1→t2 escalation) but tool errors are not traced, so the exact error is **unconfirmed**. The final call ran with `tools=None` + "This is your last query" nudge. | 1, 12 |
| 10 | Gate injected `LogActionTransaction.CompNo = 1` into the outer query of a derived table → SQL error | `gate._tables_in_from` walks into subqueries in FROM, so inner tables get predicates on the outer SELECT. Reproduced in `work/_replay_q3.txt`. | 6 |
| 11 | Runtime connected as `cds`, DB has no `t.` schema | Saved operator override (`core/dblink`) = `cds`@`Olives_BO`; `sql.run_select` silently rewrites `t.` → `dbo.`. Gate predicates kept company 1 isolated in this run, but the server-side wall and read-only login are absent. | 13 |
| 12 | Log shows `model=?` | `llm._log_usage` reads `usage.model`, which DeepSeek usage objects don't carry. | 1 |
| 13 | Best-rep metric used a correlated subquery per salesperson (1.5 s) | `metrics.build_sql("net_sales_by_salesperson")` | 3 |
| 14 | Top/bottom items picked from a partial list | `sales` grouped by item has no ORDER BY/TOP: ~245 rows, gate cap 200, model sees 50 (`_ROW_DISPLAY_CAP`). | 14 |

Business decisions (product owner, 2026-11-09): "best rep" = invoiced sales (unchanged); "lowest-selling items" = both the lowest sold items and the never-sold count (Task 14).

## Plan revision R1 (2026-11-09, product owner review) — generalize, don't fit the six questions

Self-audit after Task 2: several planned fixes were *static* (keyword lists and tests copied from the six session questions) instead of *directions* that make the model handle any phrasing. Rules from now on, binding on every task:

1. **Directions over data.** A fix teaches the model or the router a general rule (definition, grammar, structure). No fix may add a word list or alias whose only justification is one of the six golden questions.
2. **No test may use a golden question verbatim as its only case.** Router/classifier tests are tables of ≥6 varied phrasings (MSA, Levantine/Gulf dialect, typos without spaces, English), positives and negatives.
3. **Held-out set.** Generalization is measured on `evals/heldout_105.jsonl` (Task 2c) — different questions, dimensions and wording than the golden six. A change must not lower held-out accuracy.
4. **Determinism.** Non-thinking calls run at `temperature=0` (Task 2b). Thinking gears ignore sampling params, so consistency comes from structure: deterministic metric tools for ranked/aggregate questions, one fixed definition per business term (Task 3b), stable gear per turn (Task 9).
5. **Eval spend.** Per task: unit tests only — no live API calls. Live golden + held-out runs happen only at checkpoints: **C1** after Task 6, **C2** after Task 11, **C3** final (Task 15). `evals/run_evals.py` runs only at C3. Every "Golden `--baseline` → exit 0" / "run_evals" line inside a task below is replaced by this checkpoint rule.

Task order: 1, 2, 2b, 2c, 3, 3b, 4, 5, 6, **C1**, 7, 8, 9, 10, 11, **C2**, 12, 14, 15 (**C3**). Task 13 skipped.

---

### Task 2b: Deterministic sampling for non-thinking calls

**Files:** Modify `core/llm.py` (`stream_create_kwargs`); Test `tests/test_llm.py`.

- [ ] **Step 1: Failing tests**

```python
def test_non_thinking_gear_is_greedy():
    kw = llm.stream_create_kwargs(llm.gear_cfg("f0"), [{"role": "user", "content": "x"}])
    assert kw["temperature"] == 0


def test_thinking_gear_sends_no_sampling_params():
    kw = llm.stream_create_kwargs(llm.gear_cfg("t1"), [{"role": "user", "content": "x"}])
    assert "temperature" not in kw and "top_p" not in kw
```

(Use whatever the existing per-gear config accessor in `core/llm.py` is called — the function around line 94 documented "Per-request gear config"; adapt the test to its real name.)

- [ ] **Step 2:** run → first FAILS.
- [ ] **Step 3: Implement** in `stream_create_kwargs`, after building `kwargs`:

```python
    if not cfg["thinking"]:
        kwargs["temperature"] = 0
```

- [ ] **Step 4:** `py -3.13 -m pytest -q tests/test_llm.py tests/test_agent.py` → PASS. Commit `feat(llm): temperature 0 on non-thinking gears`.

---

### Task 2c: Held-out generalization set (generic, data-relative checks)

**Files:** Create `evals/heldout_105.jsonl`; Modify `evals/run_golden_session.py`; Test `tests/test_evals.py`.

Each held-out case is asked in a **fresh session** and carries its own reference SQL and expectations, so the runner stays generic (no per-question Python).

Case schema: `{"name", "question", "ref_sql", "expect": [..]}`. `ref_sql` may use `{f}` / `{t}` (last-month half-open bounds from `_last_month()`), `{JOIN}`, `{NET}`, `{W}` (type-1 non-void invoice filter for the period, as in `references()`). `expect` items, evaluated on the reference rows `R` (ordered as the SQL returns them):
- `"name:COL"` → `str(R[0][COL]).strip()` appears in the answer.
- `"amount:COL"` → `amount_matches(float(R[0][COL]), answer)`.
- `"int:COL"` → `str(int(R[0][COL]))` in `num_tokens(answer)`.
- `"rows:N:COL"` → at least `ceil(N/2)` of `str(R[i][COL]).strip()` for `i < N` appear in the answer.
A case passes iff every expectation holds and the answer has no code fence.

- [ ] **Step 1: Failing tests** — `expect_holds(expect: list[str], rows: list[dict], answer: str) -> bool` with table cases: name+amount true/false (rounded amount false), `int` whole-token (381 vs 13810), `rows:5:name` with 3 of 5 present true / 2 of 5 false, unknown expect kind raises `ValueError`.
- [ ] **Step 2:** run → FAIL (function missing).
- [ ] **Step 3: Implement** `expect_holds`, `load_cases(path)`, `render_ref_sql(text, f, t)`, and CLI `--cases PATH` (default `evals/golden_session_105.jsonl`). A case with `ref_sql` uses `expect_holds` and a fresh `session_id`; cases without it keep the existing `check()` path and the shared session. Results file stem follows the cases file stem. `--baseline` / `--rescore` work for both sets.
- [ ] **Step 4: Case file** `evals/heldout_105.jsonl` (none of these phrasings appear in the golden set):

```json
{"name": "top_customer", "question": "مين أفضل زبون عندي الشهر الماضي من حيث المبيعات؟", "ref_sql": "SELECT TOP 5 c.Name AS name, SUM({NET}) AS net {JOIN} JOIN t.Customers c ON c.CustomerID = th.CustomerID AND c.CompanyID = th.CompanyID WHERE {W} GROUP BY c.Name ORDER BY net DESC", "expect": ["name:name", "amount:net"]}
{"name": "weakest_rep", "question": "مين أضعف مندوب مبيعات بالشهر الفائت؟", "ref_sql": "SELECT sp.Name AS name, SUM({NET}) AS net {JOIN} JOIN t.SalesPersons sp ON sp.ID = th.SalesPersonID AND sp.CompanyID = th.CompanyID WHERE {W} GROUP BY sp.Name ORDER BY net ASC", "expect": ["name:name", "amount:net"]}
{"name": "top5_customers_en", "question": "Top 5 customers by sales last month", "ref_sql": "SELECT TOP 5 c.Name AS name, SUM({NET}) AS net {JOIN} JOIN t.Customers c ON c.CustomerID = th.CustomerID AND c.CompanyID = th.CompanyID WHERE {W} GROUP BY c.Name ORDER BY net DESC", "expect": ["rows:5:name"]}
{"name": "invoice_count", "question": "كم فاتورة بيع طلعنا الشهر اللي فات؟", "ref_sql": "SELECT COUNT(*) AS inv FROM t.TransactionsHeaders th WHERE {W}", "expect": ["int:inv"]}
{"name": "rep_most_invoices", "question": "اي مندوب عمل اكبر عدد فواتير الشهر الماضي", "ref_sql": "SELECT TOP 3 sp.Name AS name, COUNT(*) AS inv FROM t.TransactionsHeaders th JOIN t.SalesPersons sp ON sp.ID = th.SalesPersonID AND sp.CompanyID = th.CompanyID WHERE {W} GROUP BY sp.Name ORDER BY inv DESC", "expect": ["name:name", "int:inv"]}
{"name": "best_day", "question": "شو كان أعلى يوم مبيعات بالشهر الماضي وقديش بعنا فيه؟", "ref_sql": "SELECT TOP 3 th.TransactionDate AS d, SUM({NET}) AS net {JOIN} WHERE {W} GROUP BY th.TransactionDate ORDER BY net DESC", "expect": ["amount:net"]}
{"name": "buying_customers", "question": "كم زبون اشترى مني الشهر الماضي؟", "ref_sql": "SELECT COUNT(DISTINCT th.CustomerID) AS custs FROM t.TransactionsHeaders th WHERE {W}", "expect": ["int:custs"]}
{"name": "worst5_items_en", "question": "What were my 5 worst selling items last month?", "ref_sql": "SELECT TOP 5 td.ItemCode AS code, SUM({NET}) AS net {JOIN} WHERE {W} GROUP BY td.ItemCode ORDER BY net ASC", "expect": ["rows:5:code"]}
```

(Verify each `ref_sql` runs through `sql.run_select` for client 105 / company 1 and returns rows — read-only, no API spend — and fix column/join names to the real schema if one errors. `TransactionsHeaders` alias `th` is required because `{W}` uses it.)

- [ ] **Step 5:** unit tests green; commit `test(evals): held-out generalization set with generic expectations`. Then the controller restarts the API on this commit and records the held-out **baseline** once (`--cases evals/heldout_105.jsonl`).

---

### Task 3b: One business definition per term (directions in the system prompt)

Root cause (baseline evidence): `prompts/system.md:75` tells the model to "state both invoiced sales and booked sales orders" when the tenant type is unspecified. The model then summed them (681,501 = 57,252 invoices + 624,249 orders), and ranked salesmen by orders — so "best rep", "summary" and "top item" answers varied run to run and did not lead with the invoiced figure the product owner defined.

**Files:** Modify `prompts/system.md:68-75`; Test `tests/test_agent.py` (prompt-content assertions only).

- [ ] **Step 1: Failing test**

```python
def test_system_prompt_fixes_sales_basis_and_ranking_rules():
    text = (BASE_DIR / "prompts" / "system.md").read_text(encoding="utf-8")
    assert "Never add invoice and order amounts together" in text
    assert "Primary basis" in text
    assert "Ranking rule" in text
```

(`BASE_DIR` = repo root, as already used in tests; adapt to the existing helper.)

- [ ] **Step 2:** FAIL. **Step 3:** replace the `مبيعات (Sales)` bullet block (lines 71-75) with:

```markdown
  - **مبيعات / sales / بيع (any phrasing: best, worst, total, summary, by item/customer/rep/day)**:
    - **Primary basis** = invoiced sales: `TransactionTypeID = 1`, non-void, net of returns when returns exist. Lead every sales answer with this figure.
    - Booked orders (`OrdersHeaders`, `WFApproved = 1`, non-void) are a **separate, secondary** line, labelled «طلبات محجوزة», only when they add context (e.g. a rep with orders but no invoices). **Never add invoice and order amounts together** and never rank by a mix of both.
    - Every sales answer states its basis and exact period in one line (e.g. «على أساس الفواتير، 2026-10-01 إلى 2026-10-31»).
  - **Ranking rule** (best/worst/top/bottom/أفضل/أضعف/أقل/أكثر over any dimension): use `run_metric` `sales` with `group_by` + `order` + `limit` so the database ranks; never rank from an unordered or truncated row list. For worst/bottom items also report how many active items had **no** sales in the period (`unsold_items`). Quote amounts with 2 decimals.
```

(The `order`/`limit` filters and `unsold_items` arrive in Task 14; until then the ranking rule degrades gracefully because `run_select` with `ORDER BY`/`TOP` is still allowed.)

- [ ] **Step 4:** `py -3.13 -m pytest -q tests/test_agent.py` → PASS. Commit `fix(prompt): single sales basis, never mix invoices and orders, general ranking rule`. (The system prompt is in the cached prefix; this re-warms the cache once.)

---

## Checkpoint C1 (after Task 6) — live, ~$0.25

Run once each, with the API restarted on the branch head: `py -3.13 evals/run_golden_session.py --baseline <golden baseline>` and `py -3.13 evals/run_golden_session.py --cases evals/heldout_105.jsonl --baseline <heldout baseline>`. The held-out baseline is recorded once right after Task 2c (API restarted on the Task 2c commit, ~$0.15), before any Task 3 code is live. Gate: no REGRESSED case in either set.

## Checkpoint C2 (after Task 11) — same commands, same gate.

---

## File map

| File | Change |
|---|---|
| `core/llm.py` | model name in usage log; optional `tool_choice` passthrough |
| `core/agent.py` | tool-error trace, hard query budget, stable per-turn tool list, mid-turn escalation flag, router fixes, SQL-fence stripping, backstop on prose only, envelope/contract changes, failure-claim recompose |
| `core/metrics.py` | half-open dates everywhere; single-join best-rep SQL |
| `core/verify.py` | DISTINCT header key counts classified as header |
| `core/gate.py` | `_tables_in_from` scoped to its own SELECT |
| `core/sql.py` | fail closed without `t.` views |
| `prompts/system.md` | never put SQL in the answer text |
| `evals/golden_session_105.jsonl`, `evals/run_golden_session.py` | new golden session eval with live reference SQL + cost/latency |
| `tests/test_*.py` | one focused test per fix |

---

### Task 1: Observability — model name and tool errors in the trace

**Files:**
- Modify: `core/llm.py:120-130` (`_log_usage`), `core/llm.py:195-200,226-239` (callers)
- Modify: `core/agent.py:2110-2127` (tool error handling), `core/agent.py:2026-2037` (`_turn_trace`), `core/agent.py:1987` (state init)
- Test: `tests/test_trace_usage.py`, `tests/test_agent.py`

**Interfaces:**
- Produces: `state["tool_errors"]: list[dict]` with keys `tool`, `error` (≤300 chars); trace field `tool_errors`. `llm._log_usage(gear, usage, elapsed_s, model="")`.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_trace_usage.py
def test_log_usage_prints_model_name(capsys):
    from types import SimpleNamespace
    from core import llm
    u = SimpleNamespace(prompt_tokens=10, completion_tokens=2,
                        prompt_cache_hit_tokens=8, prompt_cache_miss_tokens=2)
    llm._log_usage("t1", u, 0.5, model="deepseek-flash")
    assert "model=deepseek-flash" in capsys.readouterr().out
```

```python
# tests/test_agent.py
def test_tool_errors_are_written_to_the_trace(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    logged = {}
    monkeypatch.setattr(agent.trace, "log_event",
                        lambda *a, **kw: logged.update(kw))
    calls = [
        _resp(_msg(tool_calls=[_tool_call("c1", "run_select", '{"sql": "SELECT 1 FROM t.Nope"}')])),
        _resp(_msg(content="لا توجد بيانات")),
    ]
    with patch.object(agent.llm, "complete", side_effect=calls + [_plain_resp("{}")]), \
         patch.object(agent.sql, "run_select", side_effect=RuntimeError("Invalid object name")):
        agent.ask("morec", "كم عدد الأصناف المباعة أمس؟", conversation=dict(SCOPE))
    assert logged["tool_errors"][0]["tool"] == "run_select"
    assert "Invalid object name" in logged["tool_errors"][0]["error"]
```

- [ ] **Step 2: Run to verify they fail**

Run: `py -3.13 -m pytest -q tests/test_trace_usage.py::test_log_usage_prints_model_name tests/test_agent.py::test_tool_errors_are_written_to_the_trace`
Expected: FAIL (`TypeError: _log_usage() got an unexpected keyword argument 'model'`; `KeyError: 'tool_errors'`).

- [ ] **Step 3: Implement**

`core/llm.py`:

```python
def _log_usage(gear: str, usage, elapsed_s: float, model: str = "") -> None:
    if usage is None:
        return
    hit = getattr(usage, "prompt_cache_hit_tokens", None)
    miss = getattr(usage, "prompt_cache_miss_tokens", None)
    print(
        f"[llm] gear={gear} model={model or getattr(usage, 'model', '?')} "
        f"in={getattr(usage, 'prompt_tokens', '?')} out={getattr(usage, 'completion_tokens', '?')} "
        f"cache_hit={hit} cache_miss={miss} {elapsed_s:.1f}s",
        flush=True,
    )
```

Pass `model=cfg["model"]` at `core/llm.py:198` and `model=model` in `_logged_stream` (`core/llm.py:237`).

`core/agent.py` — add `"tool_errors": [],` to the `state` dict (next to `"gate_errors": 0`). In the tool loop, right after `if isinstance(result, dict) and result.get("error"):` add:

```python
                state["tool_errors"].append({"tool": name, "error": str(result["error"])[:300]})
```

In `_turn_trace`, add `tool_errors=state.get("tool_errors") or [],` to the `trace.log_event(...)` call.

- [ ] **Step 4: Run to verify they pass, then the touched suites**

Run: `py -3.13 -m pytest -q tests/test_trace_usage.py tests/test_agent.py tests/test_llm.py`
Expected: all PASS.

- [ ] **Step 5: Commit**

```bash
git add core/llm.py core/agent.py tests/test_trace_usage.py tests/test_agent.py
git commit -m "feat(trace): log model name and per-turn tool errors"
```

---

### Task 2: Golden session eval with live reference SQL, cost and latency

**Files:**
- Create: `evals/golden_session_105.jsonl`
- Create: `evals/run_golden_session.py`
- Test: `tests/test_evals.py`

**Interfaces:**
- Consumes: running API on `http://127.0.0.1:8100` (`./run.ps1`), `work/trace.jsonl` per-turn records (fields `question`, `ts`, `latency_ms`, `calls[]` with `prompt`, `completion`, `cache_hit`, `cache_miss`).
- Produces: `evals/golden_session_105_results_<UTC>.json` with per-case `pass`, `latency_ms`, `llm_calls`, `usd_offpeak`, `usd_peak`, and a summary; helpers `number_variants(x: float) -> set[str]`, `cost_usd(call: dict, rates: dict) -> float`.

Reference values are computed live at run time (data-relative "last month" = month before the month of the latest invoice), so the eval stays valid when data changes.

- [ ] **Step 1: Write the failing unit tests for the pure helpers**

```python
# tests/test_evals.py
def test_number_variants_cover_comma_and_plain_forms():
    from evals.run_golden_session import number_variants
    v = number_variants(15355.228256)
    assert "15,355.23" in v and "15355.23" in v and "15,355" in v


def test_cost_usd_offpeak_matches_published_flash_rates():
    from evals.run_golden_session import cost_usd, OFFPEAK
    call = {"cache_hit": 1_000_000, "cache_miss": 1_000_000, "completion": 1_000_000}
    assert round(cost_usd(call, OFFPEAK), 6) == round(0.003 + 0.15 + 0.60, 6)
```

- [ ] **Step 2: Run to verify they fail**

Run: `py -3.13 -m pytest -q tests/test_evals.py -k "number_variants or cost_usd"`
Expected: FAIL with `ModuleNotFoundError: No module named 'evals.run_golden_session'`.

- [ ] **Step 3: Create the case file**

`evals/golden_session_105.jsonl` (one chat session, in order):

```json
{"name": "best_rep_last_month", "question": "اعطيني احسن منجوب عدي اخر شهر", "check": "top_rep"}
{"name": "top_item", "question": "اعطيني احسنمادةمبيعا", "check": "top_item"}
{"name": "bottom10_items_plan", "question": "اعطيني اقل 10 مواد بيع عندي واعطيني خطة للتحسين", "check": "bottom10"}
{"name": "best_rep_visits", "question": "شوفلي زيارات احسنمنجوب عندي،كم عميل زار في اخريومعملله،كم عميل باع منهم", "check": "visits"}
{"name": "last_month_summary", "question": "اعطيني ملخص مبيعات الشهر الماضي مع خطة للتحسين", "check": "summary"}
{"name": "howto_invoice_to_orders", "question": "كيف اغير المندوبمن عمل فواتير الى طلبات بيع ؟", "check": "howto"}
```

- [ ] **Step 4: Create the runner**

`evals/run_golden_session.py`:

```python
#!/usr/bin/env python3.13
"""Golden one-session eval for client 105 / CompanyID 1. Reference values
come from live SQL through core.sql.run_select (same gate as the bot), so
expectations follow the data. Requires the API running on :8100."""
import argparse
import json
import sys
import time
import urllib.request
import uuid
from datetime import date, datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from core import metrics, sql  # noqa: E402

CLIENT, COMPANY = "105", 1
TRACE = BASE_DIR / "work" / "trace.jsonl"
OFFPEAK = {"hit": 0.003, "miss": 0.15, "out": 0.60}   # USD per 1M, deepseek-flash
PEAK = {"hit": 0.006, "miss": 0.30, "out": 1.20}
NET = metrics.line_amount_sql("td")
JOIN = ("FROM t.TransactionsHeaders th JOIN t.TransactionsDetails td ON th.CompanyID = td.CompanyID "
        "AND th.TransactionTypeID = td.TransactionTypeID AND th.TransactionYear = td.TransactionYear "
        "AND th.TransactionNo = td.TransactionNo")


def number_variants(x: float) -> set[str]:
    return {f"{x:,.2f}", f"{x:.2f}", f"{round(x):,}", str(round(x))}


def cost_usd(call: dict, rates: dict) -> float:
    return ((call.get("cache_hit") or 0) * rates["hit"]
            + (call.get("cache_miss") or 0) * rates["miss"]
            + (call.get("completion") or 0) * rates["out"]) / 1e6


def _q(text: str) -> list[dict]:
    return sql.run_select(text, company_id=COMPANY, client=CLIENT)


def _last_month() -> tuple[str, str]:
    mx = _q("SELECT MAX(TransactionDate) AS mx FROM t.TransactionsHeaders "
            "WHERE TransactionTypeID = 1 AND ISNULL(IsVoid, 0) = 0")[0]["mx"]
    first_cur = date(mx.year, mx.month, 1)
    prev = date(first_cur.year - (first_cur.month == 1), (first_cur.month - 2) % 12 + 1, 1)
    return prev.isoformat(), first_cur.isoformat()


def references() -> dict:
    f, t = _last_month()
    W = f"th.TransactionTypeID = 1 AND ISNULL(th.IsVoid, 0) = 0 AND th.TransactionDate >= '{f}' AND th.TransactionDate < '{t}'"
    reps = _q(f"SELECT th.SalesPersonID AS id, sp.Name AS name, SUM({NET}) AS net {JOIN} "
              f"JOIN t.SalesPersons sp ON sp.ID = th.SalesPersonID AND sp.CompanyID = th.CompanyID "
              f"WHERE {W} GROUP BY th.SalesPersonID, sp.Name ORDER BY net DESC")
    items = _q(f"SELECT td.ItemCode AS code, SUM({NET}) AS net {JOIN} WHERE {W} GROUP BY td.ItemCode ORDER BY net DESC")
    summary = _q(f"SELECT SUM({NET}) AS net, COUNT(DISTINCT CAST(th.TransactionYear AS varchar(4)) + '-' + "
                 f"CAST(th.TransactionNo AS varchar(20))) AS inv, COUNT(DISTINCT th.CustomerID) AS custs {JOIN} WHERE {W}")[0]
    unsold = _q("SELECT COUNT(*) AS n FROM t.Items i WHERE ISNULL(i.IsSuspended, 0) = 0 AND NOT EXISTS ("
                f"SELECT 1 {JOIN} WHERE {W} AND td.ItemCode = i.ItemCode)")[0]["n"]
    top = reps[0]
    days = _q("SELECT TOP 2 CAST(TimeStamp AS date) AS d, COUNT(DISTINCT TRY_CAST(Data1 AS bigint)) AS visited "
              f"FROM t.LogActionTransaction WHERE ActionID = N'0' AND TRY_CAST(SalesmanID AS int) = {int(top['id'])} "
              "GROUP BY CAST(TimeStamp AS date) ORDER BY d DESC")
    visit_days = []
    for d in days:
        nxt = date.fromordinal(d["d"].toordinal() + 1).isoformat()
        s = _q("SELECT COUNT(*) AS inv, COUNT(DISTINCT CustomerID) AS sold FROM t.TransactionsHeaders "
               f"WHERE TransactionTypeID = 1 AND ISNULL(IsVoid, 0) = 0 AND SalesPersonID = {int(top['id'])} "
               f"AND TransactionDate >= '{d['d'].isoformat()}' AND TransactionDate < '{nxt}'")[0]
        visit_days.append({"visited": d["visited"], "sold": s["sold"], "inv": s["inv"]})
    return {"reps": reps, "items": items, "summary": summary, "visit_days": visit_days, "unsold": unsold}


def check(kind: str, answer: str, ref: dict) -> bool:
    a = (answer or "").replace("\u066c", ",")
    has = lambda x: any(v in a for v in number_variants(float(x)))  # noqa: E731
    if "```" in a:
        return False
    if kind == "top_rep":
        top = ref["reps"][0]
        return top["name"].strip() in a and has(top["net"])
    if kind == "top_item":
        top = ref["items"][0]
        return top["code"] in a or has(top["net"])
    if kind == "bottom10":
        # Product decision 2026-11-09: show lowest sold items AND the never-sold count.
        bottom = [r["code"] for r in ref["items"][-10:]]
        return sum(code in a for code in bottom) >= 5 and has(ref["unsold"])
    if kind == "visits":
        # Small integers are weak evidence on their own; this case also gets a manual read.
        return any(str(d["visited"]) in a and str(d["sold"]) in a and str(d["inv"]) in a
                   for d in ref["visit_days"])
    if kind == "summary":
        s = ref["summary"]
        return has(s["net"]) and str(s["inv"]) in a and str(s["custs"]) in a
    if kind == "howto":
        return any(k in a for k in ("MakeOrderTaking", "طلب بيع", "الموقف الوظيفي", "وظيف"))
    raise ValueError(kind)


def ask(question: str, session_id: str) -> dict:
    body = json.dumps({"question": question, "session_id": session_id, "company_id": COMPANY}).encode()
    req = urllib.request.Request("http://127.0.0.1:8100/ask", data=body,
                                 headers={"Content-Type": "application/json"})
    final = {}
    with urllib.request.urlopen(req, timeout=600) as resp:
        for raw in resp.read().decode("utf-8").split("\n\n"):
            if raw.startswith("data: ") and raw[6:] != "[DONE]":
                ev = json.loads(raw[6:])
                if "answer" in ev or "error" in ev or "needs_ask" in ev:
                    final = ev
    return final


def trace_for(question: str, since: float) -> dict:
    for line in reversed(TRACE.read_text(encoding="utf-8").splitlines()):
        rec = json.loads(line)
        if rec.get("ts", 0) >= since and rec.get("question") == question:
            return rec
    return {}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", help="previous results json; fail if any baseline pass now fails")
    args = ap.parse_args()
    cases = [json.loads(l) for l in (BASE_DIR / "evals" / "golden_session_105.jsonl")
             .read_text(encoding="utf-8").splitlines() if l.strip()]
    ref = references()
    sid = f"golden-{uuid.uuid4().hex[:8]}"
    rows = []
    for c in cases:
        t0 = time.time()
        res = ask(c["question"], sid)
        tr = trace_for(c["question"], t0 - 1)
        calls = tr.get("calls") or []
        rows.append({
            "name": c["name"], "pass": check(c["check"], res.get("answer") or "", ref),
            "latency_ms": tr.get("latency_ms"), "ttft_ms": tr.get("ttft_ms"),
            "llm_calls": len(calls), "tool_errors": tr.get("tool_errors"),
            "usd_offpeak": round(sum(cost_usd(x, OFFPEAK) for x in calls), 5),
            "usd_peak": round(sum(cost_usd(x, PEAK) for x in calls), 5),
            "answer": res.get("answer"),
        })
        print(f"{c['name']:<28} pass={rows[-1]['pass']} {rows[-1]['latency_ms']}ms "
              f"calls={rows[-1]['llm_calls']} ${rows[-1]['usd_offpeak']}", flush=True)
    n = len(rows)
    summary = {
        "accuracy": sum(r["pass"] for r in rows) / n,
        "usd_per_q_offpeak": round(sum(r["usd_offpeak"] for r in rows) / n, 5),
        "usd_per_q_peak": round(sum(r["usd_peak"] for r in rows) / n, 5),
        "p50_latency_ms": sorted(r["latency_ms"] or 0 for r in rows)[n // 2],
        "calls_per_q": round(sum(r["llm_calls"] for r in rows) / n, 2),
    }
    print(json.dumps(summary, indent=1))
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = BASE_DIR / "evals" / f"golden_session_105_results_{stamp}.json"
    out.write_text(json.dumps({"summary": summary, "cases": rows}, ensure_ascii=False, indent=1, default=str),
                   encoding="utf-8")
    if args.baseline:
        base = {r["name"]: r["pass"] for r in json.loads(Path(args.baseline).read_text(encoding="utf-8"))["cases"]}
        regressed = [r["name"] for r in rows if base.get(r["name"]) and not r["pass"]]
        if regressed:
            print("REGRESSED:", regressed)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 5: Run the unit tests**

Run: `py -3.13 -m pytest -q tests/test_evals.py -k "number_variants or cost_usd"`
Expected: PASS.

- [ ] **Step 6: Record the baseline (API must be running: `./run.ps1`)**

Run: `py -3.13 setup/clear_plan_cache.py --client 105` then `py -3.13 evals/run_golden_session.py`
Expected (matches the manual review): `best_rep_last_month pass=False`, `top_item pass=True`, `bottom10_items_plan pass=False`, `best_rep_visits pass=False`, `last_month_summary pass=True`, `howto_invoice_to_orders pass=True`; usd_per_q_offpeak ≈ 0.017; p50 ≈ 27 s. Save the printed results path as `BASELINE` for later tasks. Also run `py -3.13 evals/run_evals.py` and save its accuracy % and isolation result.

- [ ] **Step 7: Commit**

```bash
git add evals/golden_session_105.jsonl evals/run_golden_session.py tests/test_evals.py
git commit -m "test(evals): golden one-session eval with live references, cost and latency"
```

---

### Task 3: One date convention (half-open) for every metric + faster best-rep SQL

**Files:**
- Modify: `core/metrics.py:137-164` (`_invoice_date_filters`, `_order_date_filters`), `core/metrics.py:298-320` (`net_sales_by_salesperson`)
- Modify: `core/agent.py:35` (`PLAN_SEMANTIC_VERSION`)
- Test: `tests/test_metrics.py:113-121`

**Interfaces:**
- Produces: all metric `to_date` filters are exclusive (`<`), matching the tool schema text "YYYY-MM-DD (half-open end)".

- [ ] **Step 1: Change the existing test to the correct contract and add the best-rep tests**

Replace `test_run_metric_date_and_salesperson_filters` in `tests/test_metrics.py`:

```python
def test_run_metric_date_and_salesperson_filters():
    sql_text = metrics.build_sql(
        "net_sales",
        {"from_date": "2025-06-01", "to_date": "2025-07-01", "sales_person_id": 3},
        company_id=COMPANY_ID,
    )
    assert "TransactionDate >= '2025-06-01'" in sql_text
    assert "TransactionDate < '2025-07-01'" in sql_text
    assert "TransactionDate <=" not in sql_text
    assert "SalesPersonID = 3" in sql_text


def test_best_salesperson_is_half_open_and_has_no_correlated_subquery():
    sql_text = metrics.build_sql(
        "net_sales_by_salesperson",
        {"from_date": "2026-10-01", "to_date": "2026-11-01"},
        company_id=COMPANY_ID,
    )
    assert "TransactionDate < '2026-11-01'" in sql_text
    assert "<=" not in sql_text
    assert "th2" not in sql_text
    assert "COUNT(DISTINCT" in sql_text


def test_orders_metric_is_half_open():
    sql_text = metrics.build_sql("orders", {"from_date": "2026-10-01", "to_date": "2026-11-01"},
                                 company_id=COMPANY_ID)
    assert "OrderDate < '2026-11-01'" in sql_text
    assert "OrderDate <=" not in sql_text
```

- [ ] **Step 2: Run to verify they fail**

Run: `py -3.13 -m pytest -q tests/test_metrics.py`
Expected: the three tests above FAIL (`<=` present, `th2` present).

- [ ] **Step 3: Implement**

In `core/metrics.py` change `<=` to `<` in both helpers:

```python
    if to_date:
        parts.append(f"{alias}.TransactionDate < '{to_date}'")
```

```python
    if to_date:
        parts.append(f"{alias}.OrderDate < '{to_date}'")
```

Replace the `net_sales_by_salesperson` branch:

```python
    if metric == "net_sales_by_salesperson":
        extra = _invoice_date_filters(filters)
        return (
            "SELECT th.SalesPersonID, sp.Name AS SalesPersonName, "
            "COUNT(DISTINCT CAST(th.TransactionYear AS varchar(4)) + '-' + "
            "CAST(th.TransactionNo AS varchar(20))) AS invoice_count, "
            f"SUM({line_amount_sql('td')}) AS gross_amount "
            "FROM t.TransactionsHeaders th "
            + _detail_join()
            + "INNER JOIN t.SalesPersons sp ON sp.ID = th.SalesPersonID AND sp.CompanyID = th.CompanyID "
            "WHERE th.TransactionTypeID = 1 AND ISNULL(th.IsVoid, 0) = 0"
            + _company_id_filter(cid, "th", "td", "sp")
            + extra
            + " GROUP BY th.SalesPersonID, sp.Name "
            "ORDER BY gross_amount DESC"
        )
```

In `core/agent.py` bump `PLAN_SEMANTIC_VERSION = "3"` (old cached plans with `<=` can no longer be replayed).

- [ ] **Step 4: Run tests, then check equivalence against the database**

Run: `py -3.13 -m pytest -q tests/test_metrics.py tests/test_agent.py`
Expected: PASS.

Run (read-only):

```bash
py -3.13 -c "import sys;sys.path.insert(0,'.');from core import metrics,sql;r=sql.run_select(metrics.build_sql('net_sales_by_salesperson',{'from_date':'2026-10-01','to_date':'2026-11-01'},company_id=1),company_id=1,client='105');print([(x['SalesPersonID'],round(x['gross_amount'],2),x['invoice_count']) for x in r])"
```

Expected: `[(8, 15355.23, 79), (210, 15185.23, 85), (145, 14565.48, 111), (211, 12145.91, 106)]` — identical to the `sales` metric grouped by salesperson.

- [ ] **Step 5: Clear the poisoned plan cache, re-run golden, commit**

Run: `py -3.13 setup/clear_plan_cache.py --client 105`, restart API, `py -3.13 evals/run_golden_session.py --baseline <BASELINE>`
Expected: exit 0; `best_rep_last_month` now names Jamil 15,355.23.

```bash
git add core/metrics.py core/agent.py tests/test_metrics.py
git commit -m "fix(metrics): half-open to_date for every metric; single-join best salesperson"
```

---

### Task 4: Correct line-vs-header classification and a prose-only backstop

**Files:**
- Modify: `core/verify.py:66-76` (`_count_kind_for_select`) + new helpers
- Modify: `core/agent.py:1351-1371` (`_apply_count_backstop`)
- Test: `tests/test_verify.py`, `tests/test_agent.py`

**Interfaces:**
- Produces: `verify.count_scopes()` returns `kind="header"` when every COUNT in a detail-joined SELECT is `COUNT(DISTINCT <header key>)` (also inside `CASE … THEN th.TransactionNo END`).

- [ ] **Step 1: Confirm the sqlglot shape**

Run: `py -3.13 -c "import sqlglot;print(repr(sqlglot.parse_one('SELECT COUNT(DISTINCT CASE WHEN th.T=1 THEN th.TransactionNo END) FROM a th', read='tsql').expressions[0]))"`
Expected: `Count(this=Distinct(expressions=[Case(...)]))`. If the shape differs, adapt `_distinct_value_columns` below to it before continuing.

- [ ] **Step 2: Write the failing tests**

```python
# tests/test_verify.py
def test_distinct_header_key_count_over_detail_join_is_header():
    from core import metrics, verify
    s = metrics.build_sales_sql(1, {"from_date": "2026-10-01", "to_date": "2026-11-01"})
    assert verify.count_scopes(s) == [{"kind": "header", "func": "count"}]


def test_plain_count_star_over_detail_join_is_still_lines():
    from core import verify
    s = ("SELECT COUNT(*) AS n FROM t.TransactionsHeaders th JOIN t.TransactionsDetails td "
         "ON td.TransactionNo = th.TransactionNo")
    assert verify.count_scopes(s) == [{"kind": "lines", "func": "count"}]
```

```python
# tests/test_agent.py
def test_count_backstop_ignores_words_inside_code_fences():
    state = {"had_lines_count": True, "header_count": None}
    text = "باع لـ 5 عملاء عبر 9 فواتير.\n```sql\n-- حبيبات البنود\nSELECT 1\n```"
    out = agent._apply_count_backstop(text, state)
    assert out.endswith(agent.locale_ar.COUNT_NOTE_USER)
```

- [ ] **Step 3: Run to verify they fail**

Run: `py -3.13 -m pytest -q tests/test_verify.py tests/test_agent.py -k "distinct_header_key or count_star_over or code_fences"`
Expected: first and third FAIL.

- [ ] **Step 4: Implement**

`core/verify.py` — add above `_count_kind_for_select`:

```python
_HEADER_KEY_COLS = frozenset({"transactionno"})


def _counts_excluding_subqueries(expr: exp.Expression) -> list[exp.Count]:
    if isinstance(expr, exp.Subquery):
        return []
    if isinstance(expr, exp.Count):
        return [expr]
    out: list[exp.Count] = []
    for child in expr.args.values():
        items = child if isinstance(child, list) else [child]
        for item in items:
            if isinstance(item, exp.Expression):
                out.extend(_counts_excluding_subqueries(item))
    return out


def _distinct_value_columns(node: exp.Expression) -> list[exp.Column]:
    if isinstance(node, exp.Case):
        cols: list[exp.Column] = []
        for if_ in node.args.get("ifs") or []:
            cols.extend(if_.args["true"].find_all(exp.Column))
        if node.args.get("default") is not None:
            cols.extend(node.args["default"].find_all(exp.Column))
        return cols
    return list(node.find_all(exp.Column))


def _is_distinct_header_key(count: exp.Count) -> bool:
    inner = count.this
    if not isinstance(inner, exp.Distinct):
        return False
    cols = [c for e in inner.expressions for c in _distinct_value_columns(e)]
    return bool(cols) and all(_column_bare(c) in _HEADER_KEY_COLS for c in cols)
```

Replace the detail branch in `_count_kind_for_select`:

```python
    if tables & _DETAIL_TABLES:
        counts = [c for e in select.expressions for c in _counts_excluding_subqueries(e)]
        if counts and all(_is_distinct_header_key(c) for c in counts):
            return "header"
        return "lines"
```

(`_column_bare` is defined later in the file; move these helpers below `_column_bare` or move `_column_bare` up.)

`core/agent.py` — in `_apply_count_backstop` evaluate the regexes on prose only:

```python
_CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)


def _apply_count_backstop(final_text: str | None, state: dict) -> str:
    """Append header recount or line-grain warning when prose treats lines as invoices."""
    text = (final_text or "").strip()
    if not text or not state.get("had_lines_count"):
        return text
    prose = _CODE_FENCE_RE.sub("", text)
    if _LINES_WORD_RE.search(prose):
        return text
    if not _INVOICE_WORD_RE.search(prose):
        return text
    hc = state.get("header_count")
    if hc is not None:
        suffix = locale_ar.HEADER_COUNT_SUFFIX.format(n=hc)
        if suffix not in text:
            return f"{text}\n{suffix}"
    elif locale_ar.COUNT_NOTE_USER not in text:
        return f"{text}\n{locale_ar.COUNT_NOTE_USER}"
    return text
```

- [ ] **Step 5: Run, then golden, then commit**

Run: `py -3.13 -m pytest -q tests/test_verify.py tests/test_agent.py tests/test_metrics.py` → PASS. Golden with `--baseline` → exit 0; summary answers no longer end with the false warning.

```bash
git add core/verify.py core/agent.py tests/test_verify.py tests/test_agent.py
git commit -m "fix(verify): DISTINCT header-key counts are header grain; backstop reads prose only"
```

---

### Task 5: Never put SQL in the answer text

**Files:**
- Modify: `prompts/system.md:210`
- Modify: `core/agent.py` (new `_strip_sql_fences`, called before `_apply_count_backstop` at both call sites, `core/agent.py:2180` and `:2200`)
- Test: `tests/test_agent.py`

Note: `prompts/system.md` is part of the cached prefix — this one-time edit costs one cold prefix per tenant, then caches again.

- [ ] **Step 1: Write the failing test**

```python
def test_strip_sql_fences_removes_sql_blocks_only():
    text = "النتيجة 5 عملاء.\n\n```sql\nSELECT 1\n```\n\nملاحظة."
    assert agent._strip_sql_fences(text) == "النتيجة 5 عملاء.\n\nملاحظة."
```

- [ ] **Step 2: Run to verify it fails**

Run: `py -3.13 -m pytest -q tests/test_agent.py -k strip_sql_fences` → FAIL (`AttributeError`).

- [ ] **Step 3: Implement**

```python
_SQL_FENCE_RE = re.compile(r"\n*```(?:sql|tsql)?\s*\n.*?```\n*", re.DOTALL | re.IGNORECASE)


def _strip_sql_fences(text: str | None) -> str | None:
    if not text:
        return text
    return _SQL_FENCE_RE.sub("\n\n", text).strip()
```

At both sites: `final_text = _apply_count_backstop(_strip_sql_fences(final_text), state)`.

`prompts/system.md:210` becomes:

```markdown
- Never include SQL or code blocks in the answer text; the UI shows the executed SQL separately.
```

- [ ] **Step 4: Run, golden, commit**

Run: `py -3.13 -m pytest -q tests/test_agent.py` → PASS; golden `--baseline` → exit 0.

```bash
git add prompts/system.md core/agent.py tests/test_agent.py
git commit -m "fix(answer): strip SQL fences from answers; prompt forbids SQL in prose"
```

---

### Task 6: Gate — tenant predicates only for tables in the SELECT's own scope

**Files:**
- Modify: `core/gate.py:123-134` (`_tables_in_from`)
- Test: `tests/test_gate.py`

- [ ] **Step 1: Write the failing test**

```python
def test_derived_table_gets_tenant_predicate_inside_not_outside():
    import json
    from core import config, gate
    cache = json.loads((config.work_dir("105") / "schema_cache.json").read_text(encoding="utf-8"))
    sql = ("SELECT COUNT(DISTINCT v.c) AS n FROM (SELECT TRY_CAST(Data1 AS bigint) AS c "
           "FROM t.LogActionTransaction WHERE ActionID = N'0') v")
    out = gate.validate(sql, company_id=1, schema_cache=cache)
    inner, outer = out.split(") AS v", 1)
    assert "CompNo = 1" in inner
    assert "CompNo" not in outer
```

(If `tests/test_gate.py` uses a fixture schema cache instead of `work/105`, use that fixture with a `dbo.LogActionTransaction` entry having `CompNo`.)

- [ ] **Step 2: Run to verify it fails**

Run: `py -3.13 -m pytest -q tests/test_gate.py -k derived_table` → FAIL (outer contains `LogActionTransaction.CompNo = 1`).

- [ ] **Step 3: Implement**

```python
def _tables_in_from(select: exp.Select) -> list[exp.Table]:
    """t.* tables whose nearest enclosing SELECT is `select` — tables inside
    derived tables belong to the inner SELECT and are handled when
    find_all(exp.Select) reaches it."""
    sources = []
    from_ = select.args.get("from_")
    if from_:
        sources.append(from_)
    sources.extend(select.args.get("joins") or [])
    tables: list[exp.Table] = []
    for src in sources:
        for node in src.walk():
            if (isinstance(node, exp.Table) and (node.db or "").lower() == "t"
                    and node.find_ancestor(exp.Select) is select):
                tables.append(node)
    return tables
```

- [ ] **Step 4: Run gate + isolation, commit**

Run: `py -3.13 -m pytest -q tests/test_gate.py tests/test_tenant_wall.py` → PASS; `py -3.13 evals/run_evals.py` isolation must stay 100 %.

```bash
git add core/gate.py tests/test_gate.py
git commit -m "fix(gate): scope tenant predicate injection to each SELECT's own tables"
```

---

### Task 7: Hard query budget per tool call

**Files:**
- Modify: `core/agent.py:1462` (`run_metric`), `:1481` (`run_report`), `:1502` (`run_select`) inside `_run_tool`
- Test: `tests/test_agent.py`

**Interfaces:**
- Produces: when `len(state["queries"]) >= MAX_QUERIES`, a business-query tool returns `{"status": "budget_spent", "message": ...}` (not `"error"`, so it does not trigger gear escalation) and runs no SQL.

- [ ] **Step 1: Write the failing test**

```python
def test_parallel_tool_calls_cannot_exceed_query_budget():
    state = {"queries": ["q"] * agent.MAX_QUERIES, "question": "x"}
    with patch.object(agent.sql, "run_select") as rs:
        out = agent._run_tool("run_select", {"sql": "SELECT 1 FROM t.Items"}, {}, {}, [], 1, "105", state)
    rs.assert_not_called()
    assert out["status"] == "budget_spent"
    assert len(state["queries"]) == agent.MAX_QUERIES
```

- [ ] **Step 2: Run to verify it fails** — `py -3.13 -m pytest -q tests/test_agent.py -k parallel_tool_calls` → FAIL (`run_select` called).

- [ ] **Step 3: Implement** — at the top of `_run_tool`:

```python
    if name in ("run_select", "run_metric", "run_report") \
            and "information_schema" not in str(args.get("sql", "")).lower() \
            and len(state.get("queries") or []) >= MAX_QUERIES:
        return {"status": "budget_spent",
                "message": f"Query budget ({MAX_QUERIES}) is spent. Answer from results already returned."}
```

- [ ] **Step 4: Run, commit**

Run: `py -3.13 -m pytest -q tests/test_agent.py` → PASS.

```bash
git add core/agent.py tests/test_agent.py
git commit -m "fix(agent): enforce MAX_QUERIES per tool call, not per model turn"
```

---

### Task 8: Keep the prompt prefix cache warm — one tool list per turn

**Files:**
- Modify: `core/llm.py:144-169` (`stream_create_kwargs`), `:172-186` (`complete`) — `tool_choice` passthrough
- Modify: `core/agent.py:505-519` (`_stream_turn` signature), `:2039-2045` (loop), `_run_tool` (cap guards)
- Test: `tests/test_llm.py`, `tests/test_agent.py`

**Interfaces:**
- Produces: `llm.complete(..., tool_choice: str | None = None)`; `_stream_turn(..., tool_choice=None)`; `state["turn_tools"]` fixed at turn start. Mid-turn caps (doc search cap, vault cap, recall after rows, docs-only schema tools) are enforced in `_run_tool` returning `{"status": "unavailable", "message": ...}`.

- [ ] **Step 1: Spike — confirm the cache hypothesis and `tool_choice` support (≈ $0.02)**

Create `work/_cache_spike.py` (gitignored):

```python
import sys
sys.path.insert(0, ".")
from core import agent, config, llm
import json
cache = json.loads((config.work_dir("105") / "schema_cache.json").read_text(encoding="utf-8"))
msgs = agent._static_prefix("105", cache) + [{"role": "user", "content": "كم عدد المناديب؟"}]
full = agent.TOOLS
fewer = [t for t in full if t["function"]["name"] != "recall_turns"]
for label, tools, choice in [("warm", full, None), ("same", full, None),
                             ("fewer_tools", fewer, None), ("none_choice", full, "none")]:
    kw = llm.stream_create_kwargs(llm.resolve_gear("t1"), msgs, tools=tools)
    if choice:
        kw["tool_choice"] = choice
    r = llm._client.chat.completions.create(**kw)
    u = r.usage
    print(label, u.prompt_tokens, u.prompt_cache_hit_tokens, r.choices[0].finish_reason)
```

Run: `py -3.13 work/_cache_spike.py`
Expected: `same` hit ≈ full prefix; `fewer_tools` hit ≈ 6–9k (confirms tool-list sensitivity); `none_choice` returns without HTTP 400 and with full hit, `finish_reason=stop`. **If `tool_choice="none"` is rejected**, skip Step 4's `tool_choice` and keep passing the same tools on the final call (the budget guard from Task 7 + the existing nudge already prevent extra SQL).

- [ ] **Step 2: Write the failing tests**

```python
# tests/test_llm.py
def test_tool_choice_is_passed_through():
    from core import llm
    kw = llm.stream_create_kwargs(llm.resolve_gear("t1"), [], tools=[{"x": 1}], stream=True)
    assert "tool_choice" not in kw
    kw = llm.stream_create_kwargs(llm.resolve_gear("t1"), [], tools=[{"x": 1}], tool_choice="none", stream=True)
    assert kw["tool_choice"] == "none"
```

```python
# tests/test_agent.py
def test_tool_list_is_identical_on_every_call_of_a_turn(monkeypatch, tmp_path):
    monkeypatch.setattr(memory, "DB_PATH", tmp_path / "cache.sqlite")
    seen = []

    def fake_complete(messages, gear="t1", tools=None, stream=False, **kw):
        if stream:
            seen.append([t["function"]["name"] for t in (tools or [])])
            if len(seen) == 1:
                return _resp(_msg(tool_calls=[_tool_call("c1", "run_select",
                                                         '{"sql": "SELECT COUNT(*) AS n FROM t.Items"}')]))
            return _resp(_msg(content="عدد الأصناف 7"))
        return _plain_resp("{}")

    with patch.object(agent.llm, "complete", side_effect=fake_complete), \
         patch.object(agent.sql, "run_select", return_value=[{"n": 7}]):
        agent.ask("morec", "كم عدد الأصناف؟", conversation=dict(SCOPE))
    assert len(seen) >= 2 and all(s == seen[0] for s in seen)
```

- [ ] **Step 3: Run to verify they fail** — `py -3.13 -m pytest -q tests/test_llm.py tests/test_agent.py -k "tool_choice or identical_on_every_call"` → FAIL (second call lacks `recall_turns`).

- [ ] **Step 4: Implement**

`core/llm.py`: add `tool_choice=None` to `stream_create_kwargs` and `complete`; in `stream_create_kwargs` after `kwargs["tools"] = tools`:

```python
    if tool_choice is not None and tools is not None:
        kwargs["tool_choice"] = tool_choice
```

and forward it from `complete` (`stream_create_kwargs(cfg, messages, tools=tools, tool_choice=tool_choice, ...)`).

`core/agent.py`:
- `_stream_turn(messages, tools, gear=..., user_id=None, cancel=None, usage_acc=None, tool_choice=None)` → pass `tool_choice=tool_choice` to `llm.complete`.
- Before the `for _ in range(MAX_TURNS):` loop: `state["turn_tools"] = _active_tools(state)`.
- In the loop replace `tools = _active_tools(state)` with:

```python
        if state.get("report_unlock") and not state.get("_tools_unlocked"):
            state["turn_tools"] = _active_tools(state)   # rare path; one change allowed
            state["_tools_unlocked"] = True
        tools = state["turn_tools"]
        budget_spent = len(state["queries"]) >= MAX_QUERIES
        tool_choice = "none" if budget_spent and tools else None
```

and call `_stream_turn(messages, tools, gear=state["gear"], user_id=..., cancel=cancel, usage_acc=usage_acc, tool_choice=tool_choice)`.
- At the top of `_run_tool` (after Task 7's guard):

```python
    blocked = _mid_turn_block_reason(name, state)
    if blocked:
        return {"status": "unavailable", "message": blocked}
```

with

```python
def _mid_turn_block_reason(name: str, state: dict) -> str | None:
    if name == "search_docs" and state.get("doc_searches", 0) >= MAX_DOC_SEARCHES:
        return "No more documentation searches this turn. Answer from excerpts already retrieved."
    if name in _VAULT_TOOLS and state.get("vault_searches", 0) >= MAX_VAULT_SEARCHES:
        return "No more vault schema searches this turn."
    if name == "recall_turns" and state.get("had_business_rows"):
        return "recall_turns is not available after business rows were returned."
    if name in _DOCS_ONLY_SCHEMA_TOOLS and state.get("docs_only"):
        return "Schema tools are not available in docs-only mode."
    return None
```

- [ ] **Step 5: Run tests, golden, commit**

Run: `py -3.13 -m pytest -q tests/test_llm.py tests/test_agent.py tests/test_recall.py` → PASS.
Golden `--baseline` → exit 0; expect cache-miss tokens per question to fall sharply (no more 55k–65k misses after the first call of a turn).

```bash
git add core/llm.py core/agent.py tests/test_llm.py tests/test_agent.py
git commit -m "perf(agent): fixed tool list per turn so the DeepSeek prefix cache stays warm"
```

---

### Task 9: Gear stability experiment (mid-turn t1→t2 escalation)

**Files:**
- Modify: `core/agent.py:2125-2126`
- Test: `tests/test_agent.py`

Mid-turn escalation re-sends the whole 64k prefix uncached (Q3 call 2: 65,070 miss). Whether escalation helps accuracy is unmeasured, so ship as a flag and decide with data.

- [ ] **Step 1: Write the failing test**

```python
def test_midturn_escalation_can_be_disabled(monkeypatch):
    monkeypatch.setattr(agent, "_MIDTURN_ESCALATION", False)
    state = {"gate_errors": 1, "gear": agent.DEFAULT_GEAR}
    agent._maybe_escalate(state)
    assert state["gear"] == agent.DEFAULT_GEAR
    monkeypatch.setattr(agent, "_MIDTURN_ESCALATION", True)
    agent._maybe_escalate(state)
    assert state["gear"] == "t2"
```

- [ ] **Step 2: Run to verify it fails** → `AttributeError: _maybe_escalate`.

- [ ] **Step 3: Implement**

```python
_MIDTURN_ESCALATION = os.environ.get("CHATBOT_MIDTURN_ESCALATION", "1") == "1"


def _maybe_escalate(state: dict) -> None:
    if _MIDTURN_ESCALATION and state["gate_errors"] >= 1 and state["gear"] == DEFAULT_GEAR:
        state["gear"] = "t2"
```

Replace the inline two lines at `core/agent.py:2125-2126` with `_maybe_escalate(state)` (keep `state["gate_errors"] += 1` before it). Add `import os` if missing.

- [ ] **Step 4: A/B on data**

Run golden + `evals/run_evals.py` twice: `CHATBOT_MIDTURN_ESCALATION=1` and `=0` (restart API between runs). Flip the default to `"0"` only if accuracy is ≥ and no case regresses; otherwise keep `"1"`. Record both summaries in the commit message.

- [ ] **Step 5: Commit**

```bash
git add core/agent.py tests/test_agent.py
git commit -m "perf(agent): flag for mid-turn gear escalation (A/B: <paste summaries>)"
```

---

### Task 10: Router fixes — fast-count and how-to paths

**Files:**
- Modify: `core/agent.py:890-900` (`_is_fast_count_path`), `:938-949` (`_is_howto_path`)
- Test: `tests/test_agent.py`

- [ ] **Step 1: Write the failing tests**

Principle (plan revision R1): the fast path is an **allow-list by structure** — a short, single-clause, single-question count — instead of a deny-list of words. How-to detection is **grammar** (question word + action verb / "how do I"), not a list of our sentences.

```python
FAST_COUNT_YES = [
    "كم عدد العملاء؟", "كم زبون عندي", "كم مندوب عنا", "how many customers do I have",
    "عدد الأصناف", "كم صنف مسجل؟",
]
FAST_COUNT_NO = [  # multi-clause, multiple questions, or analysis around a count
    "كم عميل زار المندوب امس، وكم واحد اشترى منهم؟",
    "كم عميل عندي وكم واحد منهم اشترى الشهر الماضي؟",
    "how many customers did my best rep visit and how many bought",
    "كم عميل خسرنا هذا الشهر ولماذا؟",
    "كم زبون عند كل مندوب مرتبين من الاكثر للأقل مع خطة لتحسين الأضعف",
]
HOWTO_YES = [
    "كيف أضيف صنف جديد؟", "طريقة تعديل سعر مادة", "شلون أفعّل المندوب على الجهاز",
    "كيف احول المندوب من فواتير الى طلبيات", "how do I change a salesman to order taking",
    "كيفية إلغاء فاتورة",
]
HOWTO_NO = [
    "كيف أداء المناديب هذا الشهر؟", "كيف المبيعات اليوم", "كم طلب بيع عندي",
    "how are sales this month", "كيف كانت الطلبات امس",
]


@pytest.mark.parametrize("q", FAST_COUNT_YES)
def test_fast_count_accepts_single_clause_counts(q):
    assert agent._is_fast_count_path(q) is True


@pytest.mark.parametrize("q", FAST_COUNT_NO)
def test_fast_count_rejects_multi_part_or_analytic(q):
    assert agent._is_fast_count_path(q) is False


@pytest.mark.parametrize("q", HOWTO_YES)
def test_howto_action_grammar(q):
    assert agent._is_howto_path(q, "105") is True


@pytest.mark.parametrize("q", HOWTO_NO)
def test_how_is_x_is_not_howto(q):
    assert agent._is_howto_path(q, "105") is False
```

(If a YES case fails only because `_COUNT_HINT_RE` / `_MASTER_COUNT_TERMS` don't know a common word such as «زبون» or «صنف», extend those general vocabularies — that is fixing a vocabulary, not fitting a question. Do not add golden-question phrasings to any list.)

- [ ] **Step 2: Run to verify** — NO-lists and how-to YES-list mostly FAIL today.

- [ ] **Step 3: Implement**

```python
_CLAUSE_SPLIT_RE = re.compile(r"[،,؛;]|\s(?:و|and)\s*(?:كم|مين|من|شو|ما|ماذا|لماذا|ليش|how|what|why)\b", re.I)
_QUESTION_WORD_RE = re.compile(r"\b(?:كم|مين|شو|ماذا|لماذا|ليش|how many|what|why)\b", re.I)
_FAST_COUNT_MAX_WORDS = 7
_HOWTO_ACTION_RE = re.compile(
    r"(?:كيف|كيفية|طريقة|شلون)\s+(?:ا|أ|ن)?\S*?(?:غير|عدل|ضيف|اضاف|إضاف|حذف|فعل|فعّل|حول|نشئ|ربط|وقف|لغي|إلغاء|الغاء|سجل|تعديل|تغيير|تحويل)\S*"
    r"|\bhow (?:do|can|to|should) (?:i |we )?\w+",
    re.I,
)
```

In `_is_fast_count_path`, after the `_EXPLAIN_INTENT_RE` check:

```python
    if (_CLAUSE_SPLIT_RE.search(q) or len(_QUESTION_WORD_RE.findall(q)) > 1
            or len(q.split()) > _FAST_COUNT_MAX_WORDS):
        return False
```

In `_is_howto_path`, right after the empty check:

```python
    if _HOWTO_ACTION_RE.search(q) and not _COUNT_HINT_RE.search(q):
        return True
```

- [ ] **Step 4: Run tests, golden, run_evals, commit**

Run: `py -3.13 -m pytest -q tests/test_agent.py` → PASS. Golden `--baseline` → exit 0 (visits and how-to cases should improve or hold); `run_evals.py` ≥ baseline.

```bash
git add core/agent.py tests/test_agent.py
git commit -m "fix(router): multi-part questions skip fast-count; action how-tos win over metric aliases"
```

---

### Task 11: Envelope — no serial contract call on SQL turns; fresh-card follow-ups only

**Files:**
- Modify: `core/agent.py:2181-2183` and `:2201-2203` (mark new card), `:1635-1661` (`_build_envelope`)
- Test: `tests/test_agent.py`

**Interfaces:**
- Produces: `state["card_is_new"]: bool`; confidence from evidence via `_evidence_confidence(state) -> str`.

- [ ] **Step 1: Write the failing tests**

```python
def test_envelope_skips_contract_call_when_turn_made_a_card():
    state = {"queries": ["q"], "last_rows": [{"a": 1}], "doc_source_pairs": [],
             "thread_head": {"period_label": "2026-10"}, "card_is_new": True, "tool_errors": []}
    with patch.object(agent.llm, "complete") as mock_complete:
        env = agent._build_envelope("q", "answer", state)
    mock_complete.assert_not_called()
    assert env["confidence"] == "high"


def test_inherited_card_does_not_drive_followups():
    state = {"queries": [], "last_rows": None, "doc_source_pairs": [("a", "b")],
             "thread_head": {"period_label": "2026-10"}, "card_is_new": False, "tool_errors": []}
    payload = '{"answer_md": "x", "refusal": false, "confidence": "high", "followups": ["أ", "ب", "ج"]}'
    with patch.object(agent.llm, "complete", return_value=_plain_resp(payload)):
        env = agent._build_envelope("كيف اغير", "answer", state)
    assert env["followups"] == ["أ", "ب", "ج"]
```

- [ ] **Step 2: Run to verify** — both FAIL.

- [ ] **Step 3: Implement**

At both card sites:

```python
        new_card = thread.card_from_query_log(state.get("query_log"))
        state["card_is_new"] = bool(new_card)
        if new_card:
            state["thread_head"] = new_card
```

Replace `_build_envelope`:

```python
def _evidence_confidence(state: dict) -> str:
    if state.get("tool_errors"):
        return "medium"
    if isinstance(state.get("last_rows"), list) and state["last_rows"]:
        return "high"
    return "medium" if state.get("doc_source_pairs") else "low"


def _build_envelope(question: str, final_text: str, state: dict) -> dict:
    """C8/E1: structured pieces /ask returns alongside the prose."""
    table = _build_table(state["last_rows"])
    thread_head = state.get("thread_head")
    use_card = bool(thread_head) and state.get("card_is_new", True)
    contract = None
    if final_text and not use_card:
        contract = _final_contract(question, final_text, state.get("_user_id"), state.get("_usage"))
    if use_card:
        followups = thread.card_followups(thread_head)
    else:
        followups = (contract or {}).get("followups") or []
        if not followups and final_text:
            followups = list(_DEFAULT_FOLLOWUPS)
    out: dict = {
        "table": table,
        "chart": _build_chart(table),
        "sources": _build_sources(state["queries"], state["doc_source_pairs"]),
        "followups": followups,
    }
    if thread_head:
        out["thread_head"] = thread_head
    if final_text and not (contract and contract["refusal"]):
        out["confidence"] = _evidence_confidence(state)
    if state.get("report_name"):
        out["report_name"] = state["report_name"]
    return out
```

(`card_is_new` defaults to True so the plan-cache replay path, which passes a prior card, keeps today's behaviour.)

- [ ] **Step 4: Run, fix any existing envelope tests that asserted the old contract-driven confidence, golden, commit**

Run: `py -3.13 -m pytest -q tests/test_agent.py tests/test_thread.py` → PASS (update `test_build_envelope_skips_followups_when_there_is_no_final_text` only if its expected dict changes; it should not). Golden `--baseline` → exit 0; expect ~1 fewer LLM call and ~3–5 s less on SQL turns.

```bash
git add core/agent.py tests/test_agent.py
git commit -m "perf(envelope): no serial contract call on SQL turns; evidence-based confidence; fresh-card follow-ups"
```

---

### Task 12: Faithfulness guard — "couldn't extract" while rows exist

**Files:**
- Modify: `core/agent.py` (new `_claims_failure_with_rows`, used right before `_strip_sql_fences` at both final-text sites)
- Test: `tests/test_agent.py`

Do this after Task 1 has run in real use for a while: check `tool_errors` in `work/trace.jsonl` to see what actually preceded such answers, and adjust the regex to the observed phrasing.

- [ ] **Step 1: Write the failing test**

```python
def test_failure_claim_with_rows_triggers_one_recompose():
    state = {"last_rows": [{"code": "A", "net": 1.0}], "gear": "t1", "_user_id": None,
             "_usage": None, "turn_tools": None, "queries": ["q"]}
    msgs = [{"role": "user", "content": "q"}]
    with patch.object(agent.llm, "complete", return_value=_resp(_msg(content="القائمة: A 1.0"))) as m:
        out = agent._recompose_if_false_failure("تعذّر استخراج القائمة", msgs, state)
    assert out == "القائمة: A 1.0"
    assert m.call_count == 1
    assert state["recomposed"] is True
```

- [ ] **Step 2: Run to verify** → `AttributeError`.

- [ ] **Step 3: Implement**

```python
_FAILURE_CLAIM_RE = re.compile(r"تعذّ?ر|لم يكتمل|لا يمكنني استخراج|couldn't|could not|unable to", re.I)


def _recompose_if_false_failure(final_text: str | None, messages: list, state: dict) -> str | None:
    rows = state.get("last_rows")
    if not final_text or not (isinstance(rows, list) and rows) or not _FAILURE_CLAIM_RE.search(final_text):
        return final_text
    nudge = {"role": "system", "content": (
        f"The last query DID return {len(rows)} rows (in the tool results above). "
        "Answer the user's question from those rows. Do not say the query failed.")}
    text = None
    for event in _stream_turn(messages + [nudge], state.get("turn_tools"), gear=state["gear"],
                              user_id=state.get("_user_id"), usage_acc=state.get("_usage"),
                              tool_choice="none" if state.get("turn_tools") else None):
        if event["type"] == "_turn_done":
            text = _sanitize_final_text(event["message"].get("content"))
    state["recomposed"] = True
    return text if not _is_blank(text) else final_text
```

At both final-text sites (inside `if _has_evidence(state):` after `_resolve_final_text`, and in the `else:` branch): `final_text = _recompose_if_false_failure(final_text, messages, state)`. Add `recomposed=state.get("recomposed", False)` to `_turn_trace`.

- [ ] **Step 4: Run, golden (bottom10 case), commit**

Run: `py -3.13 -m pytest -q tests/test_agent.py` → PASS. Golden `--baseline` → exit 0.

```bash
git add core/agent.py tests/test_agent.py
git commit -m "fix(agent): recompose once when the answer claims failure but rows exist"
```

---

### Task 13: Fail closed without tenant views (security) — SKIPPED

> **Skipped by product owner (2026-11-09):** "keep cds user, ignore t views, keep everything direct and easy." Do not implement this task. The `cds` login and the `t.` → `dbo.` fallback in `core/sql.run_select` stay as they are; Global Constraint 2 is waived for this branch only to that extent (no other change to connections).

**Files:**
- Modify: `core/sql.py:127-136` (`run_select`)
- Test: `tests/test_tenant_wall.py`

**Operator prerequisite (do first, or the local bot will stop answering SQL):**

```bash
py -3.13 setup/03_apply_db_sql.py --db-name Olives_BO   # SA from .env; creates chatbot_ro + t. views
```

Then in the UI's DB console, replace the saved `cds` override with `chatbot_ro` (password in `work/ro_password.txt`), or clear the override so `.env` defaults apply.

- [ ] **Step 1: Write the failing test**

```python
def test_run_select_refuses_dbo_fallback_without_flag(monkeypatch):
    from core import gate, sql
    monkeypatch.delenv("CHATBOT_ALLOW_DBO_FALLBACK", raising=False)
    monkeypatch.setattr(sql.gate, "validate", lambda raw, **kw: raw)
    monkeypatch.setattr(sql.memory, "get_result", lambda *a, **kw: None)

    class FakeConn:
        def cursor(self, **kw):
            raise AssertionError("must not execute")
        def close(self):
            pass

    monkeypatch.setattr(sql, "get_conn", lambda client: FakeConn())
    monkeypatch.setattr(sql, "set_tenant", lambda conn, cid: None)
    monkeypatch.setattr(sql, "has_tenant_views", lambda conn: False)
    monkeypatch.setattr(sql, "_schema_cache", lambda client: {})
    import pytest
    with pytest.raises(gate.GateError):
        sql.run_select("SELECT 1 FROM t.Items", company_id=1, client="105")
```

- [ ] **Step 2: Run to verify** → FAIL (AssertionError from cursor, or no raise).

- [ ] **Step 3: Implement** — in `run_select`, replace the `if not has_tenant_views(conn):` block:

```python
        if not has_tenant_views(conn):
            if os.environ.get("CHATBOT_ALLOW_DBO_FALLBACK") != "1":
                raise gate.GateError(
                    "tenant views (schema t) are missing on this server; run "
                    "setup/03_apply_db_sql.py — refusing base-table fallback"
                )
            import re
            exec_sql = re.sub(r"(?i)\bfrom\s+t\.", "FROM dbo.", exec_sql)
            exec_sql = re.sub(r"(?i)\bjoin\s+t\.", "JOIN dbo.", exec_sql)
```

- [ ] **Step 4: Run, isolation, commit**

Run: `py -3.13 -m pytest -q tests/test_tenant_wall.py tests/test_db_console.py` → PASS; `py -3.13 evals/run_evals.py` isolation 100 %.

```bash
git add core/sql.py tests/test_tenant_wall.py
git commit -m "security(sql): fail closed when t. tenant views are missing"
```

---

### Task 14: Ranked item lists and never-sold items ("lowest items" = both)

Product decision (2026-11-09): "lowest-selling items" answers with BOTH the lowest N items that sold in the period AND the count (plus a sample) of active items with zero sales. "Best salesman" stays invoiced sales (no change).

Root cause this also fixes: `sales` grouped by item returns ~245 unordered rows; the gate caps at 200 and `_ROW_DISPLAY_CAP` shows the model only 50, so top/bottom items were picked from a partial, unordered list (Q2 was right by luck, Q3 could not be).

**Files:**
- Modify: `core/metrics.py` (`METRICS`, `build_sales_sql`, `build_sql`)
- Modify: `core/agent.py:746-790` (`run_metric` tool schema: new filters + metric name)
- Test: `tests/test_metrics.py`

**Interfaces:**
- Produces: `filters.order` ∈ {`"asc"`, `"desc"`} and `filters.limit` (int 1–50) for `sales` with `group_by`; new metric `unsold_items` (aliases «مواد راكدة», «اصناف راكدة», `never_sold`) returning `unsold_count, ItemCode, ItemName` for active items with no type-1 sale in `[from_date, to_date)`.

- [ ] **Step 1: Write the failing tests**

```python
def test_sales_by_item_can_be_ranked_and_limited():
    s = metrics.build_sales_sql(COMPANY_ID, {"from_date": "2026-10-01", "to_date": "2026-11-01",
                                             "group_by": "item", "order": "asc", "limit": 10})
    assert s.startswith("SELECT TOP 10 ")
    assert s.rstrip().endswith("ORDER BY gross_sales ASC")


def test_sales_rank_uses_net_measure_when_returns_net():
    s = metrics.build_sales_sql(COMPANY_ID, {"group_by": "item", "order": "desc", "returns": "net"})
    assert s.rstrip().endswith("ORDER BY net_of_returns DESC")


def test_sales_rank_rejects_bad_limit():
    import pytest
    with pytest.raises(ValueError):
        metrics.build_sales_sql(COMPANY_ID, {"group_by": "item", "order": "asc", "limit": 500})


def test_unsold_items_metric_sql():
    s = metrics.build_sql("unsold_items", {"from_date": "2026-10-01", "to_date": "2026-11-01"},
                          company_id=COMPANY_ID)
    assert "NOT EXISTS" in s
    assert "ISNULL(i.IsSuspended, 0) = 0" in s
    assert "TransactionDate < '2026-11-01'" in s
    assert "COUNT(*) OVER () AS unsold_count" in s
    assert metrics.resolve_metric("مواد راكدة") == "unsold_items"
```

- [ ] **Step 2: Run to verify they fail**

Run: `py -3.13 -m pytest -q tests/test_metrics.py -k "ranked or rank_uses or bad_limit or unsold_items"` → FAIL.

- [ ] **Step 3: Implement**

`core/metrics.py` — add to `METRICS`:

```python
    "unsold_items": {
        "aliases": ["unsold_items", "never_sold", "مواد راكدة", "أصناف راكدة"],  # metric names, not question phrasings
        "description": "Active items with zero sales invoices in the period (count + sample).",
    },
```

In `build_sales_sql`, after `group_by` is resolved and before the `return`:

```python
    order = (filters.get("order") or "").strip().lower()
    top = ""
    order_by = ""
    if order:
        if order not in ("asc", "desc") or not group_key:
            raise ValueError("order needs group_by and must be asc or desc")
        limit = int(filters.get("limit") or 10)
        if not 1 <= limit <= 50:
            raise ValueError("limit must be between 1 and 50")
        measure = "net_of_returns" if _returns == "net" else "gross_sales"
        top = f"TOP {limit} "
        order_by = f" ORDER BY {measure} {order.upper()}"
```

and change the returned string to start with `"SELECT " + top + select_dims` and end with `+ group_by + order_by`.

In `build_sql`, before the final `raise ValueError`:

```python
    if metric == "unsold_items":
        dates = _sales_half_open_dates(filters)
        limit = int(filters.get("limit") or 20)
        if not 1 <= limit <= 50:
            raise ValueError("limit must be between 1 and 50")
        return (
            f"SELECT TOP {limit} COUNT(*) OVER () AS unsold_count, i.ItemCode, i.Name AS ItemName "
            "FROM t.Items i WHERE ISNULL(i.IsSuspended, 0) = 0"
            + _company_id_filter(cid, "i")
            + " AND NOT EXISTS (SELECT 1 FROM t.TransactionsHeaders th "
            + _detail_join()
            + "WHERE th.TransactionTypeID = 1 AND ISNULL(th.IsVoid, 0) = 0"
            + _company_id_filter(cid, "th", "td")
            + dates
            + " AND td.ItemCode = i.ItemCode) ORDER BY i.ItemCode"
        )
```

`core/agent.py` `run_metric` schema: add to the `metric` description `"unsold_items (مواد راكدة: active items with no sales in the period)"`, and add filter properties:

```python
                            "order": {"type": "string", "enum": ["asc", "desc"],
                                      "description": "With group_by: rank by the primary measure (asc = lowest first)."},
                            "limit": {"type": "integer", "description": "With order: top N rows, 1-50 (default 10)."},
```

Append to the `run_metric` function description (a general rule, not a phrase match — it must cover best/worst/top/bottom over any dimension, in any language): `"Ranked questions over any dimension (best/worst/top/bottom salesman, customer, item, day): metric=sales with group_by + order (desc for best, asc for worst) + limit, so the database ranks. For worst/bottom items also call unsold_items for the same period."` The system-prompt ranking rule from Task 3b already points here.

(The tool schema is part of every request; this one-time change re-warms the prefix cache once.)

- [ ] **Step 4: Run tests, check against the database, golden, commit**

Run: `py -3.13 -m pytest -q tests/test_metrics.py tests/test_agent.py` → PASS.

Run (read-only): `py -3.13 -c "import sys;sys.path.insert(0,'.');from core import metrics,sql;print(sql.run_select(metrics.build_sql('unsold_items',{'from_date':'2026-10-01','to_date':'2026-11-01'},company_id=1),company_id=1,client='105')[0])"`
Expected: `unsold_count` equals the golden runner's `unsold` reference (1,987 on the 2026-11-09 snapshot).

Golden `--baseline` → exit 0, `bottom10_items_plan` now passes.

```bash
git add core/metrics.py core/agent.py tests/test_metrics.py
git commit -m "feat(metrics): ranked sales by dimension and unsold_items for 'lowest items'"
```

---

### Task 15: Final verification and report

- [ ] **Step 1:** `py -3.13 -m pytest -q` → all PASS.
- [ ] **Step 2:** `py -3.13 setup/clear_plan_cache.py --client 105`, restart API, `py -3.13 evals/run_golden_session.py --baseline <BASELINE>` → exit 0.
- [ ] **Step 3:** `py -3.13 evals/run_evals.py` → accuracy ≥ baseline, isolation 100 %.
- [ ] **Step 4:** Write the before/after table (accuracy, usd/question off-peak and peak, p50 latency, calls/question, cache-hit %) into the PR description.

Targets (estimates from the 2026-11-09 log, to be confirmed by Step 2): golden accuracy 2/6 → ≥ 5/6; uncached input tokens ≈ 614k → ≈ 130k per 6 questions; USD/question off-peak ≈ 0.017 → ≈ 0.005; p50 latency ≈ 27 s → ≈ 18 s (contract call removed on SQL turns, fewer wasted calls, warm cache prefill).

---

## Not in this plan (measure first, decide later)

- **Lightweight docs-only prefix** (no 64k schema for how-to turns): large saving for Q6-type questions, but it is a second cached prefix and a routing risk; decide after Task 10's router data.
- **Per-tenant instead of per-session DeepSeek `user_id`**: could make the first call of every new chat a cache hit; verify with two golden sessions back-to-back after Task 8.
- **Smaller schema in the prefix** (retrieval of relevant tables): mainly a latency lever now that cached tokens are cheap; needs its own accuracy A/B.
- `core/reports.py` also uses inclusive `<=` for report params; leave until report templates are compared with the `Rpt_*` procedure semantics.
