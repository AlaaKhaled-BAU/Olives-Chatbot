---
type: table
database: Olives_BO
name: AssetsWarehouseTransactions
schema: dbo
tags: [#assets, #backoffice, #inventory]
foreign_keys:
referenced_by:
  - [[Pro_AssetTransactionsList]]
  - [[Pro_AssetTransfer]]
  - [[Pro_AssetsDefinition]]
  - [[Pro_AssetsWarehouseTransactions]]
  - [[Pro_AssetsWarehouseTransactionsCalc]]
  - [[Pro_CustomersAndAssets]]
  - [[Pro_IssueAssets]]
  - [[Pro_WithdrawAssets]]
  - [[Tablet_AssetsTransactions_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# AssetsWarehouseTransactions


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores assetswarehousetransactions records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| TransID | numeric | YES | ✓ |  |  |
| TransType | smallint | YES |  |  |  |
| AssetID | bigint | YES |  |  |  |
| TransDate | smalldatetime | YES |  |  |  |
| AssetsTransRef | numeric | YES |  |  |  |
| IsTransfer | bit | YES |  |  |  |
| RefTransID | numeric | YES |  |  |  |
| StoreNo | int | YES |  |  |  |
| Qty | float | YES |  |  |  |
## Primary Key
CompanyID
TransID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (9):**
- [[Pro_AssetTransactionsList]]
- [[Pro_AssetTransfer]]
- [[Pro_AssetsDefinition]]
- [[Pro_AssetsWarehouseTransactions]]
- [[Pro_AssetsWarehouseTransactionsCalc]]
- [[Pro_CustomersAndAssets]]
- [[Pro_IssueAssets]]
- [[Pro_WithdrawAssets]]
- [[Tablet_AssetsTransactions_Insert]]

**Writes (3):**
- [[Pro_AssetsDefinition]]
- [[Pro_AssetsWarehouseTransactions]]
- [[Pro_AssetsWarehouseTransactionsCalc]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Orphan lines**: Detail rows without matching header — causes sync failures
- **Posting failure**: IsPosted flag stuck false — check ERP integration log
- **Duplicate vouchers**: Same VouNo generated for different transactions — run dedup check
- **Currency mismatch**: ExRate different from CurrenciesRate table — financial reconciliation off
- **Void inconsistency**: IsVoid flag but original transaction still active — check WF approval

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
