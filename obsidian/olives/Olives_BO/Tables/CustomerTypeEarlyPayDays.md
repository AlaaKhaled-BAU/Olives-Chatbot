---
type: table
database: Olives_BO
name: CustomerTypeEarlyPayDays
schema: dbo
tags: [#backoffice, #customer, #reference]
foreign_keys:
referenced_by:
  - [[Pro_CustomerTypeEarlyPayDays]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomerTypeEarlyPayDays


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customertypeearlypaydays records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| CustomerTypeID | int | NO | ✓ |  |  |
| DiscountEarlyPayDays | int | NO | ✓ |  |  |
| EarlyRepaymentDiscountPerc | float | YES |  |  |  |
## Primary Key
CompanyID
CustomerTypeID
DiscountEarlyPayDays
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_CustomerTypeEarlyPayDays]]

**Writes (1):**
- [[Pro_CustomerTypeEarlyPayDays]]

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
