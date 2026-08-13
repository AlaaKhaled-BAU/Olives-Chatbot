---
type: table
database: Olives_BO
name: CustomersItemsAssigment
schema: dbo
tags: [#backoffice, #customer, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
  - [[Items]]
  - [[Positions]]
referenced_by:
  - [[Bajali_SAP_Integ]]
  - [[ECO_Land_SAP_Integ]]
  - [[GArrow_SAP_Integ]]
  - [[Pro_CustomersItemsAssigment]]
  - [[Spartan_SAP_Integ]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomersItemsAssigment


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customersitemsassigment records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Positions]] |
| PositionsID | int | NO | ✓ | ✓ | [[Positions]] |
| CustomerID | bigint | NO | ✓ | ✓ | [[Customers]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
## Primary Key
CompanyID
PositionsID
CustomerID
ItemCode
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, PositionsID -> [[Positions]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (5):**
- [[Bajali_SAP_Integ]]
- [[ECO_Land_SAP_Integ]]
- [[GArrow_SAP_Integ]]
- [[Pro_CustomersItemsAssigment]]
- [[Spartan_SAP_Integ]]

**Writes (4):**
- [[Bajali_SAP_Integ]]
- [[ECO_Land_SAP_Integ]]
- [[GArrow_SAP_Integ]]
- [[Pro_CustomersItemsAssigment]]

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
