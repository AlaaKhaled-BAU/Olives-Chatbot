---
type: procedure
database: Olives_BO
name: X3_INTEG_ASSIGNITEMS
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersons]]
  - [[Items]]
  - msgsites
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# X3_INTEG_ASSIGNITEMS


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersonItemsAssignment, SalesPersons, Items, msgsites. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- [[Items]]
- msgsites
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersonItemsAssignment]]
- [[SalesPersons]]
- [[items]]
- msgsites

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
