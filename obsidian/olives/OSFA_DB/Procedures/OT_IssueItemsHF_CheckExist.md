---
type: procedure
database: OSFA_DB
name: OT_IssueItemsHF_CheckExist
schema: dbo
tags: [#inventory, #mobile]
reads_from:
  - [[OT_IssueItemsHF]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_IssueItemsHF_CheckExist


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_IssueItemsHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @OrderYear smallint
- @OrderNo int
- @OrderDate smalldatetime
- @SalesmanNo smallint
- @CustomerNo bigint
- @CheckInTime smalldatetime
- @PromisesDate smalldatetime
- @Posted bit
- @ErrNo SmallInt Output
- @VouDisc	float
- @VouDiscPer	float
- @Notes	varchar(200)
- @Exist SmallInt Output
- @TabletSysID	varchar(50)=''
## Tables Read
- [[OT_IssueItemsHF]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_IssueItemsHF]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
