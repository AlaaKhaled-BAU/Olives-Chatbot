---
type: table
database: OSFA_DB
name: OT_CustomersItemQtyLimit
schema: dbo
tags: [#customer, #inventory, #mobile]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_CustomersItemQtyLimit



## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Tablet-side data table in OSFA_DB, synced to/from Back Office.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| CustomerID | bigint | NO | ✓ |  |  |
| ItemCode | nvarchar | YES | ✓ |  |  |
| SoldQtyLimit | float | YES |  |  |  |
| SoldQty | float | YES |  |  |  |
## Primary Key
CompanyID
SalesmanNo
CustomerID
ItemCode
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
- [[OT_StateAccBalance]]
- [[OT_StoreItemsQty_Main]]
- [[OT_LinkedSalesman]]

- [[OT_CustomersItemsAssigment]]
- [[OT_Banks]]
- [[OT_CompanyBranches]]
- [[Glossary]]
