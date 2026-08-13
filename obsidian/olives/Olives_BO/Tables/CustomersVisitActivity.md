---
type: table
database: Olives_BO
name: CustomersVisitActivity
schema: dbo
tags: [#backoffice, #customer, #sales]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
  - [[Positions]]
referenced_by:
  - [[OT_ImportCustomerSurveyAnswers]]
  - [[Pro_CustomersVisitActivity]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomersVisitActivity


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customersvisitactivity records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Positions]] |
| CustomerID | bigint | NO | ✓ | ✓ | [[Customers]] |
| PositionsID | int | NO | ✓ | ✓ | [[Positions]] |
| VisitActivityInOrder | varchar | YES |  |  |  |
## Primary Key
CompanyID
CustomerID
PositionsID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, PositionsID -> [[Positions]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[OT_ImportCustomerSurveyAnswers]]
- [[Pro_CustomersVisitActivity]]

**Writes (1):**
- [[Pro_CustomersVisitActivity]]

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
