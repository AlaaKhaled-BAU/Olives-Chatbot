---
type: table
database: Olives_BO
name: CustomersPaymentTypesLink
schema: dbo
tags: [#backoffice, #billing, #customer, #reference]
foreign_keys:
referenced_by:
  - [[Pro_SalesPersonBonusLimit]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomersPaymentTypesLink


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customerspaymenttypeslink records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| PaymentType | int | NO | ✓ |  |  |
| CustomerID | bigint | NO | ✓ |  |  |
## Primary Key
CompanyID
PaymentType
CustomerID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_SalesPersonBonusLimit]]

**Writes (1):**
- [[Pro_SalesPersonBonusLimit]]

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
