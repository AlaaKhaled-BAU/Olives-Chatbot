---
type: procedure
database: OSFA_DB
name: OT_CustStockDF_Insert
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
# OT_CustStockDF_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_CustStockDF. Writes OT_CustStockDF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouYear smallint
- @VouNo int
- @ItemNo varchar (200)
- @Qty money
- @UnitCode varchar (100)
- @ExpDate smalldatetime=null
- @ErrNo SmallInt Output
- @Notes nvarchar(300) = ''
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

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
