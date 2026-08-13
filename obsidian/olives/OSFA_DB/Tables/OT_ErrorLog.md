---
type: table
database: OSFA_DB
name: OT_ErrorLog
schema: dbo
tags: [#log, #mobile]
foreign_keys:
referenced_by:
  - [[OT_InvoicesDelivery_Images_Insert]]
  - [[OT_InvoicesDelivery_Insert]]
support_relevance: low
last_verified: 2026-07-05
---
# OT_ErrorLog



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ID | bigint | YES | ✓ |  |  |
| CompNo | smallint | YES |  |  |  |
| SalesmanNo | int | YES |  |  |  |
| ErrDesc | ntext | YES |  |  |  |
| SysDate | smalldatetime | YES |  |  |  |
## Primary Key
ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_InvoicesDelivery_Images_Insert]]
- [[OT_InvoicesDelivery_Insert]]

**Writes (2):**
- [[OT_InvoicesDelivery_Images_Insert]]
- [[OT_InvoicesDelivery_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Rapid growth**: Table size growing fast — archive old records periodically
- **Orphan log entries**: No corresponding source transaction — investigate data source
- **No cleanup**: No purge job configured — disk space may fill up

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
