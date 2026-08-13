---
type: procedure
database: OSFA_DB
name: OT_ActionLog_CheckExist
schema: dbo
tags: [#log, #mobile]
reads_from:
  - [[OT_ActionLog]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ActionLog_CheckExist


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_ActionLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @ActionID nvarchar (40)
- @TimeStamp datetime
- @SalesmanID nvarchar (40)
- @Data1 nvarchar (max)=''
- @Data2 nvarchar (100)=''
- @Data3 nvarchar (100)=''
- @Data4 nvarchar (100)=''
- @Data5 nvarchar (100)=''
- @GpsX nchar (100)
- @GpsY nchar (100)
- @ErrNo SmallInt Output
- @Exist SmallInt Output
- @TabletSysID	varchar(50)=''
## Tables Read
- [[OT_ActionLog]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_ActionLog]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
