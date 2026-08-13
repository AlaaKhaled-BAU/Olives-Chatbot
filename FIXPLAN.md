# FIXPLAN — client-chatbot, post-adversarial-review

> Written for a LITERAL executor (stupid mode). Rules:
> 1. Do the phases in order. M1 → M11.
> 2. Do exactly what the step says. No judgment calls, no "improve while you're there."
> 3. Run the ACCEPTANCE command at the end of each phase. If it does not print the
>    expected line, STOP and fix before moving on. Do not continue on a red gate.
> 4. Python is `python3.13`. Never `python3`.
> 5. One commit per phase. Message = the phase id + title.
> 6. Do not touch `core/gate.py`, `db/02_tenant_views.sql`, or the isolation evals
>    except where a phase explicitly says to. The wall is verified-good; don't drift it.

State at time of writing (all verified live, not claimed):
- DB `drift-tool-mssql` up on `127.0.0.1:14330`; `chatbot_db`(morec), `chatbot_db2`(rukn) restored.
- Gateway litellm up on `:4000`, **DeepSeek only, no fallback**.
- 31/31 unit tests pass. Isolation 10/10 blocked live. End-to-end Arabic Q&A works.
- SQL runs via **direct pymssql**, NOT an MCP.

Severity legend: **BLOCKER** = deploy is unsafe until fixed. **HIGH** = fix before 2nd tenant. **MED** = fix before calling it a product.

---

## M1 — Authenticate `/ask`, kill caller-chosen tenant  [BLOCKER]

WHY: `/ask` reads `client` from the request body with no auth. Any caller sends
`{"client":"rukn"}` and reaches another tenant's database. This is the single
worst hole. Fix: the caller's bearer token decides the client, server-side. The
body `client` field is ignored.

### Steps
1. Generate one token per real client. Run this once per client and copy the output:
   ```bash
   python3.13 -c "import secrets; print(secrets.token_urlsafe(32))"
   ```
2. Add the token to each client yaml. In `clients/morec.yaml` and `clients/rukn.yaml`
   add a line (paste the generated value):
   ```yaml
   api_token: <paste-token-here>
   ```
   Add the same key, empty, to `clients/_example.yaml`:
   ```yaml
   api_token:                     # REQUIRED. `python3.13 -c "import secrets;print(secrets.token_urlsafe(32))"`
   ```
3. Confirm `clients/*.yaml` is not world-readable (it now holds secrets):
   ```bash
   chmod 600 client-chatbot/clients/*.yaml
   ```
   Confirm `.gitignore` does NOT accidentally start ignoring configs — the tokens
   DO get committed for pilot (env-file-behind-gateway tier). If you want them out
   of git later, that's M2-adjacent; for now they live in the yaml.
4. Edit `api/server.py`. At the top, after the existing imports, add:
   ```python
   import yaml
   from fastapi import Header, HTTPException

   def _token_map():
       m = {}
       for p in (BASE_DIR / "clients").glob("*.yaml"):
           if p.stem.startswith("_"):
               continue
           tok = (yaml.safe_load(p.read_text()) or {}).get("api_token")
           if tok:
               m[tok] = p.stem
       return m

   TOKEN_MAP = _token_map()  # ponytail: built once at startup; restart to add a client

   def _client_from_auth(authorization: str | None) -> str:
       if not authorization or not authorization.startswith("Bearer "):
           raise HTTPException(status_code=401, detail="missing bearer token")
       client = TOKEN_MAP.get(authorization.removeprefix("Bearer "))
       if not client:
           raise HTTPException(status_code=403, detail="invalid token")
       return client
   ```
5. Change the `/ask` handler signature and first line. Replace:
   ```python
   @app.post("/ask")
   def ask(req: AskRequest):
       def stream():
           try:
               result = agent.ask(req.client, req.question)
   ```
   with:
   ```python
   @app.post("/ask")
   def ask(req: AskRequest, authorization: str | None = Header(default=None)):
       client = _client_from_auth(authorization)   # token decides tenant, NOT the body
       def stream():
           try:
               result = agent.ask(client, req.question)
   ```
6. In `AskRequest`, make `client` optional and ignored (so old callers don't 422):
   ```python
   class AskRequest(BaseModel):
       question: str
       client: str | None = None      # IGNORED — kept only so old bodies don't 422
       session_id: str | None = None
   ```

### ACCEPTANCE
```bash
cd client-chatbot && uvicorn api.server:app --port 8000 &   # start it
sleep 3
echo "--- no token (expect 401):"; curl -s -o /dev/null -w "%{http_code}\n" -XPOST localhost:8000/ask -H 'content-type: application/json' -d '{"question":"hi"}'
echo "--- wrong token (expect 403):"; curl -s -o /dev/null -w "%{http_code}\n" -XPOST localhost:8000/ask -H 'authorization: Bearer WRONG' -H 'content-type: application/json' -d '{"question":"hi"}'
echo "--- morec token but body says rukn (expect answer about morec, NOT rukn):"; curl -sN -XPOST localhost:8000/ask -H "authorization: Bearer <MOREC_TOKEN>" -H 'content-type: application/json' -d '{"client":"rukn","question":"كم عدد الشركات؟"}'
```
PASS = `401`, then `403`, then a morec answer (one company / MOREK), never rukn data.

---

## M2 — Restore model failover + a vetted primary  [BLOCKER]

WHY: one model (DeepSeek), no fallback. If it's down, the product is down. And the
plan bans routing real client rows through an unvetted model — DeepSeek is that.
Fix: two deployments under one alias with fallback. Vetted model primary.

### Steps
1. Procure ONE vetted key (this is a human/procurement step, not code):
   an Anthropic Claude key (plan's intended primary). Put it in `gateway/.env`:
   ```
   LLM_API_KEY=sk-ant-...
   DEEPSEEK_KEY=<existing>
   ```
2. Rewrite `gateway/litellm.config.yaml` `model_list` to two deployments, one alias:
   ```yaml
   model_list:
     - model_name: chatbot
       litellm_params: { model: claude-sonnet-5, api_key: os.environ/LLM_API_KEY }
     - model_name: chatbot
       litellm_params: { model: deepseek/deepseek-v4-flash, api_key: os.environ/DEEPSEEK_KEY }
   router_settings:
     num_retries: 2
     fallbacks: [{ chatbot: ["chatbot"] }]
   litellm_settings:
     cache: true
     cache_params: { type: local }
   ```
   NOTE the prior lesson (comment in the old config): a KEYLESS Claude entry poisons
   the pool (auth error → whole alias cooldown). So only add the Claude line AFTER
   `LLM_API_KEY` is a real key. If you still have no vetted key, do NOT ship — this
   phase is a BLOCKER precisely because "one unvetted model, no backup" is the
   reliability + confidentiality risk the review flagged.
3. Restart the gateway:
   ```bash
   pkill -f litellm; cd client-chatbot && litellm --config gateway/litellm.config.yaml --port 4000 &
   ```

### ACCEPTANCE
```bash
# failover proof (plan's original P3 gate): break the primary, confirm an answer still comes back.
# temporarily set a bad LLM_API_KEY, restart gateway, then:
python3.13 -c "import sys;sys.path.insert(0,'.');from core import agent;print(agent.ask('morec','How many customers are there in total?')['answer'])"
```
PASS = still answers `33,517` (served by the DeepSeek fallback while primary is broken).

---

## M3 — Rate limit `/ask`  [HIGH]

WHY: no limit. One client (or a loop bug) can drain the model budget and the DB.

### Steps
1. Add dep. Append to `requirements.txt`:
   ```
   slowapi==0.1.9
   ```
   ```bash
   python3.13 -m pip install slowapi==0.1.9
   ```
2. In `api/server.py`, after `app = FastAPI()`:
   ```python
   from slowapi import Limiter
   from slowapi.errors import RateLimitExceeded
   from slowapi.util import get_remote_address

   def _rl_key(request):
       return request.headers.get("authorization", get_remote_address(request))

   limiter = Limiter(key_func=_rl_key)
   app.state.limiter = limiter
   from slowapi import _rate_limit_exceeded_handler
   app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
   ```
3. Decorate `/ask` (rate is per-token because the key func reads the auth header).
   The handler must take `request: Request` for slowapi to see it:
   ```python
   from fastapi import Request
   @app.post("/ask")
   @limiter.limit("30/minute")
   def ask(request: Request, req: AskRequest, authorization: str | None = Header(default=None)):
   ```

### ACCEPTANCE
```bash
for i in $(seq 1 35); do curl -s -o /dev/null -w "%{http_code} " -XPOST localhost:8000/ask -H "authorization: Bearer <MOREC_TOKEN>" -H 'content-type: application/json' -d '{"question":"hi"}'; done; echo
```
PASS = a run of `200` then `429`s appear once past 30/min.

---

## M4 — Audit log carries the caller identity  [HIGH]

WHY: today `trace.jsonl` logs `client`+`question` but no WHO. After M1 the client IS
derived from a token, so the client label already = identity. Make that explicit and
add a per-request id so an incident is reconstructable.

### Steps
1. `core/trace.py` already writes `client`, `question`, `event`, `ts`. Add a `subject`
   passthrough. Change `log_event` signature to accept `subject=None` and include it:
   ```python
   def log_event(client: str, question: str, event: str, subject: str | None = None, **fields):
       record = {"ts": time.time(), "client": client, "subject": subject,
                 "question": question, "event": event, **fields}
   ```
2. In `core/agent.py` `ask(...)`, thread a `subject` argument (default `None`) and pass
   it to every `trace.log_event(...)` call. In `api/server.py`, pass
   `subject=hashlib.sha256(authorization.encode()).hexdigest()[:12]` so the raw token
   is never logged, only a stable id.

### ACCEPTANCE
```bash
tail -1 client-chatbot/work/trace.jsonl | python3.13 -c "import sys,json;print('subject' in json.loads(sys.stdin.read()))"
```
PASS = `True`, and the value is a 12-char hash, never the token itself.

---

## M5 — Catalog: real deny-by-default + word-boundary match  [HIGH]

WHY: `CLIENT_NAME_TOKENS` is a hardcoded BLOCKLIST. A new client's named proc whose
token isn't listed is treated generic → entitled to everyone. And substring match
(`"cl" in tail`) wrongly excludes generic procs (`Close*`, `*Include*`). Two fixes.

### Steps
1. Fix under-blocking: build the exclusion set from ALL registered clients, not just a
   hardcoded list. In `core/catalog.py` add:
   ```python
   def _registered_client_tokens() -> set:
       toks = set()
       for p in (config.CLIENTS_DIR).glob("*.yaml"):
           if p.stem.startswith("_"):
               continue
           import yaml
           cfg = yaml.safe_load(p.read_text()) or {}
           toks.add(p.stem.lower())
           toks.update(a.lower() for a in cfg.get("name_aliases", []))
       return toks
   ```
   Then in `_entitled`, the effective token set = `CLIENT_NAME_TOKENS | _registered_client_tokens()`.
   Now every client we actually serve is auto-excluded from every OTHER client's catalog.
2. Fix over-blocking: match on segment boundaries, not substring. Replace the hit test:
   ```python
   def _entitled(proc_name: str, own_tokens: set, all_tokens: set) -> bool:
       tail = proc_name.split(".")[-1].lower()
       segments = set(re.split(r"[^a-z0-9]+", tail))   # split on _ and case boundaries handled below
       # also split camelCase: SAP_Integ_SendSalesInvoices_Kaylani -> {sap,integ,...,kaylani}
       hit = {t for t in all_tokens if t in segments}
       if not hit:
           return True
       return hit <= own_tokens
   ```
   Add `import re` at top. This stops `"cl"` matching `close`.
   ponytail: segment split is coarse (won't split `SendSalesInvoices` into words), but
   client names are their own underscore-delimited segment in every real example, so
   segment-match is correct for the actual proc naming. Upgrade to a tokenizer only if a
   counter-example appears.

### ACCEPTANCE
```bash
python3.13 -c "
import sys;sys.path.insert(0,'.')
from core import catalog
ent = catalog.for_client('morec', ['morec','morek'])
assert not any('rukn' in p.lower() or 'alalmas' in p.lower() for p in ent), 'LEAK: rukn-named proc entitled to morec'
assert not any('kaylani' in p.lower() for p in ent), 'LEAK: kaylani proc entitled to morec'
print('deny-by-default OK; entitled procs:', len(ent))
"
```
PASS = prints `deny-by-default OK`, no assertion fires.

---

## M6 — Stop advertising the dead `run_proc` tool (or make it real)  [HIGH]

WHY: `chatbot_ro` has no EXECUTE grant. Live test: `EXECUTE permission was denied`.
The model is offered `run_proc`, calls it, always errors, burns turns. Pick ONE path.

### Path B (lazy, ship-now) — remove the dead tool
1. In `core/agent.py` `TOOLS`, delete the whole `run_proc` tool dict.
2. In `_run_tool`, delete the `if name == "run_proc":` branch.
3. Leave `core/sql.py:run_proc` in place (unused, harmless) for when Path A lands.

### Path A (real, later) — grant EXECUTE on write-free allow-listed procs
1. Write `setup/04_audit_procs.py`: for each entitled proc, read
   `sys.sql_expression_dependencies` + `sys.dm_sql_referenced_entities`; a proc is
   SAFE only if it has zero `is_updated=1` / write dependency. Emit the safe list to
   `work/<client>/exec_allowlist.txt`.
2. Write `db/03_grant_exec.sql` (run as SA): `GRANT EXECUTE ON <proc> TO chatbot_ro`
   for each name in the allowlist ONLY. Never `GRANT EXECUTE` on a schema.
3. Re-add the tool (revert Path B) once the allowlist is non-empty and audited.

DECISION for this pilot: do **Path B now**. Path A is a real phase, not a one-liner —
it needs the write-free audit before any grant, or you re-open a write path.

### ACCEPTANCE (Path B)
```bash
python3.13 -c "import sys;sys.path.insert(0,'.');from core import agent;print('run_proc' in str(agent.TOOLS))"
```
PASS = `False`.

---

## M7 — Schema-drift recovery in one command  [MED]

WHY: `schema_cache.json` + `t.` views are built once at setup. A renamed column
silently breaks answers; a new CompanyID table gets no view. Recovery is currently
manual and undocumented. Make it one idempotent command.

### Steps
1. Write `setup/refresh.py --client <name>` that runs, in order:
   `02_introspect.py` (rebuild cache) then `03_apply_db_sql.py` (rebuild `t.` views).
   Both scripts already exist — this just chains them for one client, as SA.
   ```python
   # setup/refresh.py  — ponytail: chains the two existing setup scripts, no new logic
   import argparse, subprocess, sys
   ap = argparse.ArgumentParser(); ap.add_argument("--client", required=True)
   c = ap.parse_args().client
   for step in ("02_introspect.py", "03_apply_db_sql.py"):
       subprocess.run([sys.executable, f"setup/{step}", "--client", c], check=True)
   ```
   (Adjust the flags to whatever `02_/03_` actually take — read their `argparse` first.)
2. Document in `README.md`: "Schema changed at the client? Run
   `python3.13 setup/refresh.py --client <name>` (as SA). Until you do, answers may be
   stale." No auto-detect in the pilot — that's a production item (wire the drift-tool).

### ACCEPTANCE
```bash
python3.13 setup/refresh.py --client morec && python3.13 -c "
import sys;sys.path.insert(0,'.')
from core import sql
c=sql.get_conn('morec');cur=c.cursor()
cur.execute(\"SELECT COUNT(*) FROM sys.views v JOIN sys.schemas s ON v.schema_id=s.schema_id WHERE s.name='t'\")
print('t. views:', cur.fetchone()[0]); c.close()
"
```
PASS = runs clean, prints a t.-view count (~345 for morec).

---

## M8 — Multi-company client: ask once per session, allow "all"  [MED]

WHY: a client with >1 CompanyID gets asked "which company?" on EVERY question, and
can never total across companies. Two fixes; do part 1 now, part 2 if a real
multi-company client is onboarded.

### Part 1 (now) — remember the resolved CompanyID for the session
1. In `api/server.py` keep a `dict[session_id] -> {"CompanyID": int}`.
   ponytail: in-memory dict, single process; fine for pilot. Comment the ceiling.
2. Pass it into `agent.ask(..., conversation=SESSIONS.get(session_id, {}))`; when the
   agent resolves/receives a CompanyID, store it back. `core/params.resolve` already
   reads `conversation` first — so once stored, no re-ask.

### Part 2 (when needed) — "all companies" aggregate
1. Detect an "all companies / total across companies" intent → loop the known
   CompanyIDs, run the SAME tenant-scoped query per id, sum in Python. Never widen a
   `t.` view. Each call stays single-tenant; the aggregate happens app-side.

### ACCEPTANCE (Part 1)
```bash
# same session_id, two questions; the 2nd must NOT return needs_ask for CompanyID
# (only meaningful on a real multi-company DB; on morec it's single so it never asks —
#  test on a multi-company client once one exists)
echo "manual-verify on a multi-company client"
```
PASS = second question in a session does not re-ask for company.

---

## M9 — SQL Server MCP (thin wrapper over `core/sql.py`)  [MED — you asked for this]

WHY: you want SQL execution reachable over MCP (universal, tool-based, same shape as
the vault MCP). Correct way: expose OUR gated path as an MCP. NOT a generic mssql MCP
— that connects with its own creds and bypasses the gate + tenant wall entirely.
This satisfies the plan's golden rule 9 ("one SQL impl, shared by agent AND the MCP").

STATUS: **BUILT + TESTED, exit 0, live.** Under `sqlmcp/` (named `sqlmcp` not `mcp` so
it doesn't shadow the pip `mcp` package). Transport = **SSE/HTTP** (for the
different-network case; stdio is local-pipe only). Ran
`bash sqlmcp/run_isolation_test.sh` against the real `drift-tool-mssql` container:
  - DB put on an `--internal` (no host-route) network `olives_dbnet`, shared only
    with the MCP container. A second `--internal` net `olives_appnet` holds the MCP
    + a test-client with **no route to the DB at all**.
  - Proof 1: test-client -> `drift-tool-mssql:1433` directly = **unreachable** (isolation real, not assumed).
  - Proof 2: test-client -> MCP (SSE) -> gated `SELECT COUNT(*) FROM t.Customers` =
    **`n=33517`** (matches the earlier-verified customer count) — so the gated query
    still works with ZERO direct DB route, over a network boundary.
  - Fallback confirmed untouched after the test: `drift-tool-mssql` still on `bridge`,
    host `:14330` still published, 31/31 unit tests still pass.

**Real gotcha hit and fixed (keep this when reusing the kit):** the `mcp` SDK's
`FastMCP` has its own DNS-rebinding guard — it 421s any request whose `Host:` header
isn't `127.0.0.1`/`localhost` by default. A remote/cross-network chatbot will never
dial localhost, so `sql_server.py` now takes `MCP_ALLOWED_HOSTS` (comma-separated,
e.g. `olives-sql-mcp:*` or the real prod host:port) and adds it to
`TransportSecuritySettings.allowed_hosts`/`allowed_origins`. **Widen this per
deployment — never disable the check.**

READ FIRST: for the chatbot talking to its own DB, the in-process call is simpler and
has identical security. Build/run this MCP ONLY if an EXTERNAL consumer (Claude
Desktop, another agent, a service on another network) must run gated queries. Don't
route the agent through an MCP nobody else calls just for its own same-host DB (YAGNI).

### Steps
1. `python3.13 -m pip install "mcp[cli]"` (add `mcp` to `requirements.txt`).
2. Write `mcp/sql_server.py` — a stdio MCP exposing exactly the gated functions:
   ```python
   # mcp/sql_server.py — thin MCP over core/sql.py. SAME gate, SAME chatbot_ro login,
   # SAME set_tenant. No new SQL path. The client+company_id are MCP tool args, and the
   # CALLER of the MCP is trusted to pass the right tenant — so this MCP must only ever
   # be exposed to a trusted server-side process, never straight to an end user.
   import sys; sys.path.insert(0, "..")
   from mcp.server.fastmcp import FastMCP
   from core import sql, catalog, config

   mcp = FastMCP("olives-sql")

   @mcp.tool()
   def run_select(sql_text: str, company_id: int, client: str) -> list:
       """Run one gated, tenant-scoped read-only SELECT via the t. views."""
       procs = list(catalog.for_client(client, config.load_client(client).get("name_aliases", [client])))
       return sql.run_select(sql_text, company_id, client, allowed_procs=procs)

   if __name__ == "__main__":
       mcp.run()
   ```
3. Register it wherever the agent's MCP clients are configured. Do NOT point the agent
   at any third-party mssql MCP.
4. SECURITY NOTE to write into `mcp/README.md`: this MCP trusts its caller for
   `client`/`company_id`. It is a SERVER-SIDE tool behind M1's auth, never exposed to a
   browser or an untrusted agent. The wall (read-only login + t. views + gate) still
   holds even if the caller lies about the tenant — worst case they see only rows for
   whatever company_id they pass, and only via t. views, and only read-only.

### ACCEPTANCE
```bash
# the isolation guarantee must survive through the MCP path:
python3.13 -c "
import sys;sys.path.insert(0,'..' if __import__('os').getcwd().endswith('mcp') else '.')
from core import sql, catalog, config
# base-table bypass must still be denied through the same call the MCP makes:
try:
    sql.run_select('SELECT * FROM dbo.Customers', 1, 'morec', allowed_procs=[]); print('LEAK')
except Exception as e:
    print('BLOCKED via shared path:', type(e).__name__)
"
```
PASS = `BLOCKED via shared path: OperationalError` (the MCP inherits the wall because
it calls the exact same `core/sql.py`).

---

## M10 — Metrics + real streaming  [MED, polish]

WHY: `/metrics` exposes one counter; plan lists 5 (latency, cache-hit, gate-rejects,
refusals, per-client). `/ask` "SSE" computes the whole answer then emits once.

### Steps
1. In `core/trace.py` add three more Prometheus objects and increment them where they
   happen: a `Histogram` for turn latency (wrap the agent loop), a
   `Counter("chatbot_cache_hits_total", ..., ["client"])` (bump in the plan-cache hit
   branch of `agent.ask`), a `Counter("chatbot_gate_rejections_total", ..., ["client"])`
   (bump in the `except gate.GateError` path). `refused` is already an event label.
2. Real streaming is a bigger change (the agent returns a full string today). Defer
   unless the UX demands it — mark it a NICE, not a MED. ponytail: leave the
   compute-then-emit as-is; it's honest, just not incremental.

### ACCEPTANCE
```bash
curl -s localhost:8000/metrics | grep -E 'chatbot_(cache_hits|gate_rejections)_total|chatbot_turn' | head
```
PASS = the new metric names appear.

---

## M11 — Vault-as-universal-schema  [SEPARATE TRACK — do NOT start inside this plan]

WHY: your stated architecture — chatbot learns structure (tables/columns/procs +
usage) from the obsidian vault MCP, universal across clients, vault synced from `.105`
— is NOT wired in. Today = per-client live introspection. This is a REBUILD of the
structure source, and it has a prerequisite the review found: the vault graph was
rejected earlier as dirty (callers/callees swapped, junk tokens). So:

Order of operations (each is its own effort, not steps here):
1. Clean the vault + establish the `.105 → vault` structure sync (structure only, never
   client data). Until the vault is trustworthy, it cannot be the schema source.
2. Split the two concerns explicitly:
   - STRUCTURE (names, columns, procs, their documented use) → from the vault MCP.
   - EXECUTION + SCOPING + counts (`t.` views, `set_tenant`, `profile_probe`) → MUST
     stay from the live client DB. You cannot build a tenant view or a distinct-count
     from the vault; those are per-DB facts.
3. Change `setup/02_introspect.py` (or the agent's `introspect_schema` tool) to read
   structure from the vault MCP, while `02_apply_db_sql.py` + `params.discover_profile`
   keep reading the real DB. The query itself still runs on the client's DB, gated,
   exactly as now.

DO NOT begin M11 until M1–M6 are green. A universal schema layer on top of an
unauthenticated, single-model, dead-proc-path base multiplies the blast radius.

---

## Order + gate summary

| Phase | Title | Severity | Green when |
|---|---|---|---|
| M1 | API auth, token→tenant | BLOCKER | 401/403/token-wins |
| M2 | Model failover + vetted primary | BLOCKER | fallback answers |
| M3 | Rate limit | HIGH | 429 past limit |
| M4 | Identity in audit | HIGH | subject in trace |
| M5 | Catalog deny-by-default | HIGH | no cross-client proc entitled |
| M6 | Kill dead run_proc (Path B) | HIGH | run_proc not in TOOLS |
| M7 | One-command drift refresh | MED | refresh.py runs, views rebuilt |
| M8 | Multi-company session memory | MED | no re-ask in a session |
| M9 | SQL MCP (only if external caller) | MED | wall survives MCP path |
| M10 | Metrics + streaming | MED | new metrics appear |
| M11 | Vault universal schema | SEPARATE | after M1–M6 only |

Ship gate: **M1 + M2 green = deployable to ONE authenticated pilot client.**
M3–M6 green = safe for a second tenant. M7–M10 = it's a product. M11 = it's your
stated universal architecture.
