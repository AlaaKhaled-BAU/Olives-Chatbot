---
type: table
database: Olives_BO
name: VanTransferDetails
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[SalesPersons]]
  - [[VanTransferHeader]]
referenced_by:
  - [[OT_ImportVanTransfer]]
support_relevance: high
last_verified: 2026-07-05
---
# VanTransferDetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores vantransferdetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[VanTransferHeader]] |
| OrderYear | smallint | NO | ✓ | ✓ | [[VanTransferHeader]] |
| OrderNo | int | NO | ✓ | ✓ | [[VanTransferHeader]] |
| SalespersonID | int | NO | ✓ | ✓ | [[SalesPersons]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| UnitCode | nvarchar | YES | ✓ | ✓ | [[ItemsUnits]] |
| Quantity | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
SalespersonID
ItemCode
UnitCode
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitCode -> [[ItemsUnits]](CompanyID, ID)
CompanyID, SalespersonID -> [[SalesPersons]](CompanyID, ID)
CompanyID, OrderYear, OrderNo -> [[VanTransferHeader]](CompanyID, OrderYear, OrderNo)
## Impact / Procedures Using This Table

**Reads (0):**
_None_

**Writes (1):**
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
