# Wave-2: allow-listed read-only Rpt_* EXEC

Status: NOT this sprint. Do after transcript plan. Python 3.13.
`gate.DEFAULT_ALLOWED_PROCS` is `()` today. `run_report` uses in-repo SELECT templates, never EXEC.

## Why some reports stay unrunnable

A named Olives report is often a stored procedure: `#temp` tables, multiple result sets, branches. A single `run_select` cannot reproduce it. EXEC is banned until SA audit + signed allow-list + GRANT, because ownership chaining is not a read-only guarantee.

## Order (do not skip)

1. **Gate-wrap `sql.run_proc`** (TODOS.md already). Same `gate.validate`, CompanyID bind, row cap as `run_select`. No GRANT yet. Tests: EXEC of non-allow-listed name is `GateError`; `xp_` / OPENROWSET still rejected.
2. **Run** `python3.13 setup/audit_rpt_readonly.py --client morec` (SA). Writes candidates. **Never print proc bodies.**
3. **Human signs** `work/<client>/rpt_exec_allowlist.json` (`allowed: [...]`). Empty file = no GRANT.
4. **GRANT EXECUTE** only those names to `chatbot_ro` (setup script, SA).
5. Wire `run_report`: if template exists, keep SELECT; if name is on signed list and no template, `run_proc`.
6. Isolation eval: any `EXEC evil` still `GateError`. Accuracy: 2–3 named reports that had no template now match Olives print (row cap).

## Do not

- `allowed_procs=['%']`
- Reuse IIS `cds`
- Return procedure text to the model
- Grant `db_datareader`

## Parallel

Lane audit (SA machine) || Lane gate-wrap tests (no GRANT). Merge gate-wrap first. GRANT is a one-way door; separate PR.
