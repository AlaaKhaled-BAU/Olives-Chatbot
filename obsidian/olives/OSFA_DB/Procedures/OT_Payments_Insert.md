---
type: procedure
database: OSFA_DB
name: OT_Payments_Insert
schema: dbo
tags: [#billing, #mobile]
reads_from:
  - [[OT_Payments]]
writes_to:
  - [[OT_Payments]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_Payments_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_Payments. Writes OT_Payments. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouType smallint
- @VouYear smallint
- @VouNo int
- @SalesmanNo smallint
- @CustomerNo bigint
- @VouDate smalldatetime
- @DocType smallint
- @Amount float
- @GPSx varchar (50)
- @GPSY varchar (50)
- @ErrNo SmallInt Output
- @Discount float
- @RouteID	int
- @RefNo nvarchar(50)=null
- @TrDateTime smalldatetime=null
- @PrintOriginalCount int=0
- @PrintCopyCount int=0
- @IsWFApproved bit=0
- @WFApproveDesc nvarchar(200)=null
- @Currency int =1
- @ExRate float =1
- @ForeignAmount float =0
- @ForeignDiscount float =0
- @Notes varchar (max)
- @DetailCount int=-1
- @TabletSysID varchar(50)=''
- @RequestOrderYear smallint
- @RequestOrderNo int
- @Bank_TransferNo	nvarchar(200)
- @Bank_Transfer_Date	smalldatetime
- @Bank_Transfer_Amount	float
- @Bank_Transfer_BankID	int
- @Bank_Transfer_BankAccount	int
## Tables Read
- [[OT_Payments]]
## Tables Written
- [[OT_Payments]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_Payments]]

**Tables Written**
- [[OT_Payments]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
