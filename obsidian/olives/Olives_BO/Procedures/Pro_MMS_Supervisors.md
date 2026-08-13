---
type: procedure
database: Olives_BO
name: Pro_MMS_Supervisors
schema: dbo
tags: [#backoffice, #mms]
reads_from:
  - [[MMS_Supervisors]]
  - smalldatetime
writes_to:
  - [[MMS_Supervisors]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_Supervisors


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_Supervisors, smalldatetime. Writes MMS_Supervisors. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	int = null
- @SupervisorID	int	= null
- @Name	nvarchar(100)	= null
- @ForeignName	nvarchar(100)	= null
- @Reference1	nvarchar(100)	= null
- @Reference2	nvarchar(100)	= null
- @IsSuspended	bit	= null
- @MobileNo	nvarchar(500)	= null
- @Email	nvarchar(500)	= null
- @DayOff	nvarchar(100)	= null
- @TimeWorkFrom	smalldatetime	= null
- @TimeWorkTo	smalldatetime	= null
- @cmdType varchar(100) = null
- @UserID nvarchar(50) = null
## Tables Read
- [[MMS_Supervisors]]
- smalldatetime
## Tables Written
- [[MMS_Supervisors]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_Supervisors]]
- smalldatetime

**Tables Written**
- [[MMS_Supervisors]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
