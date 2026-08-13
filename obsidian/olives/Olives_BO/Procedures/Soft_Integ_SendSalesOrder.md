---
type: procedure
database: Olives_BO
name: Soft_Integ_SendSalesOrder
schema: dbo
tags: [#integration]
reads_from:
  - Customers
  - Items
  - ItemsUnits
  - OrdersDetails
  - SalesPersons
writes_to:
  - OrdersHeaders
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Soft_Integ_SendSalesOrder

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 5 table(s); writes 1; calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Customers]]
- [[Items]]
- [[ItemsUnits]]
- [[OrdersDetails]]
- [[SalesPersons]]
## Tables Written
- [[OrdersHeaders]]
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
