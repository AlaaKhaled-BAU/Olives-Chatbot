---
type: table
database: Olives_BO
name: Report5CustomersExcemptions
schema: dbo
tags: [#backoffice, #customer, #reporting]
foreign_keys:
referenced_by:
  - [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
  - [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
support_relevance: high
last_verified: 2026-07-05
---
# Report5CustomersExcemptions


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores report5customersexcemptions records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | YES |  |  |  |
| CustomerID | nvarchar | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
- [[Rpt_SalesmanTimeSpentPerCustomerQima7]]

**Writes (0):**
_None_

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
- [[Olives_BO/Procedures/DashBoard_ExceptionsIssues]]
