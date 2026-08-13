---
type: procedure
database: Olives_BO
name: Rpt_SalesAndCollectionTargetByLocation
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[Customers]]
  - Fun_GetCompanyBranchesByUser
  - [[Locations]]
  - [[Receipts]]
  - [[SalesPersonCollectionsTargets]]
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
# Rpt_SalesAndCollectionTargetByLocation


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Fun_GetCompanyBranchesByUser, Locations, Receipts, SalesPersonCollectionsTargets, SalesPersonTargets, SalesPersonTargetsDetails, SalesPersons, SalesPersonsGroups, TargetsReferences, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromSalesman int = 3003
- @ToSalesman int = 3003
- @FromLocation int = 1
- @ToLocation int = 9999
- @Year smallint = 2019
- @FromMonth smallint = 1
- @ToMonth smallint= 12
- @FromGroup int = 0
- @ToGroup int = 99999
- @UserID nvarchar(50)='admin'
## Tables Read
- [[Customers]]
- Fun_GetCompanyBranchesByUser
- [[Locations]]
- [[Receipts]]
- [[SalesPersonCollectionsTargets]]
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
- [[Customers]]
- Fun_GetCompanyBranchesByUser
- [[Locations]]
- [[Receipts]]
- [[SalesPersonCollectionsTargets]]
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
