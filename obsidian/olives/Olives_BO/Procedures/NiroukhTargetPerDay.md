---
type: procedure
database: Olives_BO
name: NiroukhTargetPerDay
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - Fun_GetCompanyBranchesByUser
  - Fun_GetWorkDays
  - GetInvoiceTotalsByItemWithYear_date
  - [[Items]]
  - [[SalesPersonTargets]]
  - [[SalesPersonTargetsDetails]]
  - [[SalesPersons]]
  - [[TargetsReferences]]
  - table
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# NiroukhTargetPerDay


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetCompanyBranchesByUser, Fun_GetWorkDays, GetInvoiceTotalsByItemWithYear_date, Items, SalesPersonTargets, SalesPersonTargetsDetails, SalesPersons, TargetsReferences, table. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 2
- @FromSalesman int = 16
- @ToSalesman int = 16
- @Year smallint = 2024
- @Month smallint = 1
- @ByAmount bit =1
- @UserID nvarchar(50)='admin'
- @AchievementType bit=1
## Tables Read
- Fun_GetCompanyBranchesByUser
- Fun_GetWorkDays
- GetInvoiceTotalsByItemWithYear_date
- [[Items]]
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[TargetsReferences]]
- table
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Fun_GetCompanyBranchesByUser
- Fun_GetWorkDays
- GetInvoiceTotalsByItemWithYear_date
- [[Items]]
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[TargetsReferences]]
- table

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
