---
type: table
database: OSFA_DB
name: OT_CompanyBranches
schema: dbo
tags: [#mobile]
foreign_keys:
referenced_by:
  - [[OT_AppService]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_CompanyBranches



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| Address | nvarchar | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_AppService]]

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
- [[OSFA_DB/Tables/OT_BonusItemRanges]]
- [[OSFA_DB/Tables/OT_GeoLevel5]]
- [[OSFA_DB/Tables/OT_BonusItemPriority]]
- [[OSFA_DB/Tables/CompetitiveItemsImage]]
- [[OSFA_DB/Tables/OT_PromotionsRangeInputOutput]]
- [[OSFA_DB/Tables/OT_SystemOptionsLists]]
- [[OSFA_DB/Tables/OT_GeoLevel3]]
- [[OSFA_DB/Tables/OT_CustomerImage]]
- [[OSFA_DB/Tables/OT_CustomersPromotionsExceptions]]
- [[OSFA_DB/Tables/OT_JsonLog_Tmp]]
- [[OSFA_DB/Tables/OT_SystemOptionsTypes]]
- [[OSFA_DB/Tables/Invt_ItemsImage]]
- [[OSFA_DB/Tables/OT_GeoLevel2]]
- [[OSFA_DB/Tables/OT_GeoLevel4]]
- [[OSFA_DB/Tables/OT_PromotionsGroupsCustomersLink]]
- [[OSFA_DB/Tables/OT_Actions]]
- [[OSFA_DB/Tables/OT_Payment_Invoices_Test]]
