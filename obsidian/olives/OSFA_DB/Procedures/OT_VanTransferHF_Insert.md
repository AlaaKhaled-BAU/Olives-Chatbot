---
type: procedure
database: OSFA_DB
name: OT_VanTransferHF_Insert
schema: dbo
tags: [#mobile, #order]
reads_from:
  - [[OT_VanTransferHF]]
writes_to:
  - [[OT_VanTransferHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_VanTransferHF_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_VanTransferHF. Writes OT_VanTransferHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @OrderYear smallint
- @OrderNo int
- @FromSalesman int
- @ToSalesman int
- @OrderDate smalldatetime
- @Notes varchar (500)
- @GPSX varchar (50)
- @GPSY varchar (50)
- @TrDateTime smalldatetime
- @PrintOriginalCount int
- @PrintCopyCount int
- @IsPosted bit
- @TabletSysID varchar (50)
- @ErrNo SmallInt Output
## Tables Read
- [[OT_VanTransferHF]]
## Tables Written
- [[OT_VanTransferHF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_VanTransferHF]]

**Tables Written**
- [[OT_VanTransferHF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
