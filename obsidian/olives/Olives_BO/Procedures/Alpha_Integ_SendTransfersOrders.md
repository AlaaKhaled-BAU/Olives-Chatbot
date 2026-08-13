---
type: procedure
database: Olives_BO
name: Alpha_Integ_SendTransfersOrders
schema: dbo
tags: [#backoffice, #integration, #order]
reads_from:
  - [[TransfersOrdersHeaders]]
  - `dbo`
writes_to:
  - [[OT_ConsOrderDF]]
  - [[OT_ConsOrderHF]]
  - [[TransfersOrdersHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_Integ_SendTransfersOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads TransfersOrdersHeaders, dbo. Writes OT_ConsOrderDF, OT_ConsOrderHF, TransfersOrdersHeaders. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[TransfersOrdersHeaders]]
- `dbo`
## Tables Written
- [[OT_ConsOrderDF]]
- [[OT_ConsOrderHF]]
- [[TransfersOrdersHeaders]]
## Callers
- [[Alpha_SendData]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[TransfersOrdersHeaders]]
- dbo

**Tables Written**
- [[OT_ConsOrderDF]]
- [[OT_ConsOrderHF]]
- [[TransfersOrdersHeaders]]

**Callers**
_None_

**Callees**
- [[Alpha_SendData]]


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
