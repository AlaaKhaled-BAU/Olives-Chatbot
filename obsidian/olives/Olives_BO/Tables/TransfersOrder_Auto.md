---
type: table
database: Olives_BO
name: TransfersOrder_Auto
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
referenced_by:
  - [[Pro_TransfersOrders_Auto]]
  - [[Rpt_TransfersOrders]]
support_relevance: high
last_verified: 2026-07-05
---
# TransfersOrder_Auto


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores transfersorder auto records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| FileID | bigint | NO | ✓ |  |  |
| CompanyID | smallint | NO | ✓ |  |  |
| SalesPersonID | int | NO | ✓ |  |  |
| ItemCode | nvarchar | YES | ✓ |  |  |
| UnitID | nvarchar | YES | ✓ |  |  |
| Quantity | float | NO |  |  |  |
| TrDateTime | smalldatetime | NO |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| FileName | nvarchar | YES |  |  |  |
| LastRunDate | smalldatetime | YES |  |  |  |
| MaxQty | float | YES |  |  |  |
## Primary Key
FileID
CompanyID
SalesPersonID
ItemCode
UnitID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_TransfersOrders_Auto]]
- [[Rpt_TransfersOrders]]

**Writes (2):**
- [[Pro_TransfersOrders_Auto]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
