---
type: procedure
database: Olives_BO
name: Pro_LastSalesmenTransactionsDateTime
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[CompanyBranches]]
  - Fun_GetCompanyBranchesByUser
  - [[SalesPersons]]
  - from
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_LastSalesmenTransactionsDateTime


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CompanyBranches, Fun_GetCompanyBranchesByUser, SalesPersons, from. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @companyid int =1
- @userid nvarchar(20) ='admin'
- @FromSalesman int=1
- @ToSalesman int=99999
## Tables Read
- [[CompanyBranches]]
- Fun_GetCompanyBranchesByUser
- [[SalesPersons]]
- from
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CompanyBranches]]
- Fun_GetCompanyBranchesByUser
- [[Salespersons]]
- from

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
