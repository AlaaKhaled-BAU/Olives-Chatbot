---
type: table
database: Olives_BO
name: VanTransferHeader
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
  - [[Companies]]
  - [[SalesPersons]]
referenced_by:
  - [[Alpha_Integ_SendVanTransfer]]
  - [[OT_ImportVanTransfer]]
support_relevance: high
last_verified: 2026-07-05
---
# VanTransferHeader


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores vantransferheader records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| FromSalespersonID | int | NO |  | ✓ | [[SalesPersons]] |
| ToSalespersonID | int | NO |  | ✓ | [[SalesPersons]] |
| OrderDate | smalldatetime | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, FromSalespersonID -> [[SalesPersons]](CompanyID, ID)
CompanyID, ToSalespersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Alpha_Integ_SendVanTransfer]]
- [[OT_ImportVanTransfer]]

**Writes (2):**
- [[Alpha_Integ_SendVanTransfer]]
- [[OT_ImportVanTransfer]]

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Shared/Runbooks/Van-Stock-Mismatch]]
