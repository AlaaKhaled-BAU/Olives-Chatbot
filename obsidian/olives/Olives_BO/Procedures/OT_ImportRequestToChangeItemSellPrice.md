---
type: procedure
database: Olives_BO
name: OT_ImportRequestToChangeItemSellPrice
schema: dbo
tags: [#backoffice, #billing, #inventory, #mobile, #workflow]
reads_from:
  - ImportRequest
  - [[RequestToChangeItemSellPrice]]
  - [[WF_MasterLog]]
  - [[WF_SubLog]]
  - `dbo`
writes_to:
  - [[OT_RequestToChangeItemSellPrice]]
  - [[RequestToChangeItemSellPrice]]
  - [[WF_MasterLog]]
  - [[WF_SubLog]]
called_by:
  - [[WF_AddWorkFlowLevelOne]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportRequestToChangeItemSellPrice


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ImportRequest, RequestToChangeItemSellPrice, WF_MasterLog, WF_SubLog, dbo. Writes OT_RequestToChangeItemSellPrice, RequestToChangeItemSellPrice, WF_MasterLog, WF_SubLog. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
## Tables Read
- ImportRequest
- [[RequestToChangeItemSellPrice]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
- `dbo`
## Tables Written
- [[OT_RequestToChangeItemSellPrice]]
- [[RequestToChangeItemSellPrice]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
## Callers
_None (no known callers)_
## Callees
- [[WF_AddWorkFlowLevelOne]]
## Impact / Dependencies

**Tables Read**
- ImportRequest
- [[RequestToChangeItemSellPrice]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
- dbo

**Tables Written**
- [[OT_RequestToChangeItemSellPrice]]
- [[RequestToChangeItemSellPrice]]
- [[WF_MasterLog]]
- [[WF_SubLog]]

**Callers**
- [[WF_AddWorkFlowLevelOne]]

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
