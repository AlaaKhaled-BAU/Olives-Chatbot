---
type: procedure
database: Olives_BO
name: AX_Integ_SendPayments_AbuTawileh
schema: dbo
tags: [#backoffice, #billing, #integration]
reads_from:
  - [[Checks]]
  - [[Customers]]
  - [[Receipts]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - Payments
  - PaymentsChecks
  - [[Receipts]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# AX_Integ_SendPayments_AbuTawileh


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, Customers, Receipts, SalesPersons, dbo. Writes Payments, PaymentsChecks, Receipts. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[Checks]]
- [[Customers]]
- [[Receipts]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- Payments
- PaymentsChecks
- [[Receipts]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Checks]]
- [[Customers]]
- [[Receipts]]
- [[SalesPersons]]
- dbo

**Tables Written**
- Payments
- PaymentsChecks
- [[Receipts]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
