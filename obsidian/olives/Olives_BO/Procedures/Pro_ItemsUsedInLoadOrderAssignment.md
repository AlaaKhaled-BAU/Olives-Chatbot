---
type: procedure
database: Olives_BO
name: Pro_ItemsUsedInLoadOrderAssignment
schema: dbo
tags: [#backoffice, #inventory, #order]
reads_from:
  - Fun_GetItemsUnits
  - [[Items]]
  - [[ItemsClasses]]
  - [[ItemsUnits]]
  - [[Positions]]
  - [[SalesPersonItemsUseInLoadOrder]]
  - [[SalesPersons]]
  - int
writes_to:
  - [[SalesPersonItemsUseInLoadOrder]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ItemsUsedInLoadOrderAssignment


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetItemsUnits, Items, ItemsClasses, ItemsUnits, Positions, SalesPersonItemsUseInLoadOrder, SalesPersons, int. Writes SalesPersonItemsUseInLoadOrder. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @PositionsID int=22
- @ItemCode nvarchar(20) = null
- @UnitID nvarchar(50) =null
- @cmdType varchar(50)='Copy To'
- @ItemsUsedInLoadOrderAssignment_Type_DATATABLE ItemsUsedInLoadOrderAssignment_Type  readonly
- @CopyFrom int = 22
- @ToGroup int = null
## Tables Read
- Fun_GetItemsUnits
- [[Items]]
- [[ItemsClasses]]
- [[ItemsUnits]]
- [[Positions]]
- [[SalesPersonItemsUseInLoadOrder]]
- [[SalesPersons]]
- int
## Tables Written
- [[SalesPersonItemsUseInLoadOrder]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Fun_GetItemsUnits
- [[Items]]
- [[ItemsClasses]]
- [[ItemsUnits]]
- [[Positions]]
- [[SalesPersonItemsUseInLoadOrder]]
- [[SalesPersons]]
- int

**Tables Written**
- [[SalesPersonItemsUseInLoadOrder]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
