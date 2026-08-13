---
type: procedure
database: Olives_BO
name: TECHNICAL_CHECKMISSINGSERIAL_OLIVES_BO_ORDER_RECEIPT_INV_RETINV
schema: dbo
tags: [#backoffice, #billing, #order]
reads_from:
  - [[OrdersHeaders]]
  - [[Receipts]]
  - SerialSequence
  - [[OrdersDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# TECHNICAL_CHECKMISSINGSERIAL_OLIVES_BO_ORDER_RECEIPT_INV_RETINV


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OrdersHeaders, Receipts, SerialSequence, OrdersDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[OrdersHeaders]]
- [[Receipts]]
- SerialSequence
- [[OrdersDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OrdersHeaders]]
- [[Receipts]]
- SerialSequence
- [[ordersdetails]]
- [[transactionsheaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
