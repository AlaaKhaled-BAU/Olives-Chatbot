# Extract orchestration status

Updated: 2026-08-13 — all four explorers finished.

## Agents

| Note | Status | Key result |
|------|--------|------------|
| `01-chatbot-code.md` | **done** | FastAPI pilot. Full-page chat, not circle widget. FTS corpus, not vault MCP. Docker SQL, not IIS `cds`. |
| `02-vault-and-mcp.md` | **done** | Only live vault: `obsidian/olives/` 2659 files / 12 MB. MCP 12 tools. Graph 2.8 MB. |
| `03-iis-webconfig-sql.md` | **done** | IIS: `Olives/` → `Olives_BO`, `srv/` → `OSFA_DB` + `CNNStrBO`. SQL auth `cds` (secrets in Web.config). Company via session/cookie, not SESSION_CONTEXT. Duplicate 901 MB dump at olives root and in chatbot folder. No widget JS. |
| `04-olives-dependencies.md` | **done** | Runtime self-contained. Setup needs drift-tool + knowledge docs. **Conflicts with user mandate:** 04 says leave vault/MCP in olives (not in current call graph). User asked to copy vault as-is for future NL2SQL. |

## Reconcile (do not assume away the user's request)

User asked to copy the vault **as-is, miss no file**. That overrides 04's "leave vault in olives" for the **current** pilot. Copy:

- `obsidian/olives/` (entire, including `.obsidian`)
- `obsidian-mcp-server.py` (retarget paths)
- `db/vault_graph.json`
- `knowledge/{reference,back-office,front-office}/` + `support-agent/system_options_guide.md` (current FTS docs)
- MCP + AGENTS.md + gitignore for secrets

Do **not** copy into git: `.env`, `work/`, `.bak`, `olives web pages/` (901 MB, untracked, zero imports), Web.config passwords.

Optional later: drift-tool slice for **dev** Docker only. Production path = customer SQL Server (same host as IIS), **not** the `cds` login — `chatbot_ro` + tenant views.

## Blocked on human

- **D1** repo location (nested git vs sibling). No copy / `git init` until answered.
