---
type: procedure
database: Olives_BO
name: WF_SelectItemsCategories
schema: dbo
tags: [#auth, #backoffice, #inventory, #workflow]
reads_from:
  - [[ItemsCategories]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# WF_SelectItemsCategories


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ItemsCategories. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID varchar(50)
## Tables Read
- [[ItemsCategories]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ItemsCategories]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Workflow procedure — called automatically by the WF engine when processing approval chains. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
