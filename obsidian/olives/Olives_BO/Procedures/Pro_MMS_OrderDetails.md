---
type: procedure
database: Olives_BO
name: Pro_MMS_OrderDetails
schema: dbo
tags: [#backoffice, #mms, #order]
reads_from:
  - [[Customers]]
  - Fun_ConvArrayToTable
  - [[MMS_DevicesInfo]]
  - [[MMS_Diagnostic]]
  - [[MMS_MaintenanceTechnician]]
  - [[MMS_OrderDetails]]
  - [[MMS_OrdersHeader]]
  - [[MMS_ScheduleSupportVisits]]
writes_to:
  - [[MMS_OrderDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_OrderDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Fun_ConvArrayToTable, MMS_DevicesInfo, MMS_Diagnostic, MMS_MaintenanceTechnician, MMS_OrderDetails, MMS_OrdersHeader, MMS_ScheduleSupportVisits. Writes MMS_OrderDetails. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	= null
- @OrderAutoID	numeric(30, 0)	= null
- @OrderSubID	int	= null
- @DeviceID	int	= null
- @DiagnosticID	int	= null
- @SerialNo	nvarchar(200)	= null
- @IsInWarranty	bit	= null
- @WarrantyNo	nvarchar(100)	= null
- @WarrantyExpireDate	smalldatetime	= null
- @PurchaseDate	smalldatetime	= null
- @PurchaseLocation	nvarchar(200)	= null
- @Notes	nvarchar(500)	= null
- @SubOrderStatus	int	= null
- @AssigmentDateTime	smalldatetime	= null
- @cmdType nvarchar(50) = null
- @FromDate smalldatetime = null
- @ToDate smalldatetime = null
- @OrderDetails_DATATABLE MMS_OrderDetails_Type readonly
- @TechID	int	= null
- @FilterString nvarchar(500) = null
## Tables Read
- [[Customers]]
- Fun_ConvArrayToTable
- [[MMS_DevicesInfo]]
- [[MMS_Diagnostic]]
- [[MMS_MaintenanceTechnician]]
- [[MMS_OrderDetails]]
- [[MMS_OrdersHeader]]
- [[MMS_ScheduleSupportVisits]]
## Tables Written
- [[MMS_OrderDetails]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- Fun_ConvArrayToTable
- [[MMS_DevicesInfo]]
- [[MMS_Diagnostic]]
- [[MMS_MaintenanceTechnician]]
- [[MMS_OrderDetails]]
- [[MMS_OrdersHeader]]
- [[MMS_ScheduleSupportVisits]]

**Tables Written**
- [[MMS_OrderDetails]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
