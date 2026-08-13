---
type: table
database: Olives_BO
name: PendingOrdersDetails
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
referenced_by:
  - [[Tablet_GetPendingOrdersTotals]]
support_relevance: high
last_verified: 2026-07-05
---
# PendingOrdersDetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores pendingordersdetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | int | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| OrderDate | smalldatetime | NO | ✓ |  |  |
| Itemcode | nvarchar | YES | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| Total | float | YES |  |  |  |
| Qantity | float | YES |  |  |  |
| Bonus | float | YES |  |  |  |
## Primary Key
CompanyID
OrderNo
OrderDate
Itemcode
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Tablet_GetPendingOrdersTotals]]

**Writes (0):**
_None_

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
