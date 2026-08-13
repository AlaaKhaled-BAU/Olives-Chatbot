---
type: procedure
database: Olives_BO
name: CheckCustexist
schema: dbo
tags: [#backoffice]
reads_from:
  - [[CustomerPhone]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# CheckCustexist


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerPhone. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo SMALLINT = 1
- @CustName VARCHAR(50) = 'test'
- @phone VARCHAR(50) = '079523214482;079775234683'
## Tables Read
- [[CustomerPhone]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerPhone]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
