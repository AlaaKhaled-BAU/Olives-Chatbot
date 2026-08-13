---
type: procedure
database: Olives_BO
name: Pro_UserCompanyBranchesLink
schema: dbo
tags: [#auth, #backoffice]
reads_from:
  - [[CompanyBranches]]
  - [[UserCompanyBranchesLink]]
  - [[Users]]
  - int
writes_to:
  - [[UserCompanyBranchesLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_UserCompanyBranchesLink


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CompanyBranches, UserCompanyBranchesLink, Users, int. Writes UserCompanyBranchesLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @UserID nvarchar(50)=null
- @UserName nvarchar(100)=null
- @CompanyBrancheID int=null
- @HavePermission bit=null
- @IsSuspended bit=null
- @CopyFrom int = null
- @cmdType varchar(50) = null
## Tables Read
- [[CompanyBranches]]
- [[UserCompanyBranchesLink]]
- [[Users]]
- int
## Tables Written
- [[UserCompanyBranchesLink]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CompanyBranches]]
- [[UserCompanyBranchesLink]]
- [[Users]]
- int

**Tables Written**
- [[UserCompanyBranchesLink]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
