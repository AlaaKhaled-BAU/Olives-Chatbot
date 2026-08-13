---
type: procedure
database: Olives_BO
name: Pro_DevicesInfo
schema: dbo
tags: [#backoffice]
reads_from:
  - [[DevicesInfo]]
  - `dbo`
writes_to:
  - [[DevicesInfo]]
  - DevicesInfoLog
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_DevicesInfo


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads DevicesInfo, dbo. Writes DevicesInfo, DevicesInfoLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	= null
- @AutoID	numeric(30, 0)	= null
- @DeviceName	nvarchar(100)	= null
- @MacAddress	nvarchar(200)	= null
- @CreateDate	smalldatetime	= null
- @IsSuspended	bit	= null
- @Reference1	nvarchar(100)	= null
- @Reference2	nvarchar(100)	= null
- @cmdType nvarchar(50) = null
- @UserID varchar(50)=null
- @MacAddressLog nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
## Tables Read
- [[DevicesInfo]]
- `dbo`
## Tables Written
- [[DevicesInfo]]
- DevicesInfoLog
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[DevicesInfo]]
- dbo

**Tables Written**
- [[DevicesInfo]]
- DevicesInfoLog

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
