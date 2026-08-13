---
type: table
database: Olives_BO
name: MMS_Link_Technician_Assistant
schema: dbo
tags: [#backoffice, #mms]
foreign_keys:
referenced_by:
  - [[Pro_MMS_Link_Technician_Assistant]]
support_relevance: high
last_verified: 2026-07-05
---
# MMS_Link_Technician_Assistant


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| TechnicianID | int | NO | ✓ |  |  |
| AssistantID | int | NO | ✓ |  |  |
## Primary Key
CompanyID
TechnicianID
AssistantID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_MMS_Link_Technician_Assistant]]

**Writes (1):**
- [[Pro_MMS_Link_Technician_Assistant]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Visit not closed**: Support visit still open — technician forgot to close
- **Missing spare parts**: Maintenance order requires parts not in technician stock
- **Schedule conflict**: Multiple visits assigned same time slot — dispatch needs review

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
