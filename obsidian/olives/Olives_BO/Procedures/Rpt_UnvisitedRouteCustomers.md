---
type: procedure
database: Olives_BO
name: Rpt_UnvisitedRouteCustomers
schema: dbo
tags: [#backoffice, #customer, #gps, #reporting, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Fun_GetCompanyBranchesByUser
  - [[LogActionTransaction]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_UnvisitedRouteCustomers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, CustomersFinancialDetails, Fun_GetCompanyBranchesByUser, LogActionTransaction, RoutesInformation, SalesPersons. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
- @SalespersonID int = 3003
- @Date smalldatetime ='2025-01-24'
- @UserID nvarchar(50)=null
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetCompanyBranchesByUser
- [[LogActionTransaction]]
- [[RoutesInformation]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
- [[Rpt_UnvisitedRouteCustomers_FromDateToDate]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetCompanyBranchesByUser
- [[LogActionTransaction]]
- [[RoutesInformation]]
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
- [[Rpt_UnvisitedRouteCustomers_FromDateToDate]]


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
