---
type: table
database: OSFA_DB
name: OT_Cust_Survey_Answers
schema: dbo
tags: [#mobile, #survey]
foreign_keys:
referenced_by:
  - [[OT_Add_Cust_Survey_Answers]]
  - [[OT_TransSigns_Images_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_Cust_Survey_Answers



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| Cust_Survey_No | bigint | NO | ✓ |  |  |
| Question_No | int | NO | ✓ |  |  |
| Answer | varchar | YES |  |  |  |
## Primary Key
Cust_Survey_No
Question_No
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_Add_Cust_Survey_Answers]]
- [[OT_TransSigns_Images_Insert]]

**Writes (1):**
- [[OT_Add_Cust_Survey_Answers]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
