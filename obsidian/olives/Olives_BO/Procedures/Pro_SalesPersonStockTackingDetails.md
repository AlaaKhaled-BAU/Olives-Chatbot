---
type: procedure
database: Olives_BO
name: Pro_SalesPersonStockTackingDetails
schema: dbo
tags: [#backoffice, #inventory, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersonStockTacking]]
  - [[SalesPersonStockTackingDetails]]
  - [[SalesPersons]]
writes_to:
  - [[SalesPersonStockTackingDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonStockTackingDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Items, ItemsUnits, SalesPersonItemsAssignment, SalesPersonItemsBalance, SalesPersonStockTacking, SalesPersonStockTackingDetails, SalesPersons. Writes SalesPersonStockTackingDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @OrderYear smallint=null
- @OrderNo INT = NULL
- @ItemCode nvarchar(50)=null
- @UnitID nvarchar(50)=null
- @Quantity Float = NULL
- @cmdType varchar(50)=null
## Tables Read
- [[ClientsActive]]
- [[Items]]
- [[ItemsUnits]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalesPersonStockTacking]]
- [[SalesPersonStockTackingDetails]]
- [[SalesPersons]]
## Tables Written
- [[SalesPersonStockTackingDetails]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Items]]
- [[ItemsUnits]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalesPersonStockTacking]]
- [[SalesPersonStockTackingDetails]]
- [[SalesPersons]]

**Tables Written**
- [[SalesPersonStockTackingDetails]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
