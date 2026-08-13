---
type: procedure
database: Olives_BO
name: Pro_OWGM_Transactions
schema: dbo
tags: [#backoffice]
reads_from:
  - [[OWGM_Gates]]
  - [[OWGM_GatesUsers]]
  - [[OWGM_Transactions]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_OWGM_Transactions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OWGM_Gates, OWGM_GatesUsers, OWGM_Transactions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
## Tables Read
- [[OWGM_Gates]]
- [[OWGM_GatesUsers]]
- [[OWGM_Transactions]]
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

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
