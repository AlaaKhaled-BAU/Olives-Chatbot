# Vault & MCP extraction notes

Investigation date: 2026-08-13. All paths and counts measured on disk at `/media/alaa/data/olives/`.

---

## 1. Live vault path, file counts, `.obsidian` config

### Load-bearing live vault

| Property | Value |
|----------|-------|
| **Absolute path** | `/media/alaa/data/olives/obsidian/olives/` |
| **Parent** | `/media/alaa/data/olives/obsidian/` (only child: `olives/`) |
| **On-disk size** | **12 MB** (`du -sh`) |
| **Total files** | **2,659** |
| **Directories** | **17** (including `.obsidian`, `media/`, DB subtrees) |

### File counts by extension (entire vault tree)

| Extension | Count | Notes |
|-----------|------:|-------|
| `.md` | **2,653** | All indexed by MCP (see below) |
| `.json` | **5** | All under `.obsidian/` only |
| `.canvas` | **1** | `Untitled.canvas` at vault root (2 bytes, empty) |
| **Total** | **2,659** | |

Non-`.obsidian` files: **2,654** (2,653 `.md` + 1 `.canvas`).

### Markdown counts by database / area

| Location | Tables | Procedures | Relations | Other `.md` | Subtotal |
|----------|-------:|-----------:|----------:|------------:|---------:|
| `Olives_BO/` | 440 | 1,722 | 30 | 1 (`_MOC-Olives_BO.md`) | **2,193** |
| `OSFA_DB/` | 193 | 213 | 9 | 1 (`_MOC-OSFA_DB.md`) | **416** |
| `Shared/` (root) | — | — | — | 14 | **14** |
| `Shared/Runbooks/` | — | — | — | 11 | **11** |
| `Shared/Workflows/` | — | — | — | 16 | **16** |
| Vault root | — | — | — | 2 (`Welcome.md`, `2026-06-20.md`) | **2** |
| `media/` | — | — | — | 1 (0-byte stub) | **1** |
| **Total `.md`** | **633** | **1,935** | **39** | **46** | **2,653** |

`Shared/` root files include: `Dashboard.md`, `Glossary.md`, `Cross-DB-Links.md`, `Schema-Drift-Log.md`, audit/report notes (`Olives_BO-Vault-Doc-Audit.md`, `OSFA_DB-Vault-Doc-Audit.md`, etc.).

### `.obsidian/` config (28 KB)

Path: `/media/alaa/data/olives/obsidian/olives/.obsidian/`

| File | Purpose |
|------|---------|
| `app.json` | `{}` (empty) |
| `appearance.json` | `{}` (empty) |
| `core-plugins.json` | Default core plugin toggles (graph, backlinks, properties, sync, bases, etc.) |
| `graph.json` | Local graph view UI state |
| `workspace.json` | Last-open tabs/panes (e.g. `Shared/Workflows/Daily-Sales-Cycle.md`) |

### Must the copy include `.obsidian`?

| Consumer | Needs `.obsidian`? |
|----------|-------------------|
| **`obsidian-mcp-server.py`** | **No.** `_build_index()` explicitly skips any path containing `.obsidian` (line 263). MCP indexes **2,653** `.md` files. |
| **Obsidian desktop app** | **Yes**, if you want plugin settings, workspace restore, and graph UI state. Harmless to copy (28 KB, 5 files). |
| **client-chatbot runtime** | **No.** Chatbot does not read the vault directly today (see §7). |

**Recommendation for as-is copy:** include `.obsidian/` — it is part of the live vault folder the user asked to copy verbatim, costs almost nothing, and preserves Obsidian UX if opened locally.

### Documented path references

- `/media/alaa/data/olives/README.md` — lists `obsidian/olives/` as the live vault; warns paths are hardcoded in `obsidian-mcp-server.py`, `db/*.py`, and **AGENTS.md**.
- **AGENTS.md** — **not present** anywhere under `/media/alaa/data/olives/` (glob search 2026-08-13). README references it but the file does not exist on disk.

---

## 2. Live vault vs `obsidian-vault/` mirror vs `olives.BAK.*`

| Path | Status (2026-08-13) | Load-bearing? |
|------|---------------------|---------------|
| `/media/alaa/data/olives/obsidian/olives/` | **EXISTS** — 2,659 files, 12 MB, has `.obsidian/` | **YES — sole live vault** |
| `/media/alaa/data/olives/obsidian-vault/` | **DOES NOT EXIST** | No |
| `/media/alaa/data/olives/obsidian/olives.BAK.*` | **DOES NOT EXIST** (no `olives.BAK.*` under `obsidian/`) | No |

Historical context (from `apps/client-chatbot/PLAN.md` §1.5, written earlier):

- `obsidian-vault/` was described as a secondary mirror **without** `.obsidian` — redundant with live vault.
- `obsidian/olives.BAK.20260714-005041/` was described as a dated snapshot backup.

**Neither path exists on this machine today.** Only `obsidian/olives/` is load-bearing. Do not wait for or depend on mirror/BAK copies for the standalone extract.

---

## 3. MCP server: tools, hardcoded paths, how to run stdio

### Server file

| Property | Value |
|----------|-------|
| Path | `/media/alaa/data/olives/obsidian-mcp-server.py` |
| Size | 26.5 KB (775 lines) |
| Protocol | JSON-RPC 2.0 over **stdio** (line-delimited JSON on stdin/stdout) |
| Server name | `obsidian-olives-mcp` v1.0.0 |
| Dependency | `yaml` (PyYAML) — `import yaml` at line 13 |

### Hardcoded absolute paths (must change after copy)

```python
VAULT = "/media/alaa/data/olives/obsidian/olives"
GRAPH_PATH = "/media/alaa/data/olives/db/vault_graph.json"
```

Also hardcoded elsewhere in the monorepo (not in MCP, but same vault path):

| File | Constant |
|------|----------|
| `/media/alaa/data/olives/verify.py` | `VAULT = "/media/alaa/data/olives/obsidian/olives"` |
| `/media/alaa/data/olives/db/bulk_edit.py` | `VAULT`, `GRAPH` |
| `/media/alaa/data/olives/db/normalize_frontmatter.py` | `VAULT`, `GRAPH`, `NAMEIDX` |
| `/media/alaa/data/olives/db/regenerate_body.py` | `VAULT`, `GRAPH`, `NAMEIDX` |
| `/media/alaa/data/olives/db/merge_graph.py` | `VAULT`, `BASE` |

### MCP tools (12)

| # | Tool | Data source | Needs `vault_graph.json`? |
|---|------|-------------|---------------------------|
| 1 | `search_notes` | Vault `.md` walk + regex | No |
| 2 | `read_note` | Vault file by name/path | No |
| 3 | `get_backlinks` | Wiki-link scan across vault | No |
| 4 | `query_by_tag` | Frontmatter `tags` | No |
| 5 | `query_by_field` | Arbitrary frontmatter field | No |
| 6 | `list_tables_db` | `*/Tables/*.md` + frontmatter | No |
| 7 | `list_procs_db` | `*/Procedures/*.md` + frontmatter | No |
| 8 | `get_common_issues` | `## Common Issues` section | No |
| 9 | `get_when_to_run` | `## When to Run` section | No |
| 10 | `get_impact` | `vault_graph.json` → `tables` | **Yes** |
| 11 | `get_proc_deps` | `vault_graph.json` → `procedures` | **Yes** |
| 12 | *(implicit)* `tools/list` | Tool metadata from `TOOLS` array | No |

Startup behavior:

1. Walk `VAULT` once → `NOTES_INDEX` (cached list of all `.md` notes).
2. Load `GRAPH_PATH` → `VAULT_GRAPH` (on failure: `{"tables": {}, "procedures": {}}`).

### How to run (stdio)

```bash
# From monorepo root (paths must match hardcoded constants)
python3 /media/alaa/data/olives/obsidian-mcp-server.py
```

No CLI args, no env vars — paths are constants only.

**Cursor / Claude MCP registration** (example for standalone layout under `client-chatbot/`):

```json
{
  "mcpServers": {
    "obsidian-olives": {
      "command": "python3",
      "args": ["/media/alaa/data/olives/apps/client-chatbot/obsidian-mcp-server.py"]
    }
  }
}
```

After copy, update `VAULT` and `GRAPH_PATH` inside the script **or** symlink to the old absolute paths.

**No MCP registration found** in-repo under `.cursor/` or `apps/client-chatbot/` — the server is invoked externally (editor MCP config).

### `vault_graph.json` shape (loaded at startup)

| Key | Entry count | Sample fields |
|-----|------------:|---------------|
| `tables` | **598** | `database`, `name`, `columns`, `procedures_reading`, `procedures_writing`, `cross_db`, … |
| `procedures` | **1,655** | `database`, `name`, `params`, `reads_from`, `writes_to`, `called_by`, `callers`, `cross_db`, … |

Table keys look like `Olives_BO::ActivityList`. Procedure keys like `Olives_BO::ABS_Integration_Jebrene`.

**Known data-quality issues** (documented in planning/review — not re-verified here in full):

- `called_by` may store callees, not callers; `callers` often empty.
- Regex-derived `reads_from` can contain junk tokens.
- See `apps/drift-tool/VALIDATION.md`, `knowledge/planning/PLAN-01-client-chatbot.md` §8.

---

## 4. `db/*.json` — what MCP needs vs optional

### Required for full MCP functionality

| File | Size | MCP usage |
|------|------|-----------|
| `/media/alaa/data/olives/db/vault_graph.json` | **2.8 MB** | `get_impact`, `get_proc_deps` only |

### Not read by MCP at runtime

| File | Size | Purpose |
|------|------|---------|
| `db/name_index.json` | 470 KB (2,356 entries) | Vault regen (`merge_graph.py`, `normalize_frontmatter.py`, `regenerate_body.py`) |
| `db/tables.json` | 1.5 MB | Input to `merge_graph.py` |
| `db/procs_csv.json` | 861 KB | Input to `merge_graph.py` |
| `db/procs_sql.json` | 680 KB | Input to `merge_graph.py` |

`db/` total on disk: **4.4 MB** (19 files including `.py` scripts and markdown bundles).

### Regeneration pipeline (optional for runtime, needed to rebuild graph)

```
data/exports/Inventory-Master.csv  →  csv_to_graph.py  →  tables.json, procs_csv.json
                                                      →  (external) procs_sql.json
merge_graph.py  →  vault_graph.json + name_index.json
normalize_frontmatter.py / regenerate_body.py  →  vault note updates
bulk_edit.py  →  bulk vault edits using graph
```

**Minimum copy for a working docs MCP:** `obsidian/olives/` + `obsidian-mcp-server.py` + `db/vault_graph.json`.

**Minimum copy to regenerate graph later:** add all four JSON files + `db/*.py` + `data/exports/Inventory-Master.csv` (CSV path hardcoded in `csv_to_graph.py`).

---

## 5. Copy recipe (standalone `apps/client-chatbot/`)

Target layout (suggested):

```
apps/client-chatbot/
├── obsidian-mcp-server.py          # from repo root
├── obsidian/olives/                # full vault tree (incl. .obsidian)
└── db/
    └── vault_graph.json            # required for graph tools
```

### rsync commands (from monorepo root)

```bash
REPO=/media/alaa/data/olives
DEST=/media/alaa/data/olives/apps/client-chatbot

# 1. Full vault as-is (includes .obsidian, media, canvas)
rsync -a --info=progress2 \
  "$REPO/obsidian/olives/" \
  "$DEST/obsidian/olives/"

# 2. MCP server
rsync -a "$REPO/obsidian-mcp-server.py" "$DEST/obsidian-mcp-server.py"

# 3. Graph JSON (minimum db artifact)
mkdir -p "$DEST/db"
rsync -a "$REPO/db/vault_graph.json" "$DEST/db/vault_graph.json"
```

Flags: `-a` (archive: permissions, times, recursion; preserves symlinks as symlinks). Add `--delete` only if you want the destination to mirror exactly (destructive).

### Post-copy path updates (required)

Edit `$DEST/obsidian-mcp-server.py`:

```python
VAULT = "/media/alaa/data/olives/apps/client-chatbot/obsidian/olives"
GRAPH_PATH = "/media/alaa/data/olives/apps/client-chatbot/db/vault_graph.json"
```

Or use env-based paths (not implemented today — would be a code change).

### Expected file counts after copy

| Artifact | Files |
|----------|------:|
| `obsidian/olives/` (entire tree) | **2,659** |
| `obsidian-mcp-server.py` | **1** |
| `db/vault_graph.json` | **1** |
| **Total** | **2,661** |

Verify:

```bash
find /media/alaa/data/olives/apps/client-chatbot/obsidian/olives -type f | wc -l
# expect 2659
```

### What breaks if `vault_graph.json` is omitted?

| Tool | Behavior without graph |
|------|------------------------|
| `get_impact` | Returns `Table 'X' not found.` for every table (empty `tables` dict) |
| `get_proc_deps` | Returns `Procedure 'X' not found.` for every procedure |
| All other 10 tools | **Work normally** — they read vault markdown only |
| Vault notes | May show `_No dependency data available in vault_graph.json._` in AUTO-generated Impact sections (cosmetic) |

MCP does **not** crash on missing graph — `_load_graph()` catches exceptions and returns empty dicts.

---

## 6. Sizes on disk

| Path | Size |
|------|------|
| `/media/alaa/data/olives/obsidian/olives/` | **12 MB** |
| `…/obsidian/olives/.obsidian/` | **28 KB** |
| `…/obsidian/olives/media/` | **16 KB** (1 file) |
| `/media/alaa/data/olives/db/vault_graph.json` | **2.8 MB** |
| `/media/alaa/data/olives/db/` (all 19 files) | **4.4 MB** |
| `/media/alaa/data/olives/obsidian-mcp-server.py` | **26.5 KB** |

**Standalone minimum (vault + MCP + graph):** ~**15 MB**.

---

## 7. How `client-chatbot` uses vault / MCP today

### Direct vault/MCP integration: **none in runtime code**

The chatbot agent does **not** call `obsidian-mcp-server.py`. Grep of `apps/client-chatbot/{core,setup,api,run.sh}` finds no imports or subprocess launches of the obsidian MCP.

### What the chatbot uses instead: `docs_corpus/` + FTS5

| Component | Path | Role |
|-----------|------|------|
| `core/docs.py` | `apps/client-chatbot/core/docs.py` | SQLite FTS5 index over `docs_corpus/` |
| `core/agent.py` | `search_docs` tool → `docs.search()` | Conceptual/how-to questions |
| `prompts/system.md` | Documents `search_docs` vs `run_select` split | No mention of obsidian MCP |
| `setup/04_assemble_docs_corpus.py` | Symlinks `knowledge/`, `support-agent/system_options_guide.md` | **Does not** symlink the obsidian vault |
| `setup/05_index_docs.py` | Builds `work/<client>/docs.sqlite` | Per-client FTS index |

Docs corpus sources (from `04_assemble_docs_corpus.py`):

- `knowledge/reference/OLIVES USER GUIDE_2021Updated2025.md`
- `knowledge/reference/Olives SQL_Documentation.md`
- `knowledge/reference/tables summary.md`
- `apps/support-agent/system_options_guide.md`
- `knowledge/back-office/` (dir)
- `knowledge/front-office/` (dir)

### Planned / referenced but not wired

| Doc | Statement |
|-----|-----------|
| `apps/client-chatbot/PLAN.md` | Vault MCP kept at monorepo root; "don't relocate under client-chatbot/" |
| `apps/client-chatbot/PLAN.md` §Phase 10 | "Feed assembled corpus into docs path (vault MCP now; wire qmd if weak)" |
| `apps/client-chatbot/FIXPLAN.md` M11 | Vault-as-universal-schema is a **separate track**, blocked on vault/graph cleanup |
| `apps/client-chatbot/TOOLS-REVIEW.md` | PoC knowledge = live introspection + existing 12-tool obsidian vault MCP |

### Separate MCP in client-chatbot: SQL only

`apps/client-chatbot/sqlmcp/sql_server.py` — FastMCP over `core/sql.py`, SSE/HTTP transport. **Unrelated** to the obsidian vault.

---

## 8. Open questions

1. **Copy BAK / mirror?** Neither `obsidian-vault/` nor `olives.BAK.*` exist on disk — skip unless they reappear elsewhere.

2. **Copy full `db/` or only `vault_graph.json`?**
   - Runtime MCP: **`vault_graph.json` only**.
   - Ability to regenerate vault/graph: copy all `db/*.json` + `db/*.py` + `data/exports/Inventory-Master.csv`.

3. **Update hardcoded paths vs env vars?** Today all paths are absolute constants. Standalone deploy needs either edited constants or a small refactor (not done in this investigation).

4. **Wire obsidian MCP into `client-chatbot` agent?** Currently deferred (M11). PoC uses `search_docs` (FTS over user guides), not vault notes.

5. **Trust `vault_graph.json` for automated decisions?** Multiple reviews flag dirty caller/callee edges and parser noise. Safe for human triage hints; not validated as ground truth for agent actions.

6. **`AGENTS.md` missing** — README says it documents vault path; file absent. Use `README.md` + this note instead.

7. **Path mismatch in `setup/05_index_docs.py`** — `REPO_ROOT = parents[2]` resolves to `apps/`, then `sys.path.insert(0, REPO_ROOT / "client-chatbot")` — works when run from monorepo layout but is fragile if `client-chatbot` is extracted alone (pre-existing issue, unrelated to vault copy).

8. **0-byte `media/alaa/data/my apps/medical center.md`** — included in as-is copy; harmless stub.

9. **Graph vs vault note count drift** — Vault has 633 table notes + 1,935 procedure notes; graph has 598 tables + 1,655 procedures. Expected naming/scope differences; not reconciled here.

---

## Quick reference: source paths

```
/media/alaa/data/olives/
├── obsidian/olives/                 # LIVE VAULT (2,659 files, 12 MB)
├── obsidian-mcp-server.py           # stdio MCP (12 tools)
├── db/vault_graph.json              # graph for get_impact / get_proc_deps (2.8 MB)
├── db/{tables,procs_csv,procs_sql,name_index}.json   # regen only
├── verify.py                        # vault verifier (hardcoded VAULT)
└── README.md                        # documents layout; mentions missing AGENTS.md
```

**Not found:**

```
/media/alaa/data/olives/obsidian-vault/          # does not exist
/media/alaa/data/olives/obsidian/olives.BAK.*/   # does not exist
/media/alaa/data/olives/AGENTS.md                # does not exist
```
