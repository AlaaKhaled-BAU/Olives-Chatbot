---
type: procedure
database: Olives_BO
name: Pro_MMS_DevicesInfo
schema: dbo
tags: [#backoffice, #mms]
reads_from:
  - Level
  - [[MMS_DevicesInfo]]
writes_to:
  - Level
  - [[MMS_DevicesInfo]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_DevicesInfo


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Level, MMS_DevicesInfo. Writes Level, MMS_DevicesInfo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	= null
- @DeviceID	int	= null
- @Parent	int	= null
- @Name	nvarchar(500)	= null
- @ForeignName	nvarchar(500)	= null
- @DeviceLevel	int	= null
- @Reference1	nvarchar(100)	= null
- @Reference2	nvarchar(100)	= null
- @IsSuspended	bit	= null
- @Size	nvarchar(100)	= null
- @Color	nvarchar(100)	= null
- @UseSerialNo	bit	= null
- @cmdType varchar(50)=null
## Tables Read
- Level
- [[MMS_DevicesInfo]]
## Tables Written
- Level
- [[MMS_DevicesInfo]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Level
- [[MMS_DevicesInfo]]

**Tables Written**
- Level
- [[MMS_DevicesInfo]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
