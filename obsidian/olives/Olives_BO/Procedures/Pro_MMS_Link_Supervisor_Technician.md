---
type: procedure
database: Olives_BO
name: Pro_MMS_Link_Supervisor_Technician
schema: dbo
tags: [#backoffice, #mms]
reads_from:
  - [[MMS_Link_Supervisor_Technician]]
  - [[MMS_MaintenanceTechnician]]
writes_to:
  - [[MMS_Link_Supervisor_Technician]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_Link_Supervisor_Technician


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_Link_Supervisor_Technician, MMS_MaintenanceTechnician. Writes MMS_Link_Supervisor_Technician. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @SupervisorID int = null
- @TechnicianID int = null
- @cmdType varchar(100) = null
- @Link_Supervisor_Technician_DATATABLE Link_Supervisor_Technician_Type  readonly
## Tables Read
- [[MMS_Link_Supervisor_Technician]]
- [[MMS_MaintenanceTechnician]]
## Tables Written
- [[MMS_Link_Supervisor_Technician]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_Link_Supervisor_Technician]]
- [[MMS_MaintenanceTechnician]]

**Tables Written**
- [[MMS_Link_Supervisor_Technician]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
