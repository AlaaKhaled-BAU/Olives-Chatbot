---
type: procedure
database: Olives_BO
name: Pro_MMS_TechnicianStock
schema: dbo
tags: [#backoffice, #inventory, #mms]
reads_from:
  - [[MMS_Items]]
  - [[MMS_MaintenanceTechnician_ItemsBalance]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_TechnicianStock


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_Items, MMS_MaintenanceTechnician_ItemsBalance. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @cmdType varchar(100)=null
- @TechnicianID int=null
## Tables Read
- [[MMS_Items]]
- [[MMS_MaintenanceTechnician_ItemsBalance]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_Items]]
- [[MMS_MaintenanceTechnician_ItemsBalance]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
