---
type: procedure
database: Olives_BO
name: Rpt_CustomerItemsYearlySales
schema: dbo
tags: [#backoffice, #customer, #inventory, #reporting, #sales]
reads_from:
  - [[Customers]]
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
# Rpt_CustomerItemsYearlySales


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Fun_GetCompanyBranchesByUser, Items, ItemsCategories, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromYear smallint
- @ToYear smallint
- @FromItem varchar
- @ToItem varchar(100)
- @FromCustomer bigint
- @ToCustomer bigint
- @FromSalesman int
- @ToSalesman int
- @FromCateg nvarchar(20)
- @ToCateg nvarchar(20)
- @FromCustType int
- @ToCustType int
- @UserID nvarchar(50)
## Tables Read
- [[Customers]]
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
