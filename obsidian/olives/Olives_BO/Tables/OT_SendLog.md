---
type: table
database: Olives_BO
name: OT_SendLog
schema: dbo
tags: [#backoffice, #log, #mobile]
foreign_keys:
referenced_by:
  - [[OT_SENDSALESMANDATAFROMORDERS]]
  - [[OT_SendSalesmanData]]
  - [[Pro_TransfersOrdersHeaders]]
  - [[SalesmanInfo]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: low
last_verified: 2026-07-05
---
# OT_SendLog


## Business Purpose

Integration data store for syncing sales transactions with external systems.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| SalesmanNo | int | YES |  |  |  |
| SysDate | datetime | YES |  |  |  |
| LogText | nvarchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (5):**
- [[OT_SENDSALESMANDATAFROMORDERS]]
- [[OT_SendSalesmanData]]
- [[Pro_TransfersOrdersHeaders]]
- [[SalesmanInfo]]
- [[WF_AddWorkFlowLevels]]

**Writes (2):**
- [[OT_SendSalesmanData]]
- [[Pro_TransfersOrdersHeaders]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Rapid growth**: Table size growing fast — archive old records periodically
- **Orphan log entries**: No corresponding source transaction — investigate data source
- **No cleanup**: No purge job configured — disk space may fill up

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
