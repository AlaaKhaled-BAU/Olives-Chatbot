---
type: procedure
database: Olives_BO
name: Tablet_GetSalesmanRoute
schema: dbo
tags: [#backoffice, #gps, #mobile, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Tablet_GetSalesmanRoute


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, RoutesInformation, SalesPersons, SalesPersonsRoutes, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int=1
- @SalesmanNo int =2
- @SupervisorNo int=89
- @RouteDate smalldatetime ='2020-07-20'
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- `dbo`
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
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
