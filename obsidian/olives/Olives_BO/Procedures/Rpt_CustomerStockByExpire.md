---
type: procedure
database: Olives_BO
name: Rpt_CustomerStockByExpire
schema: dbo
tags: [#backoffice, #customer, #inventory, #reporting]
reads_from:
  - [[CustomerStockTacking]]
  - [[CustomerStockTackingDetails]]
  - [[Customers]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[SalesPersons]]
  - [[TransactionsBatchsItemsInfo]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomerStockByExpire


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerStockTacking, CustomerStockTackingDetails, Customers, Items, ItemsCategories, SalesPersons, TransactionsBatchsItemsInfo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromSalesmanNo int = 0
- @ToSalesmanNo int= 9999
- @FromCustomerNo bigint= 0
- @ToCustomerNo bigint= 9999999999999
- @FromDate smalldatetime = '2019-08-22'
- @ToDate smalldatetime = '2019-08-22'
- @FromParent nvarchar(100) ='0'
- @ToParent nvarchar(100) ='zzzzz'
- @FromCateg nvarchar(100) ='0'
- @ToCateg nvarchar(100) ='zzzzz'
## Tables Read
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Customers]]
- [[Items]]
- [[ItemsCategories]]
- [[SalesPersons]]
- [[TransactionsBatchsItemsInfo]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Customers]]
- [[Items]]
- [[ItemsCategories]]
- [[SalesPersons]]
- [[TransactionsBatchsItemsInfo]]

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
