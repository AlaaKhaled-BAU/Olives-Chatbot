---
type: procedure
database: Olives_BO
name: Rpt_AnnualTargetAnalysis
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - Fun_GetCompanyBranchesByUser
  - Fun_GetSalesmanTreeBySalemanType
  - [[Items]]
  - [[SalesPersonTargets]]
  - [[SalesPersonTargetsDetails]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[TargetsReferences]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_AnnualTargetAnalysis


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetCompanyBranchesByUser, Fun_GetSalesmanTreeBySalemanType, Items, SalesPersonTargets, SalesPersonTargetsDetails, SalesPersons, SalesPersonsGroups, TargetsReferences, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromSalesman int
- @ToSalesman int
- @Year smallint
- @FromMonth smallint
- @ToMonth smallint
- @SalesmanType int
- @FromGroup int = 0
- @ToGroup int = 99999999
- @UserID nvarchar(50)=null
- @IsMainTarget smallint = 1
## Tables Read
- Fun_GetCompanyBranchesByUser
- Fun_GetSalesmanTreeBySalemanType
- [[Items]]
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TargetsReferences]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Fun_GetCompanyBranchesByUser
- Fun_GetSalesmanTreeBySalemanType
- [[Items]]
- [[SalesPersonTargets]]
- [[SalesPersonTargetsDetails]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TargetsReferences]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

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
