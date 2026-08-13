---
type: procedure
database: OSFA_DB
name: OT_RequestToExceedFinishAllTasks_Insert
schema: dbo
tags: [#mobile, #workflow]
reads_from:
  - [[OT_RequestToExceedFinishAllTasks]]
writes_to:
  - [[OT_RequestToExceedFinishAllTasks]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToExceedFinishAllTasks_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToExceedFinishAllTasks. Writes OT_RequestToExceedFinishAllTasks. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @Notes nvarchar(4000)
- @ErrNo smallint output
- @NewAutoID numeric(30,0) output
## Tables Read
- [[OT_RequestToExceedFinishAllTasks]]
## Tables Written
- [[OT_RequestToExceedFinishAllTasks]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToExceedFinishAllTasks]]

**Tables Written**
- [[OT_RequestToExceedFinishAllTasks]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
