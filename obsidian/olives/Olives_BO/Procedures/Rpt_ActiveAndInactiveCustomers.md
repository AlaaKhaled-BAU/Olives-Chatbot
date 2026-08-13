---
type: procedure
database: Olives_BO
name: Rpt_ActiveAndInactiveCustomers
schema: dbo
tags: [#backoffice, #customer, #reporting]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Fun_GetCompanyBranchesByUser
  - Fun_GetPositionCustomersRoutesCount
  - [[OrdersHeaders]]
  - [[Positions]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_ActiveAndInactiveCustomers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, CustomersFinancialDetails, Fun_GetCompanyBranchesByUser, Fun_GetPositionCustomersRoutesCount, OrdersHeaders, Positions, SalesPersons, SalesPersonsRoutes, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromCust bigint
- @ToCust bigint
- @FromDate smallDateTime
- @ToDate smallDateTime
- @FromSalesman int
- @ToSalesman int
- @UserID nvarchar(50)=null
- @cmdType varchar(50)=null
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetCompanyBranchesByUser
- Fun_GetPositionCustomersRoutesCount
- [[OrdersHeaders]]
- [[Positions]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetCompanyBranchesByUser
- Fun_GetPositionCustomersRoutesCount
- [[OrdersHeaders]]
- [[Positions]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
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
