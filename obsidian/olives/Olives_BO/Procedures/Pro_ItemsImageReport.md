---
type: procedure
database: Olives_BO
name: Pro_ItemsImageReport
schema: dbo
tags: [#backoffice, #inventory, #reporting]
reads_from:
  - AND
  - [[Items]]
  - [[ItemsCategories]]
  - [[PriceListDetails]]
  - datetime
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ItemsImageReport


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AND, Items, ItemsCategories, PriceListDetails, datetime. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CategCode int = NULL
- @PriceListID int )
## Tables Read
- AND
- [[Items]]
- [[ItemsCategories]]
- [[PriceListDetails]]
- datetime
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- AND
- [[Items]]
- [[ItemsCategories]]
- [[PriceListDetails]]
- datetime

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
