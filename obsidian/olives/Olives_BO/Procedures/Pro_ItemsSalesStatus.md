---
type: procedure
database: Olives_BO
name: Pro_ItemsSalesStatus
schema: dbo
tags: [#backoffice, #inventory, #sales]
reads_from:
  - AND
  - [[Items]]
  - [[ItemsCategories]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - datetime
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ItemsSalesStatus


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AND, Items, ItemsCategories, OrdersDetails, OrdersHeaders, datetime. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @DateFrom datetime
- @DateTo datetime
- @CategCode int = NULL
- @TopType nVarchar(10) = 'TOP' -- TOP / LOW )
## Tables Read
- AND
- [[Items]]
- [[ItemsCategories]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
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
- [[OrdersDetails]]
- [[OrdersHeaders]]
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
