---
type: procedure
database: Olives_BO
name: Technical_Nairoukh_Awtar_linkRoutesToPosition
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - [[CustomersFinancialDetails]]
  - [[NairoukhRouteCustomersPositionChange]]
writes_to:
  - [[CustomersFinancialDetails]]
  - [[NairoukhRouteCustomersPositionChange]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Technical_Nairoukh_Awtar_linkRoutesToPosition


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails, NairoukhRouteCustomersPositionChange. Writes CustomersFinancialDetails, NairoukhRouteCustomersPositionChange. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @deletionStatus smallint
## Tables Read
- [[CustomersFinancialDetails]]
- [[NairoukhRouteCustomersPositionChange]]
## Tables Written
- [[CustomersFinancialDetails]]
- [[NairoukhRouteCustomersPositionChange]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomersFinancialDetails]]
- [[NairoukhRouteCustomersPositionChange]]

**Tables Written**
- [[Customersfinancialdetails]]
- [[NairoukhRouteCustomersPositionChange]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
