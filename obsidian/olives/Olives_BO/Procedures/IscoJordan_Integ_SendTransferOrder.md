---
type: procedure
database: Olives_BO
name: IscoJordan_Integ_SendTransferOrder
schema: dbo
tags: [#backoffice, #integration, #order]
reads_from:
  - [[Customers]]
  - DATA
  - [[Items]]
  - [[SalesPersons]]
  - TransHeader
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - TransferHeader
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
writes_to:
  - GLIStock
  - [[TransfersOrdersHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# IscoJordan_Integ_SendTransferOrder


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, DATA, Items, SalesPersons, TransHeader, TransactionsDetails, TransactionsHeaders, TransferHeader, TransfersOrdersDetails, TransfersOrdersHeaders. Writes GLIStock, TransfersOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Customers]]
- DATA
- [[Items]]
- [[SalesPersons]]
- TransHeader
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- TransferHeader
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
## Tables Written
- GLIStock
- [[TransfersOrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- DATA
- [[Items]]
- [[SalesPersons]]
- TransHeader
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- TransferHeader
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]

**Tables Written**
- GLIStock
- [[TransfersOrdersHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
