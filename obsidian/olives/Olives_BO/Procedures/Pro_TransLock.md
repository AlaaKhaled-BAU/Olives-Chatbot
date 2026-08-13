---
type: procedure
database: Olives_BO
name: Pro_TransLock
schema: dbo
tags: [#backoffice]
reads_from:
  - [[BusinessUnits]]
  - [[CompanyBranches]]
  - [[Notifications]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
writes_to:
  - [[Notifications]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_TransLock


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BusinessUnits, CompanyBranches, Notifications, SalesPersons, SalesPersonsGroups. Writes Notifications. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @SalesmanNo int=null
- @TrDateTime datetime = null
- @GroupID int  = null
- @cmdType varchar(50)=null
- @TransLock_Type_DATATABLE TransLock_Type2  readonly
## Tables Read
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Notifications]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
## Tables Written
- [[Notifications]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[BusinessUnits]]
- [[CompanyBranches]]
- [[Notifications]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]

**Tables Written**
- [[Notifications]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
