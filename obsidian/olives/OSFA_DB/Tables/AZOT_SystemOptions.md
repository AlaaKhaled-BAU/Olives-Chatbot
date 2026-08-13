---
type: table
database: OSFA_DB
name: AZOT_SystemOptions
schema: dbo
tags: [#mobile]
foreign_keys:
referenced_by:
  - [[ADNAN_PRO_COPY_SYSTEMOPTIONS]]
support_relevance: high
last_verified: 2026-07-05
---
# AZOT_SystemOptions



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| DATE | datetime | NO |  |  |  |
| ChangeID | int | NO |  |  |  |
| CompNo | smallint | NO |  |  |  |
| Op_ID | int | NO |  |  |  |
| SalesmanNo | smallint | NO |  |  |  |
| Op_Desc | varchar | YES |  |  |  |
| Op_Value | varchar | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| PrinterType | int | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[ADNAN_PRO_COPY_SYSTEMOPTIONS]]

**Writes (0):**
_None_

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
