---
type: procedure
database: OSFA_DB
name: OT_ReturnOrderDF_CheckExist
schema: dbo
tags: [#mobile, #order]
reads_from:
  - [[OT_ReturnOrderDF]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ReturnOrderDF_CheckExist


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_ReturnOrderDF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouYear smallint
- @VouNo int
- @ItemNo varchar (200)
- @Unit varchar (100)
- @Qty money
- @Bonus money
- @Price float
- @DiscountAmount float
- @DiscountPercent money
- @VouDiscount float
- @TaxType bit
- @TaxPercent money
- @TaxAmount float
- @ErrNo SmallInt Output
- @Exist SmallInt Output
## Tables Read
- [[OT_ReturnOrderDF]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_ReturnOrderDF]]

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
