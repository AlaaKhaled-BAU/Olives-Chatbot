---
type: procedure
database: Olives_BO
name: Pro_ItemsUnitsDetails
schema: dbo
tags: [#backoffice, #inventory]
reads_from:
  - [[CustomerStockTackingDetails]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[OrdersDetails]]
  - [[ReturnOrdersDetails]]
  - [[SalesPersonStockTackingDetails]]
  - [[TransactionsDetails]]
  - [[TransfersOrdersDetails]]
writes_to:
  - [[ItemsUnitsDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ItemsUnitsDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerStockTackingDetails, Items, ItemsUnits, ItemsUnitsDetails, OrdersDetails, ReturnOrdersDetails, SalesPersonStockTackingDetails, TransactionsDetails, TransfersOrdersDetails. Writes ItemsUnitsDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ItemCode nvarchar(20) = null
- @UnitID nvarchar(50) =null
- @ConvertRate float=null
- @UnitSerial int=null
- @Barcode nvarchar (20)=null
- @Volume float =null
- @Weight float =null
- @IsSuspended bit = null
- @cmdType varchar(50)=null
- @UsedInUploadOrder bit = null
## Tables Read
- [[CustomerStockTackingDetails]]
- [[Items]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[OrdersDetails]]
- [[ReturnOrdersDetails]]
- [[SalesPersonStockTackingDetails]]
- [[TransactionsDetails]]
- [[TransfersOrdersDetails]]
## Tables Written
- [[ItemsUnitsDetails]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerStockTackingDetails]]
- [[Items]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[OrdersDetails]]
- [[ReturnOrdersDetails]]
- [[SalesPersonStockTackingDetails]]
- [[TransactionsDetails]]
- [[TransfersOrdersDetails]]

**Tables Written**
- [[ItemsUnitsDetails]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
