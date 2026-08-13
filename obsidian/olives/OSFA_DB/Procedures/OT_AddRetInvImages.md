---
type: procedure
database: OSFA_DB
name: OT_AddRetInvImages
schema: dbo
tags: [#mobile]
reads_from:
  - [[OT_InvoiceDF]]
writes_to:
  - [[OT_InvoiceDF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_AddRetInvImages


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_InvoiceDF. Writes OT_InvoiceDF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @VouYear smallint
- @VouNo int
- @VouType int
- @ItemNo nvarchar (200)
- @ItemImage image
- @ErrNo SmallInt Output
## Tables Read
- [[OT_InvoiceDF]]
## Tables Written
- [[OT_InvoiceDF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_InvoiceDF]]

**Tables Written**
- [[OT_InvoiceDF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
