---
type: table
database: Olives_BO
name: Customers2
schema: dbo
tags: [#backoffice, #customer]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# Customers2


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customers2 records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO |  |  |  |
| Name | nvarchar | YES |  |  |  |
| TypeID | int | YES |  |  |  |
| LocationID | int | YES |  |  |  |
| Salesmanno | int | YES |  |  |  |
| PaymentType | int | YES |  |  |  |
| Pricelist | int | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| ISAdded111 | bit | YES |  |  |  |
## Primary Key
(none)
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
- [[Glossary]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[NewCustomerDefaultValue]]
- [[CustomerTargetsDetails]]
- [[NewCustomerSpecialFields_Def]]
