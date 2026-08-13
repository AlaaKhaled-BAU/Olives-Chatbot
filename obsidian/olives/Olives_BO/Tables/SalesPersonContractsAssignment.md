---
type: table
database: Olives_BO
name: SalesPersonContractsAssignment
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
  - [[Contracts]]
  - [[Positions]]
referenced_by:
  - [[Pro_SalesPersonContractsAssignment]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonContractsAssignment


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersoncontractsassignment records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Positions]] |
| PositionsID | int | NO | ✓ | ✓ | [[Positions]] |
| ContractID | nvarchar | YES | ✓ | ✓ | [[Contracts]] |
## Primary Key
CompanyID
PositionsID
ContractID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ContractID -> [[Contracts]](CompanyID, ContractID)
CompanyID, PositionsID -> [[Positions]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_SalesPersonContractsAssignment]]

**Writes (1):**
- [[Pro_SalesPersonContractsAssignment]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
