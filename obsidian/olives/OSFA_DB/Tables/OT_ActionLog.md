---
type: table
database: OSFA_DB
name: OT_ActionLog
schema: dbo
tags: [#log, #mobile]
foreign_keys:
referenced_by:
  - [[OT_ActionLog_CheckExist]]
  - [[OT_ActionLog_Insert]]
  - [[OT_AppService]]
  - [[OT_AutoRefreshCustomerInfo]]
support_relevance: low
last_verified: 2026-07-05
---
# OT_ActionLog



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompNo | smallint | NO |  |  |  |
| ActionID | nvarchar | YES |  |  |  |
| TimeStamp | datetime | NO |  |  |  |
| SalesmanID | nvarchar | YES |  |  |  |
| Data1 | nvarchar | YES |  |  |  |
| Data2 | nvarchar | YES |  |  |  |
| Data3 | nvarchar | YES |  |  |  |
| Data4 | nvarchar | YES |  |  |  |
| Data5 | nvarchar | YES |  |  |  |
| GpsX | nchar | YES |  |  |  |
| GpsY | nchar | YES |  |  |  |
| RouteID | int | YES |  |  |  |
| Posted | bit | YES |  |  |  |
| SysDate | smalldatetime | YES |  |  |  |
| TabletSysID | nvarchar | YES |  |  |  |
| CarCounter | bigint | YES |  |  |  |
| GPSOn | bit | YES |  |  |  |
| NetworkOn | bit | YES |  |  |  |
| InternetOn | bit | YES |  |  |  |
| AppVersion | nvarchar | YES |  |  |  |
| CustLocLineID | nvarchar | YES |  |  |  |
| AssistantsIDs | nvarchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[OT_ActionLog_CheckExist]]
- [[OT_ActionLog_Insert]]
- [[OT_AppService]]
- [[OT_AutoRefreshCustomerInfo]]

**Writes (2):**
- [[OT_ActionLog_Insert]]
- [[OT_AutoRefreshCustomerInfo]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Rapid growth**: Table size growing fast — archive old records periodically
- **Orphan log entries**: No corresponding source transaction — investigate data source
- **No cleanup**: No purge job configured — disk space may fill up

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
