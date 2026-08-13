---
type: procedure
database: Olives_BO
name: OT_ImportRequestSalesmanWillNotVisit
schema: dbo
tags: [#backoffice, #mobile, #sales]
reads_from:
  - ImportRequest
  - [[RequestSalesmanWillNotVisit]]
  - [[WF_MasterLog]]
  - [[WF_SubLog]]
  - `dbo`
writes_to:
  - [[OT_RequestSalesmanWillNotVisit]]
  - [[RequestSalesmanWillNotVisit]]
called_by:
  - [[WF_AddWorkFlowLevelOne]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportRequestSalesmanWillNotVisit


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ImportRequest, RequestSalesmanWillNotVisit, WF_MasterLog, WF_SubLog, dbo. Writes OT_RequestSalesmanWillNotVisit, RequestSalesmanWillNotVisit. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- ImportRequest
- [[RequestSalesmanWillNotVisit]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
- `dbo`
## Tables Written
- [[OT_RequestSalesmanWillNotVisit]]
- [[RequestSalesmanWillNotVisit]]
## Callers
_None (no known callers)_
## Callees
- [[WF_AddWorkFlowLevelOne]]
## Impact / Dependencies

**Tables Read**
- ImportRequest
- [[RequestSalesmanWillNotVisit]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
- dbo

**Tables Written**
- [[OT_RequestSalesmanWillNotVisit]]
- [[RequestSalesmanWillNotVisit]]

**Callers**
- [[WF_AddWorkFlowLevelOne]]

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
