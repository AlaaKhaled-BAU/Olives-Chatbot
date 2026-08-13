---
type: procedure
database: Olives_BO
name: ProTech_Integration_SendPayment
schema: dbo
tags: [#backoffice, #billing, #integration]
reads_from:
  - [[Checks]]
  - [[Companies]]
  - [[Currencies]]
  - [[Customers]]
  - Header
  - [[Receipts]]
  - [[Receipts_PaidTrans]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
  - ar_ap_fin_mstr
  - ar_ap_fin_paper
  - [[Receipts]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# ProTech_Integration_SendPayment


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, Companies, Currencies, Customers, Header, Receipts, Receipts_PaidTrans, SalesPersons, TransactionsHeaders, dbo. Writes ar_ap_fin_mstr, ar_ap_fin_paper, Receipts. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[Checks]]
- [[Companies]]
- [[Currencies]]
- [[Customers]]
- Header
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
- ar_ap_fin_mstr
- ar_ap_fin_paper
- [[Receipts]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Checks]]
- [[Companies]]
- [[Currencies]]
- [[Customers]]
- Header
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- dbo

**Tables Written**
- ar_ap_fin_mstr
- ar_ap_fin_paper
- [[Receipts]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
