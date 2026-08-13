# Olives Client Chatbot — Pilot

**Standalone repo.** Extracted from olives `apps/client-chatbot` with vault (`obsidian/olives/`), MCP (`obsidian-mcp-server.py`), and FTS sources (`knowledge/`). Agent/orchestration notes: `AGENTS.md` and `docs/extract-notes/`. Regenerate derived `docs_corpus/` via `setup/04_assemble_docs_corpus.py`.

Read-only reporting chatbot over the Olives back-office DB. Pilot-grade: real service, key custody,
memory/cache, tracing, multi-client by config — between a bare MCP and full production.
Full build steps: **[PLAN.md](PLAN.md)**. Tool decisions: **[TOOLS-REVIEW.md](TOOLS-REVIEW.md)**.

> **Local Docker restore** (`setup/01_db_up.py` etc.) still expects olives `apps/drift-tool` on disk (or env `DRIFT_TOOL_ROOT`). Production connects to customer SQL Server as `chatbot_ro` — see `AGENTS.md`.

## Run (after the phases in PLAN.md are built)
1. `cp .env.example .env`, fill in `OLIVES_TOKEN_<CLIENT>` for each client in `clients/*.yaml` (each
   yaml names its var via `api_token_env`; the token value itself never goes in the yaml — see C2).
2. `set -a && source .env && set +a`          # load tenant tokens into the environment
3. `python3.13 setup/01_db_up.py`            # boot SQL Server (Docker) + restore the test DB
4. start the gateway (see `gateway/README.md`) # LiteLLM or OmniRoute, Claude-pinned + fallback
5. `uvicorn api.server:app`                   # chat + /health + /metrics
6. `python3.13 evals/run_evals.py`            # accuracy + isolation pass/fail

> `python3.13` only. Never connect as SA from the app — the read-only login + tenant views are the wall.
> The LLM API key lives only in the gateway, never in `core/` or logs. Tenant bearer tokens live only
> in `.env` (gitignored), never in `clients/*.yaml` (git-tracked) -- see PLAN-04 §C2.

## Client schema changed? (renamed column, new table, new/changed procedure)

```bash
python3.13 setup/refresh.py --client <name>    # as SA; rebuilds schema_cache.json + the t. views
```

Until you run this, answers may be stale against the client's real schema — there's no
auto-detection in the pilot. Safe to run anytime, including on an already-current schema
(idempotent — verified live, including cleanup of any `t.` view left behind by a table
that was later renamed/dropped). See `FIXPLAN.md` M7 for what was live-tested.
