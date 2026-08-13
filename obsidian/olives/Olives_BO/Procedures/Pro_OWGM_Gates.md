---
type: procedure
database: Olives_BO
name: Pro_OWGM_Gates
schema: dbo
tags: [#backoffice]
reads_from:
  - [[OWGM_Gates]]
writes_to:
  - [[OWGM_Gates]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_OWGM_Gates


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OWGM_Gates. Writes OWGM_Gates. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @GateID int = null
- @GateName nvarchar (200)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @IsWorking bit =null
- @cmdType varchar(50)=null
## Tables Read
- [[OWGM_Gates]]
## Tables Written
- [[OWGM_Gates]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OWGM_Gates]]

**Tables Written**
- [[OWGM_Gates]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
