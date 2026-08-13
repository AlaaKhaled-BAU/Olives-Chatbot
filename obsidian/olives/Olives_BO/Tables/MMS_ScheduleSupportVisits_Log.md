---
type: table
database: Olives_BO
name: MMS_ScheduleSupportVisits_Log
schema: dbo
tags: [#backoffice, #log, #mms, #sales]
foreign_keys:
referenced_by:
  - [[Pro_MMS_OrderAssignLog]]
  - [[Pro_MMS_ScheduleSupportVisits]]
support_relevance: low
last_verified: 2026-07-05
---
# MMS_ScheduleSupportVisits_Log


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| LogID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| OrderAutoID | numeric | YES |  |  |  |
| OrderSubID | int | YES |  |  |  |
| ScheduleID | int | YES |  |  |  |
| TrType | nvarchar | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| UserID | nvarchar | YES |  |  |  |
| TechnicianID | int | YES |  |  |  |
| AssistantsID | int | YES |  |  |  |
## Primary Key
LogID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_MMS_OrderAssignLog]]
- [[Pro_MMS_ScheduleSupportVisits]]

**Writes (1):**
- [[Pro_MMS_ScheduleSupportVisits]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Rapid growth**: Table size growing fast — archive old records periodically
- **Orphan log entries**: No corresponding source transaction — investigate data source
- **No cleanup**: No purge job configured — disk space may fill up

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
