---
type: procedure
database: Olives_BO
name: Technical_UpdateTempCFD_temp_forRouteCreation
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - [[CustomersFinancialDetails]]
  - [[Technical_CFD_temp]]
  - curTemp
  - [[Excel]]
writes_to:
  - [[Technical_CFD_temp]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Technical_UpdateTempCFD_temp_forRouteCreation


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomersFinancialDetails, Technical_CFD_temp, curTemp, Excel. Writes Technical_CFD_temp. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @compNo int
## Tables Read
- [[CustomersFinancialDetails]]
- [[Technical_CFD_temp]]
- curTemp
- [[Excel]]
## Tables Written
- [[Technical_CFD_temp]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomersFinancialDetails]]
- [[Technical_CFD_temp]]
- curTemp
- [[excel]]

**Tables Written**
- [[Technical_CFD_temp]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
