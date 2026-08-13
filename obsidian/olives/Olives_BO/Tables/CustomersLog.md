---
type: table
database: Olives_BO
name: CustomersLog
schema: dbo
tags: [#backoffice, #customer, #log]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
  - [[SalesPersons]]
referenced_by:
  - [[Pro_Customers]]
support_relevance: low
last_verified: 2026-07-05
---
# CustomersLog


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customerslog records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | bigint | YES | ✓ |  |  |
| CompanyID | smallint | YES |  | ✓ | [[SalesPersons]] |
| CustomerID | bigint | YES |  | ✓ | [[Customers]] |
| SalesPersonID | int | YES |  | ✓ | [[SalesPersons]] |
| VisitDate | smalldatetime | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (0):**
_None_

**Writes (1):**
- [[Pro_Customers]]

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
