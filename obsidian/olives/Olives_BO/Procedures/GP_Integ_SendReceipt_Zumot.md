---
type: procedure
database: Olives_BO
name: GP_Integ_SendReceipt_Zumot
schema: dbo
tags: [#backoffice, #billing, #integration]
reads_from:
  - 168
  - [[Banks]]
  - [[Receipts]]
  - SSMS
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# GP_Integ_SendReceipt_Zumot


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads 168, Banks, Receipts, SSMS. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- 168
- [[Banks]]
- [[Receipts]]
- SSMS
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- 168
- [[Banks]]
- [[Receipts]]
- SSMS

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
