---
type: procedure
database: Olives_BO
name: Rpt_Salesman_TotalCollections
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[Receipts]]
  - [[Receipts_PaidTrans]]
  - [[SalesPersons]]
  - the
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_Salesman_TotalCollections


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Receipts, Receipts_PaidTrans, SalesPersons, the. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo INT = 1
- @year INT = 2024
## Tables Read
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[SalesPersons]]
- the
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[SalesPersons]]
- the

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
