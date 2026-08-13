---
type: table
database: OSFA_DB
name: OT_ProspectiveCustomer
schema: dbo
tags: [#customer, #mobile]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ProspectiveCustomer



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| CustomerNo | bigint | NO | ✓ |  |  |
| SalesmanNo | smallint | NO | ✓ |  |  |
| ArName | varchar | YES |  |  |  |
| EngName | varchar | YES |  |  |  |
| PrNo | smallint | YES |  |  |  |
| CustType | smallint | YES |  |  |  |
| LocationID | smallint | YES |  |  |  |
| CustomerBarcode | nvarchar | YES |  |  |  |
| X_COORD | nchar | YES |  |  |  |
| Y_COORD | nchar | YES |  |  |  |
| TaxInclude | bit | YES |  |  |  |
| Tel | varchar | YES |  |  |  |
| Email | varchar | YES |  |  |  |
| CustomerRef1 | nvarchar | YES |  |  |  |
| CreditCash | int | YES |  |  |  |
| ImageID | bigint | YES |  |  |  |
| DiscountPerc | float | YES |  |  |  |
| FullAddress | nvarchar | YES |  |  |  |
## Primary Key
CompNo
CustomerNo
SalesmanNo
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


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
- [[OT_CustomersGPSLocations]]
- [[OT_RequestToAddNewCustomer]]
- [[OT_ItemsQtyAvg]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
