---
type: procedure
database: Olives_BO
name: Tech_No_Gps_Check_for_second_Visit
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - Fun_GetCustomersRouteByDate
  - [[LogActionTransaction]]
  - NOGPSCustomers
  - OSFA_DB
  - cursorsalesman
  - [[SalesPersons]]
writes_to:
  - [[OT_SystemOptions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Tech_No_Gps_Check_for_second_Visit


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetCustomersRouteByDate, LogActionTransaction, NOGPSCustomers, OSFA_DB, cursorsalesman, SalesPersons. Writes OT_SystemOptions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @Compno int
## Tables Read
- Fun_GetCustomersRouteByDate
- [[LogActionTransaction]]
- NOGPSCustomers
- OSFA_DB
- cursorsalesman
- [[SalesPersons]]
## Tables Written
- [[OT_SystemOptions]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Fun_GetCustomersRouteByDate
- [[LogActionTransaction]]
- NOGPSCustomers
- OSFA_DB
- cursorsalesman
- [[salespersons]]

**Tables Written**
- [[OT_SystemOptions]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
