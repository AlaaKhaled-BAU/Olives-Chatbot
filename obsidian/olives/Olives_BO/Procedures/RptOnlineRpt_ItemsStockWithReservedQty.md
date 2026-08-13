---
type: procedure
database: Olives_BO
name: RptOnlineRpt_ItemsStockWithReservedQty
schema: dbo
tags: [#backoffice, #integration, #inventory, #reporting]
reads_from:
  - [[Items]]
  - [[StoresBalances]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# RptOnlineRpt_ItemsStockWithReservedQty


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, StoresBalances. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int=1
- @SalesmanNo int =3003
## Tables Read
- [[Items]]
- [[StoresBalances]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[StoresBalances]]

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
