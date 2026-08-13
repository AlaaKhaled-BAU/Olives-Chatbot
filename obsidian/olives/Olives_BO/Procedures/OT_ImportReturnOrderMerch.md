---
type: procedure
database: Olives_BO
name: OT_ImportReturnOrderMerch
schema: dbo
tags: [#backoffice, #mobile, #order]
reads_from:
  - Header
  - Olives_Merch
  - `dbo`
writes_to:
  - Merch_VisitsResultsActionsDetailsReturn
  - [[OT_ReturnOrderDF]]
  - [[OT_ReturnOrderHF]]
  - [[OT_TransBatchsInfo]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportReturnOrderMerch


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Header, Olives_Merch, dbo. Writes Merch_VisitsResultsActionsDetailsReturn, OT_ReturnOrderDF, OT_ReturnOrderHF, OT_TransBatchsInfo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- Header
- Olives_Merch
- `dbo`
## Tables Written
- Merch_VisitsResultsActionsDetailsReturn
- [[OT_ReturnOrderDF]]
- [[OT_ReturnOrderHF]]
- [[OT_TransBatchsInfo]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Header
- Olives_Merch
- dbo

**Tables Written**
- Merch_VisitsResultsActionsDetailsReturn
- [[OT_ReturnOrderDF]]
- [[OT_ReturnOrderHF]]
- [[OT_TransBatchsInfo]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
