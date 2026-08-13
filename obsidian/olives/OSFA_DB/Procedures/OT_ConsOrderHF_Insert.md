---
type: procedure
database: OSFA_DB
name: OT_ConsOrderHF_Insert
schema: dbo
tags: [#mobile, #order]
reads_from:
  - [[OT_ConsOrderHF]]
  - Olives_BO
writes_to:
  - [[OT_ConsOrderHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ConsOrderHF_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_ConsOrderHF, Olives_BO. Writes OT_ConsOrderHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @OrderYear smallint
- @OrderNo int
- @OrderDate smalldatetime
- @SalesmanNo smallint
- @Posted bit
- @Notes varchar (200)
- @GPSX varchar (50)
- @GPSY varchar (50)
- @VouType int=1
- @StoreNo int=0
- @TrDateTime smalldatetime = null
- @ErrNo SmallInt Output
- @PrintOriginalCount int=0
- @PrintCopyCount int=0
## Tables Read
- [[OT_ConsOrderHF]]
- Olives_BO
## Tables Written
- [[OT_ConsOrderHF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_ConsOrderHF]]
- Olives_BO

**Tables Written**
- [[OT_ConsOrderHF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
