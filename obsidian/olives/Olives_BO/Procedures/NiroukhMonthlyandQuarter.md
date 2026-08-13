---
type: procedure
database: Olives_BO
name: NiroukhMonthlyandQuarter
schema: dbo
tags: [#backoffice]
reads_from:
  - Fun_GetCompanyBranchesByUser
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - [[SalesPersonTargets]]
  - [[SalesPersonTargetsDetails]]
  - [[SalesPersons]]
  - [[TargetsReferences]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# NiroukhMonthlyandQuarter


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetCompanyBranchesByUser, InvoiceHistoryDF, InvoiceHistoryHF, Items, SalesPersonTargets, SalesPersonTargetsDetails, SalesPersons, TargetsReferences. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromSalesman int = 108
- @ToSalesman int = 108
- @Year smallint = 2023
- @Month smallint = 4
- @Quarter int = 1
- @UserID nvarchar(50)='admin'
- @AchievementType int=2
## Tables Read
- Fun_GetCompanyBranchesByUser
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[TargetsReferences]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Fun_GetCompanyBranchesByUser
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[TargetsReferences]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
