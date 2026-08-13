---
type: procedure
database: Olives_BO
name: Pro_TransfersOrders_Auto
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - [[Items]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersons]]
  - [[TransfersOrder_Auto]]
writes_to:
  - [[TransfersOrder_Auto]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_TransfersOrders_Auto


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, ItemsUnits, ItemsUnitsDetails, SalesPersonItemsAssignment, SalesPersons, TransfersOrder_Auto. Writes TransfersOrder_Auto. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @SalesPersonID int=null
- @ToSalesPersonID int=null
- @ItemCode nvarchar(100)=null
- @MinQty float=null
- @MaxQty float=null
- @UnitID nvarchar(50) = null
- @cmdType varchar(50)=null
## Tables Read
- [[Items]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- [[TransfersOrder_Auto]]
## Tables Written
- [[TransfersOrder_Auto]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- [[TransfersOrder_Auto]]

**Tables Written**
- [[TransfersOrder_Auto]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
