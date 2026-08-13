---
type: procedure
database: Olives_BO
name: OT_ImportRequestSalesmanNoTransaction
schema: dbo
tags: [#backoffice, #mobile, #sales]
reads_from:
  - ImportRequest
  - [[RequestSalesmanNoTransaction]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[RequestSalesmanNoTransaction]]
called_by:
  - [[WF_AddWorkFlowLevelOne]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportRequestSalesmanNoTransaction


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ImportRequest, RequestSalesmanNoTransaction, SalesPersons, dbo. Writes RequestSalesmanNoTransaction. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- ImportRequest
- [[RequestSalesmanNoTransaction]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[RequestSalesmanNoTransaction]]
## Callers
_None (no known callers)_
## Callees
- [[WF_AddWorkFlowLevelOne]]
## Impact / Dependencies

**Tables Read**
- ImportRequest
- [[RequestSalesmanNoTransaction]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[RequestSalesmanNoTransaction]]

**Callers**
- [[WF_AddWorkFlowLevelOne]]

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
