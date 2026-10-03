---
type: table
database: Olives_BO
name: PriceListDetails
schema: dbo
tags: [#backoffice, #billing]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[PriceLists]]
referenced_by:
  - [[CustPricelistD_TMP]]
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[OT_SendItemsInfo]]
  - [[Pro_CopyPricelist]]
  - [[Pro_ImportData]]
  - [[Pro_ImportPriceListData]]
  - [[Pro_Items]]
  - [[Pro_ItemsImageReport]]
  - [[Pro_PriceListDetails]]
  - [[Pro_PromotionsCondUnCodOutput]]
  - [[Pro_SalesTrans]]
  - [[Pro_TransfersOrdersDetails]]
  - [[Pro_TransfersOrdersQtyAmtValidation]]
  - [[Pro_TransfersOrdersQtyValidation]]
  - [[Rpt_ItemsStockStatement]]
  - [[Rpt_LoadTransactionDetails]]
  - [[Rpt_QuantitiesLoadReport]]
  - [[Rpt_SalesmanItemsSales]]
  - [[Rpt_SalesmanStock]]
  - [[Rpt_StockTakingReport]]
  - [[Rpt_StockTakingReportWithPrices]]
  - [[Rpt_UPriceReport]]
support_relevance: high
last_verified: 2026-10-03
related_workflows:
  - Items-Master-Data-Setup
  - PriceList-Management
---
# PriceListDetails

## Business Purpose
The item-level pricing table — stores the exact selling price (`Price`), tax rate (`Tax`), and standard discount percent (`DiscountPercent`) for each product (`ItemCode`) and packaging unit (`UnitID`) under each price list (`PriceListID`). Queryable via `t.PriceListDetails`.

## Chatbot semantics
(Query `t.PriceListDetails` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| سعر المادة في قائمة الأسعار | `ItemCode`, `PriceListID`, `UnitID`, `Price` | Filter by item and price list | Direct unit selling price |
| اسم المادة وسعرها | Join `t.Items` | `Items.ItemNo = d.ItemCode` | Arabic / English item description |
| الوحدة (حبة، كرتونة، طرد) | Join `t.ItemsUnits` | `ItemsUnits.ID = d.UnitID` | Unit of measure description |
| نسبة الضريبة والخصم للمادة | `Tax`, `DiscountPercent` | Numeric | Default tax and discount rules |

## Grain & keys
- **Composite PK**: (`CompanyID`, `PriceListID`, `ItemCode`, `UnitID`)
- **Tenant key**: `CompanyID`
- **FKs**: `PriceListID` → [[PriceLists]](ID), `ItemCode` → [[Items]](ItemNo), `UnitID` → [[ItemsUnits]](ID)

## Pipeline
Configured in Back Office pricing management screens (`Pro_PriceListDetails`). Synchronized to mobile devices for automated price calculation on invoices and orders.

## Related
- [[PriceLists]]
- [[Items]]
- [[ItemsUnits]]
- [[CustomersFinancialDetails]]
- [[TransactionsDetails]]
- [[OrdersDetails]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[PriceLists]] |
| PriceListID | int | NO | ✓ | ✓ | [[PriceLists]] |
| ItemCode | nvarchar | NO | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | NO | ✓ | ✓ | [[ItemsUnits]] |
| Price | float | YES |  |  |  |
| TaxType | int | YES |  |  |  |
| Tax | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| UseInReturn | bit | YES |  |  |  |
| UseInSales | bit | YES |  |  |  |
| SellPrice2 | float | YES |  |  |  |
| SellPrice3 | float | YES |  |  |  |
| Qty | money | YES |  |  |  |
| TaxType1 | int | YES |  |  |  |
| Tax1 | float | YES |  |  |  |
| TaxType2 | int | YES |  |  |  |
| Tax2 | float | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| MaxDiscPerc | float | YES |  |  |  |

## Primary Key
CompanyID
PriceListID
ItemCode
UnitID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
CompanyID, PriceListID -> [[PriceLists]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (42):**
- [[CustPricelistD_TMP]]
- [[OT_SendItemsInfo]]
- [[Pro_CopyPricelist]]
- [[Pro_ImportData]]
- [[Pro_ImportPriceListData]]
- [[Pro_Items]]
- [[Pro_ItemsImageReport]]
- [[Pro_PriceListDetails]]
- [[Pro_PromotionsCondUnCodOutput]]
- [[Pro_SalesTrans]]
- [[Pro_TransfersOrdersDetails]]
- [[Pro_TransfersOrdersQtyAmtValidation]]
- [[Pro_TransfersOrdersQtyValidation]]
- [[Rpt_ItemsStockStatement]]
- [[Rpt_LoadTransactionDetails]]
- [[Rpt_QuantitiesLoadReport]]
- [[Rpt_SalesmanItemsSales]]
- [[Rpt_SalesmanStock]]
- [[Rpt_StockTakingReport]]
- [[Rpt_StockTakingReportWithPrices]]
- [[Rpt_UPriceReport]]

**Writes (62):**
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[Pro_ImportData]]
- [[Pro_ImportPriceListData]]
- [[Pro_PriceListDetails]]

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
