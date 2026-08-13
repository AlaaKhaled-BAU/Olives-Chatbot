---
type: procedure
database: Olives_BO
name: Rpt_SalesmanOrdersSummaryByCategory
schema: dbo
tags: [#backoffice, #order, #reference, #reporting, #sales]
reads_from:
  - Fun_GetCompanyBranchesByUser
  - [[Items]]
  - [[ItemsCategories]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanOrdersSummaryByCategory


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetCompanyBranchesByUser, Items, ItemsCategories, OrdersDetails, OrdersHeaders, SalesPersons, SalesPersonsGroups. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromDate smalldatetime = '2018-01-01'
- @ToDate smalldatetime = '2018-03-19'
- @FromSalesman int = 0
- @ToSalesman int = 99999999
- @FromCateg nvarchar(50) = '0'
- @ToCateg nvarchar(50) = 'zzzzzzzzzz'
- @FromGroup int = NULL
- @ToGroup int = NULL
- @UserID  nvarchar(50) = 'admin'
## Tables Read
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsCategories]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
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
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsCategories]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
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
