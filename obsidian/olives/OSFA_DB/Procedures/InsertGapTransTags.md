---
type: procedure
database: OSFA_DB
name: InsertGapTransTags
schema: dbo
tags: [#mobile]
reads_from:
  - [[GapTransTags]]
writes_to:
  - [[GapTransTags]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# InsertGapTransTags


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads GapTransTags. Writes GapTransTags. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint =1
- @DeviceSysID varchar(MAX)='asdasdasdasd'
- @GapTagID int=3003
- @GapTagValue varchar(MAX) ='fahed'
## Tables Read
- [[GapTransTags]]
## Tables Written
- [[GapTransTags]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[GapTransTags]]

**Tables Written**
- [[GapTransTags]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
