# Chat thread, count check, and token trace

Owner: this file. Implement phases 1, 2, 2.5, and 3 in that order. Do not start phase 4 or workstreams C, E, F until their entry trigger fires. Workstream I slice 1 is phase 2.5, not a later UI project.

## Patch (accepted, overrides any older sentence in this file)

Reviewed against the code, then accepted.

- **P1.** `agent._stream_turn` already does `if not chunk.choices: continue` before `choices[0]`. The usage chunk has empty `choices`. `_logged_stream` must not index `choices[0]` either. It reads `chunk.usage` only. Every `trace.log_event` line includes `git_sha` (process-cached `git rev-parse HEAD`) and `prefix_hash` (sha256 prefix of `_static_prefix` for that client, noted when `ask_stream` builds it). Phase 1 is implemented in code. The live streamed check is still required before phase 2.
- **P2.** A header recount copies every predicate from the answer-backing statement whose column is on `TransactionsHeaders` (or `OrdersHeaders`). If a predicate uses a detail column, or the column is not in `schema_cache.json` for that header, do not recount. Append the warning only. Before writing the recount SQL, confirm `IsVoid` and `TransactionTypeID` exist on that header in `schema_cache.json`. If either is missing, warning only. `count_scopes` runs on the answer-backing SQL only, not on every probe. The recount `run_select` is not appended to `query_log` and must not become the card source.
- **P2.5.** Workstream I slice 1 (show `data.step` while the model streams, set the bubble from `data.answer` once) is phase 2.5. It starts when phase 2's correction can be appended. It is not deferred to a later UI project.
- **P3.** Card source is the single-row result in this turn's `query_log` that has a measure column (`gross_amount`, `sales_value`, `invoiced_amount`, `net_value`). If several, use the last of those. If none, the card is grouped: period and basis from the grouped query, no headline. Do not use `last_rows` (that is the longest list). `is_judgment` is true only when the question has a judgment lexeme (قديش, قدش, منيح, كثير) and has no month name, no digit, and no metric noun (مبيعات, فاتورة, طلب, مرتجع, sales, invoice). «قديش مبيعات اليوم؟» is not a judgment. A bare follow-up inherits the card's period only when `at` falls on the same Asia/Amman calendar day as now. Otherwise the prompt tells the model to ask which period. The card stays stored for the session (company switch still clears it) so a how-to in between does not delete it. Inheritance is same-day, not "any day until the session ends."
- **P4.** Accountant item 6 is one session: July sales, then a how-to, then «ونفس الشهر قبل الضريبة». The file has at least 10 questions. The implementing agent does not invent or edit those questions. A person writes them.
- **Before phase 3.** Count follow-up phrases (`نفس`, `قبل`, `بعد`, `قديش`) in `work/trace.jsonl` and in `work/sessions.sqlite` transcripts. Record the counts in this file. If both are under 5, stop and ask before writing `thread.py`. The 2 October failure is one session. It specifies the card. It does not prove weekly volume.
- **Before phase 2 recount.** One read-only query: `SELECT SYSDATETIMEOFFSET(), GETDATE()`. Compare the date to Asia/Amman. If `GETDATE()` is not Amman, period labels and recount bounds must not treat `GETDATE()` as an Amman calendar day. That check is not part of phase 1.

## Phase 1 status

Code is in `core/usage.py`, `core/llm.py` (`stream_create_kwargs`, `_logged_stream`), `core/trace.py` (`GIT_SHA`, `note_prefix_hash`), and `ask_stream` (one `Usage` per turn, passed into `complete`, including the f0 contract, logged after that contract returns). Tests: `tests/test_trace_usage.py` passed. Live check 3 October 2026: streamed «كم عدد الأصناف؟», trace `llm_calls=2`, `prompt_tokens=62229`, `completion_tokens=175`, `git_sha` and `prefix_hash` present, gears `f0` then `f0`. Phase 2 may start. The first live attempt logged only the tool-loop call because the contract ran after `log_event`. That order is fixed. Do not repeat the live check.

No second model that rewrites the question. No module-global usage counter. No 12-hour card expiry. «نفس», «قبل الضريبة», and «بعد المرتجعات» keep the card for the life of the session.

---

## Locked

1. Gate, `chatbot_ro`, tenant wall, no `EXEC`, no writes. `gate.validate` stays the only SQL door.
2. A number in the answer came from a tool result or from a card that was copied from one. Arithmetic goes through `run_select`, `run_metric`, or `analyze`.
3. `_static_prefix` bytes stay first. The card is a later message. A playbook edit misses the disk cache for the whole prefix. Observed once on 2 October 2026: first call of a turn was about 64,119 prompt tokens, all `cache_miss`. Do not remeasure by guessing. Deploy the one playbook sentence in phase 2 at low traffic.
4. Card source order: `run_metric` name and filters first, sqlglot on `run_select` second. Headline only if the answer table has one row. Last three cards. No person names taken from the question text. An id is kept only when it appears in the SQL or in metric filters.
5. Count grain is sqlglot scope analysis. A header-only `COUNT(*)` subquery plus a detail-join `SUM` is correct and must not warn. That is the shape of `metrics.build_sql` for `net_sales`.
6. `Usage` is created in `ask_stream` and passed into each `llm.complete`. Per call: `model`, `gear`, `prompt`, `completion`, `cache_hit`, `cache_miss`, `ms`. Streamed calls set `stream_options.include_usage` true. Phase 1 includes one live streamed check.
7. Integer-word matching («خمس فواتير», «فاتورتان») and “every number must appear in a tool row” are shadow fields on the trace. They do not change the answer until a measured false-positive rate exists. That measurement is not phase 1–3.
8. Default sales stay tax-inclusive (`line_amount_sql`: `ABS(Price)` minus the three discounts). Headlines for that basis say «شامل الضريبة». Changing the default to ex-tax is an open product decision. Do not do it here. July 2025 company 2: charged 520.84, before tax 449.00, and 449.00 × 1.16 = 520.84.
9. Eval integrity for this work is not a frozen holdout hash. It is an accountant-written question list, run three times, with flake defined below. Phase 4. Entry trigger is phase 3 merged.
10. Order is phase 1, then 2, then 3.

## What we have (read in code)

Request. `api/server.py` `ask` → sync `stream()` → `agent.ask_stream(...)` with `history` and `transcript`. `asgi_stream` runs that generator on a daemon thread, one thread per request. Threads overlap.

UI. `static/app.js` appends `answer_chunk` into the bubble, then on `data.answer` sets `bot.textContent = data.answer` (replaces the stream). Steps use `data.step`.

Prefix. `agent._static_prefix`: `prompts/system.md`, then full `prompts/join_playbook.md`, then `_schema_block`, then `_all_cards_block` if any.

After the prefix, still in `ask_stream`: optional vault cards (`vault.retrieve_cards`, not on fast-count or report path), path hints, `_conversation_block` (last `MAX_HISTORY_TURNS = 4`, answer clip 220, block cap 1200), `_transcript_index_block` (questions only, first plus latest 19, 80 characters).

Tools. `TOOLS` in `agent.py`. Paths: `_HOWTO_INITIAL_TOOLS`, `_FAST_PATH_SKIP_TOOLS`, `_REPORT_PATH_INITIAL_TOOLS`. Caps: `MAX_TURNS = 12`, `MAX_QUERIES = 4`, `MAX_DOC_SEARCHES = 3`, `MAX_VAULT_SEARCHES = 3`. Model sees at most `_ROW_DISPLAY_CAP = 50` rows. Gate `TOP` is `DEFAULT_ROW_CAP = 200`.

Gate. `gate.validate`. One statement, sqlglot `tsql`, rejects writes, `SELECT INTO`, `xp_`/`OPENROWSET`. `EXEC` only if listed. `allowed_procs` default empty. `sql.connect` is a new `pymssql` connection each call. Not pooled.

Session. `sessions.record_session_turn`: transcript cap 100, history cap 4. `IDLE_SECONDS` 30 days. Company change: `api/server.py` `_set_session_company` clears `history`, `transcript`, and `last_turn` when `CompanyID` changes. `recall_turns` strips digits via `_entities_hint`. `run_metric` in `_run_tool` appends only `result["sql"]` to `state["queries"]`. Filters are not stored. `last_rows` becomes whichever row list is longer, not the list behind the answer table.

Contract. `_final_contract` (`gear=f0`) returns `answer_md`, followups, confidence. Comment at `agent.py` around the contract constants: `answer_md` never replaces `final_text`. `_build_envelope` uses followups and confidence only. Append a correction onto `final_text` after `_resolve_final_text` and before the done payload. The f0 JSON cannot drop it, because it is not the answer body.

Usage. `llm._log_usage` prints and returns. `complete()` does not pass `stream_options`. `_logged_stream` keeps usage only when a chunk has `total_tokens`. Streamed turns can log nothing.

July, 2 October 2026, client 105, company 2. «صافي مبيعات يوليو» was `run_metric` `net_sales` (header `COUNT` subquery, charged `SUM`, date literals). «قبل الضريبة» was `run_select` (`TOP 6`, `YEAR`/`MONTH`, `COUNT(*)` on the detail join) and said 5 invoices. Truth: 5 detail rows, 2 headers.

Evals. `evals/run_evals.py` `_run_accuracy_corpus`: a passing non-refusal case with `answer_sql` that survives `gate.validate` is passed to `memory.promote_verified_query(..., source="eval")`.

---

## Phase 1 — Usage on the turn

**Goal.** Every model call in a turn is on the trace, including streamed calls.

**Why first.** The card adds uncached tokens after the prefix. There is no baseline until streams report usage.

### How

Add `core/usage.py`:

```
class Usage:
    def __init__(self): ...
    def add(self, *, model, gear, prompt, completion, cache_hit, cache_miss, ms) -> None
    def totals(self) -> dict   # llm_calls, prompt_tokens, completion_tokens,
                               # cache_hit_tokens, cache_miss_tokens, calls: list
```

`llm.complete(..., usage: Usage | None = None)`. After a non-stream response, `usage.add(...)` from `resp.usage` and the gear’s model name. For `stream=True`, pass `stream_options={"include_usage": True}` inside the create kwargs (OpenAI-compatible extra; if the SDK rejects that key, put it in `extra_body` and add a one-line comment naming which one the installed SDK accepted). `_logged_stream(gear, stream_iter, usage)` still yields chunks and calls `usage.add` from the last chunk that has usage.

`ask_stream` creates one `Usage` and passes it into every `complete` on that turn, including `_final_contract` and `_retry_empty_final`. Do not use a module list or a `ContextVar`. `asgi_stream` runs each request’s generator on its own thread. A global list mixes those threads.

Every `trace.log_event` for `answer`, `needs_ask`, and `refused` in `ask_stream` includes `**usage.totals()` plus `queries=len(state["queries"])`, `path=_path_flags(...)`, `result_rows` (length of `last_rows` or 0).

Missing usage fields count as 0. A completion with `usage is None` still increments `llm_calls` and sets that call’s tokens to null in `calls[]`. Do not invent a dollar rate. Do not call `/user/balance`.

### Tests

`tests/test_trace_usage.py`. Two fake usage objects (100/20 and 50/10) → `llm_calls=2`, `prompt_tokens=150`, `completion_tokens=30`, and `calls` length 2 with gears preserved.

One test that the kwargs built for `stream=True` contain include-usage. Construct the kwargs in a function `stream_create_kwargs(gear)` in `llm.py` so the test does not hit the network.

### Live check (this phase only)

After the unit tests pass, one streamed `POST /ask` against the local server, one short question («كم عدد الزبائن؟»), company already pinned. Then the last `work/trace.jsonl` line for that question must have `prompt_tokens > 0` and `llm_calls >= 1`. If tokens are 0, stop. Do not start phase 2. Do not run a five-question script.

### Exit

Unit tests green. One live trace line with non-zero prompt tokens. Rollback: stop passing `usage`. Prints remain.

---

## Phase 2 — Line count versus invoice count

**Goal.** The `net_sales` SQL is not flagged. A detail-join `COUNT(*)` described as فواتير is followed by a real header count.

**Why.** A string search for `COUNT(*)` and `TransactionsDetails` flags the metric SQL, because both strings appear. The live miss was `run_select`, not `run_metric`.

### How

`core/verify.py`:

`count_scopes(sql) -> list[{"grain": "headers"|"lines"|"other", "n_expr": "count_star"}]`

Parse with `sqlglot.parse(sql, read="tsql")`. For each `exp.Select`, if that select’s projection has `Count` of `Star`, look only at that select’s FROM and JOINs, not outer queries.

- Grain `headers` if every table in that scope is `TransactionsHeaders` or `OrdersHeaders` (schema `t` or bare).
- Grain `lines` if that scope joins `TransactionsDetails` or `OrdersDetails`.
- Else `other`.

`net_sales` has a header scope and a SUM on the outer join. No `lines` scope. No warning.

`needs_header_recount(answer, scopes) -> bool`

True when any scope is `lines` and the answer contains فاتورة or فواتير or `invoice` (case-insensitive), and the answer does not contain بنود or سطور or `lines`.

Do not parse «خمس» or «فاتورتان» in this phase. If those appear, log shadow field `count_phrase_unparsed: true` on the trace and do not recount.

`header_recount_sql(source_sql, schema_cache) -> str | None`

Run `count_scopes` on the answer-backing SQL only. Copy every predicate in that statement whose column is on the header (`TransactionsHeaders` or `OrdersHeaders` per `schema_cache.json` columns). Confirm `IsVoid` and `TransactionTypeID` are in that column list before emitting `ISNULL(IsVoid,0)=0` or `TransactionTypeID = 1`. If a predicate references a detail column, or either of those two columns is missing from the cache, return None and set `recount_skipped`. Do not drop a header predicate to make the recount "simpler." Date literals are not the only predicates that must survive. `GETDATE` / `DATEADD` / `EOMONTH` are not rewritten into Amman dates. Return None in that case. Do not append this SQL to `query_log`.

Append to `final_text`, after `_resolve_final_text`, before `_build_envelope` and `log_event`:

`عدد الفواتير: N`

when recount returns a row. If recount is skipped, append:

`تنبيه: العدد المذكور كفواتير هو عدد البنود، وليس عدد رؤوس الفواتير.`

Do not call the model to rewrite. Do not remove the model’s sentence.

Shadow, same turn, trace only: `ungrounded_numbers`, a list of digit sequences in the answer (Arabic-Indic folded to ASCII) that are not equal to any number in `last_rows` or the recount row, after stripping thousands separators. Do not change the answer from this list.

Playbook, one sentence under the invoice money block in `prompts/join_playbook.md`: an invoice count is `COUNT(*)` on `t.TransactionsHeaders` only. `COUNT(*)` on the join to `t.TransactionsDetails` counts lines. This changes `_static_prefix`. Ship phase 2 when a full-prefix cache miss is acceptable.

### Tests

`tests/test_verify.py`

- `build_sql("net_sales", ...)` → no `lines` scope.
- July-shaped join `COUNT(*)` plus answer «5 فواتير» → `needs_header_recount` true. Stub `run_select` returns `[{invoice_count: 2}]`. Appended text is `عدد الفواتير: 2`.
- Same SQL, answer «5 بنود» → no append.
- SQL with `GETDATE()` and «فواتير» → warning sentence, `recount_skipped`, no second number.
- Half-open is not this phase’s display problem. It is phase 3.

### Exit

Those tests pass. `net_sales` is not warned. Rollback: do not call `needs_header_recount`. Leave the playbook sentence.

---

## Phase 3 — Thread ring

**Goal.** «قبل الضريبة» and «نفس» use the last sales period for the rest of the session. A grouped result does not become “the number.” A how-to does not delete the ring.

**Why.** History keeps four answers at 220 characters. `run_metric` throws away filters. The before-tax turn had an empty transcript in the script and then guessed July from `MAX(TransactionDate)`.

### Card

`session["thread"]` is a list, length at most 3, oldest dropped. Each item:

| Field | Rule |
|---|---|
| `at` | `time.time()` when written |
| `company_id` | Session pin |
| `source` | `metric` or `select` |
| `metric` | Canonical name, or null |
| `filters` | Only `from_date`, `to_date`, `date`, `sales_person_id` from the tool args. Omit unknown keys |
| `period_label` | See below. Empty string if unknown |
| `basis` | `charged`, `ex_tax`, or `net_of_returns` |
| `grain` | `company`, `salesperson`, `customer`, or `item` |
| `id_filter` | Integer from SQL or from `sales_person_id`. Never a name from the question |
| `headline` | Set only when the table has exactly one row and a measure column |
| `invoice_count` | Set only when a `headers` scope or an `invoice_count` column exists |
| `tax_label` | `شامل الضريبة` when basis is `charged`. `قبل الضريبة` when `ex_tax`. `بعد المرتجعات` when `net_of_returns` |

No `also`. No name field.

**Which query.** `state["query_log"]` entries are `{name, args, sql, rows}`. The card source is the last entry whose `rows` is exactly one row and that row has a measure column. If none, the card is grouped: period and basis from the last business query that has a `GROUP BY` or more than one row, and `headline` is omitted. Do not pick `last_rows` just because it is the longest list. The recount query from phase 2 is not in `query_log`.

**Period label.** If `source=metric` and filters have `from_date` and `to_date`, label is `from_date .. to_date`. If only `date`, that day. If `source=select`, walk sqlglot for `GTE`/`LT`/`LTE` on `TransactionDate` or `OrderDate`. `>= 'YYYY-MM-01' AND < 'YYYY-MM-01'` of the next month labels as that first month, not as ending on the first of the next month. No literals, or `GETDATE`/`DATEADD`/`EOMONTH`: `period_label=""`. Do not call the database to fill it.

**Basis.** Metric `net_sales` or `net_sales_by_salesperson` → `charged` unless filters gain a basis later (they do not today). SQL: a projection that subtracts `TaxAmount` → `ex_tax`. Both type 1 and type 2 sums with a minus → `net_of_returns`. Else if the charged expression or `gross_amount` is present → `charged`. Else do not write a card.

**Headline.** Columns in order: `gross_amount`, `sales_value`, `invoiced_amount`, `net_value`. One row only. Zero rows or many rows: omit `headline`. `net_sales_by_salesperson` is many rows. The card may store `grain=salesperson` and the period. It must not store the first person’s amount as the company number.

**When to write.** After a successful answer with a business query. Not on `needs_ask`. Not when `extract` returns None (leave the ring unchanged).

**When to clear.** `_set_session_company` already clears history on company change. Also set `session["thread"] = []` there. Do not clear on how-to. Do not clear on a 12-hour clock. The card remains stored until the company changes or the session row is deleted. **Inheritance** of its period for a bare follow-up («نفس», «قبل الضريبة», «بعد المرتجعات», a judgment with no date) happens only when `at` is the same Asia/Amman calendar day as now. On a later Amman day the prompt says ask which period, and the render does not present the old period as the default. A new date in the user's question still wins when that turn's SQL succeeds.

**Render.** After `_conversation_block`, if the ring is non-empty and `company_id` matches and not `_is_howto_path`: up to three blocks, newest last, each under 200 characters, total under 500. Include `tax_label` on any line that shows `headline`. Instructions in that same message:

- «قديش» / «منيح» / «كثير»: cite the newest card’s headline, period, and `tax_label` if headline exists. If headline is absent, say the last result was a breakdown and do not quote one row as the total. At most one comparison query (the previous calendar month, same basis and grain). Do not invent a benchmark if that query is not run.
- «قبل الضريبة» / «بعد المرتجعات» / «نفس»: keep `period_label`, `grain`, and `id_filter`. Run SQL for the new basis. Do not say there are no earlier questions.
- A month, an id, or a basis written in this question wins over the card.
- How-to: do not render. Ring stays.

`thread.is_judgment(question)` is true only when the text has قدش, قديش, منيح, or كثير, and has no digit, no month name (يناير…ديسمبر, كانون, شباط, آذار, نيسان, أيار, حزيران, تموز, آب, أيلول, تشرين, and the English month names), and no metric noun (مبيعات, فاتورة, فواتير, طلب, مرتجع, sales, invoice). «قديش منيحين؟» is a judgment. «قديش مبيعات اليوم؟» is not: it names مبيعات, so it runs SQL. `ask_stream` calls `is_judgment`. If it is true, a card exists, and the card is the same Amman day, append the judgment instruction and do not remove SQL tools. If the function is not called from `ask_stream`, delete it.

`thread.should_ignore_thread` is `_is_howto_path`. Do not add a second Arabic list.

### Tests

`tests/test_thread.py` plus `tests/test_thread_prompt.py`.

- Metric args `from_date=2025-07-01`, `to_date=2025-07-31`, one row `gross_amount=520.84`, `invoice_count=2` → card as charged, headline 520.84, label شامل الضريبة. No regex required.
- `build_sql("net_sales_by_salesperson")` shape with two rows → no headline.
- SQL `>= '2025-07-01' AND < '2025-08-01'` → label July 2025, not 1 August.
- SQL with `GETDATE()` → `period_label=""`.
- Question text «عماد» and no id in SQL → `id_filter` null.
- Ring of 4 pushes drops the oldest.
- Company id mismatch → render returns "".
- Stubbed `complete`: five scripted turns (July metric, judgment, before tax, كيف أضيف عميل, ونفس الشهر). Assert `_static_prefix` output is byte-identical with and without a ring. Assert turn 5 messages contain `2025-07` and the how-to turn’s messages do not contain the card. Assert judgment instructions are present on turn 2. No network.

### Exit

Those tests pass. Rollback: pass `thread=None`. Stored JSON is ignored.

---

## Phase 4 — Accountant questions and flake

**Entry.** Phase 3 merged.

**Not a holdout hash.** Do not add `holdout: true`. Do not hash questions against `promote_verified_query` in this phase.

**Set.** `evals/accountant_july.jsonl`, written by a person, not copied from a passing model SQL. Minimum six questions, company 2, dates inside July 2025 only:

1. صافي مبيعات يوليو 2025. Expect charged 520.84, label شامل الضريبة, 2 invoices.
2. نفس الفترة قبل الضريبة. Expect 449.00 and 2 invoices.
3. وبعد المرتجعات. Expect charged minus type-2 charged. Type-2 count for that month was 0 on 2 October 2026. Recompute the gold with a read-only SQL before locking the file. If it is still 0, expect 520.84.
4. مبيعات كل مندوب في يوليو 2025. Expect no single headline treated as the company total. Imad’s invoice total was 520.84 on that date. Recompute before lock.
5. كم فاتورة بيع غير ملغاة في يوليو 2025. Expect 2.
6. One session, three lines: صافي مبيعات يوليو 2025, then كيف أضيف عميل؟, then ونفس الشهر قبل الضريبة. Expect 449.00 on the third line, not a docs answer and not a guessed other month. The file contains at least 10 questions in total. A person writes every question. The implementing agent does not add, reword, or "complete" that file.

Gold numbers are recomputed with `sql.run_select` once, by a person, and pasted into the file. They are not promoted.

**Flake.** Run the file three times with the real model, same session per question-pair, new session between items. A flake is any numeric token in the answer that is not the same integer or the same two-decimal number across the three runs. Ship bar: zero flakes on items 1, 2, 5, and 6. Items 3 and 4 may be marked `unstable` in the file if they flake, and then they are not a gate. Do not lower the bar by editing the gold to match a run.

**Promote.** `_run_accuracy_corpus` must not be pointed at this file. `promote=False` if someone adds a loader. A comment is not enough: the loader is not added to `_DEFAULT_SUITES`.

---

## Workstream C — Knowledge

**Not in phases 1–3.** Spec below. Start only when the trigger fires.

**Entry trigger.** Either (a) `_schema_block` length, logged once at process start, exceeds 40,000 tokens by a `tiktoken` cl100k count or by `len(text)/4` if tiktoken is not installed, or (b) a table appears in `schema_cache.json` `tables` that is absent from `prompts/join_playbook.md` and from `metrics.METRICS`, and a trace from that week shows a wrong join or a wrong filter on that table.

**New table or column without a code deploy.** `work/<client>/schema_cache.json` is already produced by `setup/02_introspect.py` and read by `_schema_block` and `gate.validate`. Refreshing that file and restarting the process updates columns the model can see. No git release. Playbook sentences and `line_amount_sql` still need a deploy. Do not pretend a restart-free reload exists until this trigger fires. When it fires, add `GET /admin/reload-schema` that re-reads `schema_cache.json` into the process cache. It does not reload `metrics.py`.

**Stale notes.** When the trigger fires, a setup script compares `schema_cache.json` column names to vault table notes’ column lists and writes `work/<client>/stale_notes.json` (`table`, `missing_in_note`, `missing_in_db`). It does not edit the vault. A human updates the note.

**Metrics as versioned data.** Do not move `build_sql` in phases 1–3. Trigger to move: the same metric SQL must change for a second client without a shared formula, or `metrics.py` changes twice in 30 days with no schema change. Then load `knowledge/metrics/<name>.json` (`version`, `basis`, `sql` with `{company_id}` forbidden — company stays injected in code). Tests render each file through `gate.validate`. A file that fails validation is not loaded. Code keeps the loader and the gate. The SQL text lives in the file.

**Failure.** A bad JSON metric ships a wrong total. Mitigation: validation test is required for the file to load. Rollback: delete the file. Code path remains `build_sql`.

---

## Workstream E — Second worker

**Not in phases 1–3.**

**Entry trigger.** A second OS process must serve `POST /ask` for the same `session_id` at the same time. One process is not this trigger. A high CPU reading is not this trigger.

**Until the trigger.** Sessions stay in `work/sessions.sqlite` plus the process dict (`sessions.py` docstring). `sql.connect` stays one connection per call.

**When the trigger fires.** Session reads and writes go only through SQLite (delete the process-dict shortcut, or make it process-local and correct by reading SQLite on every `/ask`). Do not add Redis in the same change. Connection pooling starts only if, after that, `tools_ms` for `run_select` shows connect setup as more than half of `tools_ms` on 20 traced queries. Pool size equals worker count, not a guessed number.

**Failure.** Two workers, dict still hot: turn N+1 does not see the card. Rollback: one worker.

---

## Workstream F — Security and traces

**Not in phases 1–3.** Do not weaken the gate while doing them.

**Injection through rows. Entry trigger.** A traced answer follows an instruction that was present in a selected cell (for example a customer name or a note column containing “ignore your rules”). Until that event, do not add a second filter. When it fires: tool results are wrapped as data, and `run_select` results are passed with a one-line system reminder that cell text is data. That reminder is after the prefix. Measure one cache miss.

**Per-user role. Entry trigger.** A product owner names two roles that must not see the same columns, in writing. Until then every session is the pinned company, read-only, which is today’s `SESSION_CONTEXT`. Options when the trigger fires, in this order: (1) two `t.` view sets selected by an env role, still one login `chatbot_ro`. (2) a second SQL login. Do not do (2) first. The browser does not send the role. The server maps the authenticated user to the role. There is no per-user login in the app today. Building accounts is part of this trigger, not a side task.

**Trace retention. Entry trigger.** `work/trace.jsonl` exceeds 100 MB, or the owner asks for a retention period. Then delete lines with `ts` older than 30 days at process start. Do not delete inside the request path. Questions and SQL in the trace can contain names. That is why the cap exists. Do not add a new log store.

**Provider contract.** Customer rows go to DeepSeek. That stays an owner decision. This plan does not allow or forbid it.

---

## Workstream I — UI states

**Not a visual rewrite in phases 1–3.** The done payload already replaces the bubble (`static/app.js`, `data.answer` branch).

**Entry trigger for the first slice.** This slice is phase 2.5. It starts as soon as phase 2 can append a correction, because the bubble currently paints `answer_chunk` tokens and then replaces them (`static/app.js`).

**Slice behavior.** While `answer_chunk` events arrive, the bubble shows the latest `data.step` text, not the tokens. Store tokens in a variable. On `data.answer`, set the bubble to `data.answer` once. Do not paint tokens and then replace them. Status strings already exist (`running query N of 4` from `_step_label`). Empty step: show «جارٍ التحقق». Error `data.error`: show that string, leave the previous answer in the thread above, do not clear the session. Partial failure (HTTP 200, empty answer, `needs_ask` set): show `needs_ask` and do not append a fake total.

**Later slices, each with its own trigger.**

| Slice | Trigger | Spec |
|---|---|---|
| Headline row | Phase 3 merged and a card has `headline` | Above the prose: the number, `tax_label`, `period_label`. Not a second model call. Fields come from the done JSON. Add `thread_head` to the done payload in phase 3 so this slice does not parse Arabic. |
| SQL disclosure | A user asks for it in a ticket, or support copies SQL out of traces twice in a week | `<details>` with `answer_sql`. Closed by default. |
| Follow-up chips | Phase 3 merged | Three buttons from the card, not from `_final_contract`: قبل الضريبة, بعد المرتجعات, الشهر السابق. Click sends that text. |
| Edit, rename, export, charts, shortcuts | A named UI bug, not this plan | Do not build from this document. |

**Rollback of the first slice.** Paint `answer_chunk` again. Done payload still wins today, so rollback restores the flicker and not a lost answer.

---

## Tests (all phases)

| Test | Phase | Network |
|---|---|---|
| `tests/test_trace_usage.py` | 1 | No |
| One streamed `/ask`, trace `prompt_tokens > 0` | 1 | Yes, one question |
| `tests/test_verify.py` | 2 | No, stub `run_select` |
| `tests/test_thread.py`, `tests/test_thread_prompt.py` | 3 | No, stub `complete` |
| `evals/accountant_july.jsonl` × 3 | 4 | Yes, after phase 3 |
| `evals/run_evals.py` isolation | any deploy | Yes, existing suite. One leak fails the process |

Do not run the 69-question battery for this work.

---

## Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| `include_usage` rejected by the SDK | Medium | Phase 1 live check shows 0 tokens | The kwargs test records where the flag was set. If the live check is 0, try `extra_body` before any card work |
| Recount dates do not match the user’s month | Medium | A second wrong count | Literals only. Else the warning with no number |
| Card taken from a probe query | Medium | Follow-up cites the probe | `query_log` tied to `last_rows` |
| Session-long card after a topic change that is not how-to | Medium | «نفس» applies to an old month the user forgot | User-stated dates replace the period on the next successful SQL. Company switch clears the ring |
| Playbook sentence cache miss | Certain once | About one full prefix billed per warm chat | Phase 2 deploy at low traffic |
| Global `Usage` | High if someone uses a list on `llm` | Mixed tenants on the trace | Code review: `Usage()` is local to `ask_stream` |

## Open decisions

1. **Ex-tax as the default number.** Recommendation: no. Label «شامل الضريبة». Switching makes «صافي مبيعات يوليو» return 449.00 instead of 520.84 and needs new gold. Owner can override.
2. **Sending ERP rows to DeepSeek.** Owner decision. Not decided here.
3. **Role-separated columns.** No work until an owner names the two roles. See workstream F.
4. **Second worker and Redis.** No work until a second process must share a `session_id`. See workstream E.

## Do not build

- A rewriter model. The card holds the missing slots.
- Sub-agents. One loop, `MAX_QUERIES = 4`.
- A vector index. Docs are FTS5 trigram (`core/docs.py`). Miss rate is unmeasured. Measure the docs JSONL before changing the tokenizer.
- An LLM judge on totals.
- A 12-hour TTL. Rejected. «نفس» and «قبل الضريبة» are session-long.
- Auto-writing eval files from traces.
- Dollars on the trace before a rate is written down by a person.

## Devil’s advocate

Phase 3 can be wrong if users rarely follow up and the stubbed test is the only proof. Evidence that would stop phase 3 after phase 2: 50 traced sessions and fewer than 5 second-turns that refer to the first (`نفس`, قبل, بعد, قديش). Count those strings in `trace.jsonl` before writing `thread.py` if you want a kill switch. The 2 October failure is one session, which is enough to specify the card and not enough to prove weekly volume.

Recount can be wrong if the date predicate is not a pair of literals. The plan refuses to recount then. Evidence to drop recount entirely: the playbook sentence alone, and the next 20 sales traces contain no detail-join `COUNT(*)`. Check that before adding `header_recount_sql` if you want to cut scope. Default is to keep it, because the model already had money rules in the playbook and still said 5 invoices.

## KPI

| KPI | Baseline | Target | When |
|---|---|---|---|
| Streamed `prompt_tokens` | Can be 0. `include_usage` is off | `> 0` on the one live check | Phase 1 exit |
| `net_sales` SQL flagged as line count | Would be flagged by a string search | 0 in `test_verify` | Phase 2 |
| July join-count prose | Said 5. Truth 2 | Appended text contains `عدد الفواتير: 2` | Phase 2 test |
| Turn 5 prompt contains July after a how-to | Failed in the no-transcript script | Stubbed test asserts `2025-07` | Phase 3 |
| `_static_prefix` bytes vs card | Card not built | Identical | Phase 3 |
| Accountant set flakes | Unmeasured | 0 on items 1, 2, 5, 6 across 3 runs | Phase 4 |
| p95 latency | Unmeasured | Do not set | After 50 phase-1 traces |
| Docs top-5 miss rate | Unmeasured | Do not set | Before any tokenizer change |
