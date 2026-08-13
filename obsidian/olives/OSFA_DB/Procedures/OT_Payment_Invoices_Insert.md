---
type: procedure
database: OSFA_DB
name: OT_Payment_Invoices_Insert
schema: dbo
tags: [#billing, #mobile]
reads_from:
  - [[OT_Payment_Invoices]]
writes_to:
  - [[OT_Payment_Invoices]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Payment_Invoices_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_Payment_Invoices. Writes OT_Payment_Invoices. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouType smallint
- @VouYear smallint
- @VouNo int
- @InvType smallint
- @InvYear smallint
- @InvNo int
- @PaymentAmount float
- @ErrNo SmallInt Output
- @Ref1	nvarchar(500)
- @Ref2	nvarchar(500)
- @Ref3	nvarchar(500)
- @Ref4	nvarchar(500)
- @DiscountAmount float
- @DiscountPercent float
## Tables Read
- [[OT_Payment_Invoices]]
## Tables Written
- [[OT_Payment_Invoices]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_Payment_Invoices]]

**Tables Written**
- [[OT_Payment_Invoices]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
