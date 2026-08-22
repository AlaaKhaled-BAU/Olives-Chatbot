# DeepSeek Migration — Parallelized Implementation Plan

Status: READY FOR EXECUTION. Provider key verified live against `GET /models` on 2026-08-22
(returns `deepseek-v4-flash`, `deepseek-v4-pro`, `deepseek-v4-flash-vision-exp`).
Key lives only in gitignored `.env` as `DEEPSEEK_API_KEY`. OmniRoute is removed in this
migration (Lane C) — no dual-provider runtime; rollback = git revert to tag `pre-deepseek-swap`.

---

## 1. Verified provider spec (api-docs.deepseek.com, fetched 2026-08-22)

| Spec | Value |
|---|---|
| Base URL (OpenAI format) | `https://api.deepseek.com` |
| Models | `deepseek-v4-flash`, `deepseek-v4-pro` (`-vision-exp` exists — EXCLUDED, experimental) |
| Context / max output | 1M tokens / 384K tokens |
| flash $/1M (hit / miss / out), off-peak–peak | $0.007–0.014 / $0.22–0.44 / $0.66–1.32 |
| pro $/1M (hit / miss / out), off-peak–peak | $0.022–0.044 / $0.66–1.32 / $1.98–3.96 |
| Peak windows (UTC) | 01:00–04:00 and 06:00–10:00; off-peak = half price |
| Concurrency | flash 2500 / pro 500, account-level; free expansion form |
| Thinking mode | **ON by default, effort=high**; toggle `extra_body={"thinking":{"type":"enabled"/"disabled"}}`; `reasoning_effort` ∈ low/high/max (`medium` maps→high) |
| Legacy aliases | `deepseek-chat`/`deepseek-reasoner` dead since 2026-07-24 |

**Binding API contracts (each one breaks something if ignored):**

- **B1 — reasoning echo:** with `tools` + thinking enabled, every subsequent request MUST
  carry back the assistant message incl. `reasoning_content`, else **HTTP 400**.
- **B2 — KV cache semantics:** automatic disk prefix cache; hit requires FULL match of a
  persisted *cache-prefix unit* (SWA); units persist at request boundaries / common-prefix
  detection / fixed token intervals; evicted "within hours to days"; best-effort.
  Response reports `usage.prompt_cache_hit_tokens` / `usage.prompt_cache_miss_tokens`.
- **B3 — thinking ignores sampling params:** `temperature`/`top_p`/`presence_penalty`/
  `frequency_penalty` silently no-op in thinking mode.
- **B4 — `user_id`:** regex `[a-zA-Z0-9\-_]+`, ≤512 chars, no PII; OpenAI SDK requires
  `extra_body={"user_id": ...}`. Gives KVCache isolation + scheduling isolation per user.
- **B5 — keep-alive:** streaming emits `: keep-alive` SSE comments during inference;
  non-streaming sends blank lines; connection closed only if inference never starts within 10 min.

## 2. Hard constraints (reviewer checklist — apply to every PR)

- **C1 byte-stable prefix:** messages[0..2] (system+playbook, full schema, all vault cards)
  must be byte-identical across turns for a given client+company. NO dates, timestamps,
  counters, or question text inside them. Dynamic content starts at messages[3].
- **C2 reasoning echo:** any request carrying `tools` must append the full assistant message
  (content + reasoning_content + tool_calls). Covered by a hermetic test before cutover.
- **C3 no sampling-param reliance on t1/t2/p gears** (silently ignored).
- **C4 `user_id` = `sha256(f"{client}|{company_id}|{session_id}").hexdigest()[:32]`** — hex
  passes the regex; same value reused for rate limiting + trace subject.
- **C5 timeouts:** f0=30s, t1=60s, t2=90s, p=300s async-only. Gear `p` NEVER in interactive path.
- **C6 log every call:** gear, model, latency, output tokens,
  prompt_cache_hit_tokens/prompt_cache_miss_tokens (verifies C1 economics).
- **C7 Arabic-only user-visible errors** (existing `GATEWAY_UNAVAILABLE_AR` text kept, renamed);
  raw exception text never reaches SSE frames.
- **C8 golden rules intact:** gate-only SQL path, no proc bodies, env-pinned tenant, key only
  in `.env`. The migration touches none of these walls.

## 3. Lanes & dependency graph

```
Track 1 (provider core, STRICTLY sequential):
  A1 llm.py rewrite ──► A2 reasoning threading ──► A3 gear routing ──► A4 stable prefix

Track 2 (server/SSE, parallel with Track 1):   B1 stream hardening ──► B2 health rewire
Track 3 (eval integrity, parallel until end):  D1 scorer fix ─┬─► D3 re-baseline (last)
                                                               D2 promote-gate+purge
Track 4 (JSON contract, after A2 lands):       E1 answer contract
Track 5 (eradication sweep, after A1 merge):   C1 gateway dir/env/run.sh/docs cleanup
```

Merge order: A1 → (B1 ∥ D1 ∥ D2) → C → A2 → E1 → A3 → A4 → B2/B3 → D3 → final gates.

## 4. Edit specs

### Track 1 — Provider core

#### A1 · Rewrite `core/llm.py`
- **Purpose:** one thin OpenAI-compatible client pointed at DeepSeek with per-call "gear"
  (model × thinking × effort × timeout), bounded retries, correct down-detection, per-user
  isolation. Deletes OmniRoute config AND the retry stacking bug (SDK 2×app-3 retries ≈ >2min hang).
- **Change:**
  - Env read at import: `DEEPSEEK_API_KEY` (fail fast if missing — RuntimeError, same pattern
    as `pinned_client()`); base_url `https://api.deepseek.com`; SDK `max_retries=0`.
  - Models: `CHATBOT_MODEL_FAST` (default `deepseek-v4-flash`), `CHATBOT_MODEL_HEAVY`
    (default `deepseek-v4-pro`). Delete `CHATBOT_MODEL`/`auto/best-coding`.
  - `GEARS`: `f0`=flash/thinking-off/30s · `t1`=flash/think-low/60s · `t2`=flash/think-high/90s ·
    `p`=pro/think-high/300s(async-only).
  - `complete(messages, gear="t1", *, tools=None, stream=False, response_format=None, user_id=None)`:
    builds `extra_body={"thinking": {...}, "user_id": ...}` (+`reasoning_effort` when thinking on).
    Returns `(message, usage)` so callers can log cache-hit tokens.
  - Retry policy: RateLimitError → 1 retry jittered 1–3s (interactive) / ≤3 capped-30s (gear p);
    `APIConnectionError`/`APITimeoutError`/5xx → raise `ProviderUnavailableError(PROVIDER_UNAVAILABLE_AR)`
    immediately on interactive gears, after retries on `p`. AuthenticationError → loud config error, never retried.
  - Rename `GatewayUnavailableError`→`ProviderUnavailableError`, `GATEWAY_UNAVAILABLE_AR`→`PROVIDER_UNAVAILABLE_AR`
    (Arabic text unchanged). Touch list for rename: `core/llm.py`, `api/server.py:234`,
    `tests/test_api.py:127,134`, `tests/test_llm.py:44-56`.
  - Add `provider_health(timeout=5) -> bool` (GET /models with key).
- **Test:** rewrite `tests/test_llm.py` — (a) conn-refused ⇒ ProviderUnavailableError (the live-proven bug);
  (b) 502/504 ⇒ same; (c) no sleep-storm: monkeypatched time.sleep called ≤1× on rate-limit path;
  (d) gear mapping: f0 sends `extra_body.thinking.type="disabled"` and no reasoning_effort;
  t1 sends enabled+low; p targets HEAVY model; (e) user_id lands in extra_body verbatim.

#### A2 · Thread `reasoning_content` through the tool loop (`core/agent.py`)
- **Purpose:** satisfy contract B1 — otherwise every multi-tool turn dies with HTTP 400 post-cutover.
- **Change:** in the ask_stream tool loop: streaming path accumulates
  `delta.reasoning_content` separately from `delta.content`; after each assistant turn append
  the WHOLE message object (`{"role":"assistant","content":…,"reasoning_content":…,"tool_calls":…}`)
  to `messages` instead of hand-rebuilding. Reasoning is never logged or streamed to users.
- **Test:** hermetic fake client emitting thinking-mode chunks (reasoning deltas + tool_call +
  content) — assert the SECOND request's messages contain an assistant entry carrying all three
  fields exactly once; assert reasoning_content never appears in yielded SSE events.

#### A3 · Wire gear routing into `ask_stream` (`core/agent.py`)
- **Purpose:** replace OmniRoute's opaque auto-routing with our own rules tuned by our eval suite;
  keep interactive latency bounded (thinking costs seconds).
- **Change:** map existing pre-loop intent flags to gears: howto/report-howto/needs_ask/fast-count
  → `f0`; standard SQL lookups/metrics/date questions (honesty preamble present) → `t1`;
  multi-hop join questions & compound multi-part → `t2`; mid-loop escalation to `p` only when
  ≥2 gate rejections this turn OR empty-final-retry fires (agent.py `_retry_empty_final`);
  followup/envelope generation stays `f0`. Loop budget constants unchanged (MAX_QUERIES/MAX_TURNS).
- **Test:** table-driven unit tests: given intent flags → expected gear string passed to
  `llm.complete` (assert via mock call args). Escalation test: two GateErrors then next call
  uses gear `p`.

#### A4 · Stable-prefix prompt architecture + full-schema context (`core/agent.py`)
- **Purpose:** exploit B2 economics (≈$0.007/M vs $0.22/M) by shipping the previously-rationed
  context (full `t.` schema ≈87k tok + all vault cards) as a byte-stable cached prefix; delete
  most `introspect_schema` round-trips.
- **Change:** reorder system messages: [0]=system.md+join_playbook (byte-stable),
  [1]=full schema block rendered from `schema_cache.tables` (stable per `_schema_version`),
  [2]=all vault join cards (stable per vault_cards.sqlite mtime/hash), [3+]=dynamic
  (tenant_pack facts, few-shots, negatives, report cards, honesty preamble, question).
  Enforce C1 with a guard test. Keep `introspect_schema` tool as fallback. Optional eval arm:
  sliced-vs-full comparison flag.
- **Test:** (a) two consecutive `ask_stream` runs produce identical bytes for messages[0..2];
  (b) injecting a timestamp into a static builder fails the guard; (c) fake-LLM turn answers
  correctly using schema from msg[1] without calling introspect_schema.

### Track 2 — Server/SSE

#### B1 · Stream hardening (`api/server.py` `/ask`)
- **Purpose:** survive ARR/nginx buffering + idle timeouts; make SSE contract consistent on errors
  (review findings #11/#16).
- **Change:** StreamingResponse headers `X-Accel-Buffering: no`, `Cache-Control: no-transform`;
  pass through upstream `: keep-alive` comments (A1 exposes them) and synthesize one every ~15s
  of silence; yield `data: {"error":…}` THEN `data: [DONE]` on BOTH except paths (:234,:237).
- **Test:** extend `tests/test_api.py`: error frame sequence ends with `[DONE]`; heartbeat comment
  emitted when generator stalls >15s (fake clock); headers present on response.

#### B2 · Rewire `/health` provider check (`api/server.py:306-341`)
- **Purpose:** remove last OmniRoute reference; keep operator-visible provider status.
- **Change:** replace urllib probe of `GATEWAY_URL/models` with `llm.provider_health()`;
  rename response field `"gateway"`→`"provider"`. Trim payload later (out of scope here).
- **Test:** update `test_api.py::test_health_gateway_probes_models_not_liveliness` → mocks
  `llm.provider_health`; asserts `"provider"` field.

#### B3 · `run.sh` cleanup
- **Purpose:** launcher stops referencing dead gateway.
- **Change:** drop lines 9–19 (OmniRoute wait/start) and line 31 echo; print provider=model names.
- **Test:** manual boot via run.sh reaches :8100 with no gateway step.

### Track 3 — Eval integrity (independent until D3)

#### D1 · Scorer fix (`evals/run_comprehensive_ar.py:82-159`)
- **Purpose:** stop wrong-answer passes («٢»⊂«2025», «نوع» substring) so post-swap numbers are quotable.
- **Change:** numeric GT compared numerically w/ tolerance ±0.5% after folding Arabic-Indic ٠-٩→0-9;
  text tokens matched on word boundaries; refusal checks prefer JSON contract `refusal` field
  when present (E1), fall back to current markers otherwise.
- **Test:** self-test fixtures: «99» vs GT «238» fails; «٢٣٨» vs «238» passes; «نوع» alone no longer
  satisfies q34-style cases.

#### D2 · Verify-before-promote + pool purge (`evals/run_evals.py:109-114`, `api/server.py:284-288`)
- **Purpose:** stop poisoning the live few-shot pool (pool contains `SELECT 1` today).
- **Change:** both promote sites require `gate.validate(sql, company_id, schema_cache)` pass +
  single-statement check before `memory.promote_verified_query`; one-time script deletes suspect
  rows (`source='eval'` AND trivial SQL like bare `SELECT 1`) from `work/cache.sqlite` + FTS mirror.
- **Test:** promote blocked for failing SQL (unit); purge script dry-run lists exactly known-bad rows.

#### D3 · Post-swap re-baseline (gated on A1–A4+E1)
- **Purpose:** old 93–97% is void (gameable scorer + new brain). Produce the quotable number.
- **Run:** comprehensive_ar_105 + isolation + hard_en through DeepSeek gears; publish report;
  A/B arm full-schema (A4) vs sliced if time allows. No accuracy claims before this lands.

### Track 4 — JSON answer contract

#### E1 · Structured final completion (`core/agent.py` envelope path)
- **Purpose:** make golden rule 9 structural (final call has NO tools), kill tool-JSON leaks at
  source, machine-readable citations/confidence/refusal/followups; deletes serial
  `_suggest_followups` LLM call (agent.py:1010-1030) — one less RTT on every answered turn.
- **Change:** after loop: one `f0` completion, `tools=None`, `response_format={"type":"json_object"}`
  returning `{answer_md, refusal, confidence, sql_used[], rowcount, as_of, citations[], followups[]}`;
  server done-frame maps fields 1:1; parse failure → legacy sanitize/stub path (never fail a turn);
  UI consumes existing fields first, chips upgrade comes later.
- **Test:** fake final reply parses to typed envelope incl. followups; malformed JSON falls back;
  no `tools=` param on that request (assert via mock).

### Track 5 — Eradication sweep (after A1 merges)

| # | Action | Where |
|---|--------|-------|
| C-1 | Delete directory entirely (`litellm.config.yaml`, README, `.env`) | `gateway/` |
| C-2 | Remove `litellm[proxy]==1.93.0` | `requirements.txt:8` |
| C-3 | Remove `GATEWAY_URL`/`GATEWAY_API_KEY`/`CHATBOT_MODEL`; add `DEEPSEEK_API_KEY`(done)/`CHATBOT_MODEL_FAST`/`CHATBOT_MODEL_HEAVY` | `.env`, `.env.example` |
| C-4 | Delete file (gateway-specific acceptance tests) | `tests/test_gateway.py` |
| C-5 | Update env table, architecture diagram LLM arrow, golden-rule-3 wording (keys live in gitignored `.env`, read only by `core/llm.py`) | `AGENTS.md` |
| C-6 | Update `gateway_ok` marker comment (concept stays; Arabic markers unchanged) | `evals/run_evals.py:80-84` |
| C-7 | Fix stale comment `MODEL_ALIAS` ("gateway maps…" → cache-role namespace note; value `chatbot` kept — changing it would invalidate plan_cache keys) | `core/agent.py:31` |

## 5. Acceptance gates

- **G1 (after A1+B1+C):** `pytest tests -q` green (hermetic set) + live smoke: server boots with
  only `DEEPSEEK_API_KEY`, one real Arabic question streams end-to-end incl. `[DONE]`.
- **G2 (after A2+A4+E1):** soak of 20 mixed questions — zero HTTP 400s (C2 proof); logs show
  cache-hit ratio >80% within a session (C1 proof); no `introspect_schema` calls on simple lookups.
- **G3 (D3):** re-baselined eval numbers published; router confusion matrix reviewed; gear thresholds tuned once.
- **Final:** grep proves zero references: `rg -i "omniroute|litellm|GATEWAY_URL|best-coding"` → only historical docs allowed (PLAN.md marked superseded).

## 6. Rollback

Tag repo `pre-deepseek-swap` before Lane A merges. Rollback = `git revert` of Track 1+4 commits
and restore of `.env` gateway lines from history. There is deliberately no runtime provider switch:
OmniRoute code is deleted, not dormant — keeping dead fallback wiring contradicts the eradication
requirement and would rot. Re-introducing a provider later means re-adding ~70 lines in `core/llm.py`,
which is the whole point of keeping that file thin.

## 7. Explicitly out of scope (this migration)

Evidence-chip UI upgrade, join-path viz, proactive digest, widget shell, i18n table, Windows/IIS
runbook, CORS/CSP — these are the feature backlog and stay gated behind G1–G3 + Tier 0 auth work.
`-vision-exp` excluded (experimental, released 2026-08-21). Files API rejected (residency + local
FTS5 at 1.3–3.2ms median wins).
