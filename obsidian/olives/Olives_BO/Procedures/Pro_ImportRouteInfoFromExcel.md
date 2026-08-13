---
type: procedure
database: Olives_BO
name: Pro_ImportRouteInfoFromExcel
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - [[BusinessUnits]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[Excel]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
  - [[Technical_CFD_temp]]
  - UpdateCustomerFin
  - UpdateCustomerFin_2
writes_to:
  - [[Excel]]
called_by:
  - [[Technical_CreateRouteBasedonID]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Route-Planning
---
# Pro_ImportRouteInfoFromExcel


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BusinessUnits, Customers, CustomersFinancialDetails, Excel, RoutesInformation, SalesPersons, SalesPersonsRoutes, Technical_CFD_temp, UpdateCustomerFin, UpdateCustomerFin_2. Writes Excel. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- [[BusinessUnits]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Excel]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[Technical_CFD_temp]]
- UpdateCustomerFin
- UpdateCustomerFin_2
## Tables Written
- [[Excel]]
## Callers
_None (no known callers)_
## Callees
- [[Technical_CreateRouteBasedonID]]
## Impact / Dependencies

**Tables Read**
- [[BusinessUnits]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Excel]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[Technical_CFD_temp]]
- UpdateCustomerFin
- UpdateCustomerFin_2

**Tables Written**
- [[excel]]

**Callers**
- [[Technical_CreateRouteBasedonID]]

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
