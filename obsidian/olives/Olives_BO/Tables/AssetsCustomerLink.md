---
type: table
database: Olives_BO
name: AssetsCustomerLink
schema: dbo
tags: [#assets, #backoffice, #customer]
foreign_keys:
referenced_by:
  - [[PlanogramMediabyAssets]]
  - [[Pro_AssetTransfer]]
  - [[Pro_AssetsDefinition]]
  - [[Pro_AssetsWarehouseTransactionsCalc]]
  - [[Pro_Customers]]
  - [[Pro_CustomersAndAssets]]
  - [[Pro_IssueAssets]]
  - [[Pro_LocationsAndSalespersonsLink]]
  - [[Pro_WithdrawAssets]]
  - [[Rpt_AssetsByLocation]]
  - [[Rpt_NotSoldPerCateg]]
  - [[Rpt_SoldUnsoldPerRoute]]
  - [[Rpt_UnloadCustomersPerRoute]]
support_relevance: high
last_verified: 2026-07-05
---
# AssetsCustomerLink


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores assetscustomerlink records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| AssetID | bigint | NO | ✓ |  |  |
| CustomerID | bigint | YES |  |  |  |
| ContactID | bigint | YES |  |  |  |
## Primary Key
CompanyID
AssetID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (14):**
- [[PlanogramMediabyAssets]]
- [[Pro_AssetTransfer]]
- [[Pro_AssetsDefinition]]
- [[Pro_AssetsWarehouseTransactionsCalc]]
- [[Pro_Customers]]
- [[Pro_CustomersAndAssets]]
- [[Pro_IssueAssets]]
- [[Pro_LocationsAndSalespersonsLink]]
- [[Pro_WithdrawAssets]]
- [[Rpt_AssetsByLocation]]
- [[Rpt_NotSoldPerCateg]]
- [[Rpt_SoldUnsoldPerRoute]]
- [[Rpt_UnloadCustomersPerRoute]]

**Writes (3):**
- [[Pro_AssetTransfer]]
- [[Pro_AssetsWarehouseTransactionsCalc]]
- [[Pro_WithdrawAssets]]

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
- [[Olives_BO/Procedures/GetCustomerAssets]]
