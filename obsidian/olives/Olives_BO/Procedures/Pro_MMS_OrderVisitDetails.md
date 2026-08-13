---
type: procedure
database: Olives_BO
name: Pro_MMS_OrderVisitDetails
schema: dbo
tags: [#backoffice, #mms, #order, #sales]
reads_from:
  - [[MMS_OrderVisitDetails]]
  - Order
writes_to:
  - [[MMS_OrderVisitDetails]]
  - Order
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_OrderVisitDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_OrderVisitDetails, Order. Writes MMS_OrderVisitDetails, Order. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint = null
- @OrderAutoID	numeric(30, 0)	 = null
- @OrderSubID	int	 = null
- @ScheduleID	int	 = null
- @VisitID	int	 = null
- @LineID	int	 = null
- @ItemNo	nvarchar(100)	 = null
- @IsInWarranty	bit	 = null
- @Qty	money	 = null
- @ItemSerialNo	nvarchar(200)	 = null
- @cmdType nvarchar(50) = null
- @OrderVisitDetails_DATATABLE MMS_OrderVisitDetails_Type readonly
## Tables Read
- [[MMS_OrderVisitDetails]]
- Order
## Tables Written
- [[MMS_OrderVisitDetails]]
- Order
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_OrderVisitDetails]]
- Order

**Tables Written**
- [[MMS_OrderVisitDetails]]
- Order

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
