---
type: procedure
database: Olives_BO
name: Rpt_ItemsNotSold
schema: dbo
tags: [#backoffice, #inventory, #reporting]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Fun_GetCustomersByLocations
  - [[Items]]
  - [[ItemsCategories]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_ItemsNotSold


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, Fun_GetCustomersByLocations, Items, ItemsCategories, SalesPersonItemsAssignment, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int=290
- @SelectedIDs varchar(MAX)=''34,35,''
- @FromSalesMan int=99
- @ToSalesMan int=115
- @FromItemCateg VARCHAR(20)=''1''
- @ToItemCateg VARCHAR(20)=''9''
- @FromItemNo VARCHAR(100) = N''?}12400101138029''
- @ToItemNo VARCHAR(100)=N''RRR2023102450243''
- @FromDate smalldatetime=''2026-01-01 00:00:00''
- @ToDate smalldatetime=''2026-04-20 00:00:00''
- @MaxLevel int =100
- @RptType int = 1 ,  --1=ByItem -- 2 = ByCust
- @UserID nvarchar(50) = N''admin''
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetCustomersByLocations
- [[Items]]
- [[ItemsCategories]]
- [[SalesPersonItemsAssignment]]
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
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetCustomersByLocations
- [[Items]]
- [[ItemsCategories]]
- [[SalesPersonItemsAssignment]]
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
