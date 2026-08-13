---
type: procedure
database: Olives_BO
name: GetWF_TransferOrderData
schema: dbo
tags: [#workflow]
reads_from:
  - Items
  - ItemsCategories
  - ItemsPriority
  - ItemsUnits
  - PriceListDetails
  - PriceLists
  - SalesPersonItemsAssignment
  - SalesPersons
  - TransfersOrdersDetails
  - TransfersOrdersHeaders
writes_to:
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# GetWF_TransferOrderData

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 10 table(s); calls 4 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo int
- @OrderYear int
- @OrderNo bigint
## Tables Read
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriority]]
- [[ItemsUnits]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_GetItemsSuggestGroupLinkCOALESCE`
- `GetItemOrgUnitQty`
- `GetItemUnitBySerial`
- `GetItemUnitConvBySerial`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
