---
type: table
database: OSFA_DB
name: OT_SalesmanStockDF
schema: dbo
tags: [#inventory, #mobile, #sales]
foreign_keys:
  - [[OT_SalesmanStockHF]]
referenced_by:
  - [[GetSalesmanStockOnline]]
  - [[OT_SalesmanStockDF_CheckExist]]
  - [[OT_SalesmanStockDF_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_SalesmanStockDF



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ | ✓ | [[OT_SalesmanStockHF]] |
| VouYear | smallint | NO | ✓ | ✓ | [[OT_SalesmanStockHF]] |
| VouNo | int | NO | ✓ | ✓ | [[OT_SalesmanStockHF]] |
| ItemNo | varchar | YES | ✓ |  |  |
| UnitCode | varchar | YES | ✓ |  |  |
| BeginQty | money | NO |  |  |  |
| CurrQty | money | NO |  |  |  |
| Qty | money | NO |  |  |  |
| Notes | nvarchar | YES |  |  |  |
## Primary Key
CompNo
VouYear
VouNo
ItemNo
UnitCode
## Foreign Keys
CompNo, VouYear, VouNo -> [[OT_SalesmanStockHF]](CompNo, VouYear, VouNo)
## Impact / Procedures Using This Table

**Reads (3):**
- [[GetSalesmanStockOnline]]
- [[OT_SalesmanStockDF_CheckExist]]
- [[OT_SalesmanStockDF_Insert]]

**Writes (1):**
- [[OT_SalesmanStockDF_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
