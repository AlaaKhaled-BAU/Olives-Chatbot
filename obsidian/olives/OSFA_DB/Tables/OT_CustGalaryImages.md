---
type: table
database: OSFA_DB
name: OT_CustGalaryImages
schema: dbo
tags: [#mobile]
foreign_keys:
referenced_by:
  - [[OT_Add_CustGalaryImages]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_CustGalaryImages



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ImageID | bigint | YES | ✓ |  |  |
| CompNo | smallint | NO |  |  |  |
| SalesmanNo | smallint | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| ImageData | image | YES |  |  |  |
| ImageDate | smalldatetime | YES |  |  |  |
| GPSX | varchar | YES |  |  |  |
| GPSY | varchar | YES |  |  |  |
| ImageType_ID | int | YES |  |  |  |
| IsApproved | bit | YES |  |  |  |
| PlanogramFileAutoID | bigint | YES |  |  |  |
| ImageSeqType | int | YES |  |  |  |
| Notes | varchar | YES |  |  |  |
| RejectReasonID | int | YES |  |  |  |
| RejectReason | nvarchar | YES |  |  |  |
| IsValidate | bit | YES |  |  |  |
## Primary Key
ImageID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_Add_CustGalaryImages]]

**Writes (1):**
- [[OT_Add_CustGalaryImages]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Sync conflict**: Same record modified on tablet and BO simultaneously — last-write-wins may lose data
- **Orphan tablet records**: Row with no linked BO counterpart — check sync log
- **Duplicate TabletSysID**: Same tablet transaction inserted twice — run dedup check
- **Missing IsPosted flag**: Data not synced to BO — check tablet connectivity

## Cross-Database
Also exists as a **procedure** in Back Office (cross-type name collision): [[Olives_BO/Procedures/OT_CustGalaryImages]]. This note is the OSFA_DB tablet-side **table**; the BO note is the procedure that writes it.

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
