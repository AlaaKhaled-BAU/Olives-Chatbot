---
type: procedure
database: OSFA_DB
name: OT_ReprintedTransactions_CheckExist
schema: dbo
tags: [#mobile]
reads_from:
  - [[OT_ReprintedTransactions]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ReprintedTransactions_CheckExist


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_ReprintedTransactions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @TrTypeID smallint
- @TrYear smallint
- @TrNo int
- @TrID int
- @TrDateTime smalldatetime
- @ErrNo SmallInt Output
- @Exist SmallInt Output
## Tables Read
- [[OT_ReprintedTransactions]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_ReprintedTransactions]]

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
