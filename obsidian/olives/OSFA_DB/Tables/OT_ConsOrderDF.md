---
type: table
database: OSFA_DB
name: OT_ConsOrderDF
schema: dbo
tags: [#mobile, #order]
foreign_keys:
  - [[OT_ConsOrderHF]]
referenced_by:
  - [[OT_ConsOrderDF_CheckExist]]
  - [[OT_ConsOrderDF_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_ConsOrderDF



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ | ✓ | [[OT_ConsOrderHF]] |
| OrderYear | smallint | NO | ✓ | ✓ | [[OT_ConsOrderHF]] |
| OrderNo | int | NO | ✓ | ✓ | [[OT_ConsOrderHF]] |
| VouType | int | NO | ✓ | ✓ | [[OT_ConsOrderHF]] |
| ItemNo | varchar | YES | ✓ |  |  |
| UnitCode | varchar | YES | ✓ |  |  |
| Qty | money | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
## Primary Key
CompNo
OrderYear
OrderNo
VouType
ItemNo
UnitCode
## Foreign Keys
CompNo, OrderYear, OrderNo, VouType -> [[OT_ConsOrderHF]](CompNo, OrderYear, OrderNo, VouType)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_ConsOrderDF_CheckExist]]
- [[OT_ConsOrderDF_Insert]]

**Writes (1):**
- [[OT_ConsOrderDF_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
