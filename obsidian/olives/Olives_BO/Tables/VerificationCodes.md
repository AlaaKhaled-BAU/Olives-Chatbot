---
type: table
database: Olives_BO
name: VerificationCodes
schema: dbo
tags: [#backoffice, #reference]
foreign_keys:
  - [[Companies]]
  - [[SalesPersons]]
referenced_by:
  - [[Pro_SalespersonsSecurity_Android]]
  - [[Pro_VerificationCodes]]
support_relevance: high
last_verified: 2026-07-05
---
# VerificationCodes


## Business Purpose

Classification or reference codes for sales data categorization.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | YES |  | ✓ | [[SalesPersons]] |
| AutoID | numeric | YES | ✓ |  |  |
| VerificationType | int | YES |  |  |  |
| UserID | nvarchar | YES |  |  |  |
| SalespersonID | int | YES |  | ✓ | [[SalesPersons]] |
| VerificationCode | int | YES |  |  |  |
| IsUsed | bit | YES |  |  |  |
| CreateDateTime | smalldatetime | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, SalespersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_SalespersonsSecurity_Android]]
- [[Pro_VerificationCodes]]

**Writes (2):**
- [[Pro_SalespersonsSecurity_Android]]
- [[Pro_VerificationCodes]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing reference values**: Required dropdown items not present — selection fails on tablet
- **Duplicate codes**: Same code used for different descriptions — mapping ambiguity
- **Orphan references**: Referenced by deleted records — FK violation on delete attempt

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
