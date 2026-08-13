---
type: procedure
database: Olives_BO
name: Pro_WF_SetupDetails
schema: dbo
tags: [#auth, #backoffice, #workflow]
reads_from:
  - [[WF_SetupDetails]]
writes_to:
  - [[WF_SetupDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_WF_SetupDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads WF_SetupDetails. Writes WF_SetupDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @AutoID bigint = null
- @LevelID tinyint =null
- @SalesPersonType int=null
- @SetupValue float = null
- @IsFinalApprove bit = null
- @cmdType varchar(50)=null
## Tables Read
- [[WF_SetupDetails]]
## Tables Written
- [[WF_SetupDetails]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[WF_SetupDetails]]

**Tables Written**
- [[WF_SetupDetails]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
