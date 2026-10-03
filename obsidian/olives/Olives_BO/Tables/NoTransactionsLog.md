---
type: table
database: Olives_BO
name: NoTransactionsLog
schema: dbo
tags: [#backoffice, #log]
foreign_keys:
  - [[Companies]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
referenced_by:
  - [[SalesmanInfo]]
support_relevance: high
last_verified: 2026-10-03
---
# NoTransactionsLog

## Business Purpose
Fact log recording route points where a salesman logged no transaction or skipped an activity, capturing the date, salesman, route, GPS coordinates, and reason code. Links to [[NoTransactionsReasons]] via `ReasonID` to explain why the route stop had no commercial transaction. Queryable via `t.NoTransactionsLog`.

## Chatbot semantics
(Query `t.NoTransactionsLog` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| سجل عدم وجود حركات | `SalesPersonID`, `RouteID`, `VisitDate` | e.g. `CAST(VisitDate AS date) = '...'` | Shows unserviced or non-transacting stops |
| سبب عدم الحركة | `ReasonID` | Join `t.NoTransactionsReasons` on `r.ID = l.ReasonID AND r.ReasonType = 1` | Translates to text reason (e.g. no cash, closed) |
| إحداثيات وملاحظات | `Latitude`, `Longitude`, `Notes` | Direct select | GPS audit of the stop |

**Do not confuse with:**
- `LogActionTransaction`: General action log where `ActionID = N'8'` is NoSaleExit and `21` is WillNotVisit. `NoTransactionsLog` is a dedicated structured event log for non-transaction route stops.

## Grain & keys
- **PK**: `AutoID` (bigint)
- **Tenant key**: `CompanyID`
- **FKs**: `SalesPersonID` → [[SalesPersons]](ID), `RouteID` → [[RoutesInformation]](ID)

## Pipeline
Uploaded from mobile devices during end-of-visit or daily route sync.

## Related
- [[NoTransactionsReasons]]
- [[SalesPersons]]
- [[RoutesInformation]]
- [[LogActionTransaction]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | bigint | YES | ✓ |  |  |
| CompanyID | smallint | YES |  | ✓ | [[SalesPersons]] |
| SalesPersonID | int | YES |  | ✓ | [[SalesPersons]] |
| RouteID | int | YES |  | ✓ | [[RoutesInformation]] |
| ReasonID | int | YES |  |  |  |
| VisitDate | smalldatetime | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, RouteID -> [[RoutesInformation]](CompanyID, ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[SalesmanInfo]]

**Writes (0):**
_None_

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Orphan lines**: Detail rows without matching header — causes sync failures
- **Posting failure**: IsPosted flag stuck false — check ERP integration log
- **Duplicate vouchers**: Same VouNo generated for different transactions — run dedup check
- **Currency mismatch**: ExRate different from CurrenciesRate table — financial reconciliation off
- **Void inconsistency**: IsVoid flag but original transaction still active — check WF approval

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
