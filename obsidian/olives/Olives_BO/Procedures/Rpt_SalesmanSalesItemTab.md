---
type: procedure
database: Olives_BO
name: Rpt_SalesmanSalesItemTab
schema: dbo
tags: [#backoffice, #inventory, #reporting, #sales]
reads_from:
  - Fun_GetCompanyBranchesByUser
  - Fun_GetSalesmanTotalSales
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
# Rpt_SalesmanSalesItemTab


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetCompanyBranchesByUser, Fun_GetSalesmanTotalSales, Items, ItemsCategories, OrdersDetails, OrdersHeaders, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromDate smalldatetime = '2017-01-01'
- @ToDate smalldatetime = '2018-06-05'
- @FromSalesmanNo int = 0
- @ToSalesmanNo int = 999999
- @FromCateg nvarchar(50) = '0'
- @ToCateg nvarchar(50) = 'zzzzz'
- @FromItem nvarchar(100) = '0'
- @ToItem nvarchar(100) = 'zzzzz'
- @UserID nvarchar(50) = 'admin'
- @WithInvoice int = 1
- @WithOrder int = 1
## Tables Read
- Fun_GetCompanyBranchesByUser
- Fun_GetSalesmanTotalSales
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
- Fun_GetCompanyBranchesByUser
- Fun_GetSalesmanTotalSales
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
