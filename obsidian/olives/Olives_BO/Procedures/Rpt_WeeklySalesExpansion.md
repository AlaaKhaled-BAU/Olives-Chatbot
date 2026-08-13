---
type: procedure
database: Olives_BO
name: Rpt_WeeklySalesExpansion
schema: dbo
tags: [#backoffice, #reporting, #sales]
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
# Rpt_WeeklySalesExpansion


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Fun_GetCompanyBranchesByUser, Items, ItemsCategories, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint =1
- @Year smallint = 2016
- @Month smallint = 12
- @FromCustomer bigint =0
- @ToCustomer bigint=999999999
- @FromSalesman int=0
- @ToSalesman int=999999999
- @FromCateg nvarchar(20)='0'
- @ToCateg nvarchar(20) ='zzzzzzzzz'
- @FromCustType int =0
- @ToCustType int=999999999
- @FromItemNo nvarchar(100)='0'
- @ToItemNo nvarchar(100)='zzzzzzzzz' , @UserID nvarchar(50)='admin'
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
