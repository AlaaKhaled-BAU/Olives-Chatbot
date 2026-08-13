# Metabase — go/no-go (PLAN.md Phase 10)

**Scope:** reports/dashboards/scheduled push, a parallel delivery layer — not the chat brain.

## Verdict: GO, with one specific constraint

Metabase (self-hosted, open-source) has an official SQL Server driver and
is a reasonable fit for scheduled reports and permission-gated dashboards.

**The catch:** the open-source tier has no per-row multi-tenant sandboxing
(that's a paid Pro/Enterprise feature). Using it safely for more than one
client means **one Metabase data-source connection per client**, each
pointed at that client's own `chatbot_ro`-style read-only login and `t.`
schema (exactly what Phase 2/9 already built) — not one shared connection
relying on Metabase's own permission model to separate tenants. That
reuses the actual server-side wall (golden rule 3) as the isolation
boundary; Metabase itself only needs to trust the connection it's given,
the same posture `core/sql.py` already takes.

**Why not the paid sandboxing tier instead:** it would let one connection
serve every client, but it moves the tenant boundary into Metabase's own
row-security config — a second place to get it right, on top of the
SESSION_CONTEXT wall that already exists and is already tested
(`tests/test_tenant_wall.py`, `tests/test_multi_client.py`). Per-client
connections cost more setup per client, not more engineering risk.

**Not evaluated further (genuinely parallel, not blocking the pilot):**
exact dashboard content, embedding/branding, scheduling cadence. Revisit
once a first report is actually requested.
