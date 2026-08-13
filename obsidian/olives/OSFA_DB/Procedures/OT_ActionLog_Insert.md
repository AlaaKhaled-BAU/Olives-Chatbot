---
type: procedure
database: OSFA_DB
name: OT_ActionLog_Insert
schema: dbo
tags: [#log, #mobile]
reads_from:
  - [[OT_ActionLog]]
writes_to:
  - [[OT_ActionLog]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ActionLog_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_ActionLog. Writes OT_ActionLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
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
- @RouteID	int
- @ErrNo SmallInt Output
- @TabletSysID	varchar(50)=''
- @CarCounter bigint=0
- @GPSOn	bit=0
- @NetworkOn	bit=0
- @InternetOn	bit=0
- @AppVersion varchar(50)=''
- @CustLocLineID	varchar(50)=''
- @AssistantsIDs varchar(50)=''
## Tables Read
- [[OT_ActionLog]]
## Tables Written
- [[OT_ActionLog]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_ActionLog]]

**Tables Written**
- [[OT_ActionLog]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
