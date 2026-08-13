---
type: procedure
database: Olives_BO
name: Ot_OnlineCurrent_SalesmanBalance
schema: dbo
tags: [#backoffice, #inventory, #mobile, #sales]
reads_from:
  - CitMultiStoreMorek
  - [[ClientsActive]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Ot_OnlineCurrent_SalesmanBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CitMultiStoreMorek, ClientsActive. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @salesman int
## Tables Read
- CitMultiStoreMorek
- [[ClientsActive]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- CitMultiStoreMorek
- [[ClientsActive]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Cross-Database
Also exists in the other database: [[OSFA_DB/Procedures/Ot_OnlineCurrent_SalesmanBalance]] (OSFA).

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
