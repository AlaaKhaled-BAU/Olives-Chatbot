---
type: procedure
database: Olives_BO
name: Niroukh_VSQ
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
# Niroukh_VSQ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetCompanyBranchesByUser, GetInvoiceTotalsByItemWithYear, Items, SalesPersonTargets, SalesPersonTargetsDetails, SalesPersons, TargetsReferences. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 2
- @FromSalesman int = 16
- @ToSalesman int = 16
- @Year smallint = 2024
- @UserID nvarchar(50)='admin'
- @Byamount bit =1
- @FromTargetReferenceID int=66
- @ToTargetReferenceID int=66
- @AchievementType Bit=1
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
