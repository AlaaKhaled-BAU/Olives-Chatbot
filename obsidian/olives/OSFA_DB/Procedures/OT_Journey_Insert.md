---
type: procedure
database: OSFA_DB
name: OT_Journey_Insert
schema: dbo
tags: [#mobile]
reads_from:
  - [[OT_Journey]]
writes_to:
  - [[OT_Journey]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Journey_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_Journey. Writes OT_Journey. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesmanNo smallint
- @StartTime datetime
- @EndTime datetime
- @GPSX_Start varchar (50)
- @GPSY_Start varchar (50)
- @GPSX_End varchar (50)
- @GPSY_End varchar (50)
- @ErrNo SmallInt Output
## Tables Read
- [[OT_Journey]]
## Tables Written
- [[OT_Journey]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_Journey]]

**Tables Written**
- [[OT_Journey]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
