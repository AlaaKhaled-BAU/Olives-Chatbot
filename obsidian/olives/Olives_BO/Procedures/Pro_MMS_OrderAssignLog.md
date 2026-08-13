---
type: procedure
database: Olives_BO
name: Pro_MMS_OrderAssignLog
schema: dbo
tags: [#backoffice, #log, #mms, #order]
reads_from:
  - [[MMS_MaintenanceTechnician]]
  - [[MMS_OrdersHeader]]
  - [[MMS_ScheduleSupportVisits]]
  - [[MMS_ScheduleSupportVisits_Log]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_OrderAssignLog


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_MaintenanceTechnician, MMS_OrdersHeader, MMS_ScheduleSupportVisits, MMS_ScheduleSupportVisits_Log. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @OrderRef nvarchar(100)='SRON037955'
## Tables Read
- [[MMS_MaintenanceTechnician]]
- [[MMS_OrdersHeader]]
- [[MMS_ScheduleSupportVisits]]
- [[MMS_ScheduleSupportVisits_Log]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_MaintenanceTechnician]]
- [[MMS_OrdersHeader]]
- [[MMS_ScheduleSupportVisits]]
- [[MMS_ScheduleSupportVisits_Log]]

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
