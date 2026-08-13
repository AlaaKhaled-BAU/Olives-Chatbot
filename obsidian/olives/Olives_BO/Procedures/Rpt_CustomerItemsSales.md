---
type: procedure
database: Olives_BO
name: Rpt_CustomerItemsSales
schema: dbo
tags: [#backoffice, #customer, #inventory, #reporting, #sales]
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
# Rpt_CustomerItemsSales


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersTypes, Fun_GetCompanyBranchesByUser, Items, ItemsCategories, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromCustType int
- @ToCustType int
- @FromCateg nvarchar(100)
- @ToCateg nvarchar(100)
- @FromItemNo nvarchar(100)
- @ToItemNo nvarchar(100)
- @FromDate smalldatetime
- @ToDate smalldatetime
- @UserID nvarchar(50)=null
- @FromSalesman int
- @ToSalesman int
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
