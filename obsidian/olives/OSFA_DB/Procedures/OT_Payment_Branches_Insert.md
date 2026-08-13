---
type: procedure
database: OSFA_DB
name: OT_Payment_Branches_Insert
schema: dbo
tags: [#billing, #mobile]
reads_from:
  - [[OT_Payment_Branches]]
writes_to:
  - [[OT_Payment_Branches]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Payment_Branches_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_Payment_Branches. Writes OT_Payment_Branches. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouType smallint
- @VouYear smallint
- @VouNo int
- @BranchID int
- @Amount float
- @Ref1	varchar(500)
- @Ref2	varchar(500)
- @ErrNo smallint output
## Tables Read
- [[OT_Payment_Branches]]
## Tables Written
- [[OT_Payment_Branches]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_Payment_Branches]]

**Tables Written**
- [[OT_Payment_Branches]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
