---
type: table
database: OSFA_DB
name: OT_SalesmanDoneProcedures
schema: dbo
tags: [#mobile, #sales]
foreign_keys:
referenced_by:
  - [[OT_SalesmanDoneProcedures_CheckExist]]
  - [[OT_SalesmanDoneProcedures_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_SalesmanDoneProcedures



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
| TrDateTime | datetime | YES |  |  |  |
| IsPosted | bit | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
CustomerNo
ProcedureID
ProcedureDate
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_SalesmanDoneProcedures_CheckExist]]
- [[OT_SalesmanDoneProcedures_Insert]]

**Writes (1):**
- [[OT_SalesmanDoneProcedures_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
