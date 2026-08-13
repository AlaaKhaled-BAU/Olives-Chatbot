---
type: procedure
database: Olives_BO
name: Pro_Branches
schema: dbo
tags: [#backoffice]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - `dbo`
writes_to:
  - [[Branches]]
  - BranchesLog
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_Branches


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, dbo. Writes Branches, BranchesLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID smallint = null
- @BankID smallint = null
- @Name nvarchar (200)=null
- @ShortName nvarchar (100)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @AccountNumber nvarchar(50) = null
- @cmdType varchar(50)=null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @UserID nvarchar(100)=null
## Tables Read
- [[Banks]]
- [[Branches]]
- `dbo`
## Tables Written
- [[Branches]]
- BranchesLog
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- dbo

**Tables Written**
- [[Branches]]
- BranchesLog

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
