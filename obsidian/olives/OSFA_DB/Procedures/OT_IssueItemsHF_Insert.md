---
type: procedure
database: OSFA_DB
name: OT_IssueItemsHF_Insert
schema: dbo
tags: [#inventory, #mobile]
reads_from:
  - [[OT_IssueItemsHF]]
writes_to:
  - [[OT_IssueItemsHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_IssueItemsHF_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_IssueItemsHF. Writes OT_IssueItemsHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @OrderYear smallint
- @OrderNo int
- @OrderDate smalldatetime
- @SalesmanNo smallint
- @CustomerNo bigint
- @CheckInTime smalldatetime
- @PromisesDate smalldatetime
- @Posted bit
- @ErrNo SmallInt Output
- @VouDisc float
- @VouDiscPer	float
- @Notes varchar(200)
- @BusUnitID smallint=null
- @StoreNo int=null
- @DocType smallint=null
- @CustomerName varchar(200)=null
- @GPSX varchar (50)=null
- @GPSY varchar (50)=null
- @PrNo smallint=null
- @RouteID int
- @PaymentType smallint
- @TrDateTime smalldatetime = null
- @IsVoid int	=0
- @CustomerDiscountPerc float=0
- @CustomerDiscountAmount float=0
- @PrintOriginalCount int=0
- @PrintCopyCount int=0
- @ContractID nvarchar(100)=null
- @CaCr smallint=1
- @Currency int=1
- @ExRate float=1
- @DetailCount int=-1
- @TabletSysID	varchar(50)=''
- @ExtraNote nvarchar(max)=''
- @Manual_Disc float =0
- @BackOrderYear	smallint=0
- @BackOrderNo	bigint=0
## Tables Read
- [[OT_IssueItemsHF]]
## Tables Written
- [[OT_IssueItemsHF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_IssueItemsHF]]

**Tables Written**
- [[OT_IssueItemsHF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
