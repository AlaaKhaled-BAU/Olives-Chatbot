---
type: procedure
database: Olives_BO
name: OT_ImportGapTrans
schema: dbo
tags: [#backoffice, #mobile]
reads_from:
  - [[ClientsActive]]
  - [[GapTransHeaders]]
  - Header
  - `dbo`
writes_to:
  - [[GapTransHeaders]]
  - GapTransImages
  - [[GapTransTags]]
  - [[Notifications]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportGapTrans


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, GapTransHeaders, Header, dbo. Writes GapTransHeaders, GapTransImages, GapTransTags, Notifications. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[ClientsActive]]
- [[GapTransHeaders]]
- Header
- `dbo`
## Tables Written
- [[GapTransHeaders]]
- GapTransImages
- [[GapTransTags]]
- [[Notifications]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[GapTransHeaders]]
- Header
- dbo

**Tables Written**
- [[GapTransHeaders]]
- GapTransImages
- [[GapTransTags]]
- [[Notifications]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
