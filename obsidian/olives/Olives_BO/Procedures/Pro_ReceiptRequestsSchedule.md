---
type: procedure
database: Olives_BO
name: Pro_ReceiptRequestsSchedule
schema: dbo
tags: [#backoffice, #billing]
reads_from:
  - [[Customers]]
  - [[Locations]]
  - [[ReceiptRequests]]
  - [[ReceiptRequestsSchedule]]
  - [[Receipts]]
  - [[SalesPersons]]
  - [[SalespersonsMessages]]
  - [[SystemCodes]]
writes_to:
  - [[ReceiptRequests]]
  - [[ReceiptRequestsSchedule]]
  - [[SalespersonsMessages]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ReceiptRequestsSchedule


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Locations, ReceiptRequests, ReceiptRequestsSchedule, Receipts, SalesPersons, SalespersonsMessages, SystemCodes. Writes ReceiptRequests, ReceiptRequestsSchedule, SalespersonsMessages. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @FromDate smalldatetime =null
- @ToDate smalldatetime =null
- @ScheduleDateTime smalldatetime =null
- @SalesmanID int =null
- @OrderYear smallint = null
- @OrderNo int = null
- @OrderStatus smallint = null
- @UserID nvarchar(50) = null
- @ScheduleID int = null
- @cmdType nvarchar(50) = null
## Tables Read
- [[Customers]]
- [[Locations]]
- [[ReceiptRequests]]
- [[ReceiptRequestsSchedule]]
- [[Receipts]]
- [[SalesPersons]]
- [[SalespersonsMessages]]
- [[SystemCodes]]
## Tables Written
- [[ReceiptRequests]]
- [[ReceiptRequestsSchedule]]
- [[SalespersonsMessages]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[Locations]]
- [[ReceiptRequests]]
- [[ReceiptRequestsSchedule]]
- [[Receipts]]
- [[SalesPersons]]
- [[SalespersonsMessages]]
- [[SystemCodes]]

**Tables Written**
- [[ReceiptRequests]]
- [[ReceiptRequestsSchedule]]
- [[SalespersonsMessages]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
