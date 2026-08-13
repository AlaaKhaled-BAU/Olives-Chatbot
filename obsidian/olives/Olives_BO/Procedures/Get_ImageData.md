---
type: procedure
database: Olives_BO
name: Get_ImageData
schema: dbo
tags: [#backoffice]
reads_from:
  - Olives_Images
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Get_ImageData


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Olives_Images. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @OrderNo int =null
- @OrderYear int=null
## Tables Read
- Olives_Images
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Olives_Images

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
