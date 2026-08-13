---
type: procedure
database: Olives_BO
name: Pro_Positions
schema: dbo
tags: [#backoffice]
reads_from:
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - Fun_GetCompanyBranchesByUser
  - [[Positions]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - `dbo`
writes_to:
  - [[Positions]]
  - PositionsLog
called_by:
support_relevance: high
last_verified: 2026-07-05
related_workflows: [[Company-Setup]], [[Salesman-Onboarding]]
---
# Pro_Positions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CompanyParameters, Fun_GetCompanyBranchesByUser, Positions, SalesPersons, SalesPersonsGroups, dbo. Writes Positions, PositionsLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID smallint = null
- @Name nvarchar (200)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (100)=null
- @cmdType varchar(50)=null
- @GroupID int=null
- @UserID varchar(50)=null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
## Tables Read
- [[ClientsActive]]
- [[CompanyParameters]]
- Fun_GetCompanyBranchesByUser
- [[Positions]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- `dbo`
## Tables Written
- [[Positions]]
- PositionsLog
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CompanyParameters]]
- Fun_GetCompanyBranchesByUser
- [[Positions]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- dbo

**Tables Written**
- [[Positions]]
- PositionsLog

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
