---
type: table
database: OSFA_DB
name: OT_ItemsMF
schema: dbo
tags: [#inventory, #mobile]
foreign_keys:
referenced_by:
  - [[OT_GetInvImageCompItem]]
  - [[OT_GetInvImageItemMF]]
  - [[servics_app_OSFA_Mobile_Ver]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_ItemsMF



## Business Purpose


Item master data on tablet — synced subset of BO Items table for offline use.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompNo | smallint | NO | ✓ |  |  |
| SalesmanNo | int | NO | ✓ |  |  |
| ItemNo | varchar | YES | ✓ |  |  |
| ArDesc | varchar | YES |  |  |  |
| EngDesc | varchar | YES |  |  |  |
| Unit1 | varchar | YES |  |  |  |
| Conv1 | money | YES |  |  |  |
| Unit2 | varchar | YES |  |  |  |
| Conv2 | money | YES |  |  |  |
| Unit3 | varchar | YES |  |  |  |
| Conv3 | money | YES |  |  |  |
| Unit4 | varchar | YES |  |  |  |
| SellPrice | money | YES |  |  |  |
| TaxPerc | money | YES |  |  |  |
| QtyOH | money | YES |  |  |  |
| ItemBarcode | nvarchar | YES |  |  |  |
| Categ | varchar | YES |  |  |  |
| SubCateg | varchar | YES |  |  |  |
| ImageID | bigint | YES |  |  |  |
| DefaultUnit | tinyint | YES |  |  |  |
| Weight | nvarchar | YES |  |  |  |
| ItemOidRef | uniqueidentifier | YES |  |  |  |
| Ref3 | nvarchar | YES |  |  |  |
| Ref4 | nvarchar | YES |  |  |  |
| Ref5 | nvarchar | YES |  |  |  |
| MinQty | money | YES |  |  |  |
| IsTaxExempt | bit | YES |  |  |  |
| UseInCustStock | bit | YES |  |  |  |
| ItemOrderInList | int | YES |  |  |  |
| ItemsReplacmentGroup | int | YES |  |  |  |
| Van_StandardStock | float | YES |  |  |  |
| Packing | float | YES |  |  |  |
| Is_weighted | bit | YES |  |  |  |
| PDFFileName | nvarchar | YES |  |  |  |
| VideoFileName | nvarchar | YES |  |  |  |
| Van_StandardStock_Max | float | YES |  |  |  |
| TaxType | int | YES |  |  |  |
| UsedInUploadOrderUnits | nvarchar | YES |  |  |  |
| BasketItemNo | nvarchar | YES |  |  |  |
| BasketVolume | float | YES |  |  |  |
| IsBasketItem | bit | YES |  |  |  |
| IsCustStockItem | bit | YES |  |  |  |
| VanCustodyUnitSerial | smallint | YES |  |  |  |
| PromotionItemGroupID | int | YES |  |  |  |
| ClassID | int | YES |  |  |  |
| IsCashOnly | smallint | YES |  |  |  |
| IsMostSales | nvarchar | YES |  |  |  |
| Ref6 | nvarchar | YES |  |  |  |
| Ref7 | nvarchar | YES |  |  |  |
| IsForSales | nvarchar | YES |  |  |  |
## Primary Key
CompNo
SalesmanNo
ItemNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_GetInvImageCompItem]]
- [[OT_GetInvImageItemMF]]
- [[servics_app_OSFA_Mobile_Ver]]

**Writes (0):**
_None_

## Estimated Size / Volatility
Typical business table
## Common Issues


- **Duplicate barcodes**: Multiple items sharing same barcode — POS picks wrong item
- **Price mismatch**: Sell price in Items differs from PriceListDetails — customer charged wrong amount
- **Stock discrepancy**: QtyInAllStores differs from sum of StoreBalances — run CALCITEMBALANCE
- **Missing units**: Item has no valid ItemUnits — cannot be sold
- **Tax config wrong**: IsTaxExempt flag incorrect — ZATCA/legal reporting mismatch


## See also
- [[Olives_BO/Tables/Items]] (Back Office counterpart table)

## Related


- [[_MOC-OSFA_DB|OSFA_DB MOC]]
