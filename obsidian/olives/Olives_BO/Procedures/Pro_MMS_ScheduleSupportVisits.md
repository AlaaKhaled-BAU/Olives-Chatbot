---
type: procedure
database: Olives_BO
name: Pro_MMS_ScheduleSupportVisits
schema: dbo
tags: [#backoffice, #mms, #sales]
reads_from:
  - [[Customers]]
  - [[MMS_DevicesInfo]]
  - [[MMS_MaintenanceTechnician]]
  - [[MMS_OrderDetails]]
  - [[MMS_OrderStatus]]
  - [[MMS_OrderVisits]]
  - [[MMS_OrdersHeader]]
  - [[MMS_ScheduleSupportVisits]]
  - [[MMS_ScheduleSupportVisits_Log]]
  - [[MMS_Supervisors]]
writes_to:
  - [[MMS_ScheduleSupportVisits]]
  - [[MMS_ScheduleSupportVisits_Log]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_ScheduleSupportVisits


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, MMS_DevicesInfo, MMS_MaintenanceTechnician, MMS_OrderDetails, MMS_OrderStatus, MMS_OrderVisits, MMS_OrdersHeader, MMS_ScheduleSupportVisits, MMS_ScheduleSupportVisits_Log, MMS_Supervisors. Writes MMS_ScheduleSupportVisits, MMS_ScheduleSupportVisits_Log. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	= null
- @OrderAutoID	numeric(30, 0)	= null
- @OrderSubID	int	= null
- @ScheduleID	int	= null
- @SupervisorID	int	= null
- @TechnicianID	int	= null
- @AssistantsID int = null
- @ScheduleDateTime	smalldatetime	= null
- @AssigmentDateTime	smalldatetime	= null
- @Status	int	= null
- @UserID nvarchar(50) = null
- @VisitType	int	= null
- @FromDate smalldatetime = null
- @ToDate smalldatetime = null
- @cmdType nvarchar(50) = null
## Tables Read
- [[Customers]]
- [[MMS_DevicesInfo]]
- [[MMS_MaintenanceTechnician]]
- [[MMS_OrderDetails]]
- [[MMS_OrderStatus]]
- [[MMS_OrderVisits]]
- [[MMS_OrdersHeader]]
- [[MMS_ScheduleSupportVisits]]
- [[MMS_ScheduleSupportVisits_Log]]
- [[MMS_Supervisors]]
## Tables Written
- [[MMS_ScheduleSupportVisits]]
- [[MMS_ScheduleSupportVisits_Log]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[MMS_DevicesInfo]]
- [[MMS_MaintenanceTechnician]]
- [[MMS_OrderDetails]]
- [[MMS_OrderStatus]]
- [[MMS_OrderVisits]]
- [[MMS_OrdersHeader]]
- [[MMS_ScheduleSupportVisits]]
- [[MMS_ScheduleSupportVisits_Log]]
- [[MMS_Supervisors]]

**Tables Written**
- [[MMS_ScheduleSupportVisits]]
- [[MMS_ScheduleSupportVisits_Log]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
