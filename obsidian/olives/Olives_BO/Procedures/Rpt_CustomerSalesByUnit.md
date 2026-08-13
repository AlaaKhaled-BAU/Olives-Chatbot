---
type: procedure
database: Olives_BO
name: Rpt_CustomerSalesByUnit
schema: dbo
tags: [#backoffice, #customer, #inventory, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Fun_GetCompanyBranchesByUser
  - [[Items]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomerSalesByUnit


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, Fun_GetCompanyBranchesByUser, Items, ItemsUnits, ItemsUnitsDetails, RoutesInformation, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @FromItem varchar(100) = null
- @ToItem varchar(100) = null
- @FromCustomer bigint = null
- @ToCustomer bigint = null
- @FromType int = null
- @ToType int = null
- @FromRoute int= null
- @ToRoute int= null
- @FromDate smalldatetime = null
- @ToDate smalldatetime = null
- @UserID nvarchar(50)=null
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[RoutesInformation]]
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
- Fun_GetCompanyBranchesByUser
- [[Items]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[RoutesInformation]]
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
