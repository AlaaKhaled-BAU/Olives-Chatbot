---
type: table
database: Olives_BO
name: ItemsReplacementHeaders
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
referenced_by:
  - [[Alpha_Integ_SendItemsReplacement]]
  - [[DEMOSALESPERSON]]
  - [[DEMOSALESPERSON2]]
  - [[OT_ImportReplacement]]
  - [[Pro_ItemsReplacementHeaders]]
  - [[SAP_Integ_ItemsReplacementIN_Amazing]]
  - [[SAP_Integ_ItemsReplacementOut_Amazing]]
support_relevance: high
last_verified: 2026-07-05
---
# ItemsReplacementHeaders


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores itemsreplacementheaders records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| TransactionTypeID | smallint | NO | ✓ |  |  |
| TransactionYear | smallint | NO | ✓ |  |  |
| TransactionNo | int | NO | ✓ |  |  |
| TransactionDate | smalldatetime | YES |  |  |  |
| SalesPersonID | int | YES |  | ✓ | [[SalesPersons]] |
| CustomerID | bigint | YES |  | ✓ | [[Customers]] |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
| RouteID | int | YES |  | ✓ | [[RoutesInformation]] |
| TrDateTime | smalldatetime | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| PostedToERP_IN | bit | YES |  |  |  |
## Primary Key
CompanyID
TransactionTypeID
TransactionYear
TransactionNo
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, RouteID -> [[RoutesInformation]](CompanyID, ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (7):**
- [[Alpha_Integ_SendItemsReplacement]]
- [[DEMOSALESPERSON]]
- [[DEMOSALESPERSON2]]
- [[OT_ImportReplacement]]
- [[Pro_ItemsReplacementHeaders]]
- [[SAP_Integ_ItemsReplacementIN_Amazing]]
- [[SAP_Integ_ItemsReplacementOut_Amazing]]

**Writes (4):**
- [[Alpha_Integ_SendItemsReplacement]]
- [[OT_ImportReplacement]]
- [[SAP_Integ_ItemsReplacementIN_Amazing]]
- [[SAP_Integ_ItemsReplacementOut_Amazing]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate barcodes**: Multiple items sharing same barcode — POS picks wrong item
- **Price mismatch**: Sell price in Items differs from PriceListDetails — customer charged wrong amount
- **Stock discrepancy**: QtyInAllStores differs from sum of StoreBalances — run CALCITEMBALANCE
- **Missing units**: Item has no valid ItemUnits — cannot be sold
- **Tax config wrong**: IsTaxExempt flag incorrect — ZATCA/legal reporting mismatch

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
