---
type: procedure
database: Olives_BO
name: Rpt_GetAssignedRoutesDataforReport
schema: dbo
tags: [#backoffice, #gps, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Fun_Get_Salesmen_AssignedRoutes
  - [[RoutesInformation]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_GetAssignedRoutesDataforReport


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, Fun_Get_Salesmen_AssignedRoutes, RoutesInformation, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @compno int=1
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_Get_Salesmen_AssignedRoutes
- [[RoutesInformation]]
- [[SalesPersons]]
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
- Fun_Get_Salesmen_AssignedRoutes
- [[RoutesInformation]]
- [[SalesPersons]]

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
