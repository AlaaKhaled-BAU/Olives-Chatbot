---
type: procedure
database: OSFA_DB
name: GapTransImages_Insert
schema: dbo
tags: [#mobile]
reads_from:
  - `dbo`
writes_to:
  - GapTransImages
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# GapTransImages_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads dbo. Writes GapTransImages. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @TabletSysID varchar (50)
- @ImageData image
- @ErrNo SmallInt Output
## Tables Read
- `dbo`
## Tables Written
- GapTransImages
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dbo

**Tables Written**
- GapTransImages

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
