---
type: procedure
database: Olives_BO
name: OT_ImportVanTransfer
schema: dbo
tags: [#backoffice, #mobile, #order]
reads_from:
  - [[ClientsActive]]
  - Header
  - [[VanTransferHeader]]
  - `dbo`
writes_to:
  - [[OT_VanTransferHF]]
  - [[VanTransferDetails]]
  - [[VanTransferHeader]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportVanTransfer


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Header, VanTransferHeader, dbo. Writes OT_VanTransferHF, VanTransferDetails, VanTransferHeader. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[ClientsActive]]
- Header
- [[VanTransferHeader]]
- `dbo`
## Tables Written
- [[OT_VanTransferHF]]
- [[VanTransferDetails]]
- [[VanTransferHeader]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- Header
- [[VanTransferHeader]]
- dbo

**Tables Written**
- [[OT_VanTransferHF]]
- [[VanTransferDetails]]
- [[VanTransferHeader]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
