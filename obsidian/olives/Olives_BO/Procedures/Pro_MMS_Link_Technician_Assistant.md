---
type: procedure
database: Olives_BO
name: Pro_MMS_Link_Technician_Assistant
schema: dbo
tags: [#backoffice, #mms]
reads_from:
  - [[MMS_Assistants]]
  - [[MMS_Link_Technician_Assistant]]
writes_to:
  - [[MMS_Link_Technician_Assistant]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_Link_Technician_Assistant


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_Assistants, MMS_Link_Technician_Assistant. Writes MMS_Link_Technician_Assistant. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @TechnicianID int = null
- @AssistantID int = null
- @cmdType varchar(100) = null
- @Link_Technician_Assistant_Type_DATATABLE Link_Technician_Assistant_Type readonly
## Tables Read
- [[MMS_Assistants]]
- [[MMS_Link_Technician_Assistant]]
## Tables Written
- [[MMS_Link_Technician_Assistant]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_Assistants]]
- [[MMS_Link_Technician_Assistant]]

**Tables Written**
- [[MMS_Link_Technician_Assistant]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
