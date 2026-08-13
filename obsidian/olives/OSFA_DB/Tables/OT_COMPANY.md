---
type: table
database: OSFA_DB
name: OT_COMPANY
schema: dbo
tags: [#mobile]
foreign_keys:
referenced_by:
  - [[OT_AppService]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_COMPANY



## Business Purpose


- `comp_num` [smallint] (NOT NULL) - `SalesmanNo` [int] (NOT NULL) - `comp_name` [varchar](100) - `comp_ename` [varchar](100) - `comp_addr1` [varchar](200) - `comp_eaddr1` [varchar](200) - `comp_addr2` [varchar](200) - `comp_eaddr2` [varchar](200) - `comp_tel1` [varchar](50) - `comp_tel2` [varchar](50) - `comp_fax` [varchar](50) - `comp_tlx` [varchar](50) - `comp_logo` [image] - `SalesTaxNo` [varchar](50) - `NumberSavedFraction` [int] - `TruncRoundValue` [int] - `Notes` [nvarchar](500) - `CurrencyID` [int] - `ServerDate` [nvarchar](50) - `ClientActive` [nvarchar](50) - `CID` [nvarchar](50)

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| comp_num | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| comp_name | varchar | YES |  |  |  |
| comp_ename | varchar | YES |  |  |  |
| comp_addr1 | varchar | YES |  |  |  |
| comp_eaddr1 | varchar | YES |  |  |  |
| comp_addr2 | varchar | YES |  |  |  |
| comp_eaddr2 | varchar | YES |  |  |  |
| comp_tel1 | varchar | YES |  |  |  |
| comp_tel2 | varchar | YES |  |  |  |
| comp_fax | varchar | YES |  |  |  |
| comp_tlx | varchar | YES |  |  |  |
| comp_logo | image | YES |  |  |  |
| SalesTaxNo | varchar | YES |  |  |  |
| NumberSavedFraction | int | YES |  |  |  |
| TruncRoundValue | int | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| CurrencyID | int | YES |  |  |  |
| ServerDate | nvarchar | YES |  |  |  |
| ClientActive | nvarchar | YES |  |  |  |
| CID | nvarchar | YES |  |  |  |
## Primary Key
comp_num
SalesmanNo
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
