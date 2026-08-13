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
support_relevance: low
last_verified: 2026-07-05
---
# NoTransactionsLog


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores notransactionslog records.

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
