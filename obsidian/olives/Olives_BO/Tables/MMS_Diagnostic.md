---
type: table
database: Olives_BO
name: MMS_Diagnostic
schema: dbo
tags: [#backoffice, #mms]
foreign_keys:
referenced_by:
  - [[Pro_MMS_Diagnostic]]
  - [[Pro_MMS_GetDataForAndroid]]
  - [[Pro_MMS_OrderDetails]]
  - [[Pro_MMS_OrderDetailsForVisit]]
support_relevance: high
last_verified: 2026-07-05
---
# MMS_Diagnostic


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| DiagnosticID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ForeignName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| IsUnderWarranty | bit | YES |  |  |  |
## Primary Key
CompanyID
DiagnosticID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[Pro_MMS_Diagnostic]]
- [[Pro_MMS_GetDataForAndroid]]
- [[Pro_MMS_OrderDetails]]
- [[Pro_MMS_OrderDetailsForVisit]]

**Writes (1):**
- [[Pro_MMS_Diagnostic]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Visit not closed**: Support visit still open — technician forgot to close
- **Missing spare parts**: Maintenance order requires parts not in technician stock
- **Schedule conflict**: Multiple visits assigned same time slot — dispatch needs review

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
