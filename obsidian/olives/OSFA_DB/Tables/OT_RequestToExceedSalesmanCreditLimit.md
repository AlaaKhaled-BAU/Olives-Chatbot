---
type: table
database: OSFA_DB
name: OT_RequestToExceedSalesmanCreditLimit
schema: dbo
tags: [#billing, #mobile, #sales, #workflow]
foreign_keys:
referenced_by:
  - [[OT_RequestToExceedSalesmanCreditLimit_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_RequestToExceedSalesmanCreditLimit



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| InvoiceAmount | float | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsPosted | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| SalesmanCreditLimit | float | YES |  |  |  |
| SalesmanBanalce | float | YES |  |  |  |
| ExceedAmount | float | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_RequestToExceedSalesmanCreditLimit_Insert]]

**Writes (1):**
- [[OT_RequestToExceedSalesmanCreditLimit_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
