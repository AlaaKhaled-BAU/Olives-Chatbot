---
type: procedure
database: OSFA_DB
name: OT_InvoiceReturnLink_Insert
schema: dbo
tags: [#billing, #mobile, #order]
reads_from:
  - [[OT_InvoiceReturnLink]]
writes_to:
  - [[OT_InvoiceReturnLink]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_InvoiceReturnLink_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_InvoiceReturnLink. Writes OT_InvoiceReturnLink. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @RetVouType smallint
- @RetVouYear smallint
- @RetVouNo int
- @InvVouType smallint
- @InvVouYear smallint
- @InvVouNo int
- @ItemCode nvarchar(100)
- @UnitID nvarchar(50)
- @Qty float
- @Bonus float
- @UnitPrice float
- @ErrNo SmallInt Output
## Tables Read
- [[OT_InvoiceReturnLink]]
## Tables Written
- [[OT_InvoiceReturnLink]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_InvoiceReturnLink]]

**Tables Written**
- [[OT_InvoiceReturnLink]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
