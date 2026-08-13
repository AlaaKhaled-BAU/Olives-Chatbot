---
type: procedure
database: Olives_BO
name: X3_AssignItems
schema: dbo
tags: [#backoffice, #inventory]
reads_from:
  - [[Items]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# X3_AssignItems


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, SalesPersonItemsAssignment, SalesPersons, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- [[Items]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- dbo

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
