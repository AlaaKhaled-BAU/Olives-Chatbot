---
type: table
database: Olives_BO
name: CustomerTargets
schema: dbo
tags: [#backoffice, #customer, #sales]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
  - [[TargetsTypes]]
referenced_by:
  - [[BO_Online_RptCustomerSalesTargetDetails]]
  - [[Niroukh_SalesPerTeamQ]]
  - [[Pro_CustomerTargets]]
  - [[Rpt_MonthlyCompareSalesTargetWithCustomer]]
  - [[Rpt_Niroukh_SalesPerTeamQ]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomerTargets


## Business Purpose

Sales performance targets and goals for sales measurement.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Customers]] |
| CustomerID | bigint | NO | ✓ | ✓ | [[Customers]] |
| TargetYear | smallint | NO | ✓ |  |  |
| TargetMonth | int | NO | ✓ |  |  |
| TargetTypeID | int | YES |  | ✓ | [[TargetsTypes]] |
| Amount | float | YES |  |  |  |
## Primary Key
CompanyID
CustomerID
TargetYear
TargetMonth
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
TargetTypeID -> [[TargetsTypes]](ID)
## Impact / Procedures Using This Table

**Reads (5):**
- [[BO_Online_RptCustomerSalesTargetDetails]]
- [[Niroukh_SalesPerTeamQ]]
- [[Pro_CustomerTargets]]
- [[Rpt_MonthlyCompareSalesTargetWithCustomer]]
- [[Rpt_Niroukh_SalesPerTeamQ]]

**Writes (1):**
- [[Pro_CustomerTargets]]

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
