# Extract receipt — Option B standalone copy

**Date:** 2026-08-13  
**Destination:** `/media/alaa/data/client-chatbot/`  
**Source chatbot:** `/media/alaa/data/olives/apps/client-chatbot/`  
**Source vault:** `/media/alaa/data/olives/obsidian/olives/`

## Vault file count proof

| Location | `find … -type f | wc -l` |
|----------|---------------------------|
| Source vault | **2659** |
| Dest vault (`obsidian/olives/`) | **2659** |

Match verified after `rsync -a` (including `.obsidian/`).

## Git

- `git init` in `/media/alaa/data/client-chatbot`
- Initial extract commit: **`a0506d8b6134c2d05219ea3f32bef48c3a714b55`**
- HEAD (includes this receipt): **`a6331b538f1573d5ab18103eb36909c95eab528f`**
- **2772** files tracked (vault 2659 + chatbot source + knowledge + MCP + graph)
- Not pushed (per instructions)

## Copied extra assets (beyond chatbot tree)

| Asset | Source | Dest |
|-------|--------|------|
| Obsidian vault | `olives/obsidian/olives/` | `obsidian/olives/` |
| MCP server | `olives/obsidian-mcp-server.py` | `obsidian-mcp-server.py` |
| Vault graph | `olives/db/vault_graph.json` | `db/vault_graph.json` |
| Reference docs | `olives/knowledge/reference/` | `knowledge/reference/` |
| Back-office docs | `olives/knowledge/back-office/` | `knowledge/back-office/` |
| Front-office docs | `olives/knowledge/front-office/` | `knowledge/front-office/` |
| System options guide | `olives/apps/support-agent/system_options_guide.md` | `knowledge/support-agent/system_options_guide.md` |
| Extract notes | `apps/client-chatbot/_extract_notes/` | `docs/extract-notes/` |

## MCP path diff

| Variable | Olives (source) | Standalone (dest) |
|----------|-----------------|-------------------|
| `VAULT` | `/media/alaa/data/olives/obsidian/olives` | `/media/alaa/data/client-chatbot/obsidian/olives` |
| `GRAPH_PATH` | `/media/alaa/data/olives/db/vault_graph.json` | `/media/alaa/data/client-chatbot/db/vault_graph.json` |

## Path fixes applied in dest

| File | Change |
|------|--------|
| `setup/04_assemble_docs_corpus.py` | `REPO_ROOT = parents[1]`; corpus sources under `knowledge/` in this repo; `system_options_guide.md` → `knowledge/support-agent/` |
| `setup/05_index_docs.py` | `REPO_ROOT = parents[1]`; `sys.path` → repo root (mechanical fix so indexing works after 04) |

## Skipped (by design)

| Item | Reason |
|------|--------|
| `.env` | Secrets — excluded from rsync; not in git |
| `gateway/.env` | Secrets — not present in source; gitignored |
| `work/` | Runtime/generated — gitignored |
| `__pycache__/`, `.pytest_cache/` | Cache — excluded |
| `docs_corpus/` | Derived — regenerate via `04_assemble_docs_corpus.py` |
| `prompts/.~lock.system.md#` | Editor lock — excluded |
| `olives web pages/` | 901 MB untracked ASP.NET dump; olives retains copy at `olives/olives web pages/` |
| Parent olives `.git` | Standalone repo — not copied |
| `apps/drift-tool/` | Dev Docker bootstrap only — documented in `AGENTS.md` / README (`DRIFT_TOOL_ROOT` or olives path) |
| `.benchmarks/` | Pytest benchmark cache — removed from dest after rsync; not tracked |

## Not rewritten (documented only)

`setup/01_db_up.py`, `02_introspect.py`, `03_apply_db_sql.py`, `refresh.py` still use olives monorepo `parents[2]` → `apps/` and `drift-tool` sibling layout. Local Docker restore expects olives `apps/drift-tool` until a follow-up normalizes paths or honors `DRIFT_TOOL_ROOT`.

## Regenerate `docs_corpus/`

```bash
cd /media/alaa/data/client-chatbot
python3.13 setup/04_assemble_docs_corpus.py
python3.13 setup/05_index_docs.py --client <name>
```

## New files written at dest

- `AGENTS.md` — agent/orchestration guide for standalone layout
- `README.md` — prepended standalone + vault/MCP pointer
- `.gitignore` — extended (`.pytest_cache`, `gateway/.env`, `*.bak`)
- This receipt

## Questions / none

Destination path and copy set were pre-decided; no blocking ambiguities.
