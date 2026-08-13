---
type: table
database: Olives_BO
name: NewCustomerDefaultValue
schema: dbo
tags: [#backoffice, #customer]
foreign_keys:
  - [[Companies]]
  - [[PaymentsTypes]]
  - [[PriceLists]]
referenced_by:
  - [[Pro_NewCustomerDefaultValue]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Salesman-Onboarding
---
# NewCustomerDefaultValue


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores newcustomerdefaultvalue records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[PriceLists]] |
| BusinessUnitID | int | YES |  |  |  |
| PaymentTypeID | int | YES |  | ✓ | [[PaymentsTypes]] |
| PriceListID | int | YES |  | ✓ | [[PriceLists]] |
| CreditLimit | float | YES |  |  |  |
| DueDays | smallint | YES |  |  |  |
| ChqsDueDays | smallint | YES |  |  |  |
| AllowChqs | bit | YES |  |  |  |
| TaxInclude | bit | YES |  |  |  |
## Primary Key
CompanyID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, PaymentTypeID -> [[PaymentsTypes]](CompanyID, ID)
CompanyID, PriceListID -> [[PriceLists]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_NewCustomerDefaultValue]]

**Writes (1):**
- [[Pro_NewCustomerDefaultValue]]

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
