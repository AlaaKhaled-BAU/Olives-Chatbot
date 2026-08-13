---
type: procedure
database: Olives_BO
name: OT_ImportSalesmanStockTacking
schema: dbo
tags: [#backoffice, #inventory, #mobile, #sales]
reads_from:
  - [[ClientsActive]]
  - [[SalesPersonStockTacking]]
  - `dbo`
writes_to:
  - [[OT_SalesmanStockHF]]
  - [[SalesPersonStockTacking]]
  - [[SalesPersonStockTackingDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportSalesmanStockTacking


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, SalesPersonStockTacking, dbo. Writes OT_SalesmanStockHF, SalesPersonStockTacking, SalesPersonStockTackingDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[ClientsActive]]
- [[SalesPersonStockTacking]]
- `dbo`
## Tables Written
- [[OT_SalesmanStockHF]]
- [[SalesPersonStockTacking]]
- [[SalesPersonStockTackingDetails]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[SalesPersonStockTacking]]
- dbo

**Tables Written**
- [[OT_SalesmanStockHF]]
- [[SalesPersonStockTacking]]
- [[SalesPersonStockTackingDetails]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
