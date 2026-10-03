---
type: table
database: Olives_BO
name: RequestSalesmanWillNotVisit
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
referenced_by:
  - [[OT_ImportRequestSalesmanWillNotVisit]]
  - [[Rpt_WorkFlowFunctions]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-10-03
---
# RequestSalesmanWillNotVisit

## Business Purpose
Stores approval requests submitted when a salesman requests permission to skip / not visit a customer assigned to their scheduled route. Corresponds to workflow `FunctionID = 23` ("Request Salesman Will Not Visit"). Links to [[NoTransactionsReasons]] via `ReasonID` (where `ReasonType = 2`, No Visit Reason). Captures the salesman, customer, reason, timestamp, and approval state. Queryable via `t.RequestSalesmanWillNotVisit`.

## Chatbot semantics
(Query `t.RequestSalesmanWillNotVisit` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| طلبات عدم زيارة عميل في المسار | `SalesPersonNo`, `CustomerNo`, `TrDate` | Direct filter | Lists route exemption / skip requests |
| سبب عدم الزيارة | `ReasonID` | Join `t.NoTransactionsReasons` on `r.ID = req.ReasonID AND r.ReasonType = 2` | Text reason (e.g. road blocked, store closed) |
| حالة الموافقة | `IsAproved` | `IsAproved = 1` (approved), `0` or `NULL` (pending) | Direct approval status |
| الربط مع سجل الموافقات العام | Join `t.WF_MasterLog` | `m.FunctionID = 23 AND TRY_CAST(m.Ref1 AS numeric) = req.AutoID AND m.CompanyID = req.CompanyID` | View supervisor decision levels & notes |

**Do not confuse with:**
- `RequestToVisitCustomerNotInRoute`: Reverse request — asking to visit a customer *outside* route schedule (`FunctionID = 5`).
- `LogActionTransaction`: ActionID `21` ("Will Not Visit") logs the field action event, whereas this table tracks the workflow approval request.

## Grain & keys
- **PK**: `AutoID` (numeric identity, 1 row = 1 skip-visit request)
- **Tenant key**: `CompanyID`
- **Conventions**: `CustomerNo` → [[Customers]](ID), `SalesPersonNo` → [[SalesPersons]](ID), `ReasonID` → [[NoTransactionsReasons]](ID)

## Pipeline (how rows get here)
Salesman requests skipping a scheduled customer on tablet → `OT_ImportRequestSalesmanWillNotVisit` inserts into this table (`IsAproved = 0`) → calls `WF_AddWorkFlowLevelOne @CompNo, 23, @NewAutoID` → creates `WF_MasterLog` (`Ref1 = AutoID`). When supervisor approves, `WF_AddWorkFlowLevels` sets `IsAproved = 1`.

## Related
- [[WF_MasterLog]]
- [[WF_SubLog]]
- [[WF_Functions]]
- [[NoTransactionsReasons]]
- [[SalesPersonsRoutes]]
- [[LogActionTransaction]]
- [[_RequestTo-Join-Conventions]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| ReasonID | int | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| OSFA_AutoID | numeric | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_ImportRequestSalesmanWillNotVisit]]
- [[Rpt_WorkFlowFunctions]]
- [[WF_AddWorkFlowLevels]]

**Writes (3):**
- [[OT_ImportRequestSalesmanWillNotVisit]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
