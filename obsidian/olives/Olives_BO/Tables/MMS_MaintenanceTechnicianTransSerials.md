---
type: table
database: Olives_BO
name: MMS_MaintenanceTechnicianTransSerials
schema: dbo
tags: [#backoffice, #mms]
foreign_keys:
referenced_by:
  - [[Pro_MMS_GetDataForAndroid]]
  - [[Pro_MMS_MaintenanceTechnicianTransSerials]]
  - [[Pro_MMS_SetDataForAndroid]]
support_relevance: high
last_verified: 2026-07-05
---
# MMS_MaintenanceTechnicianTransSerials


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| TechnicianID | int | NO | ✓ |  |  |
| SerYear | smallint | NO | ✓ |  |  |
| InvoiceNextSerial | bigint | YES |  |  |  |
| ReceiptNextSerial | bigint | YES |  |  |  |
| InvoiceNextSerial_2 | bigint | YES |  |  |  |
## Primary Key
CompanyID
TechnicianID
SerYear
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_MMS_MaintenanceTechnicianTransSerials]]
- [[Pro_MMS_SetDataForAndroid]]

**Writes (3):**
- [[Pro_MMS_GetDataForAndroid]]
- [[Pro_MMS_MaintenanceTechnicianTransSerials]]
- [[Pro_MMS_SetDataForAndroid]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Visit not closed**: Support visit still open — technician forgot to close
- **Missing spare parts**: Maintenance order requires parts not in technician stock
- **Schedule conflict**: Multiple visits assigned same time slot — dispatch needs review

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
