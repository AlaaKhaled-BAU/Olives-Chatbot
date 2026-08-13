---
type: procedure
database: OSFA_DB
name: OT_RequestToExceedCheckDueDate_Insert
schema: dbo
tags: [#mobile, #workflow]
reads_from:
  - [[OT_RequestToExceedCheckDueDate]]
writes_to:
  - [[OT_RequestToExceedCheckDueDate]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToExceedCheckDueDate_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_RequestToExceedCheckDueDate. Writes OT_RequestToExceedCheckDueDate. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesPersonNo int
- @CustomerNo bigint
- @ReceiptAmount float
- @ChecksInfo nvarchar(max)
- @Latitude nvarchar(50)
- @Longitude nvarchar(50)
- @TabletSysID varchar(50)=null
- @CustomerDueDays smallint =0
- @ErrNo smallint output
## Tables Read
- [[OT_RequestToExceedCheckDueDate]]
## Tables Written
- [[OT_RequestToExceedCheckDueDate]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_RequestToExceedCheckDueDate]]

**Tables Written**
- [[OT_RequestToExceedCheckDueDate]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
