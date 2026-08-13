---
type: procedure
database: Olives_BO
name: OWGM_AUTOGATESASSIGMENT
schema: dbo
tags: [#backoffice]
reads_from:
  - [[OWGM_Gates]]
  - [[OWGM_GatesUsers]]
  - [[OWGM_Transactions]]
  - Trans
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OWGM_AUTOGATESASSIGMENT


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OWGM_Gates, OWGM_GatesUsers, OWGM_Transactions, Trans. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[OWGM_Gates]]
- [[OWGM_GatesUsers]]
- [[OWGM_Transactions]]
- Trans
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OWGM_Gates]]
- [[OWGM_GatesUsers]]
- [[OWGM_Transactions]]
- Trans

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
