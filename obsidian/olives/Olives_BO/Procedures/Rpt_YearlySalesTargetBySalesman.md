---
type: procedure
database: Olives_BO
name: Rpt_YearlySalesTargetBySalesman
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - AND
  - Fun_GetCompanyBranchesByUser
  - Fun_GetSalesmanTreeBySalemanType
  - [[SalesPersonTargets]]
  - [[SalesPersonTargetsDetails]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[TargetsReferences]]
  - int
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_YearlySalesTargetBySalesman


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AND, Fun_GetCompanyBranchesByUser, Fun_GetSalesmanTreeBySalemanType, SalesPersonTargets, SalesPersonTargetsDetails, SalesPersons, SalesPersonsGroups, TargetsReferences, int. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromSalesman int
- @ToSalesman int
- @FromTargetsReferences int
- @ToTargetsReferences int
- @TargetYear smallint
- @FromMonth smallint
- @ToMonth smallint
- @SalesmanType int
- @FromGroup int = 0
- @ToGroup int = 99999999
- @UserID nvarchar(50)=null
## Tables Read
- AND
- Fun_GetCompanyBranchesByUser
- Fun_GetSalesmanTreeBySalemanType
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TargetsReferences]]
- int
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- AND
- Fun_GetCompanyBranchesByUser
- Fun_GetSalesmanTreeBySalemanType
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TargetsReferences]]
- int

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
