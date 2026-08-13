---
type: procedure
database: Olives_BO
name: Pro_AutoBasketLoadItems
schema: dbo
tags: [#backoffice, #inventory, #order]
reads_from:
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - [[Items]]
  - [[TransfersOrdersDetails]]
writes_to:
  - [[TransfersOrdersDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_AutoBasketLoadItems


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CompanyParameters, Items, TransfersOrdersDetails. Writes TransfersOrdersDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=2
- @OrderYear smallint=2023
- @OrderNo INT=232550230
- @VouType int=1
## Tables Read
- [[ClientsActive]]
- [[CompanyParameters]]
- [[Items]]
- [[TransfersOrdersDetails]]
## Tables Written
- [[TransfersOrdersDetails]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CompanyParameters]]
- [[Items]]
- [[TransfersOrdersDetails]]

**Tables Written**
- [[TransfersOrdersDetails]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
