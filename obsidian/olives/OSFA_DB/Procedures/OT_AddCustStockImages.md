---
type: procedure
database: OSFA_DB
name: OT_AddCustStockImages
schema: dbo
tags: [#inventory, #mobile]
reads_from:
  - [[OT_CustStockDF]]
writes_to:
  - [[OT_CustStockDF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_AddCustStockImages


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_CustStockDF. Writes OT_CustStockDF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @VouYear smallint
- @VouNo int
- @ItemNo nvarchar (200)
- @ItemImage image
- @ErrNo SmallInt Output
## Tables Read
- [[OT_CustStockDF]]
## Tables Written
- [[OT_CustStockDF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_CustStockDF]]

**Tables Written**
- [[OT_CustStockDF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
