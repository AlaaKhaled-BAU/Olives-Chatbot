# Junior execution plan: transcript, hydrate, feedback-by-id, tools_ms

Status: READY TO IMPLEMENT (literal executor)
Python: **python3.13 only**. Never `python3`.
Branch: `deepseek-swap`
Do not: OTel, Redis, new sqlite files, compaction, raise `MAX_HISTORY_TURNS`, new HTTP path `/session`.

If a test fails, stop. Do not “improve” prompts, gate, or SQL.

---

## Goal (one sentence)

Keep a **UI transcript** (full answers, cap 100) in the existing session blob while the **model** still sees only the last 4 compressed turns. Reload paints bubbles from `GET /context`. Thumbs target a `turn_id`. JSONL gets `tools_ms`.

## Locked decisions

D1 leftover including `tools_ms`. D2 hydrate on **GET /context** only. D3 full `a` on transcript. D4 full SQL on transcript. D5 unit tests **and** visit-battery transcript length. D6 no compaction TODO.

## What you must not change

- `MAX_HISTORY_TURNS` stays **4** (`core/agent.py`).
- `del hist[:-agent.MAX_HISTORY_TURNS]` stays on **`history` only**.
- Company switch still clears memory (extend to `transcript`).
- `trace.log_event` signature stays `**fields` (already). Do not add Prometheus labels per tool.
- Do not import FastAPI from `evals/`.

---

## Shared helper (do this first; both lanes import it)

**File:** `core/sessions.py`

Add two functions. Do not rename `save`/`load`/`sweep`.

```python
import uuid
import time

TRANSCRIPT_CAP = 100


def record_session_turn(session: dict, question: str, result: dict) -> str | None:
    """Append UI transcript (full text) and model history (compressed).
    Returns turn_id or None if there is no answer to record.
    result is the ask_stream `done` event dict.
    """
    answer = result.get("answer")
    if answer is None or not str(answer).strip():
        return None
    turn_id = uuid.uuid4().hex
    sql_full = result.get("answer_sql") or ""
    session.setdefault("transcript", [])
    session["transcript"].append({
        "id": turn_id,
        "q": question,
        "a": str(answer),           # FULL — D3
        "sql": sql_full,            # FULL — D4
        "ts": time.time(),
        "cache_key": result.get("cache_key"),
        "client": None,             # server fills this
        "company_id": None,         # server fills this
    })
    del session["transcript"][:-TRANSCRIPT_CAP]
    hist = session.setdefault("history", [])
    hist.append({
        "q": question,
        "a": str(answer)[:400],
        "sql": sql_full[:200],
    })
    from core import agent as _agent
    del hist[:-_agent.MAX_HISTORY_TURNS]
    return turn_id
```

**Junior note:** avoid circular import. `core/sessions.py` must **not** import `core.agent` at module top. Either:

- pass `max_history: int = 4` as an argument with default `4` matching `MAX_HISTORY_TURNS`, **or**
- `from core import agent as _agent` **inside** the function after the transcript append.

Prefer **argument** `max_history: int = 4` and a comment: `# must equal agent.MAX_HISTORY_TURNS`. Server and visit battery pass `agent.MAX_HISTORY_TURNS`.

Fill `client` and `company_id` on the transcript row **in the server** after the helper returns (helper stays DB-free). Simpler: helper accepts `client` and `company_id` kwargs.

**Final helper signature (copy this exactly):**

```python
def record_session_turn(
    session: dict,
    *,
    question: str,
    result: dict,
    client: str,
    company_id,
    max_history: int,
) -> str | None:
```

If no answer: return `None` and do not append.

Add tests in `tests/test_session_memory.py` (file already exists) **or** `tests/test_api.py`:

1. Six fake `done` events → `len(history)==4`, `len(transcript)==6`, last transcript `a` is the full 500-char string you passed, history `a` is 400 chars + not equal to full if you used 500 chars.
2. `company_id` stored on transcript rows.

---

## Parallel regions

Two people (or two worktrees) **after** the helper exists and its unit test is green.

```
          [Lane 0] core/sessions.py helper + unit test
                         |
         +---------------+----------------+
         |                                |
    [Lane A]                         [Lane B]
    api/server.py                    core/agent.py tools_ms
    GET /context                      (no UI)
    POST /feedback
    tests/test_api.py
    tests/test_feedback.py
         |
    [Lane C]  waits for Lane A JSON shape
    static/app.js hydrate + turn_id
         |
    [Lane D]  waits for helper (Lane 0)
    evals/run_visit_battery.py
```

| Lane | Files | Depends on | Can start |
|------|--------|------------|-----------|
| 0 | `core/sessions.py`, `tests/test_session_memory.py` | — | immediately |
| A | `api/server.py`, `tests/test_api.py`, `tests/test_feedback.py` | Lane 0 | after Lane 0 green |
| B | `core/agent.py` only | — | **in parallel with Lane 0** (does not use helper) |
| C | `static/app.js` | Lane A (`transcript[].id`) | after Lane A |
| D | `evals/run_visit_battery.py` | Lane 0 | after Lane 0 |

**Conflict:** Lane A and Lane B do **not** both edit `agent.py`. Lane A only reads `done` events. If Lane B adds `tools_ms` on `done`, Lane A ignores extra keys (do not crash).

**Do not** parallelize Lane A + C in two worktrees both touching `app.js`.

---

## Lane 0 — helper (blocking)

1. Implement `record_session_turn` in `core/sessions.py` as specified.
2. Unit test: 6 turns, 500-char answer on turn 1, assert transcript[0]["a"] length 500, history[-1]["a"] length <= 401 (400 plus possible ellipsis only on the **agent** compressor; here history uses `[:400]` slice, so length == 400).
3. `python3.13 -m pytest tests/test_session_memory.py -q` (or the file you added tests to) must pass.

---

## Lane A — API (after Lane 0)

### A1. `api/server.py` imports

- `from core.sessions import record_session_turn` (module is already `from core import ... sessions`).
- Keep `import` style consistent with the file (it uses `from core import agent, ... sessions`).

### A2. `_touch_session`

Next to `state.setdefault("history", [])` add:

```python
state.setdefault("transcript", [])
```

### A3. `_set_session_company`

When company changes (existing `if prev is not None and int(prev) != int(cid)`), also:

```python
session["transcript"] = []
```

Keep `history = []` and `pop("last_turn")`.

### A4. `/ask` done branch (replace the current `hist.append` / `del hist` block)

**Today (delete this block):** `session["last_turn"] = {...}` then `hist.append` then `del hist[:-agent.MAX_HISTORY_TURNS]`.

**Replace with:**

```python
cid = session["conversation"].get("CompanyID")
turn_id = record_session_turn(
    session,
    question=req.question,
    result=result,
    client=client,
    company_id=cid,
    max_history=agent.MAX_HISTORY_TURNS,
)
session["last_turn"] = {
    "client": client,
    "company_id": cid,
    "question": req.question,
    "answer_sql": result.get("answer_sql"),
    "cache_key": result.get("cache_key"),
    "turn_id": turn_id,
}
```

`record_session_turn` already appends history. Do **not** append history twice.

`needs_ask` path: do **not** call `record_session_turn` (no answer). `last_turn` unchanged or leave previous.

### A5. `GET /context`

Do **not** put SQL/DB logic in `_context_payload` for transcript.

```python
@app.get("/context")
def get_context(session_id: str | None = None):
    client = pinned_client()
    transcript = []
    if session_id:
        session = _touch_session(...)
        _ensure_session_company(session, client)
        conversation = session["conversation"]
        transcript = list(session.get("transcript") or [])
    else:
        conversation = {}
    payload = _context_payload(client, conversation)
    payload["transcript"] = transcript
    return payload
```

No `session_id` → `"transcript": []`.

Update `test_context_endpoint_returns_shape`: if it mocks `_context_payload` only, `get_context` still adds `transcript`. Either:

- assert `resp.json()["transcript"] == []` when using real `get_context` with a session that never asked, **or**
- keep the mock test but add a **new** test that does not mock `_context_payload`.

### A6. `FeedbackRequest`

```python
class FeedbackRequest(BaseModel):
    session_id: str
    helpful: bool
    reason: str | None = None
    turn_id: str | None = None
```

### A7. `feedback()` resolver

After loading `session` from `SESSIONS` (existing):

```python
turn = None
if req.turn_id:
    for row in session.get("transcript") or []:
        if row.get("id") == req.turn_id:
            turn = {
                "client": row.get("client") or client,
                "company_id": row.get("company_id"),
                "question": row["q"],
                "answer_sql": row.get("sql"),
                "cache_key": row.get("cache_key"),
            }
            break
    if turn is None:
        raise HTTPException(status_code=404, detail="unknown turn_id")
else:
    turn = session.get("last_turn") if session else None
```

Then keep the existing promote / negative / gate logic on `turn`. If `company_id` on the row is None, keep the existing fallback `_resolve_context_company_id`.

Old clients that omit `turn_id` still work (D1 compat).

If `session` is None: 404 as today.

### A8. Tests (copy style from `tests/test_feedback.py` `_ask`)

Add to `tests/test_api.py` and `tests/test_feedback.py`:

**test_six_asks_transcript_keeps_six_history_keeps_four**

- Unique `session_id`.
- Loop `i in range(6)` `_ask` with `question=f"q{i}"`, `answer` from mock `done` = `"A"*500` on i==0 else `f"ans{i}"`, `answer_sql=f"SELECT {i}"`.
- `GET /context?session_id=...`
- `len(data["transcript"])==6`
- `data["transcript"][0]["a"] == "A"*500`
- `data["transcript"][0]["sql"] == "SELECT 0"`
- Patch `agent.ask_stream` and **capture** the `history=` kwarg on the **6th** call: `len(history)==4`.

How to capture: `def fake_stream(*args, **kwargs): captured.append(kwargs.get("history")); return [done_event]`

**test_company_switch_clears_transcript**

- Two asks, then `POST /context` with a **different** `company_id` that `_load_companies_live` accepts. Easiest: patch `_load_companies_live` to return `[{"id":1,"name":"A"},{"id":2,"name":"B"}]`, first ask with company 1, POST company 2, GET /context → `transcript == []`.

If POST /context is hard to set up, unit-test `_set_session_company` directly with a dict session (no TestClient). That is enough.

**test_feedback_turn_id_not_last** (`tests/test_feedback.py`)

- Ask session `old1` with sql `SELECT 1`.
- Ask same session with sql `SELECT 2` (different question).
- GET /context, `tid = data["transcript"][0]["id"]`
- POST `/feedback` `{"session_id", "helpful": true, "turn_id": tid}`
- `memory.get_verified_query` for the **first** question equals `SELECT 1`, **not** `SELECT 2`.

Need `company_id` on the row. `_ask` must run `_ensure_session_company` so CompanyID is set (existing `_ask` already posts `/ask` which sets company). Patch `memory.DB_PATH` like existing tests.

**test_context_without_session_id_has_empty_transcript**

- `GET /context` → `transcript == []`.

Run:

```bash
python3.13 -m pytest tests/test_api.py tests/test_feedback.py tests/test_session_memory.py -q
```

---

## Lane B — tools_ms (parallel with Lane 0)

**File:** `core/agent.py` only.

1. After `state` is created in `ask_stream` (search `state = {` in `ask_stream`), set:

```python
state.setdefault("tools_ms", {})
```

If `state` is a new dict literal, add `"tools_ms": {}` there.

2. Wrap **only** the existing `_run_tool(...)` call (~line 1704):

```python
t0 = time.monotonic()
try:
    result = _run_tool(...)
except gate.GateError as e:
    ...
except Exception as e:
    ...
finally:
    ms = int((time.monotonic() - t0) * 1000)
    state["tools_ms"][name] = state["tools_ms"].get(name, 0) + ms
```

Put `t0` **before** try so GateError still records time. `name` is the tool name already in that loop.

3. Every `trace.log_event(...)` in `ask_stream` that already runs on the success/refuse paths: add `tools_ms=state.get("tools_ms") or None`. If empty dict, pass `None` or omit. Prefer omit empty so JSONL stays small: `if state.get("tools_ms"):` then pass it.

4. Add `tools_ms` on the **`done` yield** (the big one ~1782):

```python
"tools_ms": dict(state.get("tools_ms") or {}),
```

Early `done` for `needs_ask`: omit `tools_ms` or `{}`. Server must not require the key.

5. Test: `tests/test_agent.py` or a tiny new test that mocks `_run_tool` / patches a tool to sleep 0 and asserts `done["tools_ms"]` has key `search_docs` **or** mock `time.monotonic` to jump 0.05s.

If agent tests are heavy, a unit test of the wrap is enough: patch `_run_tool` to return `{}` and `time.monotonic` to `[100.0, 100.05]` → `tools_ms[name]==50`.

Run:

```bash
python3.13 -m pytest tests/test_agent.py -q --tb=no -x
```

If that file is huge, add `tests/test_tools_ms.py` with one test and run that file only.

---

## Lane C — UI (after Lane A)

**File:** `static/app.js` only.

### C1. Replay helper

After `addMessage` (~line 120), add `replayTranscript(transcript)`:

- If `!transcript || !transcript.length` return.
- Hide empty-state the same way `addMessage` does.
- For each row: `addMessage(row.q, "user")`; `const bot = addMessage(row.a, "bot")`; if `row.sql` call `addSqlPanel(bot, row.sql, null)`; `addFeedbackRow(bot, row.id)`.

### C2. `addFeedbackRow(bot, turnId)`

Change signature. Inner fetch body:

```javascript
JSON.stringify({ session_id: sessionId(), helpful, turn_id: turnId || undefined })
```

Live SSE path: `addFeedbackRow(bot)` today after final answer. Pass the turn id from the **done** frame.

**Server must put `turn_id` on the SSE `done` JSON.** Lane A: when yielding the answer frame, include `"turn_id": turn_id` next to `answer`.

Junior: in `/ask` `json.dumps({ 'answer': answer, ...})` add `'turn_id': turn_id`.

### C3. `loadContext`

After a successful `ctx` parse, call `replayTranscript(ctx.transcript || [])`.

**Do not** replay twice on every company refresh if the DOM already has messages. Simplest junior rule:

- If `#messages` already has `.msg` children, **skip** replay (company change already cleared server transcript; user still seeing old DOM is a separate bug).

**Better junior rule for company change:** on `companySelect` `change`, after POST /context, `messages.innerHTML = ""` then `loadContext()` which replays (now empty). Otherwise old bubbles from company 1 stay on screen while server transcript is empty.

**Required:** in `companySelect` change handler, before `loadContext()`:

```javascript
document.getElementById("messages").innerHTML = "";
```

Then loadContext replays empty → empty chat. Show empty-state if you have that node (remove `hidden` from `#empty-state` if present).

### C4. Live ask

Keep rendering SSE as today. After done, feedback row uses `data.turn_id`.

Do not also append to a client-side transcript array.

No browser automation required for merge. Executor: `python3.13 -m pytest tests/test_api.py tests/test_feedback.py -q`.

---

## Lane D — visit battery (after Lane 0)

**File:** `evals/run_visit_battery.py`

This file calls `agent.ask_stream` **directly**. It never hits FastAPI. `GET /context` is **not** available here unless you start uvicorn. Do **not** start a server in this eval.

**Instead (D5 intent):** after each successful `done` with an answer, call the **same** `record_session_turn` on `session_state` that the API uses.

In `run_one`, replace the current `hist.append` / `del hist` block (~lines 86–95) with:

```python
from core.sessions import record_session_turn
record_session_turn(
    session_state,
    question=question,
    result=result,
    client=client,
    company_id=COMPANY_ID,
    max_history=agent.MAX_HISTORY_TURNS,
)
```

`ask_stream` still receives `history=session_state["history"]` (the compressed list).

After all `chain-a` scenarios in `main` (read the file’s loop), assert:

```python
# session dict for chain-a has transcript length 3
assert len(sessions["chain-a"].get("transcript") or []) == 3
```

If `main` stores per-session state in a dict `states[session_key]`, assert on that.

If a chain turn has empty answer, length may be < 3. Then assert `len(transcript) == count of non-empty answers` or skip assert when any fail. Document in a comment.

**GET /context contract** is Lane A TestClient tests, not this file.

---

## Acceptance (all lanes)

```bash
python3.13 -m pytest tests/test_session_memory.py tests/test_api.py tests/test_feedback.py tests/test_tools_ms.py -q
```

(`test_tools_ms.py` only if you created it.)

Manual (human, not required to merge): open `http://localhost:8100`, ask twice, refresh, both bubbles remain, thumbs on first still 200.

---

## NOT in scope (do not implement)

Redis, Celery, OTel, Jaeger, GET /session, new sqlite, compaction, vector memory, React, widget, login, raising model history, Prometheus per-tool labels, logging full SQL in `tools_ms`, **FTS morphology** (see `plans/fts_morphology_v1.md`).

---

## What already exists

| Piece | Where |
|-------|--------|
| Session blob | `core/sessions.py` `save`/`load` |
| Model window | `_conversation_block`, `MAX_HISTORY_TURNS=4` |
| Persist after ask | `_persist_session` |
| Feedback promote | `tests/test_feedback.py` |
| Context fetch | `loadContext()` in `static/app.js` |

---

## GSTACK REVIEW REPORT

| Review | Status |
|--------|--------|
| Eng leftover | APPROVED, this file is the executor spec |
| Autoplan | not run |

NO UNRESOLVED DECISIONS
