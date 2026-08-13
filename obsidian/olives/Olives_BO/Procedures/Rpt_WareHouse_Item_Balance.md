---
type: procedure
database: Olives_BO
name: Rpt_WareHouse_Item_Balance
schema: dbo
tags: [#backoffice, #inventory, #reporting]
reads_from:
  - [[ClientsActive]]
  - Fun_GetCompanyBranchesByUser
  - Fun_GetItemOpenBalBySalesman
  - Fun_GetItemOpenBalBySalesman_DefafCo1
  - Fun_GetItemOpenBalBySalesman_DefafCo11
  - Fun_GetItemOpenBalBySalesman_DefafCo3
  - [[Items]]
  - [[ItemsCategories]]
  - [[SalesPersons]]
  - Table_6
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[TransactionsTypes]]
  - [[TransfersOrdersDetails]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_WareHouse_Item_Balance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Fun_GetCompanyBranchesByUser, Fun_GetItemOpenBalBySalesman, Fun_GetItemOpenBalBySalesman_DefafCo1, Fun_GetItemOpenBalBySalesman_DefafCo11, Fun_GetItemOpenBalBySalesman_DefafCo3, Items, ItemsCategories, SalesPersons, Table_6, TransactionsDetails, TransactionsHeaders, TransactionsTypes, TransfersOrdersDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromSalesPerson int = 1
- @ToSalesPerson int = 3003
- @FromDate smalldatetime = '2022-08-30'
- @ToDate smalldatetime = '2022-08-30'
- @FromItem nvarchar(100) = '0'
- @ToItem nvarchar(100) = 'zzzzzzzzzz'
- @FromCateg nvarchar(20) = '0'
- @ToCateg nvarchar(20) = 'zzzzzzzzzz' , @UserID nvarchar(50)='admin'
## Tables Read
- [[ClientsActive]]
- Fun_GetCompanyBranchesByUser
- Fun_GetItemOpenBalBySalesman
- Fun_GetItemOpenBalBySalesman_DefafCo1
- Fun_GetItemOpenBalBySalesman_DefafCo11
- Fun_GetItemOpenBalBySalesman_DefafCo3
- [[Items]]
- [[ItemsCategories]]
- [[SalesPersons]]
- Table_6
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]
- [[TransfersOrdersDetails]]
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
- Fun_GetItemOpenBalBySalesman
- Fun_GetItemOpenBalBySalesman_DefafCo1
- Fun_GetItemOpenBalBySalesman_DefafCo11
- Fun_GetItemOpenBalBySalesman_DefafCo3
- [[Items]]
- [[ItemsCategories]]
- [[SalesPersons]]
- Table_6
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]
- [[TransfersOrdersDetails]]

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
