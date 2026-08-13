---
type: procedure
database: Olives_BO
name: Rpt_SalesmanSalesByTotalCategory
schema: dbo
tags: [#backoffice, #reference, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - Fun_GetCompanyBranchesByUser
  - [[Items]]
  - [[ItemsCategories]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanSalesByTotalCategory


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Fun_GetCompanyBranchesByUser, Items, ItemsCategories, OrdersDetails, OrdersHeaders, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromSalesman int
- @ToSalesman int
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromCateg nvarchar(50) ='0'
- @ToCateg nvarchar(50)='zzzzzz'
- @UserID nvarchar(50)
- @SalesmanType int=5
- @OutputType int=3
## Tables Read
- [[ClientsActive]]
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsCategories]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
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
- [[ClientsActive]]
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsCategories]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
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
