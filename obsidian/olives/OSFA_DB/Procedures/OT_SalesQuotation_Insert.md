---
type: procedure
database: OSFA_DB
name: OT_SalesQuotation_Insert
schema: dbo
tags: [#mobile, #order, #sales]
reads_from:
  - [[OT_SalesQuotationHF]]
writes_to:
  - [[OT_SalesQuotationHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_SalesQuotation_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads OT_SalesQuotationHF. Writes OT_SalesQuotationHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @OrderYear smallint
- @OrderNo int
- @OrderDate smalldatetime
- @SalesmanNo smallint
- @CustomerNo bigint
- @Posted bit
- @ErrNo SmallInt Output
- @VouDisc float
- @VouDiscPer	float
- @Notes varchar(200)
- @BusUnitID smallint=null
- @DocType smallint=null
- @CustomerName varchar(200)=null
- @GPSX varchar (50)=null
- @GPSY varchar (50)=null
- @PrNo smallint=null
- @PaymentType smallint
- @TrDateTime smalldatetime = null
- @IsVoid int	=0
- @CustomerDiscountPerc float=0
- @CustomerDiscountAmount float=0
- @PrintOriginalCount int=0
- @PrintCopyCount int=0
- @ForeignCustomerDiscountPerc float=0
- @ForeignCustomerDiscountAmount float=0
- @Currency int=1
- @ExRate float =1
- @ForeignDiscountAmount float=0
- @ForeignDiscountPercent float=0
- @CaCr smallint=1
- @DeliveryLocation	nvarchar(500)=''
- @PromisesDate	smalldatetime=NULL
- @IsProspectiveCustomer bit = 1
- @TabletSysID	varchar(50)=''
- @DeliveryDays int=0
## Tables Read
- [[OT_SalesQuotationHF]]
## Tables Written
- [[OT_SalesQuotationHF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[OT_SalesQuotationHF]]

**Tables Written**
- [[OT_SalesQuotationHF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
