---
type: table
database: Olives_BO
name: AssetsTransactions
schema: dbo
tags: [#assets, #backoffice]
foreign_keys:
  - [[Assets]]
  - [[Companies]]
  - [[Customers]]
  - [[SalesPersons]]
  - [[Users]]
referenced_by:
  - [[Pro_AssetTransactionsList]]
  - [[Pro_AssetTransfer]]
  - [[Pro_AssetsWarehouseTransactionsCalc]]
  - [[Pro_CustomersAndAssets]]
  - [[Pro_IssueAssets]]
  - [[Pro_WithdrawAssets]]
  - [[Tablet_AssetsTransactions_Insert]]
support_relevance: high
last_verified: 2026-07-05
---
# AssetsTransactions


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores assetstransactions records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Assets]], [[Customers]], [[Companies]], [[SalesPersons]] |
| TransID | numeric | NO | ✓ |  |  |
| AssetID | bigint | NO |  | ✓ | [[Assets]] |
| TransType | smallint | YES |  |  |  |
| TransDate | smalldatetime | YES |  |  |  |
| CustomerID | bigint | YES |  | ✓ | [[Customers]] |
| ContractNo | nvarchar | YES |  |  |  |
| ContractDate | smalldatetime | YES |  |  |  |
| UserID | nvarchar | YES |  | ✓ | [[Users]] |
| SalesmanNo | int | YES |  | ✓ | [[SalesPersons]] |
| WithdrawalReason | int | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| CustomerLocationID | int | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| AssetAmount | float | YES |  |  |  |
| RefTransID | numeric | YES |  |  |  |
| StoreNo | int | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| Approved | bit | YES |  |  |  |
| IsTransfer | bit | YES |  |  |  |
| ContactID | bigint | YES |  |  |  |
## Primary Key
CompanyID
TransID
## Foreign Keys
CompanyID, AssetID -> [[Assets]](CompanyID, AssetID)
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, SalesmanNo -> [[SalesPersons]](CompanyID, ID)
UserID -> [[Users]](UserID)
## Known Circular Dependencies
- Part of a circular FK chain: AssetsTransactions → SalesPersons → Users → AssetsTransactions.
## Impact / Procedures Using This Table

**Reads (7):**
- [[Pro_AssetTransactionsList]]
- [[Pro_AssetTransfer]]
- [[Pro_AssetsWarehouseTransactionsCalc]]
- [[Pro_CustomersAndAssets]]
- [[Pro_IssueAssets]]
- [[Pro_WithdrawAssets]]
- [[Tablet_AssetsTransactions_Insert]]

**Writes (4):**
- [[Pro_AssetTransfer]]
- [[Pro_IssueAssets]]
- [[Pro_WithdrawAssets]]
- [[Tablet_AssetsTransactions_Insert]]

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
