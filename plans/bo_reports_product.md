# Reports product — BO user first, then tiny EXEC

Status: READY TO IMPLEMENT after R0 agreement.
Python 3.13. No widget / Olives login in this plan.
FO FTS: keep (locked earlier).

**Do not** open 593 `Rpt_*` via EXEC. Vault purposes are AUTO-GENERATED stubs. `schema_cache` has no param defaults. `run_report` exposes five simplified keys. `report_path` locks tools so uncertified reports cannot fall back to metrics.

---

## 1. Back-office user (what I would actually ask)

A BO manager does not think in `Rpt_CustomerSalesByItems`. They ask:

| Job | Typical Arabic | Correct product path |
|-----|----------------|----------------------|
| How much did we sell? | مبيعات يوليو / هذا الشهر | `run_metric(net_sales)` — not a 15-param proc |
| Who sold most? | أفضل مندوب / مبيعات المندوب | metric **or** certified `Rpt_SalesmanSalesSummary` if they said **تقرير** |
| Collections | التحصيل / سندات القبض | certified `Rpt_DailyReceiptsDetails` / `Rpt_CashSummary` / `Rpt_CollectedReceipts` |
| Customer activity | عملاء نشطين / لم يشتروا | `Rpt_ActiveAndInactiveCustomers` |
| Unsold items | أصناف لم تباع | `Rpt_ItemsNotSold` |
| Orders vs invoices | طلبات مقابل فواتير | `Rpt_SalesAndOrders` |
| Coverage | تغطية المسارات | `Rpt_Coverage` (assigned vs visited) — **not** route summary |
| **Route summary** | ملخص المسار / تقرير المسار للمندوب | **`Rpt_RouteSummaryBySalesman`** — §1.1 (demanded T1) |
| One item / one customer | حركة صنف X / مبيعات عميل Y | `Rpt_ItemTransaction` / `Rpt_CustomersSalesDetails` |
| How do I print this in Olives? | كيف أطبع تقرير المبيعات | `search_docs` — not EXEC |
| Named morning report | تقرير المبيعات اليومي / aging | certify a **grain** or honest “not certified — nearest metric X” |

**Not v1:** 500 client-suffixed procs, `@SalesmanArray='3003,'`, `@UserID=admin` — including **`Rpt_RouteSummaryBySalesmanCombine`**.

**How I want the model to behave:**

1. Number question (“كم مبيعات…”) → metric/SQL. Never trap into `not_certified`.
2. Named certified report (“تقرير التحصيل اليومي لشهر يوليو”) → one template, dates bound, CompanyID from session, table + short Arabic.
3. Unknown `Rpt_*` → “لا يوجد قالب معتمد. أقرب شيء: [metric]. هل تريد ذلك؟” then **allow `run_metric` on the same turn**.
4. Missing dates → calendar honesty / `needs_ask`. **Never** SQL CREATE defaults (2021 snapshots in vault).
5. Never proc bodies. Never claim Olives print unless EXEC smoke-tested.

Existing eval already owns the 10 aliases: `evals/report_alias_ar_105.jsonl`.

### 1.1 Crucial: `Rpt_RouteSummaryBySalesman`

BO screen **Route Summary by Salesman** is the morning pack: for a **day + one salesman** (generic proc) it mixes **actual visits**, orders, receipts, returns, customers/CFD, routes — vault `reads_from` includes `LogActionTransaction`, `Orders*`, `Receipts`, `ReturnOrders*`, `CustomersFinancialDetails`, `RoutesInformation`, plus `CSales` (often **not** a `t.` view).

| Proc | Params (vault) | Chatbot stance |
|------|----------------|------------------|
| **`Rpt_RouteSummaryBySalesman`** | `@CompanyID`, `@FromDate` **required**; `@SalesmanNo` **required**; `@WithTax=1` | **Canonical name** for routing. Tenant inject. Date = calendar / `needs_ask`. Salesman: user id **or** “كل المناديب” (then grain is all salespersons — do not silently use Combine’s `'3003,'`). |
| **`Rpt_RouteSummaryBySalesmanCombine`** | `@FromDate`/`@ToDate` stale defaults; `@SalesmanArray='3003,'`; `@UserID`; `@VisitStatus` | **Do not EXEC in v1.** Wrapper for all-salesmen + branch-by-user. Dangerous defaults. Client Combine_* variants stay catalog-excluded. |

**How the model should behave**

| User said | Path |
|----------|------|
| تقرير ملخص المسار / route summary / `Rpt_RouteSummaryBySalesman` | **Certified report_path** (after R2 template **or** EXEC). |
| كم زيارة / زيارات المندوب **without** تقرير | Existing visit grain: `LogActionTransaction` ActionID `N'0'` — **not** this report, **not** `Rpt_Coverage`. |
| خطة المسار / زيارات قادمة | `SalesPersonsRoutes` + CFD — **not** this report. |
| Client-named Combine (Sukhtian, Wafi, …) | Refuse / generic canonical only. |

**R2 vs R3 (must pick honestly)**

- A `t.` SELECT **cannot** reproduce Olives print (`CSales`, tax, no-transaction reasons, Combine tax/visit-status). Label any template **equivalent grain**: e.g. per salesman for `@FromDate`: visit count (`LAT` CustEntry), invoice count/amount, receipt amount, order count — tables that exist on `t.` only.
- If the user **must** match the BO print → **R3 EXEC** of **`Rpt_RouteSummaryBySalesman` only** (not Combine): inject `@CompanyID`, bind `@FromDate`, require `@SalesmanNo` or expand in app to all entitled salesmen **without** Combine’s array default. Audit callees (`CSales`, etc.) before GRANT.
- `@WithTax`: default `1` in app; do not ask unless user mentions ضريبة.

**Eval:** add `report_alias` rows (Arabic ملخص المسار + English route summary) once a template or EXEC path exists. Visit-battery visit questions must **not** flip to this report.

### 1.2 Verdict: is Combine worth adding?

**No — not as its own certified report and not as v1 EXEC.** It is a **UI wrapper**, not a second grain.

| What Combine adds | Chatbot value |
|-------------------|---------------|
| Loop many salesmen (`@SalesmanArray`) | Same grain as generic proc × N. App can loop `t.` template or EXEC generic per `t.SalesPersons` when user says كل المناديب. |
| Date range `@FromDate`–`@ToDate` | Generic vault shows **one** `@FromDate`. Range is useful — implement on the **canonical** template/EXEC, not by shipping Combine. |
| `@VisitStatus` | Filter on visit outcome. Nice-to-have; only if Olives print requires it **and** we EXEC after audit. |
| `@UserID` + `Fun_GetCompanyBranchesByUser` | **Olives login.** Chatbot has no Forms user. Empty/`admin` = wrong branch set. |
| Default `'3003,'` | Silent **one salesman** (or a leftover ID). Worse than asking. |
| 10+ Combine_* client clones | Entitlement excludes most; do not index as aliases. |

**BO user “كل المناديب، ملخص المسار أمس”:** route to **`Rpt_RouteSummaryBySalesman`** with salesman=all (session company, date bound). Do **not** register Combine as a `templates.json` name (duplicate rail, worse params).

**Revisit Combine EXEC only if:** (1) generic print-parity EXEC is green, (2) we can pass a **computed** salesman CSV from `t.SalesPersons` (never the CREATE default), (3) we **omit or dummy** `@UserID` after SA proves branches still match SESSION_CONTEXT company, (4) `@VisitStatus` documented. Until then Combine stays **Not T1**.

---

## 2. Devil’s advocate (what was thrown away)

| Attack | Verdict |
|--------|---------|
| Certifying “20 reports” is folklore | **Keep.** Expand templates **only** from eval/live misses. Default add **zero**. |
| Template named `Rpt_DailySales` that is not the proc is a **lie** | **Keep.** Purpose must say **equivalent grain** or wait for EXEC. |
| Unlocking `run_select` after not_certified = hallucinated reports | **Keep restriction:** unlock `run_metric` + `ask_user` + `analyze` only. |
| Auto-binding 3700 params from `sys.parameters` | **Defer.** No introspection of defaults until an EXEC candidate exists. |
| Tiny EXEC still needs SA + GRANT | **Keep GRANT last.** v1 EXEC = 0–5 procs after audit. |
| Stricter path breaks English aliases | **Keep aliases from `templates.json` only** (len ≥ 6), not stub catalog. |
| Dual rail “مبيعات المندوب” vs metric | **Design it:** no `تقرير` → metric; with `تقرير` → certified template. |
| Dual rail “زيارات” vs route summary | **Design it:** no `تقرير` → LAT visit grain; with تقرير ملخص المسار → this report. |
| EXEC Combine because BO “runs all salesmen” | **Reject.** Array default `'3003,'` is a silent wrong team. Loop generic proc or ask salesman. |
| Stub purposes pollute `match_reports` | **Stop injecting / scoring lock on AUTO-GENERATED purpose.** |

---

## 3. Product contract

The chatbot answers **business questions** with metrics and **certified SELECTs on `t.`**. It answers **named certified reports** (the 10 in `knowledge/report_templates/templates.json` **plus `Rpt_RouteSummaryBySalesman` as a demanded T1**). Uncertified `Rpt_*` → honest refusal + nearest metric. EXEC is a **later, signed, tiny** list — not the default brain. Combine / client suffixes are not T1.

---

## 4. Waves

### R0 — Honesty and routing (do this first; no GRANT)

1. Prompt/UI: “تقرير معتمد” = `t.` template. If SELECT ≠ Olives print, say **equivalent grain**.
2. **`report_path` iff:** `تقرير`/`report` **or** `Rpt_` stem **or** certified alias ≥6 chars from **`templates.json` only**. Do not lock the turn from stub `report_catalog.json` overlap.
3. Metadata injection: certified names + **template param keys** only. No AUTO-GENERATED purpose.
4. `run_report` → `not_certified`: drop report tool lock; allow `run_metric`, `ask_user`, `analyze` only.
5. Conflict: “مبيعات المندوب” without تقرير/`report`/`Rpt_` → **`run_metric`**.
6. Conflict: “زيارات” / visit counts without تقرير → visit grain (`LAT`), **not** `Rpt_RouteSummaryBySalesman` and **not** `Rpt_Coverage`.

Files: `core/agent.py` (`_is_report_path`, `_active_tools`, block ~1538), `core/reports.py` (`match_reports`), `prompts/system.md`.

Tests: `report_alias_ar_105.jsonl` stays green. Add: “كم مبيعات يوليو” must not set `report_path`. Uncertified `Rpt_Foo` must not stay locked.

### R1 — Param UX (certified only)

- Dates: calendar honesty / last posting period; do not omit filter when user named a month.
- CompanyID: session only.
- `needs_ask` when `Rpt_ItemTransaction` lacks `item_code`.
- `needs_ask` when route-summary template/EXEC lacks `@SalesmanNo` **and** user did not say كل المناديب / all salesmen.
- No `02_introspect` default_value until EXEC is scheduled.

### R2 — Expand templates only on demand

Do **not** rewrite 593 vault notes.

Add a `templates.json` row only if: a real question appeared, you can defend the `t.` grain, and you add a `report_alias_ar_105.jsonl` row.

**Demanded T1 (do not wait for a miss):** `Rpt_RouteSummaryBySalesman` — equivalent-grain SELECT on `t.` (visits + invoices + receipts + orders by salesman for a date) **or** skip template and go R3 EXEC of the generic proc if print-parity is required. Purpose text must say equivalent grain until EXEC smoke vs Olives print.

**Not T1:** EXEC `Rpt_DailySales`, **`Rpt_RouteSummaryBySalesmanCombine`** (array/`UserID` defaults), client suffixes (`_Sukhtian`, `_Wafi`, `_Spartan`, Delivery/Merchandisers), `RptOnlineRpt_*`.

### R3 — EXEC (after R0)

Order from `plans/rpt_exec_wave.md`: gate-wrap `sql.run_proc` with `allowed=[]` first.

Admission for signed list:

- SA readonly audit (no bodies to model)
- Human one-line purpose
- Dates bound in **application**; refuse if unresolved
- `@CompanyID`/`@compno` injected from session
- No required entity/array params unless user supplied
- Smoke vs Olives print for one CompanyID + date range

**v1 EXEC: 0–5 procs.** Strong candidate #1 after audit: **`Rpt_RouteSummaryBySalesman`** (inject company + date; require salesman or explicit all-salesmen loop). **Never** Combine / client variants in the first GRANT. GRANT = **separate PR**.

### R4 — Catalog hygiene

- `setup/build_report_catalog.py`: drop phantoms; trailing-space DB names aliased or dropped.
- Prefix variants stay out of chatbot reports until named in evals.
- No bulk vault Purpose edits.

---

## 5. Merge gate

```bash
python3.13 -m pytest tests/test_docs.py tests/test_api.py tests/test_session_memory.py -q
python3.13 evals/run_evals.py --suite isolation
# report_alias suite when wired
```

Visit battery: nightly, not merge.

---

## 6. Explicitly not this plan

Widget, login, Chroma, ISRI, Redis, raising `MAX_HISTORY_TURNS`, salesman ACL, dropping FO FTS, Metabase, rewriting 593 vault purposes, `allowed_procs=['%']`, GRANT in the same PR as gate-wrap.
