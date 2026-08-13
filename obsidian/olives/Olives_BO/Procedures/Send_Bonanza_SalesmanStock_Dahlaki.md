---
type: procedure
database: Olives_BO
name: Send_Bonanza_SalesmanStock_Dahlaki
schema: dbo
tags: [#backoffice, #inventory, #sales]
reads_from:
  - [[SalesPersonStockTacking]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - InvDetailStock_Incube
  - InvHeaderStock_InCube
  - [[SalesPersonStockTacking]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Send_Bonanza_SalesmanStock_Dahlaki


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersonStockTacking, SalesPersons, dbo. Writes InvDetailStock_Incube, InvHeaderStock_InCube, SalesPersonStockTacking. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[SalesPersonStockTacking]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- InvDetailStock_Incube
- InvHeaderStock_InCube
- [[SalesPersonStockTacking]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersonStockTacking]]
- [[SalesPersons]]
- dbo

**Tables Written**
- InvDetailStock_Incube
- InvHeaderStock_InCube
- [[SalesPersonStockTacking]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
