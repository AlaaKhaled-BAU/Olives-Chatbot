# Salesman visits — three questions, three grains

Use this when the user asks about زيارات المندوب / salesman visits.

## 1. Actual visits (already happened)

**Source:** `LogActionTransaction` ← `OT_ImportActionLog` ← OSFA `OT_ActionLog`.

Query `t.LogActionTransaction`. Decode ActionID via `lookup_hot` (`LogActions`) — not WF approval codes (`WF_SubLog.Action` / `LastStatus`; see `workflow_approval_status.md`).

| Rule | Detail |
|------|--------|
| Visit login | `ActionID = N'0'` (CustEntry). `Data1` = customer id. |
| Visit logout | `ActionID = N'3'` (CustLeave). |
| **Not a visit** | `ActionID = N'7'` (SystemLogin) — often the most common row. |
| Data1 overload | Actions 4/5/9/12: `Data1` = doc **year**, `Data2` = doc **number**. |
| Last week | Filter `TimeStamp`; use tenant dates, not invoice max alone. |

Never `SalesmanVisitsSummary`. Never OSFA `OT_ActionLog` from chatbot.

## 2. Planned visits (route calendar / خطة المسار)

**Source:** BO master → `OT_SendSalesmanData` → OSFA `OT_SalesmanRoute` (tablet copy only).

Chatbot queries BO only:

1. `SalesPersons.PositionID` → `SalesPersonsRoutes` (`WeekDay` 1=Sat … 7=Fri).
2. Pick route id from correct `Week1`–`Week4` slot (`Fun_GetWeekNo` — not blind `COALESCE(Week1..Week4)`).
3. `CustomersFinancialDetails`: same `PositionsID`, matching `RouteID`, order by `VisitOrder`.
4. `RoutesInformation.Name` for route label.
5. Optional override: `SalespersonRouteByDate` (sparse).

Keywords: خطة المسار، المجدول، المخطط، زيارات قادمة (when user wants the **schedule**, not a forecast).

## 3. Forecast / analyst opinion (توقع / تحليل / رأيك)

**Source:** historical `LogActionTransaction` (`ActionID = N'0'` weekly series) + `analyze` tool.

- User asks توقع، تحليل، رأيك، كمحلل، اتجاه — **not** the static route plan.
- Retrieve GROUP BY week/month series; label estimates **تقديري**; confidence medium/low.
- Do **not** answer forecast from `SalesPersonsRoutes` unless user also asks for plan comparison.

## Sync diagram

```
PLANNED:  SalesPersonsRoutes + CFD + RoutesInformation
            → OT_SendSalesmanData → OSFA OT_SalesmanRoute

ACTUAL:   Tablet → OT_ActionLog → OT_ImportActionLog → LogActionTransaction
```
