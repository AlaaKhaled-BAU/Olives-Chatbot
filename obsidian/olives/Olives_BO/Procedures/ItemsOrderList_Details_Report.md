---
type: procedure
database: Olives_BO
name: ItemsOrderList_Details_Report
schema: dbo
tags: [#reporting]
reads_from:
  - Items
  - ItemsStoreByUser
  - ItemsUnits
  - PriceListDetails
  - SalesPersons
  - TransfersOrdersDetails
  - TransfersOrdersHeaders
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# ItemsOrderList_Details_Report

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 7 table(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @fromDate datetime
- @toDate datetime
- @TransType int
- @SalesPersonID int
- @Supervisor int
- @ItemClass nvarchar(100)
- @StoreNo nvarchar(100)
- @OrderType int
## Tables Read
- [[Items]]
- [[ItemsStoreByUser]]
- [[ItemsUnits]]
- [[PriceListDetails]]
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
- `GetItemOrgUnitQty`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
