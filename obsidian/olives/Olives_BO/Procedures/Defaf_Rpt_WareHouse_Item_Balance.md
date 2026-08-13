---
type: procedure
database: Olives_BO
name: Defaf_Rpt_WareHouse_Item_Balance
schema: dbo
tags: [#backoffice, #inventory, #reporting]
reads_from:
  - [[ClientsActive]]
  - Fun_GetCompanyBranchesByUser
  - Fun_GetItemOpenBalBySalesman
  - Fun_GetItemOpenBalBySalesman_DefafCo1
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
# Defaf_Rpt_WareHouse_Item_Balance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Fun_GetCompanyBranchesByUser, Fun_GetItemOpenBalBySalesman, Fun_GetItemOpenBalBySalesman_DefafCo1, Items, ItemsCategories, SalesPersons, Table_6, TransactionsDetails, TransactionsHeaders, TransactionsTypes, TransfersOrdersDetails. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromSalesPerson int = 61
- @ToSalesPerson int = 61
- @FromDate smalldatetime = '2017-06-01'
- @ToDate smalldatetime = '2017-06-04'
- @FromItem nvarchar(100) = 'SD001240101'
- @ToItem nvarchar(100) = 'SD001240106'
- @FromCateg nvarchar(20) = '0'
- @ToCateg nvarchar(20) = 'zzzzzzzzzz' , @UserID nvarchar(50)='admin2'
## Tables Read
- [[ClientsActive]]
- Fun_GetCompanyBranchesByUser
- Fun_GetItemOpenBalBySalesman
- Fun_GetItemOpenBalBySalesman_DefafCo1
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
- [[Defaf_SalesmenItemQTY]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- Fun_GetCompanyBranchesByUser
- Fun_GetItemOpenBalBySalesman
- Fun_GetItemOpenBalBySalesman_DefafCo1
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
- [[Defaf_SalesmenItemQTY]]


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
