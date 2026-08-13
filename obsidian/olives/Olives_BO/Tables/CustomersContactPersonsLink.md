---
type: table
database: Olives_BO
name: CustomersContactPersonsLink
schema: dbo
tags: [#backoffice, #customer]
foreign_keys:
referenced_by:
  - [[OT_ImportNewCust]]
  - [[Pro_AssetTransfer]]
  - [[Pro_Customers]]
  - [[Pro_CustomersAndAssets]]
  - [[Pro_CustomersContactPersons]]
  - [[Rpt_CustomerNameByLocation]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomersContactPersonsLink


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customerscontactpersonslink records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| CustomerID | bigint | NO | ✓ |  |  |
| ContactPersonID | int | NO | ✓ |  |  |
| ID | bigint | YES | ✓ |  |  |
## Primary Key
CompanyID
CustomerID
ContactPersonID
ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (5):**
- [[Pro_AssetTransfer]]
- [[Pro_Customers]]
- [[Pro_CustomersAndAssets]]
- [[Pro_CustomersContactPersons]]
- [[Rpt_CustomerNameByLocation]]

**Writes (2):**
- [[OT_ImportNewCust]]
- [[Pro_CustomersContactPersons]]

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
