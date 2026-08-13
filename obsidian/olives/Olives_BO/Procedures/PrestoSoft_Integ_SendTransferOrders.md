---
type: procedure
database: Olives_BO
name: PrestoSoft_Integ_SendTransferOrders
schema: dbo
tags: [#backoffice, #integration, #order]
reads_from:
  - D
  - [[Items]]
  - M
  - PRESTOSOFT
  - [[SalesPersons]]
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# PrestoSoft_Integ_SendTransferOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads D, Items, M, PRESTOSOFT, SalesPersons, TransfersOrdersDetails, TransfersOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int=1
## Tables Read
- D
- [[Items]]
- M
- PRESTOSOFT
- [[SalesPersons]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- D
- [[Items]]
- M
- PRESTOSOFT
- [[SalesPersons]]
- [[TransfersOrdersDetails]]
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
