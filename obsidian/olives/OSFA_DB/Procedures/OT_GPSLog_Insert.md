---
type: procedure
database: OSFA_DB
name: OT_GPSLog_Insert
schema: dbo
tags: [#gps, #log, #mobile]
reads_from:
  - [[OT_GPSLog]]
  - `dbo`
writes_to:
  - [[OT_GPSLog]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_GPSLog_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_GPSLog, dbo. Writes OT_GPSLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesmanNo smallint
- @CustomerNo bigint
- @TransDate datetime
- @GpsX nchar (100)
- @GpsY nchar (100)
- @ErrNo SmallInt Output
- @TabletSysID	varchar(50)=''
- @CustLocLineID	varchar(50)=''
- @CustLocName	varchar(50)	=''
## Tables Read
- [[OT_GPSLog]]
- `dbo`
## Tables Written
- [[OT_GPSLog]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_GPSLog]]
- dbo

**Tables Written**
- [[OT_GPSLog]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
