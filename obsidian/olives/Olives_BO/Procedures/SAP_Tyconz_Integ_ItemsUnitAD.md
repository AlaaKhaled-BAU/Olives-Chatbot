---
type: procedure
database: Olives_BO
name: SAP_Tyconz_Integ_ItemsUnitAD
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - `dbo`
writes_to:
  - [[ItemsUnitsDetails]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SAP_Tyconz_Integ_ItemsUnitAD


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads dbo. Writes ItemsUnitsDetails. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = 7
## Tables Read
- `dbo`
## Tables Written
- [[ItemsUnitsDetails]]
## Callers
- [[SAP_Tyconz_Integ]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dbo

**Tables Written**
- [[ItemsUnitsDetails]]

**Callers**
_None_

**Callees**
- [[SAP_Tyconz_Integ]]


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
