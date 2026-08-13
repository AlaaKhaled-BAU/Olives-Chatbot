---
type: procedure
database: Olives_BO
name: Technical_CreateRouteBasedonID
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - [[BusinessUnits]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[Excel]]
  - [[Excel2]]
  - Non
  - Null
  - [[Positions]]
  - [[RoutesInformation]]
  - [[SalesPersonsRoutes]]
  - Section
  - [[Technical_CFD_temp]]
  - UpdateCustomerFin
  - cur_Salesman
writes_to:
  - [[CustomersFinancialDetails]]
  - [[Positions]]
  - [[RoutesInformation]]
  - [[SalesPersonsRoutes]]
  - [[Technical_CFD_temp]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Technical_CreateRouteBasedonID


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BusinessUnits, Customers, CustomersFinancialDetails, Excel, Excel2, Non, Null, Positions, RoutesInformation, SalesPersonsRoutes, Section, Technical_CFD_temp, UpdateCustomerFin, cur_Salesman. Writes CustomersFinancialDetails, Positions, RoutesInformation, SalesPersonsRoutes, Technical_CFD_temp. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
- @DeleteStatus bit
- @PriceListIDG int
## Tables Read
- [[BusinessUnits]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Excel]]
- [[Excel2]]
- Non
- Null
- [[Positions]]
- [[RoutesInformation]]
- [[SalesPersonsRoutes]]
- Section
- [[Technical_CFD_temp]]
- UpdateCustomerFin
- cur_Salesman
## Tables Written
- [[CustomersFinancialDetails]]
- [[Positions]]
- [[RoutesInformation]]
- [[SalesPersonsRoutes]]
- [[Technical_CFD_temp]]
## Callers
- [[Pro_ImportRouteInfoFromExcel]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[BusinessUnits]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Excel]]
- [[Excel2]]
- Non
- Null
- [[Positions]]
- [[RoutesInformation]]
- [[SalesPersonsRoutes]]
- Section
- [[Technical_CFD_temp]]
- UpdateCustomerFin
- cur_Salesman

**Tables Written**
- [[CustomersFinancialDetails]]
- [[Positions]]
- [[RoutesInformation]]
- [[SalesPersonsRoutes]]
- [[Technical_CFD_temp]]

**Callers**
_None_

**Callees**
- [[Pro_ImportRouteInfoFromExcel]]


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
