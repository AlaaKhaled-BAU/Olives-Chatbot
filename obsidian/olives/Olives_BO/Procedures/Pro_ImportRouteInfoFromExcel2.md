---
type: procedure
database: Olives_BO
name: Pro_ImportRouteInfoFromExcel2
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - [[BusinessUnits]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
  - UpdateCustomerFin
  - UpdateCustomerFin_2
writes_to:
  - [[CustomersFinancialDetails]]
  - [[RoutesInformation]]
  - [[SalesPersonsRoutes]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ImportRouteInfoFromExcel2


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BusinessUnits, Customers, CustomersFinancialDetails, RoutesInformation, SalesPersons, SalesPersonsRoutes, UpdateCustomerFin, UpdateCustomerFin_2. Writes CustomersFinancialDetails, RoutesInformation, SalesPersonsRoutes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- [[BusinessUnits]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- UpdateCustomerFin
- UpdateCustomerFin_2
## Tables Written
- [[CustomersFinancialDetails]]
- [[RoutesInformation]]
- [[SalesPersonsRoutes]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[BusinessUnits]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- UpdateCustomerFin
- UpdateCustomerFin_2

**Tables Written**
- [[CustomersFinancialDetails]]
- [[RoutesInformation]]
- [[SalesPersonsRoutes]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
