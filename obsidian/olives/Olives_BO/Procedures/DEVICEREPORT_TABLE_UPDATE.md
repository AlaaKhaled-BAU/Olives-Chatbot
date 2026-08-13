---
type: procedure
database: Olives_BO
name: DEVICEREPORT_TABLE_UPDATE
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[DeviceReportsList]]
  - [[Positions]]
  - [[SalesPersons]]
  - [[SalesPersonsDevicePermissions]]
  - [[SalesPersonsDeviceReportsPermissions]]
  - db_cursor
  - db_cursor_D
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# DEVICEREPORT_TABLE_UPDATE


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads DeviceReportsList, Positions, SalesPersons, SalesPersonsDevicePermissions, SalesPersonsDeviceReportsPermissions, db_cursor, db_cursor_D. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
_None_
## Tables Read
- [[DeviceReportsList]]
- [[Positions]]
- [[SalesPersons]]
- [[SalesPersonsDevicePermissions]]
- [[SalesPersonsDeviceReportsPermissions]]
- db_cursor
- db_cursor_D
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[DeviceReportsList]]
- [[Positions]]
- [[SalesPersons]]
- [[SalesPersonsDevicePermissions]]
- [[SalesPersonsDeviceReportsPermissions]]
- db_cursor
- db_cursor_D

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
