---
type: procedure
database: Olives_BO
name: Pro_SalesPersonItemBonusTarget_Online
schema: dbo
tags: [#backoffice, #inventory, #sales]
reads_from:
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - Fun_GetSalesmanBonusItemForTarget
  - [[Items]]
  - [[SalesPersonGroupItemBonusTarget]]
  - [[SalesPersonItemBonusTarget]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonItemBonusTarget_Online


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CompanyParameters, Fun_GetSalesmanBonusItemForTarget, Items, SalesPersonGroupItemBonusTarget, SalesPersonItemBonusTarget, SalesPersons, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 2
- @SalesmanNo int = 68
## Tables Read
- [[ClientsActive]]
- [[CompanyParameters]]
- Fun_GetSalesmanBonusItemForTarget
- [[Items]]
- [[SalesPersonGroupItemBonusTarget]]
- [[SalesPersonItemBonusTarget]]
- [[SalesPersons]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CompanyParameters]]
- Fun_GetSalesmanBonusItemForTarget
- [[Items]]
- [[SalesPersonGroupItemBonusTarget]]
- [[SalesPersonItemBonusTarget]]
- [[SalesPersons]]
- dbo

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
