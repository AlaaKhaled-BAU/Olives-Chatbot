# Accountant holdout battery (Lane L3)

Holdout dialogue set for how accountants, supervisors, and helpdesk staff talk to the chatbot. **Not** part of `run_evals.py` `_DEFAULT_SUITES`. The loader **never** calls `memory.promote_verified_query`.

## Files

| File | Role |
|------|------|
| `accountant_holdout.jsonl` | Authored turns (≥60 turns, ≥30 `session` values) |
| `run_accountant_holdout.py` | Runner → JSON report |
| `accountant_holdout_results.json` | Last run output (gitignored if large; safe to commit summaries only) |

## JSONL schema

One JSON object per line:

- `id` — unique case id (`ah-NNN`)
- `session` — thread key (1–4 turns share a session)
- `turn` — 1-based turn index within the session
- `question` — user text (Jordanian, MSA, English, mixed)
- `company_id` — tenant scope for `SESSION_CONTEXT`
- `lang` — tag only (`ar-jo`, `ar-msa`, `en`, …)
- `expects` — object with `type`: `number` | `label` | `howto` | `opinion` | `clarify`

Do **not** put `expect_tool`, `run_metric`, or `search_docs` in the jsonl.

### Gold numbers

For `expects.type == "number"`, set `"gold": "pending"` until a human runs read-only SQL (or a certified report) and pastes the value. The runner **skips** scoring when gold is `pending`.

Optional fields on `expects`:

- `gold_int` — integer-friendly tolerance
- `no_single_headline_total` — multi-row salesperson breakdown must not collapse to one company total
- `phrases` — citation cues for `howto` / `label`
- `must_not_invent_target` — for `opinion`
- `asks_period`, `must_not_reuse_yesterday`, … — for `clarify`

Questions were drafted from topics in `knowledge/back-office/`, `knowledge/guide-headed/back-office/`, and one front-office tablet how-to (`knowledge/reference/create_sales_invoice.md`).

## Runner

Uses `agent.ask_stream` with the same session fields as `api/server.py`: `conversation`, `history`, `transcript`, and `record_session_turn` after each answered turn.

Provider guard (default **refuse** production DeepSeek):

```bash
set -a && source .env && set +a
python3.13 evals/run_accountant_holdout.py --self-check
# Battery on temporary Composer endpoint (after L0 env switch):
python3.13 evals/run_accountant_holdout.py
# Only if you intentionally spend production key:
python3.13 evals/run_accountant_holdout.py --allow-deepseek
```

Reads `CHATBOT_LLM_BASE_URL` (defaults to `https://api.deepseek.com`). Uses whatever `core/llm.py` is configured to call; does not import DeepSeek by name.

### pass^3

Run three full passes and compare numeric tokens on cases with locked gold:

```bash
python3.13 evals/run_accountant_holdout.py --repeat 3
```

Report field `flake` lists ids whose extracted numbers differ across runs. Gate numeric items on zero flakes after gold is filled.

## After the battery

Revert temporary Composer settings per `plans/sales_basis_phases` / chat-thread plan: remove `CHATBOT_LLM_BASE_URL` and `CHATBOT_LLM_API_KEY` from `.env`, confirm `/health` hits DeepSeek again. Do not commit `.env`.
