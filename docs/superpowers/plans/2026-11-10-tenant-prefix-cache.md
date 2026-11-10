# Tenant Prefix Cache Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Raise DeepSeek prefix-cache hit rate across chats of the same company by optionally sharing one `user_id` per client+CompanyID, while each chat's question, history, transcript, and thread card stay after the static prefix.

**Architecture:** `CHATBOT_CACHE_SCOPE` is read inside `core.agent._user_id` on every call. `session` (default) keeps today's hash of `client|company_id|subject`. `tenant` hashes `client|company_id` only, so a new `session_id` reuses the same DeepSeek `user_id` and the byte-stable opening (`_static_prefix`: system.md + join playbook + schema block + vault cards) can hit. `api/server.py` still derives `subject` from `session_id`; that value is ignored only when the scope is `tenant`. Conversation text is already appended after `_prefix_messages` in `ask_stream`; this plan locks that boundary with tests and does not move it.

**Tech Stack:** Python 3.13 (`py -3.13`), pytest, existing `core/agent.py` + `core/llm.py` (`user_id` via `extra_body`). No new dependencies.

## Global Constraints

- Python 3.13 only (`py -3.13`, never python3).
- LLM keys only in gitignored `.env`, read by core/llm.py.
- Do not bypass core/gate.py. Do not add credentials.
- Do not put session text into the static prefix.
- Default CHATBOT_CACHE_SCOPE=session so behavior does not change until the flag is set.
- Windows: do not inline multi-line Python in `py -c`; if a step needs a script, tell them to write a file under work/ (gitignored).

---

## File structure

| File | Responsibility |
|------|----------------|
| `core/agent.py` `_user_id` (lines 125–130) | Only product-code change. Same signature `(client: str, company_id, subject: str \| None) -> str`. Reads `CHATBOT_CACHE_SCOPE` at call time. |
| `.env.example` | Document the flag next to `CHATBOT_CLIENT`. No secret. |
| `tests/test_agent.py` | New unit tests. No network, no SQL, no live model. |
| `work/cache_scope_check.py` | Checkpoint-only reader of `work/trace.jsonl`. Gitignored. Not product code. |

Do not edit `prompts/system.md`, `prompts/join_playbook.md`, `core/gate.py`, `core/sql.py`, or `api/server.py`.

Verified call sites (leave the calls as they are; they already pass `client`, `company_id`, `subject`):

- `core/agent.py` plan-cache replay: `user_id=_user_id(client, company_id, subject)` (~line 2040)
- `core/agent.py` full turn state: `"_user_id": _user_id(client, company_id, subject)` (~line 2291)

`core/llm.py` `stream_create_kwargs` already puts `user_id` on `extra_body` when it is non-empty. DeepSeek treats the same `user_id` plus identical leading request bytes as a prefix-cache hit. A new chat today gets a new `subject` (sha256 of `session_id`, 12 hex chars, `api/server.py` ~line 410), so `_user_id` changes and the first call misses the ~64k-token prefix. Later calls in the same chat already hit ~94–98%. Task 8 already snapshots `turn_tools` once per turn (`state["turn_tools"]` ~lines 2315–2322); do not touch that.

`_static_prefix(client, cache)` returns system + schema + vault cards only. `_prefix_messages` appends the thread card after that list. `prefix_hash` dumps `_static_prefix` only, so a thread card cannot change the hash. History (`_conversation_block`), transcript (`_transcript_index_block`), the CompanyID pin line, and the user question are appended later in `ask_stream` (~lines 2224–2246), after `_prefix_messages` (~line 2093).

## Task 1: Failing tests for `_user_id` scope

**Files:**
- Modify: `tests/test_agent.py` (append at end of file)
- Test: `tests/test_agent.py`

**Interfaces:**
- Consumes: `core.agent._user_id(client: str, company_id, subject: str | None) -> str` as it exists today (always hashes `f"{client}|{company_id}|{subject or 'anon'}"` with SHA-256, first 32 hex chars).
- Produces: tests that Task 2 must turn green. No new public function.

- [ ] **Step 1: Append the failing tests**

Append this block at the end of `tests/test_agent.py`. Do not change existing tests.

```python
import hashlib
import re

_USER_ID_RE = re.compile(r"^[a-zA-Z0-9_-]+$")


def test_user_id_session_scope_differs_by_subject(monkeypatch):
    monkeypatch.setenv("CHATBOT_CACHE_SCOPE", "session")
    a = agent._user_id("morec", 1, "subject-aaa")
    b = agent._user_id("morec", 1, "subject-bbb")
    again = agent._user_id("morec", 1, "subject-aaa")
    assert a != b
    assert a == again
    assert len(a) == 32 and _USER_ID_RE.fullmatch(a)
    assert len(b) == 32 and _USER_ID_RE.fullmatch(b)


def test_user_id_unset_scope_matches_session_hash(monkeypatch):
    monkeypatch.delenv("CHATBOT_CACHE_SCOPE", raising=False)
    got = agent._user_id("morec", 1, "subject-aaa")
    raw = "morec|1|subject-aaa"
    assert got == hashlib.sha256(raw.encode()).hexdigest()[:32]


def test_user_id_blank_subject_uses_anon_in_session_scope(monkeypatch):
    monkeypatch.setenv("CHATBOT_CACHE_SCOPE", "session")
    assert agent._user_id("morec", 1, None) == agent._user_id("morec", 1, "")
    raw = "morec|1|anon"
    assert agent._user_id("morec", 1, None) == hashlib.sha256(raw.encode()).hexdigest()[:32]


def test_user_id_tenant_scope_ignores_subject(monkeypatch):
    monkeypatch.setenv("CHATBOT_CACHE_SCOPE", "tenant")
    a = agent._user_id("morec", 1, "subject-aaa")
    b = agent._user_id("morec", 1, "subject-bbb")
    c = agent._user_id("morec", 1, None)
    assert a == b == c
    raw = "morec|1"
    assert a == hashlib.sha256(raw.encode()).hexdigest()[:32]
    assert len(a) == 32 and _USER_ID_RE.fullmatch(a)


def test_user_id_tenant_scope_splits_company_and_client(monkeypatch):
    monkeypatch.setenv("CHATBOT_CACHE_SCOPE", "tenant")
    same = agent._user_id("morec", 1, "s1")
    other_company = agent._user_id("morec", 2, "s1")
    other_client = agent._user_id("rukn", 1, "s1")
    assert same != other_company
    assert same != other_client
    assert other_company != other_client


def test_user_id_unknown_scope_stays_on_session(monkeypatch):
    monkeypatch.setenv("CHATBOT_CACHE_SCOPE", "TENANT ")
    shared = agent._user_id("morec", 1, "s1")
    monkeypatch.setenv("CHATBOT_CACHE_SCOPE", "bogus")
    split_a = agent._user_id("morec", 1, "s1")
    split_b = agent._user_id("morec", 1, "s2")
    # "tenant" with surrounding whitespace is tenant; anything else is session.
    assert shared == hashlib.sha256("morec|1".encode()).hexdigest()[:32]
    assert split_a != split_b
    assert split_a == hashlib.sha256("morec|1|s1".encode()).hexdigest()[:32]
```

`hashlib` and `re` are not imported at the top of `tests/test_agent.py` today. The block above imports them. If a later edit adds those imports at module top, delete the duplicates in this block so the file imports each name once.

- [ ] **Step 2: Run the new tests and confirm the tenant cases fail**

Run:

```
py -3.13 -m pytest tests/test_agent.py::test_user_id_session_scope_differs_by_subject tests/test_agent.py::test_user_id_unset_scope_matches_session_hash tests/test_agent.py::test_user_id_blank_subject_uses_anon_in_session_scope tests/test_agent.py::test_user_id_tenant_scope_ignores_subject tests/test_agent.py::test_user_id_tenant_scope_splits_company_and_client tests/test_agent.py::test_user_id_unknown_scope_stays_on_session -v
```

Expected: the three `session` / unset / blank-subject tests PASS (today's hash). `test_user_id_tenant_scope_ignores_subject` FAILS because two subjects still produce two ids (`assert a == b`). `test_user_id_tenant_scope_splits_company_and_client` may PASS by accident (different client/company already differ) or FAIL the implicit tenant equality used by the next test; `test_user_id_unknown_scope_stays_on_session` FAILS on `shared == sha256("morec|1")` because whitespace-stripped `tenant` is not implemented. Do not change `core/agent.py` in this task.

- [ ] **Step 3: Commit the failing tests**

```
git add tests/test_agent.py
git commit -m "test: lock DeepSeek user_id session and tenant scopes"
```

## Task 2: Read `CHATBOT_CACHE_SCOPE` inside `_user_id`

**Files:**
- Modify: `core/agent.py` (function `_user_id`, lines 125–130)
- Modify: `.env.example` (after the `CHATBOT_CLIENT=morec` line)
- Test: `tests/test_agent.py` (tests from Task 1)

**Interfaces:**
- Consumes: Task 1 tests. `os` is already imported in `core/agent.py`.
- Produces: `_user_id(client: str, company_id, subject: str | None) -> str` — 32 chars matching `^[a-zA-Z0-9_-]+$`. `CHATBOT_CACHE_SCOPE=tenant` (case-insensitive, surrounding whitespace stripped) hashes `f"{client}|{company_id}"`. Any other value, including unset, hashes `f"{client}|{company_id}|{subject or 'anon'}"`. `company_id` is interpolated with `str()` via the f-string, same as today (int `1` becomes `"1"`).

- [ ] **Step 1: Replace `_user_id`**

Replace the whole function (lines 125–130) with:

```python
def _user_id(client: str, company_id, subject: str | None) -> str:
    """DeepSeek user_id (regex [a-zA-Z0-9_-]+).

    CHATBOT_CACHE_SCOPE=session (default): hash of client|company_id|subject
    so chats do not share a prefix-cache id.
    CHATBOT_CACHE_SCOPE=tenant: hash of client|company_id only, so every chat
    of that company reuses the prefix cache. Subject is ignored. Never drop
    client or company_id. Session text is not part of this id.
    """
    scope = os.environ.get("CHATBOT_CACHE_SCOPE", "session").strip().lower()
    if scope == "tenant":
        raw = f"{client}|{company_id}"
    else:
        raw = f"{client}|{company_id}|{subject or 'anon'}"
    return hashlib.sha256(raw.encode()).hexdigest()[:32]
```

Read the env inside the function. Do not cache it at import time (`_MIDTURN_ESCALATION` is import-time; this flag must not be, or pytest `monkeypatch.setenv` will not see it).

- [ ] **Step 2: Document the flag in `.env.example`**

Insert these lines immediately after `CHATBOT_CLIENT=morec`:

```
# DeepSeek prefix-cache id. session = one id per chat (default).
# tenant = one id per CHATBOT_CLIENT + CompanyID. Session text stays out of the cached prefix.
# Rollback: set this back to session and restart. No schema or prompt change.
CHATBOT_CACHE_SCOPE=session
```

Do not put a value in the gitignored `.env` unless the operator asks. Default in code is `session` when the variable is absent.

- [ ] **Step 3: Run the Task 1 tests**

Run the same `py -3.13 -m pytest ...` command as Task 1 Step 2.

Expected: 6 passed.

- [ ] **Step 4: Commit**

```
git add core/agent.py .env.example
git commit -m "feat: share DeepSeek user_id per company when cache scope is tenant"
```

## Task 3: Lock the static-prefix boundary

**Files:**
- Modify: `tests/test_agent.py` (append)
- Test: `tests/test_agent.py`
- Modify product code only if Step 2 fails because history, the question, or the thread card is inside `_static_prefix` or inside `prefix_hash`.

**Interfaces:**
- Consumes: `_static_prefix(client: str, cache: dict) -> list[dict]`, `prefix_hash(client: str, cache: dict) -> str`, `_prefix_messages(client: str, cache: dict, thread_head: dict | None = None) -> list[dict]`, `_conversation_block(history) -> str | None`, `_transcript_index_block(transcript) -> str | None`.
- Produces: tests that fail the build if a later edit moves session text into the hashed prefix. No new agent function. `ask_stream` message order stays: `_prefix_messages` (static prefix, then optional thread card), then later system notes, then `_conversation_block(history)`, `_transcript_index_block(transcript)`, then `{"role": "user", "content": question}`.

Current code already keeps history and the question out of `_static_prefix`. This task records that. Do not refactor the prefix, the playbook, or the tool list to chase a larger hit.

- [ ] **Step 1: Append the locking tests**

Append at the end of `tests/test_agent.py`:

```python
_TINY_CACHE = {
    "has_tenant_view": {"dbo.Customers": True},
    "tables": {
        "dbo.Customers": [
            {"column": "ID", "type": "int", "nullable": False},
            {"column": "Name", "type": "nvarchar", "nullable": True},
        ]
    },
}


def _messages_like_ask_stream(client, cache, *, thread_head, history, transcript, question):
    """Same boundary ask_stream uses: static prefix, then thread card, then
    history/transcript/question. Skips few-shots and report cards, which are
    also appended after _prefix_messages and are not part of prefix_hash."""
    messages = agent._prefix_messages(client, cache, thread_head)
    conv_block = agent._conversation_block(history)
    if conv_block:
        messages.append({"role": "system", "content": conv_block})
    index_block = agent._transcript_index_block(transcript)
    if index_block:
        messages.append({"role": "system", "content": index_block})
    messages.append({"role": "user", "content": question})
    return messages


def test_static_prefix_ignores_history_question_and_thread(monkeypatch):
    monkeypatch.setattr(agent, "_all_cards_block", lambda client: "CARD-BLOCK")
    static = agent._static_prefix("morec", _TINY_CACHE)
    blob = json.dumps(static, ensure_ascii=False)
    assert "SESSION-B-SECRET-ANSWER" not in blob
    assert "how many customers" not in blob
    assert "thread-title-b" not in blob
    h1 = agent.prefix_hash("morec", _TINY_CACHE)
    h2 = agent.prefix_hash("morec", _TINY_CACHE)
    assert h1 == h2
    assert len(h1) == 16
    # prefix_hash has no thread_head parameter; the card must not affect it.
    with_card = agent._prefix_messages("morec", _TINY_CACHE, {"title": "thread-title-b"})
    without_card = agent._prefix_messages("morec", _TINY_CACHE, None)
    assert without_card == static
    assert with_card[: len(static)] == static
    assert with_card[-1]["content"] != static[-1]["content"]
    assert agent.prefix_hash("morec", _TINY_CACHE) == h1


def test_two_sessions_share_static_prefix_bytes_and_differ_after_it(monkeypatch):
    monkeypatch.setattr(agent, "_all_cards_block", lambda client: "CARD-BLOCK")
    static = agent._static_prefix("morec", _TINY_CACHE)
    session_a = _messages_like_ask_stream(
        "morec",
        _TINY_CACHE,
        thread_head={"title": "card-A"},
        history=[{"q": "question A only", "a": "answer A only"}],
        transcript=[{"q": "question A only"}],
        question="how many customers in A",
    )
    session_b = _messages_like_ask_stream(
        "morec",
        _TINY_CACHE,
        thread_head={"title": "card-B"},
        history=[{"q": "question B only", "a": "SESSION-B-SECRET-ANSWER"}],
        transcript=[{"q": "question B only"}],
        question="list unpaid invoices in B",
    )
    n = len(static)
    assert session_a[:n] == static
    assert session_b[:n] == static
    assert session_a[:n] == session_b[:n]
    tail_a = json.dumps(session_a[n:], ensure_ascii=False)
    tail_b = json.dumps(session_b[n:], ensure_ascii=False)
    prefix_a = json.dumps(session_a[:n], ensure_ascii=False)
    assert "SESSION-B-SECRET-ANSWER" in tail_b
    assert "SESSION-B-SECRET-ANSWER" not in prefix_a
    assert "list unpaid invoices in B" not in prefix_a
    assert "how many customers in A" not in json.dumps(session_b[:n], ensure_ascii=False)
    assert tail_a != tail_b
    assert "answer A only" in tail_a
    assert "answer A only" not in json.dumps(session_b[:n], ensure_ascii=False)
```

`json` is not imported in `tests/test_agent.py` today. This block needs `import json` once (add it next to the Task 1 `hashlib` / `re` imports if those are still local, or at module top). `_all_cards_block` is stubbed so the test does not open `work/<client>/` vault sqlite.

- [ ] **Step 2: Run the locking tests**

```
py -3.13 -m pytest tests/test_agent.py::test_static_prefix_ignores_history_question_and_thread tests/test_agent.py::test_two_sessions_share_static_prefix_bytes_and_differ_after_it -v
```

Expected: PASS on the current `ask_stream` layout. A PASS here means Task 4 is "no product change".

If a test FAILs because `SESSION-B-SECRET-ANSWER`, a question string, or `thread-title-b` appears inside `_static_prefix` or changes `prefix_hash`: stop. The fix is to keep that text in the messages appended after `_static_prefix` (thread card only via `_prefix_messages`, history via `_conversation_block`). Do not add the text to `prompts/system.md`. Do not change `prefix_hash` to hash `_prefix_messages`. Re-run this command until both tests PASS, then continue.

- [ ] **Step 3: Commit the locking tests (and a prefix fix only if Step 2 required one)**

```
git add tests/test_agent.py
git commit -m "test: keep chat history outside the DeepSeek static prefix"
```

If Step 2 forced a change in `core/agent.py`, add that file to the same commit and say so in the message body in one sentence: history or the thread card had entered the hashed prefix and was moved back after `_static_prefix`.

## Task 4: No prefix refactor when the boundary already holds

**Files:**
- None, when Task 3 Step 2 passed without editing `core/agent.py`.

**Interfaces:**
- Consumes: Task 3 result.
- Produces: an explicit stop. Later work must not "improve" hit rate by folding history, the transcript, the thread card, or the user question into `_static_prefix`.

- [ ] **Step 1: Record the Task 3 result**

If both Task 3 tests passed with zero edits under `core/`, this task is done. Do not edit `core/agent.py`, prompts, the gate, or SQL.

If Task 3 required a product edit, that edit already landed in the Task 3 commit. Do not open a second refactor.

- [ ] **Step 2: Re-run the user-id tests and the prefix tests together**

```
py -3.13 -m pytest tests/test_agent.py::test_user_id_session_scope_differs_by_subject tests/test_agent.py::test_user_id_unset_scope_matches_session_hash tests/test_agent.py::test_user_id_blank_subject_uses_anon_in_session_scope tests/test_agent.py::test_user_id_tenant_scope_ignores_subject tests/test_agent.py::test_user_id_tenant_scope_splits_company_and_client tests/test_agent.py::test_user_id_unknown_scope_stays_on_session tests/test_agent.py::test_static_prefix_ignores_history_question_and_thread tests/test_agent.py::test_two_sessions_share_static_prefix_bytes_and_differ_after_it -v
```

Expected: 8 passed.

There is no `test_agent.py` test today whose name covers `_user_id`. `test_final_contract_call_carries_no_tools_and_json_mode` only asserts a stub `user_id` of `"uid123"` forwarded into `llm.complete`. Do not require `evals/run_evals.py`.

- [ ] **Step 3: No commit if the tree is clean**

`git status` should show no staged product changes from this task. Do not create an empty commit.

## Task 5: Two-session cache checkpoint (manual, no product change)

**Files:**
- Create: `work/cache_scope_check.py` (gitignored; do not `git add` it)
- Modify: none of the application

**Interfaces:**
- Consumes: `CHATBOT_CACHE_SCOPE` from Task 2. Trace rows from `core.trace.log_event`: each `event=="answer"` row includes `subject` (12-hex sha256 prefix of `session_id`), `question`, `cache_hit_tokens`, `cache_miss_tokens`, and `calls` (list from `Usage.totals()`, each call has `cache_hit` and `cache_miss`). `work/trace.jsonl` is appended; do not delete it.
- Produces: a pass/fail printout. Rollback remains `CHATBOT_CACHE_SCOPE=session` plus process restart. No DB migration, no prompt rewrite, no SQL change.

Do not run the live bot, bind port 8100, or call DeepSeek while writing this plan. The implementer runs this task only after Tasks 1–4 are committed.

Unit tests do not start the server. This checkpoint is the only live step.

- [ ] **Step 1: Write `work/cache_scope_check.py`**

```python
"""Read work/trace.jsonl and score the latest answer for two subjects.

Usage:
  py -3.13 work/cache_scope_check.py <subject_a> <subject_b> <mode>

mode is "tenant" or "session".
Prints hit ratios only. Does not print API keys.
"""
import json
import sys
from pathlib import Path

TRACE = Path(__file__).resolve().parent / "trace.jsonl"


def latest_answer(subject: str) -> dict:
    found = None
    with TRACE.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if row.get("event") == "answer" and row.get("subject") == subject:
                found = row
    if found is None:
        raise SystemExit(f"no answer row for subject {subject}")
    return found


def call0_ratio(row: dict) -> tuple[int, int, float]:
    calls = row.get("calls") or []
    if calls:
        hit = int(calls[0].get("cache_hit") or 0)
        miss = int(calls[0].get("cache_miss") or 0)
    else:
        hit = int(row.get("cache_hit_tokens") or 0)
        miss = int(row.get("cache_miss_tokens") or 0)
    total = hit + miss
    ratio = (hit / total) if total else 0.0
    return hit, miss, ratio


def main() -> None:
    subject_a, subject_b, mode = sys.argv[1], sys.argv[2], sys.argv[3]
    row_a = latest_answer(subject_a)
    row_b = latest_answer(subject_b)
    hit_b, miss_b, ratio_b = call0_ratio(row_b)
    answer_a = str(row_a.get("answer") or row_a.get("final_text") or "")
    # log_event stores the question, not the answer prose. The done-event
    # answer is not a trace field. Compare questions, and compare answer
    # text only when the caller pasted it into the optional argv slot.
    print(f"mode={mode}")
    print(f"subject_a={subject_a} question={row_a.get('question')!r}")
    print(f"subject_b={subject_b} question={row_b.get('question')!r}")
    print(f"session_b_call0 hit={hit_b} miss={miss_b} ratio={ratio_b:.3f}")
    print(f"questions_differ={row_a.get('question') != row_b.get('question')}")
    if mode == "tenant":
        ok = ratio_b >= 0.8 and row_a.get("question") != row_b.get("question")
    elif mode == "session":
        ok = ratio_b < 0.5 and row_a.get("question") != row_b.get("question")
    else:
        raise SystemExit("mode must be tenant or session")
    print("PASS" if ok else "FAIL")
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
```

Trace `answer` events do not store the model answer text (`log_event` fields are `question`, `event`, usage totals, and `calls`). The operator compares the two chat answers on screen: they must not be copies of each other. The script enforces different questions plus the hit ratio. If the on-screen answers are identical or session B answers session A's question, treat the checkpoint as FAIL even when the script prints PASS, and only then consider a golden session (`evals/run_evals.py` is not required for this change).

`calls[0]` is the first LLM call of that turn (`Usage.totals()` preserves call order). That is "call #0". If `calls` is missing, fall back to the turn totals `cache_hit_tokens` / `cache_miss_tokens`.

- [ ] **Step 2: Restart the API with tenant scope**

Set `CHATBOT_CACHE_SCOPE=tenant` in the gitignored `.env` (leave `CHATBOT_CLIENT` as the pinned tenant). Stop the existing API process. Start it the way this repo already starts (see `README.md` / `run.ps1` or `run.sh`). Do not start a second copy on the same port.

Confirm the process picked up the env var. Do not print `DEEPSEEK_API_KEY`.

- [ ] **Step 3: Two new chats, tenant scope**

Use two brand-new `session_id` values that have never been sent, same company (the UI company already pinned for this process). One short question each, and the questions must be different, for example:

- session `cache-scope-a`: `كم عدد العملاء؟`
- session `cache-scope-b`: `كم عدد المندوبين؟`

Send them in that order, one `/ask` each, through the existing chat UI or the existing `/ask` client. Wait until each request finishes.

Subject in the trace is `sha256(session_id.encode()).hexdigest()[:12]` (`api/server.py`). Compute the two subjects with a file under `work/` if needed (do not use a multi-line `py -c`). One-line form that is valid in PowerShell:

```
py -3.13 -c "import hashlib; print(hashlib.sha256(b'cache-scope-a').hexdigest()[:12]); print(hashlib.sha256(b'cache-scope-b').hexdigest()[:12])"
```

- [ ] **Step 4: Score tenant scope**

```
py -3.13 work/cache_scope_check.py <subject_a> <subject_b> tenant
```

Pass when the script prints `PASS`: session B call #0 `hit / (hit + miss) >= 0.8`, and the two questions differ. Also read the two on-screen answers: each must address its own question (a customer count is not a copy of a salesman count). Do not paste secrets from the trace.

A miss on session B call #0 with the flag set to `tenant` means the `user_id` did not stick (process not restarted, or scope still `session`) or the leading bytes diverged (tool list / gear / prompt edit). Do not fix that by moving history into `_static_prefix`.

- [ ] **Step 5: Repeat with session scope**

Set `CHATBOT_CACHE_SCOPE=session`, restart the API, and send two more brand-new session ids (not the ones from Step 3), same company, two different short questions, session B after session A.

```
py -3.13 work/cache_scope_check.py <subject_a2> <subject_b2> session
```

Pass when the script prints `PASS`: session B call #0 ratio `< 0.5` (a miss). That shows the flag changes behavior. Session A's own later round-trip inside one chat may still hit; this check is only call #0 of a new session id.

- [ ] **Step 6: Leave the default in place**

After the checkpoint, set `CHATBOT_CACHE_SCOPE=session` in `.env` unless the operator wants `tenant` left on. `.env` stays untracked. Do not commit `work/cache_scope_check.py`.

No product commit belongs to this task.

---

## Spec coverage

| Requirement | Task |
|-------------|----------------|
| `session` default, two subjects → two ids, same subject stable | 1, 2 |
| `tenant` ignores subject; different company or client → different id | 1, 2 |
| `user_id` regex and length 32 | 1, 2 |
| `prefix_hash` / `_static_prefix` ignore history, question, thread card | 3, 4 |
| Message list: first N == `_static_prefix`; history and question only after that | 3 |
| Two sessions share prefix bytes and differ afterward; session B text not inside session A's prefix | 3 |
| Do not claim the model cannot leak | 3 (assertion is about bytes we send) |
| Live two-session hit ratio ≥ 0.8 in `tenant`, < 0.5 in `session`; answers not copies | 5 |
| No live bot during unit tasks; no `evals/run_evals.py` requirement | 1–4 vs 5 |
| No edits to prompts, playbook, gate, SQL in Tasks 1–5 | Tasks 1–5 |
| Rollback of the id = env back to `session` | 2 (`.env.example`), 5 |
| Shrink the static prefix without moving session text into it | Tasks 6–8 |
| Each prefix cut has a unit test and a before/after char count | Tasks 6–7 |
| Live check stays two short questions, not a golden session | Task 8 |
| Defects that need a wording revision are listed, not silently "fixed" by deletion | Defect map below |

---

## Static prefix (the ~64k tokens)

Measured on client 105 from `prompts/system.md`, `prompts/join_playbook.md`, `work/105/schema_cache.json`, and `work/105/vault_cards.sqlite` (no database connection). Three system messages, 222,039 characters, about 55,500 tokens at 4 characters per token. Tool JSON is about 1,900 tokens and is not inside `prefix_hash`.

| Piece | Chars | Share |
|---|---:|---:|
| system.md + join playbook | 26,607 | 12% |
| `_schema_block` (411 views) | 104,319 | 47% |
| `_all_cards_block` (507 cards) | 91,113 | 41% |

Tasks 1–5 do not change these bytes. Tasks 6–7 change only the schema line and the card line. They do not edit `prompts/system.md` or `prompts/join_playbook.md`. A shorter prompt is a separate revision (see the defect map). Mixing it into this experiment would make a worse answer impossible to attribute.

### Defect map

| Defect | Root cause | Test that locks it | Applied in this plan? |
|---|---|---|---|
| First call of a new chat misses ~64k tokens | `_user_id` includes `session_id` (`api/server.py` subject hash) | Task 1–2 unit; Task 5 / Task 8 live hit ratio | Yes (flag, default off) |
| Schema block is half the prefix | Every column is `name:type?`, and `CompanyID` is repeated on 372 tables | Task 6: rendered line has no `:`, no `?`, no `CompanyID` | Yes |
| Old/temp views look like real tables | `_schema_block` keeps every `has_tenant_view` entry, including `CustomersFinancialDetails_Old`, `Technical_CFD_temp`, `LogActionTransaction_` | Task 6: those names are absent | Yes |
| Card block repeats primary keys the schema line already lists | `_all_cards_block` appends `\| PK …` | Task 7: no `\| PK` in the block; `\| FK` remains | Yes |
| «صافي» means charged total in the playbook and net of returns in `system.md` | Two authors, both files are in message 0 | Not a size cut. Do not delete either sentence in this plan. A later revision must make one definition and point both files at it | No |
| Empty month: offer last period vs wait for confirm | Three paragraphs in `system.md` | Wording revision, not a byte-diet task | No |
| Playbook names `OT_StoreItemsQty` / `OT_ItemsMF`; they are not `t.` views here | Playbook written for another client shape. Only `OT_SendLog` is in the 411-view block | Wording revision | No |
| `WFApproved` vs also `Approved` | Playbook order-taking line is stricter than `system.md` | Wording revision | No |
| 28 tables with no `t.` view still have cards | Cards DB is wider than `has_tenant_view` | Task 7 does not drop those cards. Dropping them needs a check that no join text is lost | No |
| Alias cards omit `maps_to` | `_all_cards_block` prints the Arabic name only | Revision: print `maps_to`. Not in the diet, because adding text does not shrink the prefix | No |

### Task 6: Schema lines are bare column names

**Files:**
- Modify: `core/agent.py` `_schema_block` (about lines 288–311)
- Test: `tests/test_agent.py`

**Interfaces:**
- Consumes: `cache["tables"]`, `cache["has_tenant_view"]`, `gate.HIDDEN_TABLES`.
- Produces: `_schema_block(cache) -> str`. Same signature. Columns are space-separated names. `CompanyID` is omitted. A table whose bare name ends with `_old`, `_temp`, or `_` is omitted (case-insensitive). Types and `?` are omitted. Header sentences stay.

- [ ] **Step 1: Write the failing test**

```python
def test_schema_block_drops_types_companyid_and_junk_views():
    cache = {
        "has_tenant_view": {
            "dbo.Items": True,
            "dbo.CustomersFinancialDetails_Old": True,
            "dbo.Technical_CFD_temp": True,
            "dbo.LogActionTransaction_": True,
        },
        "tables": {
            "dbo.Items": [
                {"column": "CompanyID", "type": "smallint", "nullable": False},
                {"column": "ItemCode", "type": "nvarchar", "nullable": False},
                {"column": "Name", "type": "nvarchar", "nullable": True},
            ],
            "dbo.CustomersFinancialDetails_Old": [{"column": "ID", "type": "int", "nullable": False}],
            "dbo.Technical_CFD_temp": [{"column": "ID", "type": "int", "nullable": False}],
            "dbo.LogActionTransaction_": [{"column": "ID", "type": "int", "nullable": False}],
        },
    }
    text = agent._schema_block(cache)
    assert "dbo.Items(ItemCode, Name)" in text
    assert "CompanyID" not in text
    assert "nvarchar" not in text and "?" not in text
    assert "CustomersFinancialDetails_Old" not in text
    assert "Technical_CFD_temp" not in text
    assert "LogActionTransaction_" not in text
```

- [ ] **Step 2: Run it and confirm FAIL**

Run: `py -3.13 -m pytest tests/test_agent.py::test_schema_block_drops_types_companyid_and_junk_views -q`
Expected: FAIL (`CompanyID` or a type is still present).

- [ ] **Step 3: Implement**

In `_schema_block`, skip a table when `bare.endswith("_old") or bare.endswith("_temp") or bare.endswith("_")`. Render columns with:

```python
names = [c.get("column") for c in cols if isinstance(c, dict) and c.get("column") and str(c.get("column")).lower() != "companyid"]
rendered = ", ".join(names)
```

- [ ] **Step 4: Run the test**

Run: `py -3.13 -m pytest tests/test_agent.py::test_schema_block_drops_types_companyid_and_junk_views -q`
Expected: PASS

- [ ] **Step 5: Commit**

```
git add core/agent.py tests/test_agent.py
git commit -m "perf(prefix): schema lines list column names only"
```

### Task 7: Cards keep purpose and foreign keys, drop primary keys

**Files:**
- Modify: `core/agent.py` `_all_cards_block` (the non-relation branch)
- Test: `tests/test_agent.py`

**Interfaces:**
- Consumes: `vault._load_cards(client)`.
- Produces: same `_all_cards_block(client) -> str`. Relation lines unchanged. Table lines have no `| PK`.

- [ ] **Step 1: Write the failing test**

Monkeypatch `agent.vault._load_cards` to return one table card and one relation card:

```python
def test_cards_block_omits_primary_key(monkeypatch):
    monkeypatch.setattr(agent.vault, "_load_cards", lambda client: [
        {"kind": "table", "name": "Items", "purpose": "sellable items",
         "primary_key": "ItemCode", "foreign_keys": "CompanyID"},
        {"kind": "relation", "parent": "Items", "referenced": "Categories",
         "columns": "CategoryID"},
    ])
    text = agent._all_cards_block("105")
    assert "| PK" not in text
    assert "sellable items" in text
    assert "| FK CompanyID" in text
    assert "Items→Categories" in text or "Items" in text and "Categories" in text
```

- [ ] **Step 2: Confirm FAIL** (`| PK` is present).

- [ ] **Step 3: Stop appending `pk` in the non-relation branch.** Leave `purpose` and `fk` as they are.

- [ ] **Step 4: PASS**

- [ ] **Step 5: Commit** `perf(prefix): drop primary keys from vault card lines`

### Task 8: Light before/after, two questions only

No golden session. No held-out. No `run_evals.py`. Two `/ask` calls total on the worktree server.

- [ ] **Step 1: Char counts with no network**

A script under `work/` (gitignored) loads `work/105/schema_cache.json` and calls `_schema_block` and `_all_cards_block` and `_static_prefix`. Print chars for message 0, schema, cards, and the total. This is the "after" size. The "before" size is the table at the top of this section (222,039 characters). Record both in the worktree note. Do not start the API for this step.

- [ ] **Step 2: Two live questions, one new session, tenant scope**

Restart the API from the worktree on port **8101** so the existing server on 8100 is left alone. `CHATBOT_CACHE_SCOPE=tenant`. One session, two different short questions:

1. `كم عدد العملاء؟`
2. `كم عدد المندوبين؟`

Pass: question 2 call #0 hit ratio ≥ 0.8 (the prefix is warm inside the session; this does not by itself prove cross-session sharing). Question 2's answer is a salesperson count, not a copy of the customer count. If either answer is an error or a refusal, record the trace `tool_errors` and stop. Do not send a third question to "retry".

- [ ] **Step 3: Map anything worse**

If the answers are wrong, name the root cause from the defect map (missing type, missing CompanyID column, dropped junk view, or an unrelated model miss). Do not widen the prefix again in the same turn. Write the numbers (chars, hit ratio, latency, usd if the trace has calls) into `work/prefix_diet_note.md` in the worktree only. That file stays gitignored.
