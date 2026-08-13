---
type: procedure
database: Olives_BO
name: Pro_MMS_MaintenanceTechnicianTransSerials
schema: dbo
tags: [#backoffice, #mms]
reads_from:
  - [[MMS_MaintenanceTechnician]]
  - [[MMS_MaintenanceTechnicianTransSerials]]
writes_to:
  - [[MMS_MaintenanceTechnicianTransSerials]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_MaintenanceTechnicianTransSerials


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_MaintenanceTechnician, MMS_MaintenanceTechnicianTransSerials. Writes MMS_MaintenanceTechnicianTransSerials. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	= null
- @TechnicianID	int	= null
- @SerYear	smallint	= null
- @InvoiceNextSerial	bigint	= null
- @ReceiptNextSerial	bigint	= null
- @cmdType nvarchar(50) = null
## Tables Read
- [[MMS_MaintenanceTechnician]]
- [[MMS_MaintenanceTechnicianTransSerials]]
## Tables Written
- [[MMS_MaintenanceTechnicianTransSerials]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_MaintenanceTechnician]]
- [[MMS_MaintenanceTechnicianTransSerials]]

**Tables Written**
- [[MMS_MaintenanceTechnicianTransSerials]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
