---
type: procedure
database: Olives_BO
name: Soft_Integ_SendLoadOrder
schema: dbo
tags: [#integration]
reads_from:
  - Items
  - ItemsUnits
  - SalesPersons
  - TransfersOrdersDetails
writes_to:
  - TransfersOrdersHeaders
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Soft_Integ_SendLoadOrder

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 4 table(s); writes 1; calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Items]]
- [[ItemsUnits]]
- [[SalesPersons]]
- [[TransfersOrdersDetails]]
## Tables Written
- [[TransfersOrdersHeaders]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `GetItemOrgUnitQty`
## When to Run

Run during API sync cycles: pulls from or pushes to an external ERP/API when new data is ready or on-demand refresh.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
