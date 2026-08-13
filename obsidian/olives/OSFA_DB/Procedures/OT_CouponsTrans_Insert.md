---
type: procedure
database: OSFA_DB
name: OT_CouponsTrans_Insert
schema: dbo
tags: [#mobile]
reads_from:
  - [[OT_CouponsTrans]]
writes_to:
  - [[OT_CouponsTrans]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_CouponsTrans_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_CouponsTrans. Writes OT_CouponsTrans. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @CuoponNumber varchar(100)
- @UsedInTrType smallint
- @UsedInTrNo bigint
- @UsedInTrYear int
- @ErrNo SmallInt Output
## Tables Read
- [[OT_CouponsTrans]]
## Tables Written
- [[OT_CouponsTrans]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_CouponsTrans]]

**Tables Written**
- [[OT_CouponsTrans]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
