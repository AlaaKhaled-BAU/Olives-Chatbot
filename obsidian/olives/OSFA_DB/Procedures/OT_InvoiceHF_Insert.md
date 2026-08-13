---
type: procedure
database: OSFA_DB
name: OT_InvoiceHF_Insert
schema: dbo
tags: [#billing, #mobile]
reads_from:
  - [[OT_InvoiceHF]]
writes_to:
  - [[OT_InvoiceHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_InvoiceHF_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_InvoiceHF. Writes OT_InvoiceHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @VouType smallint
- @VouYear smallint
- @VouNo int
- @SalesmanNo smallint
- @CustomerNo bigint
- @StoreNo int
- @VouDate smalldatetime
- @CaCr bit
- @DocType smallint
- @DiscountAmount float
- @DiscountPercent float
- @GPSX varchar (50)
- @GPSY varchar (50)
- @Notes varchar (200)
- @Currency smallint
- @ExRate float
- @ErrNo SmallInt Output
- @PrNo smallint=null
- @RouteID	int
- @IsVoid int	=0
- @CustomerName	varchar(200)=''
- @TrDateTime smalldatetime = null
- @BusUnitID int=null
- @PaymentType int=null
- @CustomerDiscountPerc float=0
- @CustomerDiscountAmount float=0
- @PrintOriginalCount int=0
- @PrintCopyCount int=0
- @IsWFApproved bit=0
- @WFApproveDesc nvarchar(200)=null
- @IsCheckInvoice bit=0
- @ContractID nvarchar(100)=null
- @SalesmanStoreNo int=null
- @IsLinkedWithInv bit=0
- @DetailCount int=-1
- @TabletSysID	varchar(50)=''
- @PayAmount_Curr1 float = 0
- @PayAmount_Curr2 float = 0
- @PatientName	varchar(3000)=''
- @FileNo	varchar(300)=''
- @LocationLineID	int=NULL
- @InvDueDays	int=0
- @IsDirectOnline bit=0
- @DeliveryOrderYear smallint=0
- @DeliveryOrderNo int=0
- @Manual_Disc float=0
- @IsLoan bit = 0
- @LoanApproveBy nvarchar(100)=''
- @SalesmanStockYear	int	=0
- @SalesmanStockNo	int	=0
## Tables Read
- [[OT_InvoiceHF]]
## Tables Written
- [[OT_InvoiceHF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_InvoiceHF]]

**Tables Written**
- [[OT_InvoiceHF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
