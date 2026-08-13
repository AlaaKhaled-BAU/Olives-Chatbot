---
type: procedure
database: Olives_BO
name: Rpt_SalesTargetByCustCount_Telegraph
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Fun_GetSalesmanTreeByID
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsPriority]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
  - [[SalespersonCustStockItemsTargetLink]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesTargetByCustCount_Telegraph


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, Fun_GetSalesmanTreeByID, Items, ItemsCategories, ItemsPriority, SalesPersons, SalesPersonsRoutes, SalespersonCustStockItemsTargetLink, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int=1
- @SalesmanNo int=205
- @FromDate smalldatetime='2024-1-1'
- @ToDate smalldatetime='2024-5-8'
- @FromCateg Varchar(1000)='0'
- @ToCateg Varchar(1000)='zzzzzzzzzzz'
- @customertype bigint= 33
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetSalesmanTreeByID
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriority]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[SalespersonCustStockItemsTargetLink]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetSalesmanTreeByID
- [[Items]]
- [[ItemsCategories]]
- [[ItemsPriority]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[SalespersonCustStockItemsTargetLink]]
- dbo

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
