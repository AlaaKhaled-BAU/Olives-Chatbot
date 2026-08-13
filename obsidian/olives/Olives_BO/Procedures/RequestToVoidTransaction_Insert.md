---
type: procedure
database: Olives_BO
name: RequestToVoidTransaction_Insert
schema: dbo
tags: [#backoffice, #workflow]
reads_from:
  - [[RequestToVoidTransaction]]
writes_to:
  - [[RequestToVoidTransaction]]
called_by:
  - [[WF_AddWorkFlowLevelOne]]
support_relevance: high
last_verified: 2026-07-05
---
# RequestToVoidTransaction_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads RequestToVoidTransaction. Writes RequestToVoidTransaction. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @TrTypeID smallint
- @TrTypeYear smallint
- @TrTypeNo int
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @ErrNo smallint output
## Tables Read
- [[RequestToVoidTransaction]]
## Tables Written
- [[RequestToVoidTransaction]]
## Callers
_None (no known callers)_
## Callees
- [[WF_AddWorkFlowLevelOne]]
## Impact / Dependencies

**Tables Read**
- [[RequestToVoidTransaction]]

**Tables Written**
- [[RequestToVoidTransaction]]

**Callers**
- [[WF_AddWorkFlowLevelOne]]

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
