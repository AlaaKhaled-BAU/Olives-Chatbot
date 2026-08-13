---
type: procedure
database: OSFA_DB
name: OT_InvoiceHF_CheckExist
schema: dbo
tags: [#billing, #mobile]
reads_from:
  - [[OT_InvoiceHF]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_InvoiceHF_CheckExist


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_InvoiceHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouType smallint
- @VouYear smallint
- @VouNo int
- @SalesmanNo smallint
- @CustomerNo bigint
- @StoreNo int
- @VouDate smalldatetime
- @CaCr bit
- @DocType smallint
- @DiscountAmount float
- @DiscountPercent float
- @GPSX varchar (50)
- @GPSY varchar (50)
- @Notes varchar (200)
- @Currency smallint
- @ExRate money
- @ErrNo SmallInt Output
- @Exist SmallInt Output
- @TabletSysID	varchar(50)=''
## Tables Read
- [[OT_InvoiceHF]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_InvoiceHF]]

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
- [[Shared/Runbooks/Duplicate-Keys]]
