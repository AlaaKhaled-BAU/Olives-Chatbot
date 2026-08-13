---
type: procedure
database: Olives_BO
name: Fill_In_Missing_PositionRoute
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - [[Excel]]
  - cur_Salesman
  - [[SalesPersonsRoutes]]
writes_to:
  - [[SalesPersonsRoutes]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Fill_In_Missing_PositionRoute


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Excel, cur_Salesman, SalesPersonsRoutes. Writes SalesPersonsRoutes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[Excel]]
- cur_Salesman
- [[SalesPersonsRoutes]]
## Tables Written
- [[SalesPersonsRoutes]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Excel]]
- cur_Salesman
- [[salespersonsroutes]]

**Tables Written**
- [[salespersonsroutes]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
