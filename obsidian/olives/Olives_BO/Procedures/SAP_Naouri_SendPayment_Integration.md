---
type: procedure
database: Olives_BO
name: SAP_Naouri_SendPayment_Integration
schema: dbo
tags: [#backoffice, #billing, #integration]
reads_from:
  - [[Banks]]
  - [[Checks]]
  - [[Customers]]
  - [[Receipts]]
  - [[Receipts_PaidTrans]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[Receipts]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SAP_Naouri_SendPayment_Integration


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Checks, Customers, Receipts, Receipts_PaidTrans, SalesPersons, dbo. Writes Receipts. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @SalesmanNo int = null
- @CmdType nvarchar(100) = null
- @VouYear smallint = null
- @VouNo int = null
- @RefPaymentNo nvarchar(50) = null
## Tables Read
- [[Banks]]
- [[Checks]]
- [[Customers]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[Receipts]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Checks]]
- [[Customers]]
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[Receipts]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
