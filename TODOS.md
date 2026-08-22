# TODOs

## Later metrics (transfers, collections $, aging)

- **What:** After the first `run_metric` pack (net sales, returns, orders, van stock, CFD assignment), add grains from `knowledge/reference/tables summary.md`: `TransfersOrdersHeaders/Details`, receipt amounts vs invoiced amounts, CFD aging/credit buckets.
- **Why:** Accountant general use includes تحصيل vs مبيعات and van load/unload, not only invoices. Live H07/H08 already showed receipts-vs-invoices is a real question.
- **Pros:** Completes tables-summary coverage without EXEC of Rpt_*.
- **Cons:** More cards delay the Arabic accuracy gate if built in the same slice.
- **Context:** First pack is locked by eng review (2026-08-14): `run_metric` + tenant pack + Arabic Wave 5. Do not expand until that gate is green on client 105 / CompanyID 2.
- **Depends on:** `core/metrics.py` (or equivalent) shipping and Arabic evals passing.
- **Source:** /plan-eng-review D8 → 7A

## Gate-wrap `sql.run_proc` before any GRANT EXECUTE

- **What:** `core/sql.py` `run_proc` (lines 81–107) must run through `gate.validate`, CompanyID/CompNo binding, and row cap — same as `run_select`. Today it `cursor.execute`s parameterized EXEC after `set_tenant` only.
- **Why:** The first GRANT PR would otherwise give `chatbot_ro` a weaker EXEC path than SELECT (no sqlglot, no CompNo rewrite, no row cap). Ownership chaining means EXEC is not automatically read-only.
- **Pros:** T5 cannot ship a raw EXEC hole; xp_/OPENROWSET still denied.
- **Cons:** Dead code until GRANT; easy to over-engineer the wrap.
- **Context:** D2 = no GRANT in `feat/general-bo-assistant` first PR. D3 = reuse `run_proc`, do not add `run_exec`. Outside voice (2026-08-15) found the skip. Start at `run_proc` and `gate.validate` EXEC branch (gate.py:225–229).
- **Depends on / blocked by:** Signed `rpt_exec_allowlist.json` + setup GRANT. Do not implement in the SELECT-template PR.
- **Source:** /plan-eng-review D9 → A

## Wave-2 GRANT EXECUTE for audited read-only Rpt_*

- **What:** After templates + audit script exist, Grok signs rejects, then `GRANT EXECUTE` on specific procs to `chatbot_ro` and wire `run_report` → `run_proc`.
- **Why:** Some reports cannot be one SELECT (`#temp`, multiple result sets).
- **Pros:** Same resultset as Olives print.
- **Cons:** One-way permission door; regex audit is incomplete (`sp_executesql`, nested EXEC).
- **Context:** First PR: `allowed_procs=[]`. Templates in-repo. Audit writes candidates only.
- **Depends on:** Gate-wrap TODO above, `setup/audit_rpt_readonly.py`, human sign-off.
- **Source:** /plan-eng-review D2=A, D7=A

