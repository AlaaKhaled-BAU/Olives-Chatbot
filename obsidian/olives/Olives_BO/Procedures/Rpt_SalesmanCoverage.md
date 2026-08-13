---
type: procedure
database: Olives_BO
name: Rpt_SalesmanCoverage
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - Fun_GetCustomerActualVisitsCount
  - Fun_GetCustomerCount
  - Fun_GetOrdersCount
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanCoverage


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetCustomerActualVisitsCount, Fun_GetCustomerCount, Fun_GetOrdersCount, SalesPersons, SalesPersonsGroups. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @FromDate nvarchar(50)='2023-12-10'
- @ToDate nvarchar(50)='2023-12-10'
- @FromSalespersonsID int=1
- @ToSalespersonsID int=99999
- @FromSalesmanGroup int=1
- @ToSalesmanGroup int=99999
## Tables Read
- Fun_GetCustomerActualVisitsCount
- Fun_GetCustomerCount
- Fun_GetOrdersCount
- [[SalesPersons]]
- [[SalesPersonsGroups]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Fun_GetCustomerActualVisitsCount
- Fun_GetCustomerCount
- Fun_GetOrdersCount
- [[SalesPersons]]
- [[SalesPersonsGroups]]

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
