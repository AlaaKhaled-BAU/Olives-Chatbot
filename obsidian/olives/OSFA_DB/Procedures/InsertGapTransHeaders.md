---
type: procedure
database: OSFA_DB
name: InsertGapTransHeaders
schema: dbo
tags: [#mobile]
reads_from:
  - [[GapTransHeaders]]
writes_to:
  - [[GapTransHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# InsertGapTransHeaders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads GapTransHeaders. Writes GapTransHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint =1
- @SalesmanNo int=3003
- @Notes varchar(MAX) ='fahed'
- @ActionDate smalldatetime=null
- @AssginedSalesmanNo int=1
- @IsDone bit=false
- @DeviceSysID varchar(MAX)  ='sadsadasd'
- @CustomerNo	bigint
## Tables Read
- [[GapTransHeaders]]
## Tables Written
- [[GapTransHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[GapTransHeaders]]

**Tables Written**
- [[GapTransHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
