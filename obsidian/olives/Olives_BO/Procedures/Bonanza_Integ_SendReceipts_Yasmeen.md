---
type: procedure
database: Olives_BO
name: Bonanza_Integ_SendReceipts_Yasmeen
schema: dbo
tags: [#backoffice, #billing, #integration]
reads_from:
  - [[Checks]]
  - [[Customers]]
  - [[Receipts]]
  - `dbo`
writes_to:
  - CollChecks_InCube
  - [[Receipts]]
  - Transactions_InCube
  - TrnHeader_InCube
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Bonanza_Integ_SendReceipts_Yasmeen


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, Customers, Receipts, dbo. Writes CollChecks_InCube, Receipts, Transactions_InCube, TrnHeader_InCube. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Checks]]
- [[Customers]]
- [[Receipts]]
- `dbo`
## Tables Written
- CollChecks_InCube
- [[Receipts]]
- Transactions_InCube
- TrnHeader_InCube
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Checks]]
- [[Customers]]
- [[Receipts]]
- dbo

**Tables Written**
- CollChecks_InCube
- [[Receipts]]
- Transactions_InCube
- TrnHeader_InCube

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
