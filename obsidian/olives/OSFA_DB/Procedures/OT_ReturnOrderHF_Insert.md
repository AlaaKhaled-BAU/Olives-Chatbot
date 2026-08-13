---
type: procedure
database: OSFA_DB
name: OT_ReturnOrderHF_Insert
schema: dbo
tags: [#mobile, #order]
reads_from:
  - [[OT_ReturnOrderHF]]
  - `dbo`
writes_to:
  - [[OT_ReturnOrderHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ReturnOrderHF_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_ReturnOrderHF, dbo. Writes OT_ReturnOrderHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouYear smallint
- @VouNo int
- @SalesmanNo smallint
- @CustomerNo bigint
- @StoreNo int
- @VouDate smalldatetime
- @CaCr bit
- @DiscountAmount float
- @DiscountPercent money
- @GPSX varchar (50)
- @GPSY varchar (50)
- @Notes varchar (200)
- @Currency smallint
- @ExRate money
- @ErrNo SmallInt Output
- @PrNo smallint=null
- @RouteID	int
- @IsVoid int	=0
- @CustomerName	varchar(200)=''
- @TrDateTime smalldatetime = null
- @CustomerDiscountPerc float=0
- @CustomerDiscountAmount float=0
- @PrintOriginalCount int=0
- @PrintCopyCount int=0
- @IsWFApproved bit=0
- @WFApproveDesc nvarchar(200)=null
- @DocType smallint=null
- @ExtraNotes	varchar(4000)=null
## Tables Read
- [[OT_ReturnOrderHF]]
- `dbo`
## Tables Written
- [[OT_ReturnOrderHF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_ReturnOrderHF]]
- dbo

**Tables Written**
- [[OT_ReturnOrderHF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
