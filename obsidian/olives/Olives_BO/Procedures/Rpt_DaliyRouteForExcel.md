---
type: procedure
database: Olives_BO
name: Rpt_DaliyRouteForExcel
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[CustomersFinancialDetails]]
  - Olives_BO
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_DaliyRouteForExcel


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails, Olives_BO, RoutesInformation, SalesPersons, SalesPersonsRoutes, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 2
## Tables Read
- [[CustomersFinancialDetails]]
- Olives_BO
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
- [[CustomersFinancialDetails]]
- Olives_BO
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

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
