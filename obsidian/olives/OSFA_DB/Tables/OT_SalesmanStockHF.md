---
type: table
database: OSFA_DB
name: OT_SalesmanStockHF
schema: dbo
tags: [#inventory, #mobile, #sales]
foreign_keys:
referenced_by:
  - [[GetSalesmanStockOnline]]
  - [[OT_SalesmanStockHF_CheckExist]]
  - [[OT_SalesmanStockHF_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_SalesmanStockHF



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| VouYear | smallint | NO | ✓ |  |  |
| VouNo | int | NO | ✓ |  |  |
| VouDate | smalldatetime | YES |  |  |  |
| SalesmanNo | int | YES |  |  |  |
| Posted | bit | NO |  |  |  |
| Notes | varchar | YES |  |  |  |
| GPSX | varchar | YES |  |  |  |
| GPSY | varchar | YES |  |  |  |
| RouteID | int | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| ExtraNote | nvarchar | YES |  |  |  |
## Primary Key
CompNo
VouYear
VouNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[GetSalesmanStockOnline]]
- [[OT_SalesmanStockHF_CheckExist]]
- [[OT_SalesmanStockHF_Insert]]

**Writes (1):**
- [[OT_SalesmanStockHF_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
