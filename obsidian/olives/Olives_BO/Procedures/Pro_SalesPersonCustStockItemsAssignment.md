---
type: procedure
database: Olives_BO
name: Pro_SalesPersonCustStockItemsAssignment
schema: dbo
tags: [#backoffice, #inventory, #sales]
reads_from:
  - [[Items]]
  - [[ItemsCategories]]
  - [[SalespersonCustStockItemsAssignment]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersons]]
  - int
writes_to:
  - [[SalespersonCustStockItemsAssignment]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonCustStockItemsAssignment


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, ItemsCategories, SalespersonCustStockItemsAssignment, SalesPersonItemsAssignment, SalesPersons, int. Writes SalespersonCustStockItemsAssignment. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @ItemCode nvarchar(20) = null
- @CompanyID smallint=null
- @PositionsID int = null
- @CopyFrom int = null
- @FilterValue varchar(100) = ''
- @ToGroup int = null
- @cmdType varchar(50) = null
- @SalesPersonCustStockItemsAssignment_Type_DATATABLE SalesPersonCustStockItemsAssignment_Type  readonly
## Tables Read
- [[Items]]
- [[ItemsCategories]]
- [[SalespersonCustStockItemsAssignment]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- int
## Tables Written
- [[SalespersonCustStockItemsAssignment]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[ItemsCategories]]
- [[SalesPersonCustStockItemsAssignment]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- int

**Tables Written**
- [[SalespersonCustStockItemsAssignment]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
