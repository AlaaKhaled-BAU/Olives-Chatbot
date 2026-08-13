---
type: procedure
database: Olives_BO
name: Technical_CreateRouteBasedonReference1_UpdateOnly
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - [[BusinessUnits]]
  - CTE
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[Excel]]
  - Non
  - Null
  - [[Positions]]
  - [[RoutesInformation]]
  - [[SalesPersonsRoutes]]
  - Section
  - [[Technical_CFD_temp]]
  - UpdateCustomerFin
  - after
writes_to:
  - [[CustomersFinancialDetails]]
  - [[Positions]]
  - [[RoutesInformation]]
  - [[SalesPersonsRoutes]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Technical_CreateRouteBasedonReference1_UpdateOnly


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BusinessUnits, CTE, Customers, CustomersFinancialDetails, Excel, Non, Null, Positions, RoutesInformation, SalesPersonsRoutes, Section, Technical_CFD_temp, UpdateCustomerFin, after. Writes CustomersFinancialDetails, Positions, RoutesInformation, SalesPersonsRoutes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[BusinessUnits]]
- CTE
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Excel]]
- Non
- Null
- [[Positions]]
- [[RoutesInformation]]
- [[SalesPersonsRoutes]]
- Section
- [[Technical_CFD_temp]]
- UpdateCustomerFin
- after
## Tables Written
- [[CustomersFinancialDetails]]
- [[Positions]]
- [[RoutesInformation]]
- [[SalesPersonsRoutes]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[BusinessUnits]]
- CTE
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Excel]]
- Non
- Null
- [[Positions]]
- [[RoutesInformation]]
- [[SalesPersonsRoutes]]
- Section
- [[Technical_CFD_temp]]
- UpdateCustomerFin
- after

**Tables Written**
- [[CustomersFinancialDetails]]
- [[Positions]]
- [[RoutesInformation]]
- [[SalesPersonsRoutes]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
