---
type: procedure
database: Olives_BO
name: Rpt_CustomersSalesDetails
schema: dbo
tags: [#backoffice, #customer, #reporting, #sales]
reads_from:
  - [[CompanyBranches]]
  - [[Customers]]
  - [[CustomersTypes]]
  - Fun_GetCompanyBranchesByUser
  - [[Items]]
  - [[ItemsCategories]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[TransactionsTypes]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomersSalesDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CompanyBranches, Customers, CustomersTypes, Fun_GetCompanyBranchesByUser, Items, ItemsCategories, SalesPersons, TransactionsDetails, TransactionsHeaders, TransactionsTypes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = 1
- @FromDate smalldatetime = '2017-01-01'
- @ToDate smalldatetime = '2017-11-29'
- @FromItem nvarchar(100) = '0'
- @ToItem nvarchar(100) = 'zzzzz'
- @FromCategCode nvarchar(100) = '0'
- @ToCategCode nvarchar(100) = 'zzzzz'
- @UserID nvarchar(50) = 'admin'
## Tables Read
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersTypes]]
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsCategories]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersTypes]]
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsCategories]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]

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
