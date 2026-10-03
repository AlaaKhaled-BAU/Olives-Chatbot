---
type: table
database: Olives_BO
name: DeviceReportsList
schema: dbo
tags: [#backoffice, #reporting]
foreign_keys:
referenced_by:
  - [[Fill_Sales_Device_Reports]]
  - [[Pro_SalesPersonsDevicePermissions]]
support_relevance: high
last_verified: 2026-07-05
---
# DeviceReportsList


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores devicereportslist records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ID | int | NO | ✓ |  |  |
| NameAR | nvarchar | YES |  |  |  |
| NameEN | nvarchar | YES |  |  |  |
| Reference1 | varchar | YES |  |  |  |
| Reference2 | varchar | YES |  |  |  |
| Sp_Name | varchar | YES |  |  |  |
## Primary Key
ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[Fill_Sales_Device_Reports]]
- [[Pro_SalesPersonsDevicePermissions]]

**Writes (0):**
_None_

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Olives_BO/Procedures/Rpt_VoidOrder]]
- [[Olives_BO/Procedures/DashBoard_ExceptionsIssues]]
- [[Olives_BO/Procedures/PRO_REPORT]]
- [[Olives_BO/Procedures/Rpt_Hakkak_TargetReportFromAlpha]]
