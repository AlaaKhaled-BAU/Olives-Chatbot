---
type: table
database: Olives_BO
name: MMS_Assistants
schema: dbo
tags: [#backoffice, #mms]
foreign_keys:
referenced_by:
  - [[Pro_MMS_Assistants]]
  - [[Pro_MMS_Link_Technician_Assistant]]
support_relevance: high
last_verified: 2026-07-05
---
# MMS_Assistants


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| AssistantsID | int | NO | ✓ |  |  |
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
## Primary Key
CompanyID
AssistantsID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_MMS_Assistants]]
- [[Pro_MMS_Link_Technician_Assistant]]

**Writes (1):**
- [[Pro_MMS_Assistants]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Visit not closed**: Support visit still open — technician forgot to close
- **Missing spare parts**: Maintenance order requires parts not in technician stock
- **Schedule conflict**: Multiple visits assigned same time slot — dispatch needs review

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
