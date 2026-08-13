---
type: procedure
database: Olives_BO
name: Pro_MMS_OrderDetailsForVisit
schema: dbo
tags: [#backoffice, #mms, #order, #sales]
reads_from:
  - [[Customers]]
  - Fun_GetSysCode
  - [[MMS_DevicesInfo]]
  - [[MMS_Diagnostic]]
  - [[MMS_MaintenanceTechnician]]
  - [[MMS_OrderDetails]]
  - [[MMS_OrderStatus]]
  - [[MMS_OrderVisits]]
  - [[MMS_OrdersHeader]]
  - [[MMS_ScheduleSupportVisits]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_OrderDetailsForVisit


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Fun_GetSysCode, MMS_DevicesInfo, MMS_Diagnostic, MMS_MaintenanceTechnician, MMS_OrderDetails, MMS_OrderStatus, MMS_OrderVisits, MMS_OrdersHeader, MMS_ScheduleSupportVisits. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	= 1
- @FromDate smalldatetime = '2020-01-01'
- @ToDate smalldatetime = '2020-12-30'
## Tables Read
- [[Customers]]
- Fun_GetSysCode
- [[MMS_DevicesInfo]]
- [[MMS_Diagnostic]]
- [[MMS_MaintenanceTechnician]]
- [[MMS_OrderDetails]]
- [[MMS_OrderStatus]]
- [[MMS_OrderVisits]]
- [[MMS_OrdersHeader]]
- [[MMS_ScheduleSupportVisits]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- Fun_GetSysCode
- [[MMS_DevicesInfo]]
- [[MMS_Diagnostic]]
- [[MMS_MaintenanceTechnician]]
- [[MMS_OrderDetails]]
- [[MMS_OrderStatus]]
- [[MMS_OrderVisits]]
- [[MMS_OrdersHeader]]
- [[MMS_ScheduleSupportVisits]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
