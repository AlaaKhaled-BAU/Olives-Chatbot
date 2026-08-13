---
type: procedure
database: OSFA_DB
name: OT_AddPaymentChecksImages
schema: dbo
tags: [#billing, #mobile]
reads_from:
  - [[OT_ChecksImages]]
writes_to:
  - [[OT_ChecksImages]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_AddPaymentChecksImages


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_ChecksImages. Writes OT_ChecksImages. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouType smallint
- @VouYear smallint
- @VouNo int
- @ChqNo int
- @BankNo int
- @BranchNo int
- @CustomerNo bigint
- @CheckImage image
- @ErrNo SmallInt Output
## Tables Read
- [[OT_ChecksImages]]
## Tables Written
- [[OT_ChecksImages]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_ChecksImages]]

**Tables Written**
- [[OT_ChecksImages]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
