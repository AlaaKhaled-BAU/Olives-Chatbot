---
type: table
database: Olives_BO
name: CustomersItemsLog
schema: dbo
tags: [#backoffice, #customer, #inventory, #log]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
  - [[Items]]
  - [[SalesPersons]]
referenced_by:
support_relevance: low
last_verified: 2026-07-05
---
# CustomersItemsLog


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customersitemslog records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | bigint | YES | ✓ |  |  |
| CompanyID | smallint | YES |  | ✓ | [[SalesPersons]] |
| CustomerID | bigint | YES |  | ✓ | [[Customers]] |
| SalesPersonID | int | YES |  | ✓ | [[SalesPersons]] |
| ItemCode | nvarchar | YES |  | ✓ | [[Items]] |
| VisitDate | smalldatetime | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
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
- [[Olives_BO/Tables/Tech_CustomizationPerformedTasks]]
- [[Olives_BO/Tables/forupdateonly]]
- [[Olives_BO/Tables/EmpDetails]]
- [[Olives_BO/Procedures/GetCustomerAssets]]
- [[Olives_BO/Procedures/EncodeArabicToUTF8DataFromOSFA_API]]
- [[Olives_BO/Procedures/SMSSEND_ZUMOT]]
- [[Olives_BO/Procedures/Test_Banks]]
