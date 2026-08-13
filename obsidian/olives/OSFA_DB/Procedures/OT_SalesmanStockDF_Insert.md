---
type: procedure
database: OSFA_DB
name: OT_SalesmanStockDF_Insert
schema: dbo
tags: [#inventory, #mobile, #sales]
reads_from:
  - [[OT_SalesmanStockDF]]
writes_to:
  - [[OT_SalesmanStockDF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_SalesmanStockDF_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_SalesmanStockDF. Writes OT_SalesmanStockDF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouYear smallint
- @VouNo int
- @ItemNo varchar (200)
- @Qty money
- @UnitCode varchar (100)
- @BeginQty money
- @CurrQty money
- @ErrNo SmallInt Output
- @Notes nvarchar(300) = ''
## Tables Read
- [[OT_SalesmanStockDF]]
## Tables Written
- [[OT_SalesmanStockDF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_SalesmanStockDF]]

**Tables Written**
- [[OT_SalesmanStockDF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
