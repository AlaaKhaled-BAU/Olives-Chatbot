---
type: procedure
database: OSFA_DB
name: OT_SalesmanStockHF_Insert
schema: dbo
tags: [#inventory, #mobile, #sales]
reads_from:
  - [[OT_SalesmanStockHF]]
writes_to:
  - [[OT_SalesmanStockHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_SalesmanStockHF_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_SalesmanStockHF. Writes OT_SalesmanStockHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouYear smallint
- @VouNo int
- @VouDate smalldatetime
- @SalesmanNo smallint
- @Posted bit
- @Notes varchar (200)
- @GPSX varchar (50)
- @GPSY varchar (50)
- @ErrNo SmallInt Output
- @RouteID	int
- @TrDateTime smalldatetime = null
- @PrintOriginalCount int=0
- @PrintCopyCount int=0
- @ExtraNote	nvarchar(3000)=''
## Tables Read
- [[OT_SalesmanStockHF]]
## Tables Written
- [[OT_SalesmanStockHF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_SalesmanStockHF]]

**Tables Written**
- [[OT_SalesmanStockHF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
