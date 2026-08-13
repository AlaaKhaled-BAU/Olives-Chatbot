---
type: procedure
database: Olives_BO
name: Pro_CustomerStockTackingDetails
schema: dbo
tags: [#backoffice, #customer, #inventory]
reads_from:
  - [[CustomerStockTackingDetails]]
  - [[Items]]
  - [[ItemsUnits]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CustomerStockTackingDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerStockTackingDetails, Items, ItemsUnits. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @OrderNo INT = NULL
- @cmdType varchar(50)=null
## Tables Read
- [[CustomerStockTackingDetails]]
- [[Items]]
- [[ItemsUnits]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerStockTackingDetails]]
- [[Items]]
- [[ItemsUnits]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
