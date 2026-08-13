---
type: procedure
database: Olives_BO
name: DEMOSALESPERSON
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[ItemsReplacementHeaders]]
  - OSFA_DB
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[ReturnOrdersHeaders]]
  - [[TransfersOrdersHeaders]]
  - olives_BO
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# DEMOSALESPERSON


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ItemsReplacementHeaders, OSFA_DB, OrdersHeaders, Receipts, ReturnOrdersHeaders, TransfersOrdersHeaders, olives_BO. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[ItemsReplacementHeaders]]
- OSFA_DB
- [[OrdersHeaders]]
- [[Receipts]]
- [[ReturnOrdersHeaders]]
- [[TransfersOrdersHeaders]]
- olives_BO
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ItemsReplacementHeaders]]
- OSFA_DB
- [[OrdersHeaders]]
- [[Receipts]]
- [[ReturnOrdersHeaders]]
- [[TransfersOrdersHeaders]]
- olives_BO

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
