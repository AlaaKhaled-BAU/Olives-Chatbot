---
type: procedure
database: OSFA_DB
name: OT_RequestToExceedChqLimit_Insert
schema: dbo
tags: [#mobile, #workflow]
reads_from:
  - [[OT_RequestToExceedChqLimit]]
writes_to:
  - [[OT_RequestToExceedChqLimit]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToExceedChqLimit_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToExceedChqLimit. Writes OT_RequestToExceedChqLimit. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @ReceiptAmount float
- @ChecksInfo nvarchar(max)
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @TabletSysID varchar(50)=null
- @ErrNo smallint output
- @NewAutoID numeric(30,0) output
- @CustomerCreditLimit float =0
- @CustomerBanalce float=0
- @CustomerChqBanalce float =0
- @ExceedAmount float=0
## Tables Read
- [[OT_RequestToExceedChqLimit]]
## Tables Written
- [[OT_RequestToExceedChqLimit]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToExceedChqLimit]]

**Tables Written**
- [[OT_RequestToExceedChqLimit]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
