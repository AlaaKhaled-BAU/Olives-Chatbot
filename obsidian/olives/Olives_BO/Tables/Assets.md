---
type: table
database: Olives_BO
name: Assets
schema: dbo
tags: [#assets, #backoffice]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[PlanogramMediabyAssets]]
  - [[Pro_AssetTransactionsList]]
  - [[Pro_AssetTransfer]]
  - [[Pro_AssetsDefinition]]
  - [[Pro_AssetsWarehouseTransactions]]
  - [[Pro_CustomersAndAssets]]
  - [[Pro_IssueAssets]]
  - [[Pro_LocationsAndSalespersonsLink]]
  - [[Pro_SalesTrans]]
  - [[Pro_WithdrawAssets]]
  - [[Rpt_AssetsByLocation]]
  - [[Rpt_AssetsByStore]]
support_relevance: high
last_verified: 2026-07-05
---
# Assets


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores assets records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| AssetID | bigint | NO | ✓ |  |  |
| AssetName | varchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| AssetType | int | YES |  |  |  |
| AssetSerial | nvarchar | YES |  |  |  |
| Status | int | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| AssetValue | float | YES |  |  |  |
| AssetVolume | float | YES |  |  |  |
## Primary Key
CompanyID
AssetID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (12):**
- [[PlanogramMediabyAssets]]
- [[Pro_AssetTransactionsList]]
- [[Pro_AssetTransfer]]
- [[Pro_AssetsDefinition]]
- [[Pro_AssetsWarehouseTransactions]]
- [[Pro_CustomersAndAssets]]
- [[Pro_IssueAssets]]
- [[Pro_LocationsAndSalespersonsLink]]
- [[Pro_SalesTrans]]
- [[Pro_WithdrawAssets]]
- [[Rpt_AssetsByLocation]]
- [[Rpt_AssetsByStore]]

**Writes (4):**
- [[Pro_AssetsDefinition]]
- [[Pro_AssetsWarehouseTransactions]]
- [[Pro_IssueAssets]]
- [[Pro_LocationsAndSalespersonsLink]]

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
