---
type: procedure
database: Olives_BO
name: SAP_Tyconz_Integ_SendPayments
schema: dbo
tags: [#backoffice, #billing, #integration]
reads_from:
  - [[Banks]]
  - [[BanksAccounts]]
  - [[Checks]]
  - [[Customers]]
  - [[DocumentsTypes]]
  - [[Receipts]]
  - [[Receipts_PaidTrans]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - ChecksPayment
  - PaymentHF
  - PaymentInvoicesSettlement
  - [[Receipts]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SAP_Tyconz_Integ_SendPayments


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, BanksAccounts, Checks, Customers, DocumentsTypes, Receipts, Receipts_PaidTrans, SalesPersons, dbo. Writes ChecksPayment, PaymentHF, PaymentInvoicesSettlement, Receipts. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 7
## Tables Read
- [[Banks]]
- [[BanksAccounts]]
- [[Checks]]
- [[Customers]]
- [[DocumentsTypes]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- ChecksPayment
- PaymentHF
- PaymentInvoicesSettlement
- [[Receipts]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[BanksAccounts]]
- [[Checks]]
- [[Customers]]
- [[DocumentsTypes]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[SalesPersons]]
- dbo

**Tables Written**
- ChecksPayment
- PaymentHF
- PaymentInvoicesSettlement
- [[Receipts]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
