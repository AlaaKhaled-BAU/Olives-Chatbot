---
type: procedure
database: OSFA_DB
name: OT_ReprintedTransactions_Insert
schema: dbo
tags: [#mobile]
reads_from:
  - [[OT_ReprintedTransactions]]
writes_to:
  - [[OT_ReprintedTransactions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ReprintedTransactions_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_ReprintedTransactions. Writes OT_ReprintedTransactions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @TrTypeID smallint
- @TrYear smallint
- @TrNo int
- @TrID int
- @TrDateTime smalldatetime
- @ReprintReasonID int
- @CopyCount int=0
- @IsRePrint bit=0
- @TabletSysID nvarchar(50)=''
- @ErrNo SmallInt Output
## Tables Read
- [[OT_ReprintedTransactions]]
## Tables Written
- [[OT_ReprintedTransactions]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_ReprintedTransactions]]

**Tables Written**
- [[OT_ReprintedTransactions]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
