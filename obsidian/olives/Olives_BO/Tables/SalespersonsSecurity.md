---
type: table
database: Olives_BO
name: SalespersonsSecurity
schema: dbo
tags: [#auth, #backoffice, #sales]
foreign_keys:
  - [[Companies]]
  - [[SalesPersons]]
referenced_by:
  - [[Pro_SalespersonsSecurity]]
  - [[Pro_SalespersonsSecurity_Android]]
support_relevance: high
last_verified: 2026-07-05
---
# SalespersonsSecurity


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonssecurity records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| SalespersonID | int | NO | ✓ | ✓ | [[SalesPersons]] |
| UserID | nvarchar | YES |  |  |  |
| Pass | nvarchar | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| LastPassChangeDate | smalldatetime | YES |  |  |  |
| LastActivationCodeChangeDate | smalldatetime | YES |  |  |  |
## Primary Key
CompanyID
SalespersonID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, SalespersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_SalespersonsSecurity]]
- [[Pro_SalespersonsSecurity_Android]]

**Writes (2):**
- [[Pro_SalespersonsSecurity]]
- [[Pro_SalespersonsSecurity_Android]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
