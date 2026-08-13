---
type: procedure
database: Olives_BO
name: Pro_CompanyBranches
schema: dbo
tags: [#backoffice]
reads_from:
  - [[CompanyBranches]]
writes_to:
  - [[CompanyBranches]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CompanyBranches


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CompanyBranches. Writes CompanyBranches. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @ID smallint = null
- @Name nvarchar (200)=null
- @ShortName nvarchar (100)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @cmdType varchar(50)=null
- @Address nvarchar (300) = null
## Tables Read
- [[CompanyBranches]]
## Tables Written
- [[CompanyBranches]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CompanyBranches]]

**Tables Written**
- [[CompanyBranches]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
