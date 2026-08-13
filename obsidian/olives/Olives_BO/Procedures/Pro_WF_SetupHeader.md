---
type: procedure
database: Olives_BO
name: Pro_WF_SetupHeader
schema: dbo
tags: [#auth, #backoffice, #workflow]
reads_from:
  - [[Positions]]
  - [[SalesPersonsGroups]]
  - [[WF_Functions]]
  - [[WF_SetupHeader]]
writes_to:
  - [[WF_SetupHeader]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_WF_SetupHeader


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Positions, SalesPersonsGroups, WF_Functions, WF_SetupHeader. Writes WF_SetupHeader. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @AutoID bigint = null
- @CompanyID smallint=null
- @FromType smallint = null
- @FromID bigint=null
- @FunctionID smallint=null
- @LevelCount tinyint = null
- @IsSuspended bit = null
- @cmdType varchar(50)=null
## Tables Read
- [[Positions]]
- [[SalesPersonsGroups]]
- [[WF_Functions]]
- [[WF_SetupHeader]]
## Tables Written
- [[WF_SetupHeader]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Positions]]
- [[SalesPersonsGroups]]
- [[WF_Functions]]
- [[WF_SetupHeader]]

**Tables Written**
- [[WF_SetupHeader]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
