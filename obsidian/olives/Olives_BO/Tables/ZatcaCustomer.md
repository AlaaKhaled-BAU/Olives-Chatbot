---
type: table
database: Olives_BO
name: ZatcaCustomer
schema: dbo
tags: [#backoffice, #customer, #legal]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# ZatcaCustomer


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores zatcacustomer records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| CustomerID | bigint | NO | ✓ |  |  |
| IdentificationID | nvarchar | YES | ✓ |  |  |
| TaxNumber | nvarchar | YES | ✓ |  |  |
| IdentificationSchemeID | nvarchar | YES |  |  |  |
| StreetName | nvarchar | YES |  |  |  |
| BuildingNumber | nvarchar | YES |  |  |  |
| CityName | nvarchar | YES |  |  |  |
| PostalZone | nvarchar | YES |  |  |  |
| CitySubdiVisionName | nvarchar | YES |  |  |  |
| RegistrationName | nvarchar | YES |  |  |  |
| CustomerType | int | NO |  |  |  |
## Primary Key
CompanyID
CustomerID
IdentificationID
TaxNumber
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate customers**: Multiple records with same name/phone created during sync — support agent sees duplicate entries in dropdowns
- **Orphan references**: Customer records referenced by transactions that were soft-deleted — causes FK violation on cleanup
- **Balance mismatch**: CustomerBalance field diverges from actual calculated balance — run reconciliation proc
- **Suspend stuck**: IsSuspended flag not clearing after payment — check WF approval chain
- **GPS not collected**: IsCollectedGPS flag false — affects route optimization

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[NewCustomerDefaultValue]]
- [[CustomerTargetsDetails]]
- [[NewCustomerSpecialFields_Def]]

- [[ZatcaMode]]
- [[ZatcaResultGenerateXml]]
- [[ZatcaCompany]]
