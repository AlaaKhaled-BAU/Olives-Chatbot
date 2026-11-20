# Consumption Monitor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Record each finished chat's cache-hit, cache-miss, and completion tokens, price them in USD from env rates, and expose the totals on a read-only JSON endpoint an Olives developer can open on the same host as `/health`.

**Architecture:** `core/consumption.py` owns the rate card, the USD formula, and a gitignored SQLite file `work/consumption.sqlite`. `POST /ask` already finishes with one `done` event whose token fields come from `core.usage.Usage` (filled by `core/llm.py` from the provider usage object). The server adds those integers into the SQLite row for `(client, company_id, session_id, UTC day)` and does not call the model again. `GET /usage` reads the counters and multiplies by the current env rates, so cash is calculated when someone looks, not when the chat finished. There is no login. v1's "user" is the chat `session_id`. A later login replaces that key only; the USD function stays the same.

**Tech Stack:** Python 3.13 (`py -3.13`), stdlib `sqlite3` and `decimal`, existing FastAPI app in `api/server.py`, pytest. No new dependency.

## Global Constraints

- Python 3.13 only (`py -3.13 -m pytest …`). Never `python3`.
- Do not start the chatbot. Do not listen on or request port 8100. Tests use in-process calls and, for the route only, `fastapi.testclient.TestClient` (it does not bind a port).
- No secrets in git. Do not print or return `DEEPSEEK_API_KEY`. Do not commit `.env`. Document the three rate names and the off-peak numbers in `.env.example` only (no second config file). The same numbers also live in code as the fallback when the env var is missing. Real overrides live in gitignored `.env`.
- Do not edit `prompts/`, `core/gate.py`, or `core/sql.py`. Do not open SQL Server from the monitor. Do not bill SQL result rows.
- `work/` is gitignored. The new database is `work/consumption.sqlite` only. Honor `CHATBOT_WORK_DIR` the same way `core/sessions.py` does, so tests never write the developer's real file.
- Tenant stays pinned by `CHATBOT_CLIENT`. The browser cannot pick the client on `/usage`.
- One rate card. Do not auto-switch peak vs off-peak. Do not add a second card for `deepseek-v4-pro`.
- No auth middleware, API key, or login. No reset endpoint. No prompt text in the JSON or in the SQLite row.

---

## Verified baseline (do not re-discover)

These are the facts in the tree this plan was written against. Line numbers drift; search the quoted code if a line moved.

**There is no end-user login.** `CHATBOT_CLIENT` pins the tenant (`api/server.py` `pinned_client()`). A chat sends `session_id` on `AskRequest`. `POST /ask` hashes it for the trace subject only:

```python
subject = hashlib.sha256((req.session_id or "anon").encode()).hexdigest()[:12]
```

That 12-hex `subject` is not the consumption key. The monitor stores the raw `session_id` (or `anon`) so a developer can look up the chat they have open. `static/app.js` `sessionId()` is a `crypto.randomUUID()` kept in `sessionStorage`.

**Token totals already exist.** `core/usage.py` `Usage.totals()` returns `llm_calls`, `prompt_tokens`, `completion_tokens`, `cache_hit_tokens`, `cache_miss_tokens`. `core/llm.py` fills them from `prompt_cache_hit_tokens`, `prompt_cache_miss_tokens`, and `completion_tokens`. `core/agent.py` copies those totals onto the main answer `done` events (plan-cache replay around the `source="plan_cache"` yield, and the final yield at the bottom of `ask_stream`). Two early `done` yields do **not** copy them today:

- calendar short-circuit: `yield {"type": "done", "answer": None, "needs_ask": calendar_ask}`
- `ask_user`: `yield {"type": "done", "answer": None, "needs_ask": asked}`

`ask_user` has already called the model. `Usage` has the tokens, and `_turn_trace` writes them to `work/trace.jsonl`, but the `done` dict the server sees omits them. Task 3 stamps all four `done` yields from the same `Usage` object. Do not parse `trace.jsonl` for billing: each line contains the question text.

**`prompt_tokens` overlaps the cache split.** DeepSeek's input bill is hit tokens plus miss tokens. `prompt_tokens` is about that sum, not a third input class. The USD formula uses hit, miss, and completion only. Adding `prompt_tokens` on top would double-charge input. If a finished turn has `prompt_tokens > 0` and both cache counters are 0, v1 still bills input as 0. Do not invent miss tokens from `prompt_tokens`.

**Tool rows are not tokens.** `trace.log_event` stores `result_rows`. The `done` event can also carry `queries` and a table. None of those are tokens.

**Routes today:**

| Route | What it returns | Decision |
|---|---|---|
| `GET /health` | JSON liveness: `provider`, `ok`, `pinned_client`, per-client `db` probe. No token fields. | Do not extend. A health probe would start doing billing I/O, and the shape is not usage. |
| `GET /metrics` | Prometheus text (`generate_latest()`, `CONTENT_TYPE_LATEST`). Not JSON. | Do not extend. A JSON field would break scrapers. |
| `GET /context` | Company picker plus `transcript` (question text). | Do not extend. Spend must not sit next to prompts. |
| `GET /usage` | Does not exist. | **Add this.** Register it next to `/health`, above `app.mount("/")`. |

**Eval prices are not the runtime card.** `evals/run_golden_session.py` has `OFFPEAK = {"hit": 0.003, "miss": 0.15, "out": 0.60}` and `PEAK` at double (`0.006`, `0.30`, `1.20`), USD per 1M tokens, and `cost_usd()` divides by `1e6`. Those are the v1 defaults. `plans/deepseek_swap_parallel_plan.md` lists a different flash card (`0.007 / 0.22 / 0.66` off-peak). Do not "correct" the defaults to that document, and do not import the eval module from `core/`. If the live invoice uses another card, the operator sets the three env vars.

**Gear `p` (pro) is rare.** Interactive turns do not use it. Empty-final rescue can. v1 prices those tokens on the same three env rates. That understates pro when the env still holds flash prices. Accepted. No per-model counters.

**SQLite neighbors:** `core/memory.py` uses `work/cache.sqlite`. `core/sessions.py` uses `work/sessions.sqlite`, WAL, `timeout=10`, `busy_timeout=5000`, and `CHATBOT_WORK_DIR` read at call time. Copy that path rule. Do not add a table to `cache.sqlite` or `sessions.sqlite`.

## Locked decisions

1. **Actor.** Column `session_id` stores the chat id. Missing, blank, or whitespace-only becomes `anon`. Longer than 128 characters becomes `long:` plus the first 32 hex chars of SHA-256 (so a huge id cannot bloat the row and cannot land in `anon`). A future login writes a user id into this same column. `usd()` does not change.
2. **Company.** `company_id` is the int already on the ask (`session["conversation"]["CompanyID"]` after `_ensure_session_company` / `ask_stream`). Missing becomes `0` (its own bucket, not company 1). Company JSON is the sum across sessions. Session JSON is the sum across companies for that one session id (a chat that switches company still has one session total).
3. **Key.** `(client, company_id, session_id, day)` with `day` as `YYYY-MM-DD` in UTC. Counters on the row: `cache_hit_tokens`, `cache_miss_tokens`, `completion_tokens`, `requests`. One finished `/ask` adds `requests += 1` and adds the three token sums from that turn (already summed across LLM calls inside `Usage`). Do not increment `requests` by `llm_calls`.
4. **USD, at read time.** `usd = (hit * HIT + miss * MISS + out * OUT) / 1_000_000` using `decimal.Decimal`, quantize to 6 places, `ROUND_HALF_UP`. Rates are USD per 1M tokens. Do not store USD. Changing env reprices today and all-time. That is what "dynamically calculates" means.
5. **Env.** `CHATBOT_USD_PER_M_HIT`, `CHATBOT_USD_PER_M_MISS`, `CHATBOT_USD_PER_M_OUT`. Read on each `report()` call. Do not cache at import. Do not call `load_dotenv` inside `core/consumption.py` (`api/server.py` already loads `.env`). Missing or blank → `Decimal("0.003")`, `Decimal("0.15")`, `Decimal("0.60")`. Present but not a finite number `>= 0` → `ConsumptionConfigError` (no fallback, so a typo does not silently look like the cheap card). `GET /usage` then returns HTTP 500. Do not echo the bad value.
6. **Peak.** One env set. Off-peak defaults above. Peak is the operator pasting `0.006`, `0.30`, `1.20` into `.env` and restarting. No clock, no UTC window check.
7. **When to record.** Once, in `api/server.py` `stream()`, after `ask_stream` yields `type == done` and before the answer SSE frame. Covers answer, refusal, and `needs_ask`. Does not cover a blank question (returns before the agent), `TurnCancelled` (client disconnect: the `done` event never arrives; v1 drops that spend), or the provider/generic `except` paths that return before `done`. A sqlite failure is logged with `logging.exception` and does not break the chat. Log the client name only — not the question, not the API key.
8. **JSON.** `GET /usage` with optional `session_id`. Omitted param → `"session": null` (do not treat omit as `anon`). Present param, even with no rows → that session's today and all-time, zeros allowed. Always include `rates_usd_per_m` and `companies` (every company_id for the pinned client, sorted, `[]` if none). Bucket fields: `cache_hit_tokens`, `cache_miss_tokens`, `completion_tokens`, `requests`, `usd`. No `prompt_tokens`, no question, no SQL, no API key, no list of other session ids.
9. **Access.** Same process and host as `/health`. Local dev is localhost. IIS is the existing site binding. No new auth. Putting that host on the public internet exposes spend totals and any session id the caller already knows. Keep the same network trust as `/health`.
10. **Reset.** Not in v1. Deleting gitignored `work/consumption.sqlite` is the operator escape hatch. No route for it.

## File structure

| File | Responsibility |
|---|---|
| Create: `core/consumption.py` | Rate card, `usd`, actor key, `tokens_from_done`, `fields_from_usage`, SQLite upsert, `report()` dict. No FastAPI, no LLM, no SQL Server. |
| Create: `tests/test_consumption.py` | Unit tests. Temp dir via `CHATBOT_WORK_DIR`. No port 8100. |
| Modify: `core/agent.py` | Import `consumption`. Spread `fields_from_usage(usage_acc)` on all four `done` yields. Do not change tool handling, prompts, or gears. |
| Modify: `api/server.py` | Import `consumption` and `logging`. Record once per finished ask. Add `GET /usage` above the static mount. |
| Modify: `.env.example` | Document the three rate names and the off-peak/peak numbers. |

Do not create a Prometheus metric, a second database, or a UI page.

---

### Task 1: Rate card and USD formula

**Files:**
- Create: `core/consumption.py`
- Create: `tests/test_consumption.py`
- Modify: `.env.example` (append after the `CHATBOT_CLIENT` block)
- Test: `tests/test_consumption.py`

**Interfaces:**
- Consumes: nothing from later tasks. Reads `os.environ` at call time.
- Produces:
  - `class ConsumptionConfigError(ValueError)` with attribute `name: str` (the env var name). `str(exc)` is that name only.
  - `rates_from_env(env: Mapping[str, str] | None = None) -> dict[str, Decimal]` keys `hit`, `miss`, `out`. `None` reads `os.environ`.
  - `usd(hit: int, miss: int, out: int, rates: dict[str, Decimal]) -> Decimal` quantized to `0.000001`.

- [ ] **Step 1: Write the failing tests**

Create `tests/test_consumption.py`:

```python
"""USD rate card for the consumption monitor. No server, no port 8100."""
import os
from decimal import Decimal

import pytest

from core import consumption


def _clear_rates(monkeypatch) -> None:
    for name in (
        "CHATBOT_USD_PER_M_HIT",
        "CHATBOT_USD_PER_M_MISS",
        "CHATBOT_USD_PER_M_OUT",
    ):
        monkeypatch.delenv(name, raising=False)


def test_one_million_miss_tokens_cost_0_15(monkeypatch):
    _clear_rates(monkeypatch)
    rates = consumption.rates_from_env()
    assert consumption.usd(0, 1_000_000, 0, rates) == Decimal("0.150000")


def test_hit_tokens_use_the_hit_rate_not_the_miss_rate(monkeypatch):
    _clear_rates(monkeypatch)
    rates = consumption.rates_from_env()
    assert consumption.usd(1_000_000, 0, 0, rates) == Decimal("0.003000")
    assert consumption.usd(1_000_000, 0, 0, rates) != Decimal("0.150000")


def test_hit_miss_and_completion_add(monkeypatch):
    _clear_rates(monkeypatch)
    rates = consumption.rates_from_env()
    # 0.003 + 0.15 + 0.60 per 1M
    assert consumption.usd(1_000_000, 1_000_000, 1_000_000, rates) == Decimal("0.753000")


def test_missing_env_uses_offpeak_flash_defaults(monkeypatch):
    _clear_rates(monkeypatch)
    rates = consumption.rates_from_env()
    assert rates == {
        "hit": Decimal("0.003"),
        "miss": Decimal("0.15"),
        "out": Decimal("0.60"),
    }


def test_blank_env_uses_the_same_defaults(monkeypatch):
    monkeypatch.setenv("CHATBOT_USD_PER_M_HIT", "  ")
    monkeypatch.setenv("CHATBOT_USD_PER_M_MISS", "")
    monkeypatch.setenv("CHATBOT_USD_PER_M_OUT", "")
    rates = consumption.rates_from_env()
    assert rates["hit"] == Decimal("0.003")
    assert rates["miss"] == Decimal("0.15")
    assert rates["out"] == Decimal("0.60")


def test_env_override_is_used(monkeypatch):
    _clear_rates(monkeypatch)
    monkeypatch.setenv("CHATBOT_USD_PER_M_MISS", "0.30")
    rates = consumption.rates_from_env()
    assert consumption.usd(0, 1_000_000, 0, rates) == Decimal("0.300000")


def test_bad_rate_names_the_var_and_hides_the_value(monkeypatch):
    _clear_rates(monkeypatch)
    monkeypatch.setenv("CHATBOT_USD_PER_M_HIT", "nope")
    with pytest.raises(consumption.ConsumptionConfigError) as raised:
        consumption.rates_from_env()
    assert raised.value.name == "CHATBOT_USD_PER_M_HIT"
    assert "nope" not in str(raised.value)


def test_negative_rate_is_rejected(monkeypatch):
    _clear_rates(monkeypatch)
    monkeypatch.setenv("CHATBOT_USD_PER_M_OUT", "-1")
    with pytest.raises(consumption.ConsumptionConfigError) as raised:
        consumption.rates_from_env()
    assert raised.value.name == "CHATBOT_USD_PER_M_OUT"
```

- [ ] **Step 2: Run the tests and confirm they fail**

Run:

```
py -3.13 -m pytest tests/test_consumption.py -v
```

Expected: FAIL with `ModuleNotFoundError` or `ImportError` for `core.consumption`. Do not start uvicorn.

- [ ] **Step 3: Write the rate card**

Create `core/consumption.py`:

```python
"""Per-chat token counters and USD price.

USD is computed when the report is read, from CHATBOT_USD_PER_M_HIT / _MISS / _OUT
(USD per 1,000,000 tokens). Blank or missing env uses the off-peak flash card
0.003 / 0.15 / 0.60. Peak is the operator's job: put 0.006 / 0.30 / 1.20 in
gitignored .env and restart. This module does not look at the clock.

The v1 actor key is the chat session_id (there is no login). A future login
can store a user id in that same column. usd() does not care which string it is.

prompt_tokens are not a billed class: they overlap cache hit + cache miss.
SQL row counts are not tokens.
"""
from __future__ import annotations

import os
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

_QUANT = Decimal("0.000001")

_DEFAULTS: dict[str, Decimal] = {
    "CHATBOT_USD_PER_M_HIT": Decimal("0.003"),
    "CHATBOT_USD_PER_M_MISS": Decimal("0.15"),
    "CHATBOT_USD_PER_M_OUT": Decimal("0.60"),
}

_KEYS = (
    ("CHATBOT_USD_PER_M_HIT", "hit"),
    ("CHATBOT_USD_PER_M_MISS", "miss"),
    ("CHATBOT_USD_PER_M_OUT", "out"),
)


class ConsumptionConfigError(ValueError):
    def __init__(self, name: str) -> None:
        self.name = name
        super().__init__(name)


def rates_from_env(env=None) -> dict[str, Decimal]:
    source = os.environ if env is None else env
    parsed: dict[str, Decimal] = {}
    for env_name, key in _KEYS:
        raw = source.get(env_name)
        if raw is None or str(raw).strip() == "":
            parsed[key] = _DEFAULTS[env_name]
            continue
        try:
            value = Decimal(str(raw).strip())
        except InvalidOperation:
            raise ConsumptionConfigError(env_name) from None
        if not value.is_finite() or value < 0:
            raise ConsumptionConfigError(env_name)
        parsed[key] = value
    return parsed


def usd(hit: int, miss: int, out: int, rates: dict[str, Decimal]) -> Decimal:
    total = (
        Decimal(int(hit)) * rates["hit"]
        + Decimal(int(miss)) * rates["miss"]
        + Decimal(int(out)) * rates["out"]
    ) / Decimal(1_000_000)
    return total.quantize(_QUANT, rounding=ROUND_HALF_UP)
```

Append this block to `.env.example` after the `CHATBOT_CLIENT` line. These numbers are the documented defaults, not a secret:

```
# USD per 1,000,000 tokens for GET /usage. Off-peak flash defaults.
# Peak is double: HIT=0.006 MISS=0.30 OUT=1.20. Edit gitignored .env to swap.
# The app does not switch peak by clock. Blank falls back to these same defaults.
# plans/deepseek_swap_parallel_plan.md lists a different flash card; do not
# follow that card unless you set it here on purpose.
CHATBOT_USD_PER_M_HIT=0.003
CHATBOT_USD_PER_M_MISS=0.15
CHATBOT_USD_PER_M_OUT=0.60
```

- [ ] **Step 4: Run the tests and confirm they pass**

Run:

```
py -3.13 -m pytest tests/test_consumption.py -v
```

Expected: 8 passed. Do not start uvicorn.

- [ ] **Step 5: Commit**

```
git add core/consumption.py tests/test_consumption.py .env.example
git commit -m "feat(consumption): price hit, miss, and output tokens from env rates"
```

---

### Task 2: SQLite aggregates and the report dict

**Files:**
- Modify: `core/consumption.py`
- Modify: `tests/test_consumption.py`
- Test: `tests/test_consumption.py`

**Interfaces:**
- Consumes: `rates_from_env`, `usd`, `ConsumptionConfigError` from Task 1.
- Produces:
  - `actor_session(session_id: str | None) -> str`
  - `tokens_from_done(event: dict) -> tuple[int, int, int]` as `(hit, miss, completion)`. Ignores `prompt_tokens`, `result_rows`, `queries`.
  - `fields_from_usage(usage_acc) -> dict` with keys `llm_calls`, `prompt_tokens`, `completion_tokens`, `cache_hit_tokens`, `cache_miss_tokens` (ints). This is what `done` events spread. It is not the public `/usage` shape (`prompt_tokens` stays off the HTTP JSON).
  - `record(client: str, company_id: int, session_id: str | None, cache_hit_tokens: int = 0, cache_miss_tokens: int = 0, completion_tokens: int = 0, *, day: str | None = None) -> None`
  - `report(client: str, session_id: str | None = None, *, today: str | None = None) -> dict`
  - Database file: `$CHATBOT_WORK_DIR/consumption.sqlite` if that env is set, else `work/consumption.sqlite`. Read the env inside the function, not at import.

`report` shape:

```python
{
    "client": str,
    "day_utc": "YYYY-MM-DD",
    "rates_usd_per_m": {"hit": float, "miss": float, "out": float},
    "session": None,  # or {"session_id", "today": bucket, "all_time": bucket}
    "companies": [{"company_id": int, "today": bucket, "all_time": bucket}, ...],
}
```

`bucket` is:

```python
{
    "cache_hit_tokens": int,
    "cache_miss_tokens": int,
    "completion_tokens": int,
    "requests": int,
    "usd": float,  # quantized Decimal converted with float()
}
```

`session_id is None` means the caller did not ask for a session (`"session": null`). A string, including `""`, is looked up via `actor_session`. Rates are resolved before any SQL. A bad rate raises `ConsumptionConfigError` and does not look like zero spend.

- [ ] **Step 1: Append the failing tests**

Append to `tests/test_consumption.py`:

```python
from core.usage import Usage


def test_fields_from_usage_copies_totals():
    usage = Usage()
    usage.add(
        model="m", gear="t1", prompt=10, completion=4,
        cache_hit=3, cache_miss=7, ms=1.0,
    )
    assert consumption.fields_from_usage(usage) == {
        "llm_calls": 1,
        "prompt_tokens": 10,
        "completion_tokens": 4,
        "cache_hit_tokens": 3,
        "cache_miss_tokens": 7,
    }


def test_tool_rows_and_prompt_tokens_are_not_billed():
    hit, miss, out = consumption.tokens_from_done({
        "cache_hit_tokens": 5,
        "cache_miss_tokens": 7,
        "completion_tokens": 9,
        "prompt_tokens": 1_000_000,
        "result_rows": 1_000_000,
        "queries": 4,
    })
    assert (hit, miss, out) == (5, 7, 9)


def test_two_sessions_do_not_mix(monkeypatch, tmp_path):
    monkeypatch.setenv("CHATBOT_WORK_DIR", str(tmp_path))
    _clear_rates(monkeypatch)
    consumption.record("morec", 1, "sess-a", cache_miss_tokens=1_000_000, day="2026-11-10")
    consumption.record("morec", 1, "sess-b", cache_miss_tokens=2_000_000, day="2026-11-10")
    body = consumption.report("morec", "sess-a", today="2026-11-10")
    assert body["session"]["session_id"] == "sess-a"
    assert body["session"]["today"]["cache_miss_tokens"] == 1_000_000
    assert body["session"]["today"]["usd"] == 0.15
    assert body["session"]["all_time"]["cache_miss_tokens"] == 1_000_000
    company = body["companies"][0]
    assert company["company_id"] == 1
    assert company["today"]["cache_miss_tokens"] == 3_000_000
    assert company["today"]["requests"] == 2
    assert company["today"]["usd"] == 0.45


def test_two_companies_do_not_mix(monkeypatch, tmp_path):
    monkeypatch.setenv("CHATBOT_WORK_DIR", str(tmp_path))
    _clear_rates(monkeypatch)
    consumption.record("morec", 1, "sess-a", cache_hit_tokens=1_000_000, day="2026-11-10")
    consumption.record("morec", 2, "sess-a", cache_hit_tokens=1_000_000, day="2026-11-10")
    body = consumption.report("morec", None, today="2026-11-10")
    assert body["session"] is None
    by_id = {row["company_id"]: row for row in body["companies"]}
    assert by_id[1]["today"]["cache_hit_tokens"] == 1_000_000
    assert by_id[2]["today"]["cache_hit_tokens"] == 1_000_000
    assert by_id[1]["today"]["usd"] == 0.003
    # Session total sums both companies. Company buckets stay split.
    one = consumption.report("morec", "sess-a", today="2026-11-10")
    assert one["session"]["today"]["cache_hit_tokens"] == 2_000_000


def test_other_client_is_excluded(monkeypatch, tmp_path):
    monkeypatch.setenv("CHATBOT_WORK_DIR", str(tmp_path))
    _clear_rates(monkeypatch)
    consumption.record("morec", 1, "sess-a", cache_miss_tokens=1_000_000, day="2026-11-10")
    consumption.record("other", 1, "sess-a", cache_miss_tokens=9_000_000, day="2026-11-10")
    body = consumption.report("morec", "sess-a", today="2026-11-10")
    assert body["session"]["today"]["cache_miss_tokens"] == 1_000_000
    assert body["companies"][0]["today"]["cache_miss_tokens"] == 1_000_000


def test_missing_session_id_buckets_as_anon(monkeypatch, tmp_path):
    monkeypatch.setenv("CHATBOT_WORK_DIR", str(tmp_path))
    _clear_rates(monkeypatch)
    consumption.record("morec", 1, None, completion_tokens=1_000_000, day="2026-11-10")
    consumption.record("morec", 1, "   ", completion_tokens=1_000_000, day="2026-11-10")
    body = consumption.report("morec", "", today="2026-11-10")
    assert body["session"]["session_id"] == "anon"
    assert body["session"]["today"]["completion_tokens"] == 2_000_000
    assert body["session"]["today"]["usd"] == 1.2


def test_long_session_id_does_not_collapse_into_anon(monkeypatch, tmp_path):
    monkeypatch.setenv("CHATBOT_WORK_DIR", str(tmp_path))
    _clear_rates(monkeypatch)
    huge = "x" * 129
    consumption.record("morec", 1, huge, cache_miss_tokens=100, day="2026-11-10")
    consumption.record("morec", 1, None, cache_miss_tokens=5, day="2026-11-10")
    anon = consumption.report("morec", "anon", today="2026-11-10")
    assert anon["session"]["today"]["cache_miss_tokens"] == 5
    named = consumption.report("morec", huge, today="2026-11-10")
    assert named["session"]["session_id"].startswith("long:")
    assert named["session"]["today"]["cache_miss_tokens"] == 100
    assert huge not in named["session"]["session_id"]


def test_today_excludes_other_utc_days(monkeypatch, tmp_path):
    monkeypatch.setenv("CHATBOT_WORK_DIR", str(tmp_path))
    _clear_rates(monkeypatch)
    consumption.record("morec", 1, "sess-a", cache_miss_tokens=1_000_000, day="2026-11-09")
    consumption.record("morec", 1, "sess-a", cache_miss_tokens=1_000_000, day="2026-11-10")
    body = consumption.report("morec", "sess-a", today="2026-11-10")
    assert body["day_utc"] == "2026-11-10"
    assert body["session"]["today"]["cache_miss_tokens"] == 1_000_000
    assert body["session"]["today"]["requests"] == 1
    assert body["session"]["all_time"]["cache_miss_tokens"] == 2_000_000
    assert body["session"]["all_time"]["requests"] == 2
    assert body["session"]["all_time"]["usd"] == 0.3


def test_usd_is_repriced_when_env_changes(monkeypatch, tmp_path):
    monkeypatch.setenv("CHATBOT_WORK_DIR", str(tmp_path))
    _clear_rates(monkeypatch)
    consumption.record("morec", 1, "sess-a", cache_miss_tokens=1_000_000, day="2026-11-10")
    monkeypatch.setenv("CHATBOT_USD_PER_M_MISS", "0.30")
    body = consumption.report("morec", "sess-a", today="2026-11-10")
    assert body["rates_usd_per_m"]["miss"] == 0.3
    assert body["session"]["all_time"]["usd"] == 0.3
    assert body["session"]["all_time"]["cache_miss_tokens"] == 1_000_000


def test_unknown_session_is_zero_not_an_error(monkeypatch, tmp_path):
    monkeypatch.setenv("CHATBOT_WORK_DIR", str(tmp_path))
    _clear_rates(monkeypatch)
    body = consumption.report("morec", "nobody", today="2026-11-10")
    assert body["session"]["today"]["usd"] == 0.0
    assert body["session"]["today"]["requests"] == 0
    assert body["session"]["today"]["cache_hit_tokens"] == 0
    assert body["companies"] == []
    assert "prompt" not in body["session"]["today"]


def test_second_record_accumulates_the_same_bucket(monkeypatch, tmp_path):
    monkeypatch.setenv("CHATBOT_WORK_DIR", str(tmp_path))
    _clear_rates(monkeypatch)
    consumption.record(
        "morec", 1, "sess-a",
        cache_hit_tokens=10, cache_miss_tokens=20, completion_tokens=30,
        day="2026-11-10",
    )
    consumption.record(
        "morec", 1, "sess-a",
        cache_hit_tokens=1, cache_miss_tokens=2, completion_tokens=3,
        day="2026-11-10",
    )
    bucket = consumption.report("morec", "sess-a", today="2026-11-10")["session"]["today"]
    assert bucket["cache_hit_tokens"] == 11
    assert bucket["cache_miss_tokens"] == 22
    assert bucket["completion_tokens"] == 33
    assert bucket["requests"] == 2
```

- [ ] **Step 2: Run the new tests and confirm they fail**

Run:

```
py -3.13 -m pytest tests/test_consumption.py -v -k "fields_from_usage or tool_rows or two_sessions or two_companies or other_client or missing_session or long_session or today_excludes or repriced or unknown_session or second_record"
```

Expected: FAIL with `AttributeError` (`record` / `report` / `tokens_from_done` / `fields_from_usage` missing). Task 1 tests still pass. Do not start uvicorn.

- [ ] **Step 3: Add the store and the report**

Keep Task 1's `ConsumptionConfigError`, `_DEFAULTS`, `_KEYS`, `rates_from_env`, and `usd` unchanged. Add these imports next to the existing ones:

```python
import hashlib
import sqlite3
import threading
from datetime import date, datetime, timezone
from pathlib import Path
```

Append the rest of the module:

```python
_SESSION_MAX = 128
_lock = threading.Lock()

_SCHEMA = """
CREATE TABLE IF NOT EXISTS consumption (
    client TEXT NOT NULL,
    company_id INTEGER NOT NULL,
    session_id TEXT NOT NULL,
    day TEXT NOT NULL,
    cache_hit_tokens INTEGER NOT NULL DEFAULT 0,
    cache_miss_tokens INTEGER NOT NULL DEFAULT 0,
    completion_tokens INTEGER NOT NULL DEFAULT 0,
    requests INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (client, company_id, session_id, day)
)
"""


def actor_session(session_id: str | None) -> str:
    text = (session_id or "").strip()
    if not text:
        return "anon"
    if len(text) > _SESSION_MAX:
        digest = hashlib.sha256(text.encode()).hexdigest()[:32]
        return f"long:{digest}"
    return text


def tokens_from_done(event: dict) -> tuple[int, int, int]:
    return (
        int(event.get("cache_hit_tokens") or 0),
        int(event.get("cache_miss_tokens") or 0),
        int(event.get("completion_tokens") or 0),
    )


def fields_from_usage(usage_acc) -> dict:
    totals = usage_acc.totals() if usage_acc is not None else {}

    def _n(key: str) -> int:
        return int(totals.get(key) or 0)

    return {
        "llm_calls": _n("llm_calls"),
        "prompt_tokens": _n("prompt_tokens"),
        "completion_tokens": _n("completion_tokens"),
        "cache_hit_tokens": _n("cache_hit_tokens"),
        "cache_miss_tokens": _n("cache_miss_tokens"),
    }


def _utc_day(day: str | None) -> str:
    if day is None:
        return datetime.now(timezone.utc).date().isoformat()
    return date.fromisoformat(day).isoformat()


def db_path() -> Path:
    env_work = os.environ.get("CHATBOT_WORK_DIR")
    root = Path(env_work) if env_work else Path(__file__).resolve().parent.parent / "work"
    return root / "consumption.sqlite"


def _conn() -> sqlite3.Connection:
    path = db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path, timeout=10)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA busy_timeout=5000")
    conn.execute(_SCHEMA)
    return conn


def _nonneg(value: int) -> int:
    number = int(value or 0)
    return number if number > 0 else 0


def record(
    client: str,
    company_id: int,
    session_id: str | None,
    cache_hit_tokens: int = 0,
    cache_miss_tokens: int = 0,
    completion_tokens: int = 0,
    *,
    day: str | None = None,
) -> None:
    sid = actor_session(session_id)
    day_text = _utc_day(day)
    with _lock:
        conn = _conn()
        try:
            conn.execute(
                """
                INSERT INTO consumption (
                    client, company_id, session_id, day,
                    cache_hit_tokens, cache_miss_tokens, completion_tokens, requests
                ) VALUES (?, ?, ?, ?, ?, ?, ?, 1)
                ON CONFLICT(client, company_id, session_id, day) DO UPDATE SET
                    cache_hit_tokens = cache_hit_tokens + excluded.cache_hit_tokens,
                    cache_miss_tokens = cache_miss_tokens + excluded.cache_miss_tokens,
                    completion_tokens = completion_tokens + excluded.completion_tokens,
                    requests = requests + 1
                """,
                (
                    client,
                    int(company_id),
                    sid,
                    day_text,
                    _nonneg(cache_hit_tokens),
                    _nonneg(cache_miss_tokens),
                    _nonneg(completion_tokens),
                ),
            )
            conn.commit()
        finally:
            conn.close()


def _json_number(value: Decimal) -> float:
    return float(value)


def _bucket(hit, miss, out, requests, card: dict[str, Decimal]) -> dict:
    hit_i, miss_i, out_i = int(hit), int(miss), int(out)
    return {
        "cache_hit_tokens": hit_i,
        "cache_miss_tokens": miss_i,
        "completion_tokens": out_i,
        "requests": int(requests),
        "usd": _json_number(usd(hit_i, miss_i, out_i, card)),
    }


def _rates_json(card: dict[str, Decimal]) -> dict[str, float]:
    return {
        "hit": _json_number(card["hit"]),
        "miss": _json_number(card["miss"]),
        "out": _json_number(card["out"]),
    }


_SUMS = """
    COALESCE(SUM(CASE WHEN day = ? THEN cache_hit_tokens ELSE 0 END), 0),
    COALESCE(SUM(CASE WHEN day = ? THEN cache_miss_tokens ELSE 0 END), 0),
    COALESCE(SUM(CASE WHEN day = ? THEN completion_tokens ELSE 0 END), 0),
    COALESCE(SUM(CASE WHEN day = ? THEN requests ELSE 0 END), 0),
    COALESCE(SUM(cache_hit_tokens), 0),
    COALESCE(SUM(cache_miss_tokens), 0),
    COALESCE(SUM(completion_tokens), 0),
    COALESCE(SUM(requests), 0)
"""


def report(client: str, session_id: str | None = None, *, today: str | None = None) -> dict:
    card = rates_from_env()
    day_text = _utc_day(today)
    day_params = (day_text, day_text, day_text, day_text)
    conn = _conn()
    try:
        company_rows = conn.execute(
            f"SELECT company_id, {_SUMS} FROM consumption WHERE client = ? "
            "GROUP BY company_id ORDER BY company_id",
            (*day_params, client),
        ).fetchall()
        session_block = None
        if session_id is not None:
            sid = actor_session(session_id)
            row = conn.execute(
                f"SELECT {_SUMS} FROM consumption WHERE client = ? AND session_id = ?",
                (*day_params, client, sid),
            ).fetchone()
            session_block = {
                "session_id": sid,
                "today": _bucket(row[0], row[1], row[2], row[3], card),
                "all_time": _bucket(row[4], row[5], row[6], row[7], card),
            }
    finally:
        conn.close()
    companies = [
        {
            "company_id": int(row[0]),
            "today": _bucket(row[1], row[2], row[3], row[4], card),
            "all_time": _bucket(row[5], row[6], row[7], row[8], card),
        }
        for row in company_rows
    ]
    return {
        "client": client,
        "day_utc": day_text,
        "rates_usd_per_m": _rates_json(card),
        "session": session_block,
        "companies": companies,
    }
```

Negative token inputs are stored as 0 so a bad event cannot decrease a counter. `requests` still increments.

- [ ] **Step 4: Run the tests and confirm they pass**

Run:

```
py -3.13 -m pytest tests/test_consumption.py -v
```

Expected: all tests in the file passed (Task 1 and Task 2). Confirm no `work/consumption.sqlite` appeared at the repo root from these tests (they set `CHATBOT_WORK_DIR` to pytest's `tmp_path`). Do not start uvicorn.

- [ ] **Step 5: Commit**

```
git add core/consumption.py tests/test_consumption.py
git commit -m "feat(consumption): store daily token counters per session and company"
```

---

### Task 3: Stamp usage on every finished agent turn

**Files:**
- Modify: `core/agent.py` (import line, and the four `yield {"type": "done" ...}` sites)
- Modify: `tests/test_consumption.py`
- Test: `tests/test_consumption.py`

**Interfaces:**
- Consumes: `consumption.fields_from_usage(usage_acc) -> dict` from Task 2. `usage_acc` is the `Usage()` already created at the start of `ask_stream`.
- Produces: every `done` event includes `llm_calls`, `prompt_tokens`, `completion_tokens`, `cache_hit_tokens`, `cache_miss_tokens`. Existing keys (`answer`, `needs_ask`, `answer_sql`, envelopes) stay. Do not remove `prompt_tokens` from the event; evals and traces already understand it. Billing still ignores it via `tokens_from_done`.

- [ ] **Step 1: Append the failing test**

Append to `tests/test_consumption.py`:

```python
def test_every_done_yield_spreads_usage_fields():
    text = (Path(__file__).resolve().parent.parent / "core" / "agent.py").read_text(encoding="utf-8")
    needle = "**consumption.fields_from_usage(usage_acc)"
    assert text.count(needle) == 4
```

Add `from pathlib import Path` to the imports at the top of `tests/test_consumption.py` if it is not already there.

- [ ] **Step 2: Run the test and confirm it fails**

Run:

```
py -3.13 -m pytest tests/test_consumption.py::test_every_done_yield_spreads_usage_fields -v
```

Expected: FAIL because the count is 0, not 4. Do not start uvicorn.

- [ ] **Step 3: Wire the four yields**

On the import line in `core/agent.py` that starts `from . import catalog, config, docs, ...`, add `consumption` in alphabetical order (after `config`, before `docs`).

Calendar short-circuit. Replace:

```python
        yield {"type": "done", "answer": None, "needs_ask": calendar_ask}
```

with:

```python
        yield {
            "type": "done",
            "answer": None,
            "needs_ask": calendar_ask,
            **consumption.fields_from_usage(usage_acc),
        }
```

Plan-cache answer. Delete the `_usage_pc = usage_acc.totals()` line and the five `"llm_calls"` / `"prompt_tokens"` / `"completion_tokens"` / `"cache_hit_tokens"` / `"cache_miss_tokens"` lines inside that yield. Keep every other key. The yield ends as:

```python
            yield {"type": "done", "answer": answer, "needs_ask": None,
                   "answer_sql": "; ".join(queries), "queries": list(queries),
                   "cache_key": key,
                   "hold_stream": False, "thread_head": prior_card,
                   "doc_search_count": 0,
                   **consumption.fields_from_usage(usage_acc),
                   **envelope}
```

`ask_user` short-circuit. Replace:

```python
                yield {"type": "done", "answer": None, "needs_ask": asked}
```

with:

```python
                yield {
                    "type": "done",
                    "answer": None,
                    "needs_ask": asked,
                    **consumption.fields_from_usage(usage_acc),
                }
```

Final yield at the bottom of `ask_stream`. Delete `_usage = usage_acc.totals()` and the five token lines in the yield. Keep `_ql`, `_qlog`, and the envelope. Spread the helper in the same place the five lines occupied:

```python
    yield {"type": "done", "answer": final_text, "needs_ask": None,
           "answer_sql": _answer_sql(state), "queries": list(_ql), "query_log": _qlog,
           "cache_key": key,
           "hold_stream": bool(state.get("hold_stream")),
           "thread_head": state.get("thread_head"),
           "doc_search_count": state.get("doc_searches", 0),
           "vault_search_count": state.get("vault_searches", 0),
           "tools_ms": dict(state.get("tools_ms") or {}),
           **consumption.fields_from_usage(usage_acc),
           **envelope}
```

Do not add a new LLM call. Do not read `trace.jsonl`. The substring `**consumption.fields_from_usage(usage_acc)` must appear exactly four times and nowhere else in `core/agent.py` (the test counts it).

- [ ] **Step 4: Run the tests and confirm they pass**

Run:

```
py -3.13 -m pytest tests/test_consumption.py tests/test_deepswap_guard_order.py::test_calendar_guard_fires_even_when_a_cached_plan_exists tests/test_agent.py::test_ask_user_tool_call_returns_needs_ask_immediately -q
```

Expected: PASS. The two existing tests only assert `needs_ask` / that no LLM ran; extra token keys are compatible. If the guard test cannot load the local schema cache, fix only a test-path issue caused by this edit. Do not change the guard. Do not start uvicorn.

- [ ] **Step 5: Commit**

```
git add core/agent.py tests/test_consumption.py
git commit -m "fix(agent): include token usage on every finished turn"
```

---

### Task 4: Record finished asks and serve GET /usage

**Files:**
- Modify: `api/server.py` (module docstring, imports, the `stream()` function inside `ask`, a new route directly above `@app.get("/health")`)
- Modify: `tests/test_consumption.py`
- Test: `tests/test_consumption.py`

**Interfaces:**
- Consumes: `consumption.record`, `consumption.tokens_from_done`, `consumption.report`, `consumption.ConsumptionConfigError`.
- Produces: `GET /usage` on the same app as `GET /health`. Query `session_id: str | None = None`. Status 200 body is exactly `consumption.report(pinned_client(), session_id)` (omit the query → pass `None`). Status 500 body is `{"detail": {"error": "invalid consumption rate", "name": "<ENV_NAME>"}}` and the bad value is not in the body.

Record site, inside `stream()`, after the `for event in agent.ask_stream(...)` loop and its `except` blocks, and before `session["pending_ask"] = ...`:

```python
        if result is not None:
            cid = session.get("conversation", {}).get("CompanyID")
            try:
                hit, miss, out = consumption.tokens_from_done(result)
                consumption.record(
                    client,
                    int(cid) if cid is not None else 0,
                    req.session_id,
                    cache_hit_tokens=hit,
                    cache_miss_tokens=miss,
                    completion_tokens=out,
                )
            except Exception:
                logging.getLogger("consumption").exception(
                    "consumption record failed client=%s", client)
```

Call this once. Do not also call it on the blank-question return, on `TurnCancelled`, or in the error returns. A failure here must still yield the answer. Existing `/ask` unit tests that mock `ask_stream` will insert a zero-token request into whatever sqlite `CHATBOT_WORK_DIR` or `work/consumption.sqlite` points at. That file is gitignored. Do not special-case pytest.

- [ ] **Step 1: Append the failing tests**

Append to `tests/test_consumption.py`:

```python
def test_get_usage_json_has_usd_and_token_fields(monkeypatch, tmp_path):
    monkeypatch.setenv("CHATBOT_WORK_DIR", str(tmp_path))
    os.environ.setdefault("CHATBOT_CLIENT", "morec")
    from fastapi.testclient import TestClient
    from api.server import PINNED_CLIENT, app

    # Import runs load_dotenv, which fills vars that are unset. Clear after import.
    _clear_rates(monkeypatch)
    consumption.record(
        PINNED_CLIENT, 1, "sess-a",
        cache_miss_tokens=1_000_000,
    )
    resp = TestClient(app).get("/usage", params={"session_id": "sess-a"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["client"] == PINNED_CLIENT
    assert body["rates_usd_per_m"]["miss"] == 0.15
    today = body["session"]["today"]
    assert today["cache_miss_tokens"] == 1_000_000
    assert today["cache_hit_tokens"] == 0
    assert today["completion_tokens"] == 0
    assert today["requests"] == 1
    assert today["usd"] == 0.15
    assert "prompt" not in today
    assert "DEEPSEEK" not in resp.text
    assert "question" not in body["session"]
    company = next(row for row in body["companies"] if row["company_id"] == 1)
    assert company["all_time"]["usd"] == 0.15
    assert company["all_time"]["cache_hit_tokens"] == 0
    assert company["all_time"]["cache_miss_tokens"] == 1_000_000


def test_get_usage_without_session_id_has_null_session(monkeypatch, tmp_path):
    monkeypatch.setenv("CHATBOT_WORK_DIR", str(tmp_path))
    os.environ.setdefault("CHATBOT_CLIENT", "morec")
    from fastapi.testclient import TestClient
    from api.server import app

    _clear_rates(monkeypatch)
    resp = TestClient(app).get("/usage")
    assert resp.status_code == 200
    assert resp.json()["session"] is None


def test_get_usage_rejects_a_bad_rate_without_echoing_it(monkeypatch, tmp_path):
    monkeypatch.setenv("CHATBOT_WORK_DIR", str(tmp_path))
    os.environ.setdefault("CHATBOT_CLIENT", "morec")
    from fastapi.testclient import TestClient
    from api.server import app

    _clear_rates(monkeypatch)
    monkeypatch.setenv("CHATBOT_USD_PER_M_OUT", "nope")
    resp = TestClient(app).get("/usage")
    assert resp.status_code == 500
    detail = resp.json()["detail"]
    assert detail["error"] == "invalid consumption rate"
    assert detail["name"] == "CHATBOT_USD_PER_M_OUT"
    assert "nope" not in resp.text
```

`api.server` calls `load_dotenv` on import and does not override vars that are already set. Clearing or setting the rate vars **after** that import is what the test asserts, because a blank slot in the environment gets filled from `.env` at import. These tests do not import `api.server` at module scope. `TestClient` must not be pointed at `http://127.0.0.1:8100`.

- [ ] **Step 2: Run the new tests and confirm they fail**

Run:

```
py -3.13 -m pytest tests/test_consumption.py::test_get_usage_json_has_usd_and_token_fields tests/test_consumption.py::test_get_usage_without_session_id_has_null_session tests/test_consumption.py::test_get_usage_rejects_a_bad_rate_without_echoing_it -v
```

Expected: FAIL with HTTP 404 on `/usage`. Do not start uvicorn.

- [ ] **Step 3: Hook the server**

In `api/server.py`:

- Change the module docstring's first line so it lists `GET /usage` next to `GET /health`.
- Add `import logging` with the other stdlib imports.
- Add `consumption` to `from core import agent, config, dblink, gate, llm, memory, params, sessions, sql, trace`.
- Insert the record block from this task's Interfaces section.
- Insert this route directly above `@app.get("/health")` and above `app.mount(...)`:

```python
@app.get("/usage")
def usage(session_id: str | None = None):
    """Read-only spend for the pinned client. Same host and same lack of
    login as /health. Do not put this on the public internet unless /health
    is already restricted the same way. No prompt text, no API key."""
    try:
        return consumption.report(pinned_client(), session_id)
    except consumption.ConsumptionConfigError as exc:
        raise HTTPException(
            status_code=500,
            detail={"error": "invalid consumption rate", "name": exc.name},
        ) from None
```

Do not add a limiter decorator. Do not add a write method. Do not add the numbers to `/health` or `/metrics`.

- [ ] **Step 4: Run the tests and confirm they pass**

Run:

```
py -3.13 -m pytest tests/test_consumption.py tests/test_api.py::test_health_reports_pinned_client -q
```

Expected: PASS. `/health` still returns `pinned_client` and does not grow a usage object (the existing health test does not require a new assertion; do not change it to call the model). Do not start uvicorn. Do not request port 8100.

- [ ] **Step 5: Commit**

```
git add api/server.py tests/test_consumption.py
git commit -m "feat(api): expose read-only GET /usage for session and company spend"
```

---

## Spec coverage (self-check)

| Requirement | Task |
|---|---|
| User is `session_id`; company rollup; future login swaps the key only | Tasks 2 and 4, module docstring |
| SQLite under `work/`, key client + company + session + UTC day | Task 2 |
| Four counters; USD from the three env names; off-peak defaults | Tasks 1 and 2 |
| Record from the finished ask's existing `Usage`; no second LLM call | Tasks 3 and 4 |
| JSON: optional session, companies today and all-time, rates; no key; no prompt | Tasks 2 and 4 |
| No new auth; same host as `/health`; public bind exposes spend | Task 4 docstring and Locked decision 9 |
| One env set for peak; hit rate on hit tokens; `anon`; ignore tool rows; no reset | Tasks 1, 2, and Locked decisions 6–10 |
| Unit examples (1e6 miss = 0.15, hit rate, missing env, sessions don't mix, JSON has `usd` and token fields) | Tasks 1, 2, and 4 |

## Out of scope

- Login, API keys, or a header shared with IIS `cds`.
- A reset route, a UI page, Prometheus token series, per-model or per-gear prices, and clock-based peak switching.
- Replaying `work/trace.jsonl` to backfill history.
- Billing a client disconnect that never produced `done`.
- Editing prompts, the SQL gate, or `core/sql.py`.
