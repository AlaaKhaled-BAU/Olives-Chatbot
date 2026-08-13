---
type: table
database: OSFA_DB
name: OT_SalesmanProcedures
schema: dbo
tags: [#mobile, #sales]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_SalesmanProcedures



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| CustomerNo | bigint | NO | ✓ |  |  |
| ProcedureID | int | NO | ✓ |  |  |
| ProcedureDate | smalldatetime | NO | ✓ |  |  |
| ProcedureName | nvarchar | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
CustomerNo
ProcedureID
ProcedureDate
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[OT_LinkedSalesman]]
- [[OT_PromotionsCondUnCodInput]]
- [[OT_PromotionsSalesmanGroupsLink]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
