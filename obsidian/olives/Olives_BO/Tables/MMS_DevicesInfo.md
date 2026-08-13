---
type: table
database: Olives_BO
name: MMS_DevicesInfo
schema: dbo
tags: [#backoffice, #mms]
foreign_keys:
referenced_by:
  - [[Pro_MMS_DevicesInfo]]
  - [[Pro_MMS_GetDataForAndroid]]
  - [[Pro_MMS_OrderDetails]]
  - [[Pro_MMS_OrderDetailsForVisit]]
  - [[Pro_MMS_OrderVisits]]
  - [[Pro_MMS_ScheduleSupportVisits]]
  - [[Rpt_TechnicianVisitDetails]]
support_relevance: high
last_verified: 2026-07-05
---
# MMS_DevicesInfo


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| DeviceID | int | NO | ✓ |  |  |
| Parent | int | YES |  |  |  |
| Name | nvarchar | YES |  |  |  |
| ForeignName | nvarchar | YES |  |  |  |
| DeviceLevel | int | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| Size | nvarchar | YES |  |  |  |
| Color | nvarchar | YES |  |  |  |
| UseSerialNo | bit | YES |  |  |  |
## Primary Key
CompanyID
DeviceID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (7):**
- [[Pro_MMS_DevicesInfo]]
- [[Pro_MMS_GetDataForAndroid]]
- [[Pro_MMS_OrderDetails]]
- [[Pro_MMS_OrderDetailsForVisit]]
- [[Pro_MMS_OrderVisits]]
- [[Pro_MMS_ScheduleSupportVisits]]
- [[Rpt_TechnicianVisitDetails]]

**Writes (1):**
- [[Pro_MMS_DevicesInfo]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Visit not closed**: Support visit still open — technician forgot to close
- **Missing spare parts**: Maintenance order requires parts not in technician stock
- **Schedule conflict**: Multiple visits assigned same time slot — dispatch needs review

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
