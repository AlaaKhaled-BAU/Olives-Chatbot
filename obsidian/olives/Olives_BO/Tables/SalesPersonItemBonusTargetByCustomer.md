---
type: table
database: Olives_BO
name: SalesPersonItemBonusTargetByCustomer
schema: dbo
tags: [#backoffice, #customer, #inventory, #sales]
foreign_keys:
referenced_by:
  - [[Pro_SalesPersonItemBounceTargetByCustomer]]
support_relevance: high
last_verified: 2026-07-05
---
# SalesPersonItemBonusTargetByCustomer


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonitembonustargetbycustomer records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| SalesPersonID | int | NO | ✓ |  |  |
| TargetYear | smallint | NO | ✓ |  |  |
| CustomerID | bigint | NO | ✓ |  |  |
| ItemCode | nvarchar | YES | ✓ |  |  |
| UnitID | nvarchar | YES | ✓ |  |  |
| M1 | float | YES |  |  |  |
| M2 | float | YES |  |  |  |
| M3 | float | YES |  |  |  |
| M4 | float | YES |  |  |  |
| M5 | float | YES |  |  |  |
| M6 | float | YES |  |  |  |
| M7 | float | YES |  |  |  |
| M8 | float | YES |  |  |  |
| M9 | float | YES |  |  |  |
| M10 | float | YES |  |  |  |
| M11 | float | YES |  |  |  |
| M12 | float | YES |  |  |  |
## Primary Key
CompanyID
SalesPersonID
TargetYear
CustomerID
ItemCode
UnitID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_SalesPersonItemBounceTargetByCustomer]]

**Writes (1):**
- [[Pro_SalesPersonItemBounceTargetByCustomer]]

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
