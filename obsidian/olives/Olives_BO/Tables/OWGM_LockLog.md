---
type: table
database: Olives_BO
name: OWGM_LockLog
schema: dbo
tags: [#backoffice, #log]
foreign_keys:
referenced_by:
  - [[OWGM_AppService]]
support_relevance: low
last_verified: 2026-07-05
---
# OWGM_LockLog


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores owgm locklog records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| GateUserID | int | YES |  |  |  |
| LogDateTime | datetime | YES |  |  |  |
| Barcode | nvarchar | YES |  |  |  |
| DeviceTransType | int | YES |  |  |  |
| CurrentTransType | int | YES |  |  |  |
| LockReason | varchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OWGM_AppService]]

**Writes (1):**
- [[OWGM_AppService]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Rapid growth**: Table size growing fast — archive old records periodically
- **Orphan log entries**: No corresponding source transaction — investigate data source
- **No cleanup**: No purge job configured — disk space may fill up

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Olives_BO/Tables/MMS_DV_ErrorLog]]
- [[Olives_BO/Tables/LogActions]]
