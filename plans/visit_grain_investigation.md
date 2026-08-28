# Visit grain investigation

Working notes on salesman visit data grain, sync direction, and chatbot source-of-truth decisions.

---

## OSFA ↔ BO visit & route sync

### Sync overview

Two distinct pipelines:

1. **Route / planned visits** — master data maintained in BO, pushed to the tablet during `OT_SendSalesmanData`.
2. **Actual field activity** — captured on the tablet into OSFA `OT_ActionLog`, pulled into BO `LogActionTransaction` by `OT_ImportActionLog`.

```
PLANNED (BO → OSFA, master-data push)
  SalesPersonsRoutes + CustomersFinancialDetails + RoutesInformation
    └─ OT_SendSalesmanData
         ├─ OSFA OT_RouteMF          (route name lookup per salesman)
         └─ OSFA OT_SalesmanRoute    (denormalized daily customer visit list)

ACTUAL (OSFA → BO, transaction pull)
  Tablet app
    └─ OSFA OT_ActionLog (Posted=0)
         └─ OT_ImportActionLog
              └─ BO LogActionTransaction (OSFA_AutoID = tablet row)
```

`knowledge/reference/tables summary.md` header rule applies: **transaction tables OSFA → BO; master data BO → OSFA**. Route planning is master data; action log is transactional.

### Direction table

| Entity | BO table | OSFA table | Sync direction | Source of truth (chatbot) |
|--------|----------|------------|----------------|---------------------------|
| Weekly route calendar (position × weekday × week-slot → RouteID) | `SalesPersonsRoutes` | — (derived at push time) | BO → OSFA (via `OT_SendSalesmanData`) | **`t.SalesPersonsRoutes`** |
| Customer ↔ route assignment + visit order | `CustomersFinancialDetails` (`RouteID`, `VisitOrder`, `PositionsID`) | — (joined at push into `OT_SalesmanRoute`) | BO → OSFA | **`t.CustomersFinancialDetails`** |
| Route names | `RoutesInformation` | `OT_RouteMF` (route desc lookup pushed per salesman) | BO → OSFA | **`t.RoutesInformation`** |
| Date-specific route override (some clients, e.g. client 74) | `SalespersonRouteByDate` | — (used when building `OT_SalesmanRoute` / `OT_RouteMF`) | BO → OSFA | **`t.SalespersonRouteByDate`** (when present) |
| Daily visit plan on tablet (customer × date, `Visited` flag) | — (not stored; computed from calendar + CFD) | `OT_SalesmanRoute` | BO → OSFA (rebuilt each `OT_SendSalesmanData`; `Visited` updated on OSFA from `OT_ActionLog` during same proc) | **Do not query OSFA.** Reconstruct from BO calendar tables above. |
| Field action / visit events | `LogActionTransaction` (`OSFA_AutoID` links to tablet row) | `OT_ActionLog` (`Posted` flag) | OSFA → BO (`OT_ImportActionLog`) | **`t.LogActionTransaction`** |
| Journey start/end (GPS bookends) | — (no BO mirror found) | `OT_Journey` | Tablet-local; not primary visit fact | **Not available in chatbot** (`t.` views) |
| Off-route visit requests | — | `OT_RequestToVisitCustomerNotInRoute` | Tablet → (workflow) | **Not in BO visit facts** |

### Planned visits: where truth lives after sync

**Authoritative schedule is always in BO**, not on the tablet copy.

Resolution path for «الزيارات القادمة» / next-week planned visits:

1. `SalesPersons.PositionID` → `SalesPersonsRoutes` for the target weekday (`WeekDay` 1=Saturday … 7=Friday).
2. Pick route slot: `Week1`–`Week4` via BO week logic (`Fun_GetWeekNo` in reports; do not assume calendar week-of-month).
3. Customers on that route: `CustomersFinancialDetails` where `PositionsID` = salesman position and `RouteID` matches the resolved slot.
4. Route label: `RoutesInformation.Name`.

`OT_SendSalesmanData` materializes this onto the tablet:

- **Deletes** then **re-inserts** `OSFA_DB.dbo.OT_SalesmanRoute` for `(CompNo, SalesmanNo)`.
- Builds rows from `SalesPersonsRoutes` × `CustomersFinancialDetails` × `OT_CustomerMF` (salesman-scoped customers).
- For client 74, also unions `SalespersonRouteByDate` date overrides.
- Pushes route names into `OT_RouteMF` from `RoutesInformation` (and `SalespersonRouteByDate` where applicable).

`OT_SalesmanRoute` is a **tablet working copy** with per-date rows (`RouteDate`, `CustomerNo`, `VisitOrder`, `Visited`, `TodayRoute`). During the same `OT_SendSalesmanData` run, `Visited` is stamped on OSFA from same-day `OT_ActionLog` rows where `ActionID = N'0'` (CustEntry). That flag is UX state on the device, not the BO calendar.

`Tablet_GetSalesmanRoute` reads BO `SalesPersonsRoutes` directly (no OSFA hop) — confirms BO is the definition source.

### Actual visits: confirm LogActionTransaction path

**Confirmed one-way import path:**

1. Tablet writes `OSFA_DB.dbo.OT_ActionLog` as events occur (`Posted = 0`).
2. `OT_ImportActionLog` (@CompNo) during OSFA sync service:
   - Reads unposted `OSFA_DB.dbo.OT_ActionLog` (`Posted = 0`, excludes `ActionID = 49`).
   - Inserts into `Olives_BO.dbo.LogActionTransaction` with `OSFA_AutoID` = OSFA `AutoID`.
   - Sets `OT_ActionLog.Posted = 1`.
   - Side effects: stamps GPS/`LocationLineID` onto invoices/orders/receipts; fills `PendingInvoices` for action 49; assistant splits.
3. Chatbot reads **`t.LogActionTransaction` only** — never `OT_ActionLog`.

**Visit counting rules** (from vault + `knowledge/reference/visits_grain.md`):

| ActionID | Meaning | Use for visit count? |
|----------|---------|----------------------|
| `N'0'` | CustEntry (customer visit login) | **Yes** — primary visit grain |
| `N'3'` | CustLeave | Pair with 0 for duration |
| `N'7'` | SystemLogin (app open) | **No** — more frequent, not a customer visit |
| `N'4'`,`N'5'`,`N'9'`,`N'12'` | Invoice/order/return/payment | **No** — `Data1`/`Data2` are document year/no, not customer |

`Data1` = customer id only for visit-like actions (0, 3, 8, 14, 15, 21, 31). For document actions, `Data1` = year and `Data2` = doc number.

If `OT_ImportActionLog` fails, rows remain unposted in OSFA and BO visit/GPS data is stale. Chatbot will under-count until import succeeds.

### Live DB check (local `Olives_BO` / `OSFA_DB`, 2026-08-28)

| Table | DB | Row count | Notes |
|-------|-----|-----------|-------|
| `OT_SalesmanRoute` | OSFA | 3,776 | Daily plan copy; recent dates ~3 customers/day in sample |
| `OT_RouteMF` | OSFA | 69 | Route name lookup pushed from BO |
| `OT_ActionLog` | OSFA | 7,159 | All `Posted=0` on this instance (import not run recently) |
| `OT_Journey` | OSFA | 6,929 | Journey bookends; no BO mirror |
| `SalesPersonsRoutes` | BO | 434 | Weekly calendar |
| `SalespersonRouteByDate` | BO | 12 | Date overrides (sparse) |
| `LogActionTransaction` | BO | 86,752 | 63,533 rows have `OSFA_AutoID` set |

OSFA route/visit-related tables found: `OT_SalesmanRoute`, `OT_RouteMF`, `OT_Journey`, `OT_RequestToVisitCustomerNotInRoute`, `OT_RequestSalesmanWillNotVisit`, `OT_RequestToExceedCustomerVisitOrder`. Only `OT_SalesmanRoute` mirrors the route-calendar concept; it is a push derivative, not a second master.

### Chatbot decision summary

| Question | Answer |
|----------|--------|
| Actual visits last week? | `t.LogActionTransaction` WHERE `ActionID = N'0'` |
| Planned visits next week? | `t.SalesPersonsRoutes` + `t.CustomersFinancialDetails` + `t.RoutesInformation` |
| Compare planned vs actual? | Join calendar (above) to `t.LogActionTransaction` on customer + date; do not use `OT_SalesmanRoute.Visited` |
| Query OSFA tables? | **Never** from chatbot runtime |

---

## SalesPersonsRoutes vs alternatives (planned visits)

**Investigator:** explore agent (fd945d2e) + live DB counts.

### Verdict

**`SalesPersonsRoutes` is the correct primary table** for the weekly route calendar — but **never alone**. Planned visits are a **join chain**, not one table:

```
SalesPersons (PositionID)
  → SalesPersonsRoutes (WeekDay 1=Sat…7=Fri, Week1–Week4 → RouteID)
  → CustomersFinancialDetails (PositionsID + RouteID + VisitOrder)
  → RoutesInformation (route name)
```

`CFD.VisitOrder` is stop sequence on a route, not a schedule table.

### Alternatives — when to use each

| Table | Role for planned visits |
|-------|-------------------------|
| **`SalesPersonsRoutes`** | Default weekly template: which route runs which weekday |
| **`CustomersFinancialDetails`** | Which customers sit on that route + visit order |
| **`RoutesInformation`** | Route name / id |
| **`SalespersonRouteByDate`** | Sparse **date override** (e.g. ClientActive=74 in send-data); not the main calendar |
| **`SalespersonCustomersVisitsByDate`** | Per-customer dated exceptions (online workflow reports); not main calendar |
| **`CustomersVisitActivity`** | Visit-activity checklist synced to tablet — **not** scheduling |

### Live row counts (local `Olives_BO`, 2026-08-28)

| Table | Rows | Notes |
|-------|------|-------|
| `SalesPersonsRoutes` | 434 | Dense (≈43 positions × 7 weekdays) |
| `SalespersonRouteByDate` | 12 | Max date 2026-03-26; **0 future** on this DB |
| `SalespersonCustomersVisitsByDate` | 13 | Sparse exceptions |
| `CustomersVisitActivity` | 865 | Activity tokens, not schedule |

### Chatbot guidance (pending note refactor)

- «زيارات قادمة / خطة المسار» → `SalesPersonsRoutes` + `CFD` + `RoutesInformation`; resolve `Week1`–`Week4` with BO week logic (`Fun_GetWeekNo`), not naive calendar week.
- «توقع / تحليل» → **not** this chain alone; use `LogActionTransaction` history + analyst mode (forecast from CustEntry trend).
- Do **not** use `COALESCE(Week1..Week4)` without weekday + week-slot resolution — that was a shortcut in early bot tests.

**Confidence:** high on SPR as calendar master; medium on week-slot resolution (client-specific `Fun_GetWeekNo`).

---

## OT_SendSalesmanData (BO → OSFA)

**Investigator:** generalPurpose agent (fae9adf7) + live `OBJECT_DEFINITION` (~901 KB).

### Business purpose

Master-data **push from BO to the salesman tablet** (`@CompNo`, `@SalesmanNo`, `@SendDate`). Run after onboarding or when admin triggers «Send Data to Salesman». Deletes and repopulates OSFA `OT_*` working tables for that salesman, then the tablet pulls them on «Update Data».

Opposite of **`OT_ImportActionLog`** (tablet actions → BO). This proc **does not** import visits; it **ships** the plan and catalog the tablet needs to work.

### Orchestration (business flow, IF branches omitted)

1. **Logging / guards** — `OT_SendLog`, `ClientsActive`, salesman validation.
2. **`OT_SendItemsInfo`** — items, units, prices, categories, store balances, assignments → many `OT_Items*`, `OT_StoreItemsQty`, price lists, etc.
3. **`OT_SendCustomersInfo`** — customers, financial details, GPS, classes → `OT_CustomerMF`, `OT_CustomersGPSLocations`, credit lists, etc.
4. **Route / visit plan** (critical for «زيارات قادمة»):
   - Read BO **`SalesPersonsRoutes`** (+ **`SalespersonRouteByDate`** for some clients, e.g. 74).
   - Push route names → **`OSFA_DB.OT_RouteMF`** (from `RoutesInformation`).
   - Expand **`@SendDate` forward** (~1 month default; ~7 days for some ClientActive values).
   - For each calendar day: resolve route id from `WeekDay` + `Week1`–`Week4` (uses **`Fun_GetWeekNo`**).
   - Join **`CustomersFinancialDetails`** (`RouteID`, **`VisitOrder`**) for customers on that route.
   - Delete + insert **`OSFA_DB.OT_SalesmanRoute`** (daily customer visit list: date, customer, visit order, route).
   - Stamp `Visited` on OSFA rows from same-day `OT_ActionLog` ActionID=`0` (tablet UX only).
5. **Salesman profile** — `OT_SalesmanMF`, device permissions, serials, targets, system options, surveys, contracts, etc.
6. **Transaction staging** — pending invoices/orders/receipts headers for tablet pickup (not visit facts).

`Tablet_GetSalesmanRoute` reads BO **`SalesPersonsRoutes` directly** — confirms BO defines the calendar; OSFA copy is derivative.

### Route-related BO → OSFA mapping

| BO source | OSFA target | Meaning |
|-----------|-------------|---------|
| `SalesPersonsRoutes` + `RoutesInformation` | `OT_RouteMF` | Route id/name lookup per salesman |
| `SalesPersonsRoutes` × `CustomersFinancialDetails` × date expansion | `OT_SalesmanRoute` | **Daily planned customer visits** (date, customer, VisitOrder) |
| `SalespersonRouteByDate` (client-specific) | merged into above | Date override when configured |

### What this is NOT

- Not the source of **actual** visits (that's `OT_ActionLog` → `LogActionTransaction` via import).
- Not safe for chatbot to query OSFA tables — BO calendar tables are authoritative.
- Not a single table answer: visit plan = **SPR + CFD + RoutesInformation + week-slot logic**.

### Implications for note refactor

| Topic | Current notes risk | Correct story |
|-------|-------------------|---------------|
| Planned visits | Only `SalesPersonsRoutes` | Add CFD + RoutesInformation + `Fun_GetWeekNo`; mention `SalespersonRouteByDate` override |
| `OT_SalesmanRoute` | May be missing in vault | Document as OSFA push child of send-data; chatbot ignores |
| `OT_SendSalesmanData` | Auto-generated proc stub | Replace Purpose with business push list above |
| Analyst «توقع» | Confused with route plan | Forecast = `LogActionTransaction` trend; plan = SPR chain |

**Confidence:** high on route push mechanics (verified in live proc: 18× `SalesPersonsRoutes`, 20× `OT_SalesmanRoute`, 26× `VisitOrder`, 3× `Fun_GetWeekNo`). Medium on full ~77-table inventory (client branches). Vault frontmatter `writes_to` on `OT_SendSalesmanData.md` lists many BO tables incorrectly as writes — treat as unreliable until refactor.

---

## Evaluation checklist (before accepting vault edits)

- [ ] `SalesPersonsRoutes.md` — planned visits = template; must join CFD + RoutesInformation
- [ ] `CustomersFinancialDetails.md` — RouteID + VisitOrder in visit plan chain
- [ ] `LogActionTransaction.md` — actual visits; link to import; Data1 overload table
- [ ] `OT_ImportActionLog.md` — OSFA → BO action log (already partially done)
- [ ] `OT_SendSalesmanData.md` — BO → OSFA master push; route → `OT_SalesmanRoute`
- [ ] `visits_grain.md` / join playbook — distinguish plan vs actual vs analyst forecast
- [ ] Add `OSFA_DB.OT_SalesmanRoute` table note (OSFA, not chatbot-queryable) if missing
- [ ] Remove / never resurrect `SalesmanVisitsSummary`
