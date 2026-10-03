---
type: table
database: Olives_BO
name: CustomersBalanceAging
schema: dbo
tags: [#backoffice, #customer, #inventory]
foreign_keys:
referenced_by:
  - [[RptOnlineRpt_CustAging]]
  - [[Rpt_CustomerAccountStatement_Sukhtian]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomersBalanceAging


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customersbalanceaging records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| CustomerID | bigint | NO | ✓ |  |  |
| BalanceAge1 | float | YES |  |  |  |
| BalanceAge2 | float | YES |  |  |  |
| BalanceAge3 | float | YES |  |  |  |
| BalanceAge4 | float | YES |  |  |  |
| BalanceAge5 | float | YES |  |  |  |
| BalanceAge6 | float | YES |  |  |  |
| BalanceAge7 | float | YES |  |  |  |
| BalanceAge8 | float | YES |  |  |  |
| BalanceAge9 | float | YES |  |  |  |
| BalanceAge10 | float | YES |  |  |  |
## Primary Key
CompanyID
CustomerID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[RptOnlineRpt_CustAging]]
- [[Rpt_CustomerAccountStatement_Sukhtian]]

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
