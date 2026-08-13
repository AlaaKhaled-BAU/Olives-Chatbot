---
type: procedure
database: Olives_BO
name: Pro_TargetsReferences
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[TargetsReferences]]
writes_to:
  - [[TargetsReferences]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_TargetsReferences


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads TargetsReferences. Writes TargetsReferences. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID smallint = null
- @IsFocusItems bit = null
- @Name nvarchar (200)=null
- @ShortName nvarchar (100)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @cmdType varchar(50)=null
## Tables Read
- [[TargetsReferences]]
## Tables Written
- [[TargetsReferences]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[TargetsReferences]]

**Tables Written**
- [[TargetsReferences]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
