---
type: procedure
database: Olives_BO
name: Rpt_SalesmanOrders
schema: dbo
tags: [#backoffice, #order, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersTypes]]
  - Fun_GetCompanyBranchesByUser
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, CustomersTypes, Fun_GetCompanyBranchesByUser, OrdersDetails, OrdersHeaders, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromSalesman int
- @ToSalesman int
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromCust bigint
- @Tocust bigint
- @FromCustType int
- @ToCustType int
- @UserID nvarchar(50)=null
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersTypes]]
- Fun_GetCompanyBranchesByUser
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
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
- [[CustomersTypes]]
- Fun_GetCompanyBranchesByUser
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]

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
