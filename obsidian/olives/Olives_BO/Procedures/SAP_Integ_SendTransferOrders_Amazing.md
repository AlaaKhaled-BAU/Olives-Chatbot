---
type: procedure
database: Olives_BO
name: SAP_Integ_SendTransferOrders_Amazing
schema: dbo
tags: [#backoffice, #integration, #order]
reads_from:
  - [[SalesPersons]]
  - [[TransfersOrdersHeaders]]
  - `dbo`
writes_to:
  - [[TransfersOrdersHeaders]]
  - UploadOrder
  - UploadOrderItems
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SAP_Integ_SendTransferOrders_Amazing


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersons, TransfersOrdersHeaders, dbo. Writes TransfersOrdersHeaders, UploadOrder, UploadOrderItems. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[SalesPersons]]
- [[TransfersOrdersHeaders]]
- `dbo`
## Tables Written
- [[TransfersOrdersHeaders]]
- UploadOrder
- UploadOrderItems
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersons]]
- [[TransfersOrdersHeaders]]
- dbo

**Tables Written**
- [[TransfersOrdersHeaders]]
- UploadOrder
- UploadOrderItems

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
