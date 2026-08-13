---
type: table
database: Olives_BO
name: CustomersContactPersons
schema: dbo
tags: [#backoffice, #customer]
foreign_keys:
referenced_by:
  - [[Pro_AssetTransactionsList]]
  - [[Pro_AssetsDefinition]]
  - [[Pro_Customers]]
  - [[Pro_CustomersAndAssets]]
  - [[Pro_CustomersContactPersons]]
  - [[Rpt_AssetsByLocation]]
  - [[Rpt_CustomerNameByLocation]]
support_relevance: high
last_verified: 2026-07-05
---
# CustomersContactPersons


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores customerscontactpersons records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (7):**
- [[Pro_AssetTransactionsList]]
- [[Pro_AssetsDefinition]]
- [[Pro_Customers]]
- [[Pro_CustomersAndAssets]]
- [[Pro_CustomersContactPersons]]
- [[Rpt_AssetsByLocation]]
- [[Rpt_CustomerNameByLocation]]

**Writes (1):**
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
