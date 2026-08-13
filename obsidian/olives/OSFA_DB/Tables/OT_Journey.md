---
type: table
database: OSFA_DB
name: OT_Journey
schema: dbo
tags: [#mobile]
foreign_keys:
referenced_by:
  - [[OT_Journey_CheckExist]]
  - [[OT_Journey_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_Journey



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | bigint | YES | ✓ |  |  |
| CompNo | smallint | NO |  |  |  |
| SalesmanNo | smallint | YES |  |  |  |
| StartTime | datetime | YES |  |  |  |
| EndTime | datetime | YES |  |  |  |
| GPSX_Start | varchar | YES |  |  |  |
| GPSY_Start | varchar | YES |  |  |  |
| GPSX_End | varchar | YES |  |  |  |
| GPSY_End | varchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_Journey_CheckExist]]
- [[OT_Journey_Insert]]

**Writes (1):**
- [[OT_Journey_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
