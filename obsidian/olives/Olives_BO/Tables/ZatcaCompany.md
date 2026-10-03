---
type: table
database: Olives_BO
name: ZatcaCompany
schema: dbo
tags: [#backoffice, #legal]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# ZatcaCompany


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores zatcacompany records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| IdentificationID | nvarchar | YES | ✓ |  |  |
| TaxNumber | nvarchar | YES | ✓ |  |  |
| IdentificationSchemeID | nvarchar | YES |  |  |  |
| StreetName | nvarchar | YES |  |  |  |
| BuildingNumber | nvarchar | YES |  |  |  |
| CityName | nvarchar | YES |  |  |  |
| PostalZone | nvarchar | YES |  |  |  |
| CitySubdiVisionName | nvarchar | YES |  |  |  |
| RegistrationName | nvarchar | YES |  |  |  |
| ModeID | int | YES |  |  |  |
| BranchID | int | YES |  |  |  |
| Location | nvarchar | YES |  |  |  |
| BusinessCategory | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
IdentificationID
TaxNumber
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**

**Writes (0):**
_None_

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
