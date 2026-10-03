---
type: table
database: Olives_BO
name: ERPStores
schema: dbo
tags: [#backoffice, #integration]
foreign_keys:

referenced_by:
  - [[Pro_AssetTransactionsList]]
  - [[Pro_AssetsWarehouseTransactions]]
  - [[Pro_CustomersAndAssets]]
  - [[Pro_ERPStoresLinkWithItems]]
  - [[Pro_Store]]
  - [[Pro_TransfersOrdersHeaders]]
  - [[Pro_WithdrawAssets]]
  - [[Rpt_Sales_Statistics]]
  - [[Rpt_SalesmanCashSales]]
  - [[Rpt_SalesmanSalesByItems]]
  - [[Rpt_TransferOrderWH]]
support_relevance: high
last_verified: 2026-07-05
---
# ERPStores


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores erpstores records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| StoreNo | int | NO | ✓ |  |  |
| ArDesc | varchar | YES |  |  |  |
| EngDesc | varchar | YES |  |  |  |
| Reference1 | varchar | YES |  |  |  |
| Reference2 | varchar | YES |  |  |  |
| OID | nvarchar | YES |  |  |  |
| CarNo | nvarchar | YES |  |  |  |
| Remark | nvarchar | YES |  |  |  |

## Primary Key
CompanyID
StoreNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (13):**
- [[Pro_AssetTransactionsList]]
- [[Pro_AssetsWarehouseTransactions]]
- [[Pro_CustomersAndAssets]]
- [[Pro_ERPStoresLinkWithItems]]
- [[Pro_Store]]
- [[Pro_TransfersOrdersHeaders]]
- [[Pro_WithdrawAssets]]
- [[Rpt_Sales_Statistics]]
- [[Rpt_SalesmanCashSales]]
- [[Rpt_SalesmanSalesByItems]]
- [[Rpt_TransferOrderWH]]

**Writes (2):**
- [[Pro_Store]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Integration stuck**: IsPosted flag not clearing — check ERP connection and error log
- **Duplicate sent**: Same transaction sent multiple times — ERP shows duplicates
- **Mapping error**: Field mapping fails — check IntegrationPostedTransactions for error details
- **Timeout**: Large batch exceeds ERP timeout — split into smaller batches

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
