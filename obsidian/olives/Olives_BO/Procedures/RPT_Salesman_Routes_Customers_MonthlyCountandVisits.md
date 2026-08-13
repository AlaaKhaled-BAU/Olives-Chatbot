---
type: procedure
database: Olives_BO
name: RPT_Salesman_Routes_Customers_MonthlyCountandVisits
schema: dbo
tags: [#backoffice, #customer, #gps, #reporting, #sales]
reads_from:
  - [[CustomersFinancialDetails]]
  - Fun_GetCustomersRouteByDate
  - [[LogActionTransaction]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-07-05
---
# RPT_Salesman_Routes_Customers_MonthlyCountandVisits


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails, Fun_GetCustomersRouteByDate, LogActionTransaction, RoutesInformation, SalesPersons, SalesPersonsRoutes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @compno int
## Tables Read
- [[CustomersFinancialDetails]]
- Fun_GetCustomersRouteByDate
- [[LogActionTransaction]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomersFinancialDetails]]
- Fun_GetCustomersRouteByDate
- [[LogActionTransaction]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[salespersonsroutes]]

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
