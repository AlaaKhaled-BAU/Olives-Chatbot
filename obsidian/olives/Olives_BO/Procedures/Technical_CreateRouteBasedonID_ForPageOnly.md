---
type: procedure
database: Olives_BO
name: Technical_CreateRouteBasedonID_ForPageOnly
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - [[BusinessUnits]]
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
  - Technical_CFD_temp_1
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
# Technical_CreateRouteBasedonID_ForPageOnly


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BusinessUnits, Customers, CustomersFinancialDetails, Excel, Non, Null, Positions, RoutesInformation, SalesPersonsRoutes, Section, Technical_CFD_temp, Technical_CFD_temp_1, UpdateCustomerFin, after. Writes CustomersFinancialDetails, Positions, RoutesInformation, SalesPersonsRoutes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
- @DeleteStatus bit
- @pricelistid int
## Tables Read
- [[BusinessUnits]]
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
- Technical_CFD_temp_1
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
- Technical_CFD_temp_1
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
