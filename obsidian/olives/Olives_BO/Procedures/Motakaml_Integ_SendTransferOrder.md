---
type: procedure
database: Olives_BO
name: Motakaml_Integ_SendTransferOrder
schema: dbo
tags: [#backoffice, #integration, #order]
reads_from:
  - OLIV
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
writes_to:
  - [[TransfersOrdersHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Motakaml_Integ_SendTransferOrder


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OLIV, TransfersOrdersDetails, TransfersOrdersHeaders. Writes TransfersOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- OLIV
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
## Tables Written
- [[TransfersOrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- OLIV
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]

**Tables Written**
- [[TransfersOrdersHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
