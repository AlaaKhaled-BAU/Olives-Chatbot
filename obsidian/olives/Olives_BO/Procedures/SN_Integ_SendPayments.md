---
type: procedure
database: Olives_BO
name: SN_Integ_SendPayments
schema: dbo
tags: [#backoffice, #billing, #integration]
reads_from:
  - [[Banks]]
  - [[Checks]]
  - Curs_Payment
  - [[Customers]]
  - [[Drawers]]
  - [[IntegrationErrorLog]]
  - [[Receipts]]
  - SN
  - [[SalesPersons]]
  - [[TransfersOrdersHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SN_Integ_SendPayments


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Checks, Curs_Payment, Customers, Drawers, IntegrationErrorLog, Receipts, SN, SalesPersons, TransfersOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[Banks]]
- [[Checks]]
- Curs_Payment
- [[Customers]]
- [[Drawers]]
- [[IntegrationErrorLog]]
- [[Receipts]]
- SN
- [[SalesPersons]]
- [[TransfersOrdersHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Checks]]
- Curs_Payment
- [[Customers]]
- [[Drawers]]
- [[IntegrationErrorLog]]
- [[Receipts]]
- SN
- [[SalesPersons]]
- [[TransfersOrdersHeaders]]

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
