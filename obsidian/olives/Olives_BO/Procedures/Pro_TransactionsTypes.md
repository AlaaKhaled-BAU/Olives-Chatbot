---
type: procedure
database: Olives_BO
name: Pro_TransactionsTypes
schema: dbo
tags: [#backoffice, #reference]
reads_from:
  - [[TransactionsTypes]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_TransactionsTypes


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads TransactionsTypes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @cmdType varchar(50)=null
## Tables Read
- [[TransactionsTypes]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[TransactionsTypes]]

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
