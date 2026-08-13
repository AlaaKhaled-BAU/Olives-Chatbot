---
type: table
database: OSFA_DB
name: OT_GPSLog
schema: dbo
tags: [#gps, #log, #mobile]
foreign_keys:
referenced_by:
  - [[OT_GPSLog_CheckExist]]
  - [[OT_GPSLog_Insert]]
  - [[servics_app_OSFA_Mobile_Ver]]
support_relevance: low
last_verified: 2026-07-05
---
# OT_GPSLog



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | smallint | NO | ✓ |  |  |
| CustomerNo | bigint | NO | ✓ |  |  |
| TransDate | datetime | NO | ✓ |  |  |
| GpsX | varchar | YES |  |  |  |
| GpsY | varchar | YES |  |  |  |
| Posted | bit | YES |  |  |  |
| Approve | bit | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| CustLocLineID | varchar | YES |  |  |  |
| CustLocName | varchar | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
CustomerNo
TransDate
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_GPSLog_CheckExist]]
- [[OT_GPSLog_Insert]]
- [[servics_app_OSFA_Mobile_Ver]]

**Writes (1):**
- [[OT_GPSLog_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Rapid growth**: Table size growing fast — archive old records periodically
- **Orphan log entries**: No corresponding source transaction — investigate data source
- **No cleanup**: No purge job configured — disk space may fill up

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
