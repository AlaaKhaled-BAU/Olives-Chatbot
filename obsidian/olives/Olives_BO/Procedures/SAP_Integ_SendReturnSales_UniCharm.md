---
type: procedure
database: Olives_BO
name: SAP_Integ_SendReturnSales_UniCharm
schema: dbo
tags: [#backoffice, #integration, #order, #sales]
reads_from:
  - [[Customers]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
  - ARCreditMemo
  - ARCreditMemoItems
  - [[TransactionsHeaders]]
called_by:
  - SAP_Integration_Unicharm
support_relevance: high
last_verified: 2026-07-05
---
# SAP_Integ_SendReturnSales_UniCharm


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, SalesPersons, TransactionsHeaders, dbo. Writes ARCreditMemo, ARCreditMemoItems, TransactionsHeaders. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[Customers]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
- ARCreditMemo
- ARCreditMemoItems
- [[TransactionsHeaders]]
## Callers
_None (no known callers)_
## Callees
- SAP_Integration_Unicharm
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- dbo

**Tables Written**
- ARCreditMemo
- ARCreditMemoItems
- [[TransactionsHeaders]]

**Callers**
- SAP_Integration_Unicharm

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
