---
type: procedure
database: Olives_BO
name: OT_ImportUnloadOrderForSalesmanStock
schema: dbo
tags: [#backoffice, #inventory, #mobile, #order, #sales]
reads_from:
  - Header
  - OSFA_DB
  - Olives_Bo
  - db
writes_to:
  - [[OT_ConsOrderDF]]
  - [[OT_ConsOrderHF]]
  - [[SalesPersonStockTacking]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportUnloadOrderForSalesmanStock


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Header, OSFA_DB, Olives_Bo, db. Writes OT_ConsOrderDF, OT_ConsOrderHF, SalesPersonStockTacking. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- Header
- OSFA_DB
- Olives_Bo
- db
## Tables Written
- [[OT_ConsOrderDF]]
- [[OT_ConsOrderHF]]
- [[SalesPersonStockTacking]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Header
- OSFA_DB
- Olives_Bo
- db

**Tables Written**
- [[OT_ConsOrderDF]]
- [[OT_ConsOrderHF]]
- [[SalesPersonStockTacking]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
