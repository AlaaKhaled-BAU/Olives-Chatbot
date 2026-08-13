---
type: procedure
database: Olives_BO
name: Pro_MMS_Link_Supervisor_MaintenanceUnit
schema: dbo
tags: [#backoffice, #inventory, #mms]
reads_from:
  - [[MMS_Link_Supervisor_MaintenanceUnit]]
  - [[MMS_MaintenanceUnit]]
writes_to:
  - [[MMS_Link_Supervisor_MaintenanceUnit]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_Link_Supervisor_MaintenanceUnit


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_Link_Supervisor_MaintenanceUnit, MMS_MaintenanceUnit. Writes MMS_Link_Supervisor_MaintenanceUnit. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	= null
- @SupervisorID	int	= null
- @MaintenanceUnitID	int	= null
- @cmdType varchar(100) = null
- @Link_Supervisor_MaintenanceUnit_DATATABLE Link_Supervisor_MaintenanceUnit_Type  readonly
## Tables Read
- [[MMS_Link_Supervisor_MaintenanceUnit]]
- [[MMS_MaintenanceUnit]]
## Tables Written
- [[MMS_Link_Supervisor_MaintenanceUnit]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_Link_Supervisor_MaintenanceUnit]]
- [[MMS_MaintenanceUnit]]

**Tables Written**
- [[MMS_Link_Supervisor_MaintenanceUnit]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
