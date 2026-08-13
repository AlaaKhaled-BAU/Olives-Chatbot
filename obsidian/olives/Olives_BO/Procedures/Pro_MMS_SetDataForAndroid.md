---
type: procedure
database: Olives_BO
name: Pro_MMS_SetDataForAndroid
schema: dbo
tags: [#backoffice, #mms, #mobile]
reads_from:
  - [[MMS_InvoiceDetails]]
  - [[MMS_InvoicesHeaders]]
  - [[MMS_MaintenanceTechnician]]
  - [[MMS_MaintenanceTechnicianTransSerials]]
  - [[MMS_OrderVisitDetails]]
  - [[MMS_OrderVisitImages]]
  - [[MMS_OrderVisits]]
  - [[MMS_PaymentsChecksDetails]]
  - [[MMS_PaymentsHeader]]
  - [[MMS_ScheduleSupportVisits]]
writes_to:
  - [[MMS_InvoiceDetails]]
  - [[MMS_InvoicesHeaders]]
  - [[MMS_MaintenanceTechnician]]
  - [[MMS_MaintenanceTechnicianTransSerials]]
  - [[MMS_OrderVisitDetails]]
  - [[MMS_OrderVisitImages]]
  - [[MMS_OrderVisits]]
  - [[MMS_PaymentsChecksDetails]]
  - [[MMS_PaymentsHeader]]
  - [[MMS_ScheduleSupportVisits]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_SetDataForAndroid


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_InvoiceDetails, MMS_InvoicesHeaders, MMS_MaintenanceTechnician, MMS_MaintenanceTechnicianTransSerials, MMS_OrderVisitDetails, MMS_OrderVisitImages, MMS_OrderVisits, MMS_PaymentsChecksDetails, MMS_PaymentsHeader, MMS_ScheduleSupportVisits. Writes MMS_InvoiceDetails, MMS_InvoicesHeaders, MMS_MaintenanceTechnician, MMS_MaintenanceTechnicianTransSerials, MMS_OrderVisitDetails, MMS_OrderVisitImages, MMS_OrderVisits, MMS_PaymentsChecksDetails, MMS_PaymentsHeader, MMS_ScheduleSupportVisits. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @cmdType varchar(50)=null
- @TechnicianID int=null
- @OrderAutoID numeric=null
- @OrderSubID int=null
- @ScheduleID int=null
- @UsedVisitID int =0 Output
- @StartDateTime smalldatetime=null
- @EndDateTime smalldatetime=null
- @StartDateTime_Sys smalldatetime=null
- @EndDateTime_Sys smalldatetime=null
- @ProcedureDescription nvarchar (MAX)=null
- @IsDeviceBring bit=null
- @BringDate smalldatetime=null
- @DeviceAttachment nvarchar (1000)=null
- @DeviceStatus nvarchar (1000)=null
- @Notes nvarchar (1000)=null
- @VisitResult int=null
- @DeviceSerialNo nvarchar (400)=null
- @TabletSysID nvarchar(100)=null
- @DeviceID	int	=null
- @WarrantyNo	nvarchar(100)	=null
- @WarrantyExpireDate	smalldatetime	=null
- @PurchaseDate	smalldatetime	=null
- @PurchaseLocation	nvarchar(200)	=null
- @Cust_FullAddress	nvarchar(500)	=null
- @Cust_TelephoneNo	nvarchar(500)	=null
- @Cust_TaxTypeID	int		=null
- @Cust_MobileNo	nvarchar(500)	=null
- @ExpectedAmount	float		=null
- @DiagnosticDesc 	nvarchar(1000)	=null
- @CloseReasonID	int		=null
- @DiagnosticID	int		=null
- @ServiceResolutionID	int		=null
- @ServiceConditionID	int		=null
- @CustName	nvarchar(500)	=null
- @ShowRoomID	int		=null
- @OtherShowRoom	nvarchar(500) 	=null
- @InvRef 	nvarchar(500) 	=null
- @IsValidSerialNo	bit		=0
- @VisitID int=null
- @LineID int=null
- @ItemNo nvarchar (200)=null
- @IsInWarranty bit=null
- @Qty money=null
- @ItemSerialNo nvarchar (400)=null
- @InvoiceYear smallint=null
- @InvoiceNo bigint=null
- @InvoiceDate smalldatetime=null
- @InvoiceDiscountPercent float=null
- @TotalInvoiceDiscountValue float=null
- @TotalItemDiscountValue float=null
- @TotalTaxValue float=null
- @TotalPrice float=null
- @InvType int =0
- @DetailCount int=-1
- @UnitPrice float=null
- @Price float=null
- @TaxPercent float=null
- @TaxValue float=null
- @ItemDiscountPercent float=null
- @ItemDiscountValue float=null
- @InvoiceDiscountValue float=null
- @PaymentYear smallint=null
- @PaymentNo bigint=null
- @PaymentDate smalldatetime=null
- @CashAmount float=null
- @CheckAmount float=null
- @CheckNo int=null
- @DueDate smalldatetime=null
- @Amount float=null
- @BankID int=null
- @BranchID int=null
- @DrawerName nvarchar (1000)=null
- @UsedLineID int=null
- @ImageData image=null
- @IsCustSigns bit=0
- @IsBlackList	bit	=0
- @POInvNo	nvarchar(500)=''
- @Cust_CityID	int	=0
- @Cust_AreaID	int=0
- @OrderStatusReasonID	int=0
- @IsReplace	bit=0
- @ReplaceNote	nvarchar(MAX)=''
- @ReadingVoltage	nvarchar(500)=''
- @ReadingAmber	nvarchar(500)=''
- @ReadingHertz	nvarchar(500)=''
- @ReadingTemp	nvarchar(500)=''
- @ImageDataBase64	nvarchar(MAX)=''
- @ImagesCount	nvarchar(500)=''
## Tables Read
- [[MMS_InvoiceDetails]]
- [[MMS_InvoicesHeaders]]
- [[MMS_MaintenanceTechnician]]
- [[MMS_MaintenanceTechnicianTransSerials]]
- [[MMS_OrderVisitDetails]]
- [[MMS_OrderVisitImages]]
- [[MMS_OrderVisits]]
- [[MMS_PaymentsChecksDetails]]
- [[MMS_PaymentsHeader]]
- [[MMS_ScheduleSupportVisits]]
## Tables Written
- [[MMS_InvoiceDetails]]
- [[MMS_InvoicesHeaders]]
- [[MMS_MaintenanceTechnician]]
- [[MMS_MaintenanceTechnicianTransSerials]]
- [[MMS_OrderVisitDetails]]
- [[MMS_OrderVisitImages]]
- [[MMS_OrderVisits]]
- [[MMS_PaymentsChecksDetails]]
- [[MMS_PaymentsHeader]]
- [[MMS_ScheduleSupportVisits]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_InvoiceDetails]]
- [[MMS_InvoicesHeaders]]
- [[MMS_MaintenanceTechnician]]
- [[MMS_MaintenanceTechnicianTransSerials]]
- [[MMS_OrderVisitDetails]]
- [[MMS_OrderVisitImages]]
- [[MMS_OrderVisits]]
- [[MMS_PaymentsChecksDetails]]
- [[MMS_PaymentsHeader]]
- [[MMS_ScheduleSupportVisits]]

**Tables Written**
- [[MMS_InvoiceDetails]]
- [[MMS_InvoicesHeaders]]
- [[MMS_MaintenanceTechnician]]
- [[MMS_MaintenanceTechnicianTransSerials]]
- [[MMS_OrderVisitDetails]]
- [[MMS_OrderVisitImages]]
- [[MMS_OrderVisits]]
- [[MMS_PaymentsChecksDetails]]
- [[MMS_PaymentsHeader]]
- [[MMS_ScheduleSupportVisits]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
