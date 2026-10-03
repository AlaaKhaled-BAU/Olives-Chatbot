---
type: table
database: Olives_BO
name: CustomersMonthlyCollectionTarget
schema: dbo
tags: [#backoffice, #customer, #sales]
foreign_keys:
referenced_by:
  - [[DA_SalesTarget]]
  - [[Rpt_LuxuryItemsCustTarget]]
  - [[SalesmanInfo]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomersMonthlyCollectionTarget


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customersmonthlycollectiontarget records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| TargetMonth | smallint | NO | ✓ |  |  |
| TargetYear | smallint | NO | ✓ |  |  |
| SalesmanID | smallint | NO | ✓ |  |  |
| CustomerRef1 | nvarchar | YES | ✓ |  |  |
| CustomerRef2 | nvarchar | YES | ✓ |  |  |
## Primary Key
CompanyID
TargetMonth
TargetYear
SalesmanID
CustomerRef1
CustomerRef2
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[DA_SalesTarget]]
- [[Rpt_LuxuryItemsCustTarget]]
- [[SalesmanInfo]]

**Writes (1):**

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
