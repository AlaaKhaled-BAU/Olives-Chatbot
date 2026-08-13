---
type: procedure
database: Olives_BO
name: Alpha_Integ_SendVanTransfer
schema: dbo
tags: [#backoffice, #integration, #order]
reads_from:
  - [[SalesPersons]]
  - [[VanTransferHeader]]
  - `dbo`
writes_to:
  - [[OT_VanTransferDF]]
  - [[OT_VanTransferHF]]
  - [[VanTransferHeader]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_Integ_SendVanTransfer


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersons, VanTransferHeader, dbo. Writes OT_VanTransferDF, OT_VanTransferHF, VanTransferHeader. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- [[SalesPersons]]
- [[VanTransferHeader]]
- `dbo`
## Tables Written
- [[OT_VanTransferDF]]
- [[OT_VanTransferHF]]
- [[VanTransferHeader]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersons]]
- [[VanTransferHeader]]
- dbo

**Tables Written**
- [[OT_VanTransferDF]]
- [[OT_VanTransferHF]]
- [[VanTransferHeader]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
