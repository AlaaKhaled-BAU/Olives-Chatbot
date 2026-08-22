# Olives Client Chatbot — Pilot

**Standalone repo.** Vault (`obsidian/olives/`), MCP (`obsidian-mcp-server.py`), FTS sources (`knowledge/`). See `AGENTS.md`. Regenerate `docs_corpus/` via `setup/04_assemble_docs_corpus.py`.

Read-only reporting chatbot over the Olives back-office DB. Pilot-grade: real service, key custody,
memory/cache, tracing, multi-client by config — between a bare MCP and full production.
Full build steps: **[PLAN.md](PLAN.md)**. Tool decisions: **[TOOLS-REVIEW.md](TOOLS-REVIEW.md)**.

> **Native SQL Server** (port 1433, Azure Data Studio / local `mssql` container) is the default dev path — see **Run** below. Legacy Docker scratch DB: `setup/01_db_up.py --mode docker` + `DRIFT_TOOL_ROOT`.

**Main DB backups** (gitignored, ~4.7 GB): `data/db-snapshots/backup test/`. Mount parent folder into SQL Server as `/snapshots` for `RESTORE`.

## Run

1. `cp .env.example .env` — set `DEEPSEEK_API_KEY`, `DB_SA_PASSWORD`, tenant tokens
2. `set -a && source .env && set +a`
3. Bootstrap the DB (skip if already done):
   - **DB already exists** (`Olives_BO` on your instance):  
     `python3.13 setup/native_bootstrap.py --client morec`
   - **Restore from `.bak` first**:  
     `python3.13 setup/01_db_up.py --mode native --db-name Olives_BO` then bootstrap as above
4. `./run.sh` or manually: `uvicorn api.server:app --port 8100` (DeepSeek direct — no gateway)
5. `python3.13 evals/run_evals.py` (optional gate)

> `python3.13` only. App connects as **`chatbot_ro`** + tenant `t.` views — never SA, never IIS `cds`.

## Client schema changed? (renamed column, new table, new/changed procedure)

```bash
python3.13 setup/refresh.py --client <name>    # as SA; rebuilds schema_cache.json + the t. views
```

Until you run this, answers may be stale against the client's real schema — there's no
auto-detection in the pilot. Safe to run anytime, including on an already-current schema
(idempotent — verified live, including cleanup of any `t.` view left behind by a table
that was later renamed/dropped). See `FIXPLAN.md` M7 for what was live-tested.
