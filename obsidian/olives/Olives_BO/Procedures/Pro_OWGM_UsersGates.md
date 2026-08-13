---
type: procedure
database: Olives_BO
name: Pro_OWGM_UsersGates
schema: dbo
tags: [#auth, #backoffice]
reads_from:
  - [[OWGM_GatesUsers]]
writes_to:
  - [[OWGM_GatesUsers]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_OWGM_UsersGates


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OWGM_GatesUsers. Writes OWGM_GatesUsers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @GateID int = null
- @GateUserID int = null
- @GateUserName nvarchar (200)=null
- @MacAddress nvarchar (500)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @IsSuspended bit =null
- @DevicePassword varchar(40)=null
- @cmdType varchar(50)=null
- @AllowDelivery bit= null
- @AllowPrepare bit= null
## Tables Read
- [[OWGM_GatesUsers]]
## Tables Written
- [[OWGM_GatesUsers]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OWGM_GatesUsers]]

**Tables Written**
- [[OWGM_GatesUsers]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
