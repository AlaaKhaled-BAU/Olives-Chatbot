---
type: procedure
database: Olives_BO
name: Pro_Vacations
schema: dbo
tags: [#backoffice]
reads_from:
  - [[SystemCodes]]
  - [[Vacations]]
writes_to:
  - [[Vacations]]
called_by:
  - [[WF_AddWorkFlowLevelOne]]
support_relevance: high
last_verified: 2026-07-05
---
# Pro_Vacations


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SystemCodes, Vacations. Writes Vacations. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @CmdType nvarchar(200)='SelectAll'
- @SalesmanNo int=null
- @VacType nvarchar(50)=null
- @FromDate smalldatetime=null
- @ToDate smalldatetime=null
- @Notes nvarchar(300) = null
## Tables Read
- [[SystemCodes]]
- [[Vacations]]
## Tables Written
- [[Vacations]]
## Callers
_None (no known callers)_
## Callees
- [[WF_AddWorkFlowLevelOne]]
## Impact / Dependencies

**Tables Read**
- [[SystemCodes]]
- [[Vacations]]

**Tables Written**
- [[Vacations]]

**Callers**
- [[WF_AddWorkFlowLevelOne]]

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
