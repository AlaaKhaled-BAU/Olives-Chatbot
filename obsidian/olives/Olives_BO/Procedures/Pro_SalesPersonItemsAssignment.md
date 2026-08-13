---
type: procedure
database: Olives_BO
name: Pro_SalesPersonItemsAssignment
schema: dbo
tags: [#backoffice, #inventory, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsClasses]]
  - [[ItemsUnits]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersons]]
  - int
writes_to:
  - [[SalesPersonItemsAssignment]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonItemsAssignment


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Items, ItemsCategories, ItemsClasses, ItemsUnits, SalesPersonItemsAssignment, SalesPersons, int. Writes SalesPersonItemsAssignment. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @DefinitionDate smallDateTime = null
- @ItemCode nvarchar(20) = null
- @CompanyID smallint=null
- @PositionsID int = null
- @CopyFrom int = null
- @IsSuspended bit  =null
- @FilterValue varchar(100) = ''
- @ToGroup int = null
- @cmdType varchar(50) = null
- @SalesmanNo int = null
- @SalesPersonItemsAssignment_Type_DATATABLE SalesPersonItemsAssignment_Type  readonly
## Tables Read
- [[ClientsActive]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsClasses]]
- [[ItemsUnits]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- int
## Tables Written
- [[SalesPersonItemsAssignment]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsClasses]]
- [[ItemsUnits]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- int

**Tables Written**
- [[SalesPersonItemsAssignment]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
