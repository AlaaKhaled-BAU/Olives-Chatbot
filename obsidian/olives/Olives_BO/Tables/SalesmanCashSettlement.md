---
type: table
database: Olives_BO
name: SalesmanCashSettlement
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
  - [[SalesPersons]]
referenced_by:
  - [[Pro_SalesmanCashSettlement]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesmanCashSettlement


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salesmancashsettlement records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| ID | decimal | YES | ✓ |  |  |
| SalesmanID | int | NO |  | ✓ | [[SalesPersons]] |
| CurrencyID | int | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| TotalAmount | float | YES |  |  |  |
| PaidAmount | float | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, SalesmanID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_SalesmanCashSettlement]]

**Writes (1):**
- [[Pro_SalesmanCashSettlement]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
