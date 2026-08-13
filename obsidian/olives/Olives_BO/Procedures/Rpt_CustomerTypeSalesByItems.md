---
type: procedure
database: Olives_BO
name: Rpt_CustomerTypeSalesByItems
schema: dbo
tags: [#backoffice, #customer, #inventory, #reference, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersTypes]]
  - Fun_GetCompanyBranchesByUser
  - [[Items]]
  - [[ItemsCategories]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomerTypeSalesByItems


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersTypes, Fun_GetCompanyBranchesByUser, Items, ItemsCategories, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromDate smalldatetime='2022-01-01'
- @ToDate smalldatetime='2025-01-01'
- @FromItemCategCode varchar(100)='0'
- @ToItemCategCode varchar(100)='zzzzzzzzzzz'
- @FromItem varchar(100)='0'
- @ToItem varchar(100)='zzzzzzzzzzz'
- @FromCustomerType int=1
- @ToCustomerType int=999999
- @FromSalesPerson int =1
- @ToSalesPerson int =99999
- @UserID nvarchar(50)='admin'
## Tables Read
- [[Customers]]
- [[CustomersTypes]]
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsCategories]]
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
- [[CustomersTypes]]
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsCategories]]
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
