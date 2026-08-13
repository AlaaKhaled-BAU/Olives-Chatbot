---
type: table
database: Olives_BO
name: MMS_MaintenanceTechnician
schema: dbo
tags: [#backoffice, #mms]
foreign_keys:
referenced_by:
  - [[Pro_MMS_GetDataForAndroid]]
  - [[Pro_MMS_InvoicesHeaders]]
  - [[Pro_MMS_Link_Supervisor_Technician]]
  - [[Pro_MMS_MaintenanceTechnician]]
  - [[Pro_MMS_MaintenanceTechnicianTransSerials]]
  - [[Pro_MMS_OrderAssignLog]]
  - [[Pro_MMS_OrderDetails]]
  - [[Pro_MMS_OrderDetailsForVisit]]
  - [[Pro_MMS_PaymentsHeader]]
  - [[Pro_MMS_ScheduleSupportVisits]]
  - [[Pro_MMS_SetDataForAndroid]]
  - [[Rpt_PrintInvoices]]
  - [[Rpt_TechnicianSatement]]
  - [[Rpt_TechnicianSummary]]
  - [[Rpt_TechnicianVisitDetails]]
support_relevance: high
last_verified: 2026-07-05
---
# MMS_MaintenanceTechnician


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| TechnicianID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ForeignName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| DayOff | nvarchar | YES |  |  |  |
| TimeWorkFrom | smalldatetime | YES |  |  |  |
| TimeWorkTo | smalldatetime | YES |  |  |  |
| MobileNo | nvarchar | YES |  |  |  |
| Email | nvarchar | YES |  |  |  |
| DevicePassword | nvarchar | YES |  |  |  |
| IsUpdateStock | bit | YES |  |  |  |
## Primary Key
CompanyID
TechnicianID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (15):**
- [[Pro_MMS_GetDataForAndroid]]
- [[Pro_MMS_InvoicesHeaders]]
- [[Pro_MMS_Link_Supervisor_Technician]]
- [[Pro_MMS_MaintenanceTechnician]]
- [[Pro_MMS_MaintenanceTechnicianTransSerials]]
- [[Pro_MMS_OrderAssignLog]]
- [[Pro_MMS_OrderDetails]]
- [[Pro_MMS_OrderDetailsForVisit]]
- [[Pro_MMS_PaymentsHeader]]
- [[Pro_MMS_ScheduleSupportVisits]]
- [[Pro_MMS_SetDataForAndroid]]
- [[Rpt_PrintInvoices]]
- [[Rpt_TechnicianSatement]]
- [[Rpt_TechnicianSummary]]
- [[Rpt_TechnicianVisitDetails]]

**Writes (3):**
- [[Pro_MMS_GetDataForAndroid]]
- [[Pro_MMS_MaintenanceTechnician]]
- [[Pro_MMS_SetDataForAndroid]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Visit not closed**: Support visit still open — technician forgot to close
- **Missing spare parts**: Maintenance order requires parts not in technician stock
- **Schedule conflict**: Multiple visits assigned same time slot — dispatch needs review

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
