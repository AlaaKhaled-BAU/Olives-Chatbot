---
type: procedure
database: Olives_BO
name: TechnicalSupportTools_CopyReportsfornewSalesman
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[SalesPersonsDeviceReportsPermissions]]
  - and
  - int
  - [[SalesPersons]]
writes_to:
  - [[SalesPersonsDeviceReportsPermissions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# TechnicalSupportTools_CopyReportsfornewSalesman


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersonsDeviceReportsPermissions, and, int, SalesPersons. Writes SalesPersonsDeviceReportsPermissions. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @companyID int
- @Fromsalesperson int
- @ToSalesperson int
## Tables Read
- [[SalesPersonsDeviceReportsPermissions]]
- and
- int
- [[SalesPersons]]
## Tables Written
- [[SalesPersonsDeviceReportsPermissions]]
## Callers
- [[copdevicereportsPermissions_ByRange]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersonsDeviceReportsPermissions]]
- and
- int
- [[salespersons]]

**Tables Written**
- [[SalesPersonsDeviceReportsPermissions]]

**Callers**
_None_

**Callees**
- [[copdevicereportsPermissions_ByRange]]


## When to Run This

Diagnostic or repair procedure. Run when investigating data integrity issues. Check parameters carefully — this may modify data.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
