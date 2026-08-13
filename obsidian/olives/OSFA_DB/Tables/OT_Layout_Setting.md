---
type: table
database: OSFA_DB
name: OT_Layout_Setting
schema: dbo
tags: [#mobile]
foreign_keys:
referenced_by:
  - [[Pro_OT_Layout_Setting]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Company-Setup
---
# OT_Layout_Setting



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| LayoutId | int | NO | ✓ |  |  |
| PropertyID | int | NO | ✓ |  |  |
| LayoutName | nvarchar | YES |  |  |  |
| Description | nvarchar | YES |  |  |  |
| Value1 | nvarchar | YES |  |  |  |
| Value2 | nvarchar | YES |  |  |  |
## Primary Key
CompNo
LayoutId
PropertyID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_OT_Layout_Setting]]

**Writes (1):**
- [[Pro_OT_Layout_Setting]]

## Estimated Size / Volatility
Typical business table
## PropertyID Reference


| PropertyID | Description | Value1 | Value2 |
|---|---|---|---|
| 1 | Layout Width | Print area width (numeric) | — |
| **2** | **Font** | **Font family name (e.g. Arial, Calibri)** | **Font size (numeric, e.g. 8, 10, 12)** |
| 3 | Logo Size | Logo width | Logo height |
| 4 | Sewoo 4 inch Page Width | Page width for 4-inch Sewoo printers | — |

## Layout Assignment Flow


1. BO user assigns a `LayoutId` to a salesman via **Salespersons → Edit → Layout Design**
2. OSFA tablet syncs and reads the assigned `LayoutId` from `OT_SystemOptions`
3. When printing, the OSFA app reads this table for the layout's properties
4. PropertyID=2 (Font) determines printed text appearance

## Common Issues


- **Font not changing after update**: Verify the correct `LayoutId` is assigned to the salesman's `OT_SystemOptions` and re-sync the tablet
- **Layout not found**: The `LayoutId` must exist in this table before assigning it to a salesman
- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
