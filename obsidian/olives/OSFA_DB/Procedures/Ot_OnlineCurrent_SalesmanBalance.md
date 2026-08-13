---
type: procedure
database: OSFA_DB
name: Ot_OnlineCurrent_SalesmanBalance
schema: dbo
tags: [#inventory, #mobile, #sales]
reads_from:
  - CitMultiStoreMorek
  - olives_bo
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Ot_OnlineCurrent_SalesmanBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads CitMultiStoreMorek, olives_bo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @salesman int
## Tables Read
- CitMultiStoreMorek
- olives_bo
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- CitMultiStoreMorek
- olives_bo

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
Also exists in the other database: [[Olives_BO/Procedures/Ot_OnlineCurrent_SalesmanBalance]] (BO).

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
