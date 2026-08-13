---
type: procedure
database: OSFA_DB
name: GapTransTimeLine_Insert
schema: dbo
tags: [#mobile]
reads_from:
  - `dbo`
writes_to:
  - [[GapTransTimeLine]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# GapTransTimeLine_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads dbo. Writes GapTransTimeLine. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @GapTransYear smallint=1
- @GapTransNo bigint=1
- @TimeLineID int output
- @SalesmanNo int=1
- @TimeLineDateTime smalldatetime='2020-01-01'
- @Notes varchar(max)='fahed'
## Tables Read
- `dbo`
## Tables Written
- [[GapTransTimeLine]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dbo

**Tables Written**
- [[GapTransTimeLine]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
