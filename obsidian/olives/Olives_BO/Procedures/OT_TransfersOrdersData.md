---
type: procedure
database: Olives_BO
name: OT_TransfersOrdersData
schema: dbo
tags: [#maintenance]
reads_from:
  - CompanyParameters
writes_to:
  - TransactionsSerials
  - TransfersOrdersDetails
  - TransfersOrdersHeaders
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# OT_TransfersOrdersData

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 1 table(s); writes 3; calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @OrderYear smallint
- @OrderNo int
- @ItemNo nvarchar(100)
- @UnitCode nvarchar(50)
- @Qty float
- @cmdType varchar(50)
- @SalesPersonID int
- @OrderDate smalldatetime
- @Notes nvarchar(500)
- @DocType int
- @VouType int
## Tables Read
- [[CompanyParameters]]
## Tables Written
- [[TransactionsSerials]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[CompanyParameters]]
## Callers
_None_
## Callees
- `GetItemMasterUnitQty`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
