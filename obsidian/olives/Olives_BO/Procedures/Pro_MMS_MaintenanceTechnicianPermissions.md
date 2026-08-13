---
type: procedure
database: Olives_BO
name: Pro_MMS_MaintenanceTechnicianPermissions
schema: dbo
tags: [#auth, #backoffice, #mms]
reads_from:
  - [[MMS_MaintenanceTechnicianPermissions]]
  - [[MMS_MaintenanceTechnicianPermissions_Def]]
writes_to:
  - [[MMS_MaintenanceTechnicianPermissions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_MaintenanceTechnicianPermissions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_MaintenanceTechnicianPermissions, MMS_MaintenanceTechnicianPermissions_Def. Writes MMS_MaintenanceTechnicianPermissions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @cmdType nvarchar(50) = null
- @CompanyID	smallint	 = null
- @TechnicianID	int	 = null
- @PermissionID	int	 = null
- @PermissionAccess	bit	 = null
- @MaintenanceTechnicianPermissions_Type_DATATABLE MaintenanceTechnicianPermissions_Type readonly
## Tables Read
- [[MMS_MaintenanceTechnicianPermissions]]
- [[MMS_MaintenanceTechnicianPermissions_Def]]
## Tables Written
- [[MMS_MaintenanceTechnicianPermissions]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_MaintenanceTechnicianPermissions]]
- [[MMS_MaintenanceTechnicianPermissions_Def]]

**Tables Written**
- [[MMS_MaintenanceTechnicianPermissions]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
