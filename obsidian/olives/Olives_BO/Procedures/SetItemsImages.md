---
type: procedure
database: Olives_BO
name: SetItemsImages
schema: dbo
tags: [#backoffice, #inventory]
reads_from:
  - [[Items]]
writes_to:
  - [[Items]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SetItemsImages


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items. Writes Items. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ItemImage image = null
- @ItemCode nvarchar (100) = null
- @cmdType varchar(50)=null
## Tables Read
- [[Items]]
## Tables Written
- [[Items]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]

**Tables Written**
- [[Items]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
