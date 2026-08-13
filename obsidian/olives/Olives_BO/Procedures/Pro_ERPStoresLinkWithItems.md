---
type: procedure
database: Olives_BO
name: Pro_ERPStoresLinkWithItems
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - [[ERPStores]]
  - [[ERPStoresItemsLink]]
  - [[Items]]
writes_to:
  - [[ERPStoresItemsLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ERPStoresLinkWithItems


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ERPStores, ERPStoresItemsLink, Items. Writes ERPStoresItemsLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @StoreNo int=null
- @ItemCode varchar(max)=null
- @cmdType varchar(50)=null
## Tables Read
- [[ERPStores]]
- [[ERPStoresItemsLink]]
- [[Items]]
## Tables Written
- [[ERPStoresItemsLink]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ERPStores]]
- [[ERPStoresItemsLink]]
- [[Items]]

**Tables Written**
- [[ERPStoresItemsLink]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
