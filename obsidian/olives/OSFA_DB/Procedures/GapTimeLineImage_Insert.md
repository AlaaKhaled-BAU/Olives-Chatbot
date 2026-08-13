---
type: procedure
database: OSFA_DB
name: GapTimeLineImage_Insert
schema: dbo
tags: [#mobile]
reads_from:
  - `dbo`
writes_to:
  - GapTimeLineImage
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# GapTimeLineImage_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads dbo. Writes GapTimeLineImage. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @TabletSysID varchar (50)='00202'
- @ImageData image=null
- @TimeLineID nvarchar(500)=0
- @GapTransYear int=0
- @GapTransNo int=0
- @ErrNo SmallInt output
## Tables Read
- `dbo`
## Tables Written
- GapTimeLineImage
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dbo

**Tables Written**
- GapTimeLineImage

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
