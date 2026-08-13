---
type: procedure
database: Olives_BO
name: All_Visits
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[ClientsActive]]
  - [[CustomersFinancialDetails]]
  - [[LogActionTransaction]]
  - [[OrdersHeaders]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
  - cursorsalesman
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# All_Visits


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CustomersFinancialDetails, LogActionTransaction, OrdersHeaders, RoutesInformation, SalesPersons, SalesPersonsRoutes, cursorsalesman. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint =1
- @fromdate smalldatetime='2023-05-18'
## Tables Read
- [[ClientsActive]]
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- cursorsalesman
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CustomersFinancialDetails]]
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- cursorsalesman

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
