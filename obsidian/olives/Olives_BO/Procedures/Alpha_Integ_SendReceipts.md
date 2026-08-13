---
type: procedure
database: Olives_BO
name: Alpha_Integ_SendReceipts
schema: dbo
tags: [#backoffice, #billing, #integration]
reads_from:
  - [[Customers]]
  - [[Receipts]]
  - `dbo`
writes_to:
  - [[OT_Checks]]
  - [[OT_Payments]]
  - [[OT_Payment_Currency]]
  - [[OT_Payment_Invoices]]
  - [[Receipts]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_Integ_SendReceipts


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Receipts, dbo. Writes OT_Checks, OT_Payments, OT_Payment_Currency, OT_Payment_Invoices, Receipts. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Customers]]
- [[Receipts]]
- `dbo`
## Tables Written
- [[OT_Checks]]
- [[OT_Payments]]
- [[OT_Payment_Currency]]
- [[OT_Payment_Invoices]]
- [[Receipts]]
## Callers
- [[Alpha_SendData]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[Receipts]]
- dbo

**Tables Written**
- [[OT_Checks]]
- [[OT_Payments]]
- [[OT_Payment_Currency]]
- [[OT_Payment_Invoices]]
- [[Receipts]]

**Callers**
_None_

**Callees**
- [[Alpha_SendData]]


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
