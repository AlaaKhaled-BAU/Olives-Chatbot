---
type: procedure
database: Olives_BO
name: AccPack_Integ_SendTransfersOrders_LuxuryItems
schema: dbo
tags: [#backoffice, #integration, #inventory, #order]
reads_from:
  - [[SalesPersons]]
  - [[TransfersOrdersHeaders]]
  - `dbo`
writes_to:
  - cds_integration
  - [[TransfersOrdersHeaders]]
  - UploadOrders
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# AccPack_Integ_SendTransfersOrders_LuxuryItems


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersons, TransfersOrdersHeaders, dbo. Writes cds_integration, TransfersOrdersHeaders, UploadOrders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[SalesPersons]]
- [[TransfersOrdersHeaders]]
- `dbo`
## Tables Written
- cds_integration
- [[TransfersOrdersHeaders]]
- UploadOrders
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
- cds_integration
- [[TransfersOrdersHeaders]]
- UploadOrders

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
