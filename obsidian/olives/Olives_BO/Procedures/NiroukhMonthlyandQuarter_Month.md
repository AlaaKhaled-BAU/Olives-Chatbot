---
type: procedure
database: Olives_BO
name: NiroukhMonthlyandQuarter_Month
schema: dbo
tags: [#backoffice]
reads_from:
  - Fun_GetCompanyBranchesByUser
  - GetInvoiceTotalsByItemWithYear
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
# NiroukhMonthlyandQuarter_Month


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetCompanyBranchesByUser, GetInvoiceTotalsByItemWithYear, Items, SalesPersonTargets, SalesPersonTargetsDetails, SalesPersons, TargetsReferences. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromSalesman int = 1
- @ToSalesman int = 9999
- @Year smallint = 2024
- @Month smallint =1
- @UserID nvarchar(50)='admin'
- @quarter int=1
- @Byamount bit=1
- @AchievementType int=1
## Tables Read
- Fun_GetCompanyBranchesByUser
- GetInvoiceTotalsByItemWithYear
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
- GetInvoiceTotalsByItemWithYear
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
