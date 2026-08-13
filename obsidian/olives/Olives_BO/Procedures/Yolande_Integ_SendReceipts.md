---
type: procedure
database: Olives_BO
name: Yolande_Integ_SendReceipts
schema: dbo
tags: [#backoffice, #billing, #integration]
reads_from:
  - [[Customers]]
  - [[Receipts]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[Checks]]
  - Payments
  - Payment_Invoices
  - [[Receipts]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Yolande_Integ_SendReceipts


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Receipts, SalesPersons, dbo. Writes Checks, Payments, Payment_Invoices, Receipts. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Customers]]
- [[Receipts]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[Checks]]
- Payments
- Payment_Invoices
- [[Receipts]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[Receipts]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[Checks]]
- Payments
- Payment_Invoices
- [[Receipts]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
