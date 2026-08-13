---
type: procedure
database: Olives_BO
name: Pro_MMS_OrderVisits
schema: dbo
tags: [#backoffice, #mms, #order, #sales]
reads_from:
  - [[MMS_DevicesInfo]]
  - [[MMS_OrderDetails]]
  - [[MMS_OrderVisits]]
  - [[MMS_ScheduleSupportVisits]]
  - [[MMS_SystemCodes]]
  - Order
writes_to:
  - [[MMS_OrderVisits]]
  - Order
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_OrderVisits


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_DevicesInfo, MMS_OrderDetails, MMS_OrderVisits, MMS_ScheduleSupportVisits, MMS_SystemCodes, Order. Writes MMS_OrderVisits, Order. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	= null
- @OrderAutoID	numeric(30, 0)	= null
- @OrderSubID	int	= null
- @ScheduleID	int	= null
- @VisitID	int	= null
- @StartDateTime	smalldatetime	= null
- @EndDateTime	smalldatetime	= null
- @ProcedureDescription	nvarchar(MAX)	= null
- @IsDeviceBring	bit	= null
- @BringDate	smalldatetime	= null
- @DeviceAttachment	nvarchar(500)	= null
- @DeviceStatus	nvarchar(500)	= null
- @Notes	nvarchar(500)	= null
- @VisitResult	int	= null
- @DeviceSerialNo	nvarchar(200)	= null
- @TabletSysID	varchar(50)	= null
- @cmdType nvarchar(50) = null
- @DeviceID	int	= null
- @WarrantyNo	nvarchar(100)	= null
- @WarrantyExpireDate	smalldatetime	= null
- @PurchaseDate	smalldatetime	= null
- @PurchaseLocation	nvarchar(200)	= null
- @Cust_FullAddress	nvarchar(500)	= null
- @Cust_TelephoneNo	nvarchar(500)	= null
- @Cust_TaxTypeID	int	= null
- @Cust_MobileNo	nvarchar(500)	= null
- @ExpectedAmount	float	= null
- @IsReplace	bit= null
- @ReplaceNote	nvarchar(MAX)= null
- @ReadingVoltage	nvarchar(500)= null
- @ReadingAmber	nvarchar(500)= null
- @ReadingHertz	nvarchar(500)= null
- @ReadingTemp	nvarchar(500)= null
- @StartDateTime_Sys	smalldatetime	= null
- @EndDateTime_Sys	smalldatetime	= null
## Tables Read
- [[MMS_DevicesInfo]]
- [[MMS_OrderDetails]]
- [[MMS_OrderVisits]]
- [[MMS_ScheduleSupportVisits]]
- [[MMS_SystemCodes]]
- Order
## Tables Written
- [[MMS_OrderVisits]]
- Order
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_DevicesInfo]]
- [[MMS_OrderDetails]]
- [[MMS_OrderVisits]]
- [[MMS_ScheduleSupportVisits]]
- [[MMS_SystemCodes]]
- Order

**Tables Written**
- [[MMS_OrderVisits]]
- Order

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
