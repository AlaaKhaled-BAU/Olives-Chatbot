---
type: procedure
database: Olives_BO
name: SAP_Integ_SendPayments_UniCharm
schema: dbo
tags: [#backoffice, #billing, #integration]
reads_from:
  - [[Checks]]
  - [[Customers]]
  - [[Receipts]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[Checks]]
  - Payments
  - [[Receipts]]
called_by:
  - SAP_Integration_Unicharm
support_relevance: high
last_verified: 2026-07-05
---
# SAP_Integ_SendPayments_UniCharm


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, Customers, Receipts, SalesPersons, dbo. Writes Checks, Payments, Receipts. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[Checks]]
- [[Customers]]
- [[Receipts]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[Checks]]
- Payments
- [[Receipts]]
## Callers
_None (no known callers)_
## Callees
- SAP_Integration_Unicharm
## Impact / Dependencies

**Tables Read**
- [[Checks]]
- [[Customers]]
- [[Receipts]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[Checks]]
- Payments
- [[Receipts]]

**Callers**
- SAP_Integration_Unicharm

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
