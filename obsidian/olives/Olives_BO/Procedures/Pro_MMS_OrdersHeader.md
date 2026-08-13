---
type: procedure
database: Olives_BO
name: Pro_MMS_OrdersHeader
schema: dbo
tags: [#backoffice, #mms, #order]
reads_from:
  - [[MMS_OrdersHeader]]
writes_to:
  - [[MMS_OrdersHeader]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_OrdersHeader


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_OrdersHeader. Writes MMS_OrdersHeader. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	 = null
- @OrderAutoID	numeric(30, 0)	 = null
- @OrderYear	smallint	 = null
- @OrderNo	bigint	 = null
- @OrderDate	smalldatetime	 = null
- @CustomerID	numeric(20, 0)	 = null
- @OrderTypeID	int	 = null
- @TaxTypeID	int	 = null
- @ReporterID	int	 = null
- @ShowRoom	nvarchar(200)	 = null
- @Notes	nvarchar(500)	 = null
- @UserID	nvarchar(50)	 = null
- @OrderStatus	int	 = null
- @CallCenterID	int	 = null
- @EnteryDateTime	smalldatetime	 = null
- @cmdType nvarchar(50)
- @UsedOrderID bigint = null output
## Tables Read
- [[MMS_OrdersHeader]]
## Tables Written
- [[MMS_OrdersHeader]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_OrdersHeader]]

**Tables Written**
- [[MMS_OrdersHeader]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
