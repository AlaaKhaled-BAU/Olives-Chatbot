---
type: procedure
database: Olives_BO
name: SAP_Integ_SendReturnOrder_Karadsheh
schema: dbo
tags: [#backoffice, #integration, #order]
reads_from:
  - [[Customers]]
  - [[ReturnOrdersHeaders]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - ARCreditMemo
  - ARCreditMemoItems
  - [[ReturnOrdersHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SAP_Integ_SendReturnOrder_Karadsheh


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, ReturnOrdersHeaders, SalesPersons, dbo. Writes ARCreditMemo, ARCreditMemoItems, ReturnOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 2
## Tables Read
- [[Customers]]
- [[ReturnOrdersHeaders]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- ARCreditMemo
- ARCreditMemoItems
- [[ReturnOrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[ReturnOrdersHeaders]]
- [[SalesPersons]]
- dbo

**Tables Written**
- ARCreditMemo
- ARCreditMemoItems
- [[ReturnOrdersHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
