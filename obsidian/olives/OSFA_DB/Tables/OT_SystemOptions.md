---
type: table
database: OSFA_DB
name: OT_SystemOptions
schema: dbo
tags: [#mobile]
foreign_keys:
referenced_by:
  - [[ADNAN_PRO_COPY_SYSTEMOPTIONS]]
  - [[OT_CopySystemOption]]
  - [[OT_GetSystemOptions]]
  - [[OT_RestoreSystemOptionsclass]]
  - [[Technical_CopySystemoptionsForSeveralSalespersons]]
  - [[Technical_OT_CopySystemOption]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Data-Sync-Cycle
---
# OT_SystemOptions



## Business Purpose


Tablet-side configuration settings controlling app behavior and feature availability.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| Op_ID | int | NO | ✓ |  |  |
| SalesmanNo | smallint | NO | ✓ |  |  |
| Op_Desc | varchar | YES |  |  |  |
| Op_Value | varchar | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| PrinterType | int | YES |  |  |  |
## Primary Key
CompNo
Op_ID
SalesmanNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (6):**
- [[ADNAN_PRO_COPY_SYSTEMOPTIONS]]
- [[OT_CopySystemOption]]
- [[OT_GetSystemOptions]]
- [[OT_RestoreSystemOptionsclass]]
- [[Technical_CopySystemoptionsForSeveralSalespersons]]
- [[Technical_OT_CopySystemOption]]

**Writes (3):**
- [[OT_CopySystemOption]]
- [[OT_RestoreSystemOptionsclass]]
- [[Technical_OT_CopySystemOption]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[Olives_BO/Procedures/CopySystemOption]]
- [[Olives_BO/Procedures/CopySystemOption_Delete_Insert_fromsalesmantosalesman]]
