---
type: table
database: Olives_BO
name: SalespersonsProcedures
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
  - [[Positions]]
referenced_by:
  - [[OT_ImportSalesmanDoneProcedures]]
  - [[Pro_SalesPersonDailyProcedure]]
  - [[Pro_SalespersonsProcedures]]
support_relevance: high
last_verified: 2026-07-05
---
# SalespersonsProcedures


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonsprocedures records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Positions]] |
| ProcedureID | int | NO | ✓ | ✓ | [[DailyProcedures]] |
| PositionID | int | NO | ✓ | ✓ | [[Positions]] |
| CustomerID | bigint | NO | ✓ | ✓ | [[Customers]] |
| ProcedureDate | smalldatetime | NO | ✓ |  |  |
| Status | bit | YES |  |  |  |
| TrDateTime | datetime | YES |  |  |  |
## Primary Key
CompanyID
ProcedureID
PositionID
CustomerID
ProcedureDate
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, ProcedureID -> [[DailyProcedures]](CompanyID, ID)
CompanyID, PositionID -> [[Positions]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_ImportSalesmanDoneProcedures]]
- [[Pro_SalesPersonDailyProcedure]]
- [[Pro_SalespersonsProcedures]]

**Writes (2):**
- [[OT_ImportSalesmanDoneProcedures]]
- [[Pro_SalespersonsProcedures]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
