---
type: procedure
database: Olives_BO
name: POA_Save
schema: dbo
tags: [#backoffice]
reads_from:
  - [[POADetails]]
  - [[POAHeader]]
writes_to:
  - [[POADetails]]
  - [[POAHeader]]
called_by:
  - [[WF_AddWorkFlowLevelOne]]
support_relevance: high
last_verified: 2026-07-05
---
# POA_Save


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads POADetails, POAHeader. Writes POADetails, POAHeader. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @cmdType varchar(50)=null
- @SalesPersonID	int	=null
- @POAYear int =null
- @POAMonth int =null
- @CustomerID	bigint =null
- @VisitCount	int =null
- @POAID BIGINT=0 OUTPUT
## Tables Read
- [[POADetails]]
- [[POAHeader]]
## Tables Written
- [[POADetails]]
- [[POAHeader]]
## Callers
_None (no known callers)_
## Callees
- [[WF_AddWorkFlowLevelOne]]
## Impact / Dependencies

**Tables Read**
- [[POADetails]]
- [[POAHeader]]

**Tables Written**
- [[POADetails]]
- [[POAHeader]]

**Callers**
- [[WF_AddWorkFlowLevelOne]]

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
