---
type: table
database: Olives_BO
name: ItemsCategories
schema: dbo
tags: [#backoffice, #inventory]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[AppDashBoard]]
  - [[GetWF_SalesOrderData]]
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[OT_SendCompData]]
  - [[OT_SendItemsInfo]]
  - [[Pro_CustomersItemsAssigment]]
  - [[Pro_Dashboard_Almalak]]
  - [[Pro_ImportData]]
  - [[Pro_Items]]
  - [[Pro_ItemsCategories]]
  - [[Pro_ItemsImageReport]]
  - [[Pro_ItemsSalesStats]]
  - [[Pro_ItemsSalesStatus]]
  - [[Pro_ReturnlineManagerApproval]]
  - [[Pro_SalesPersonCustStockItemsAssignment]]
  - [[Pro_SalesPersonItemsAssignment]]
  - [[Pro_SalespersonsTargetDashboard]]
  - [[Pro_Tree]]
  - [[RG_Rpt_PromotionInformation]]
  - [[RPT_ZalloumReportONE]]
  - [[RPT_ZalloumReportTWO]]
  - [[Rpt_CategTransaction]]
  - [[Rpt_CategoriesSalesPerCustomer]]
  - [[Rpt_CategorySalesmanSalesByDay]]
  - [[Rpt_CustomerDailySales]]
  - [[Rpt_CustomerItemsMonthlySales]]
  - [[Rpt_CustomerItemsSales]]
  - [[Rpt_CustomerItemsSalesBySelection]]
  - [[Rpt_CustomerItemsWeeklySales]]
  - [[Rpt_CustomerItemsYearlySales]]
  - [[Rpt_CustomerMonthlySales]]
  - [[Rpt_CustomerMonthlySalesByArea]]
  - [[Rpt_CustomerReturnOrdersDetails]]
  - [[Rpt_CustomerSalesByItems]]
  - [[Rpt_CustomerSalesByItemsBySelection]]
  - [[Rpt_CustomerStockByExpire]]
  - [[Rpt_CustomerStockNotExistByDocType]]
  - [[Rpt_CustomerStockNotExistByDocType_Summary]]
  - [[Rpt_CustomerTypeSalesByItems]]
  - [[Rpt_CustomersExpansion]]
  - [[Rpt_CustomersSalesDetails]]
  - [[Rpt_DailySales]]
  - [[Rpt_DailySalesByCateg]]
  - [[Rpt_GA_SalesmanAnalysis]]
  - [[Rpt_InvoiceDetails]]
  - [[Rpt_InvoiceDetailsSummary]]
  - [[Rpt_ItemTransaction]]
  - [[Rpt_ItemsMonthlySales]]
  - [[Rpt_ItemsMonthlySalesBySelection]]
  - [[Rpt_ItemsNotSold]]
  - [[Rpt_ItemsSalesPerCustomer]]
  - [[Rpt_NetSalesBySubCat]]
  - [[Rpt_NetSalesItems]]
  - [[Rpt_OrdersSalesReportByCategoty]]
  - [[Rpt_SalesAmountWithDiscountByCategories]]
  - [[Rpt_SalesAreaAndCategoryByCust]]
  - [[Rpt_SalesAreaByCategory]]
  - [[Rpt_SalesTargetByCustCount_Telegraph]]
  - [[Rpt_SalesTransactionByDocumentsTypes]]
  - [[Rpt_SalesmanCategorySales]]
  - [[Rpt_SalesmanDaySummary]]
  - [[Rpt_SalesmanExpansionByItems]]
  - [[Rpt_SalesmanItemsSalesSummary]]
  - [[Rpt_SalesmanOrdersSummaryByCategory]]
  - [[Rpt_SalesmanSalesByCategory]]
  - [[Rpt_SalesmanSalesByCategory2]]
  - [[Rpt_SalesmanSalesByItems]]
  - [[Rpt_SalesmanSalesByItemsBySelection]]
  - [[Rpt_SalesmanSalesByTotalCategory]]
  - [[Rpt_SalesmanSalesByTotalCategorySama]]
  - [[Rpt_SalesmanSalesCashCreditByCateg]]
  - [[Rpt_SalesmanSalesCashCreditByCategSeparateTax]]
  - [[Rpt_SalesmanSalesComparison]]
  - [[Rpt_SalesmanSalesDetails]]
  - [[Rpt_SalesmanSalesItemTab]]
  - [[Rpt_WF_GeneralSalesByItem]]
  - [[Rpt_WareHouse_Category_Balance]]
  - [[Rpt_WareHouse_Item_Balance]]
  - [[Rpt_WeeklySalesExpansion]]
  - [[Rpt_WithdrawalVoucher_Report]]
  - [[WF_SelectItemsCategories]]
support_relevance: high
last_verified: 2026-07-05
---
# ItemsCategories


## Business Purpose
Product categorization and merchandise hierarchy table in Olives_BO. Organizes the product catalog into multi-level category trees (`Level`, `Parent`), defining brand names, product lines, and sub-categories (`Name`, `ForeignName`, `ShortName`).
- **Classification & Reporting**: Central to sales analysis, focus item targets, and category-level sales reporting (`Rpt_SalesmanCategorySales`, `Rpt_SalesmanSalesByCategory`).
- **Item Link**: Pairs with `Items.CategoryID` via `CategCode`.

## Chatbot semantics
(Query `t.ItemsCategories` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule |
|----------------------|-----------|---------------|
| فئات / تصنيفات الأصناف | `CategCode`, `Name`, `Parent` | `IsSuspended = 0` (فئات نشطة) |
| تصنيف رئيسي مقابل فرعي | `Level`, `Parent` | `Level = 1` (رئيسي) أو `Parent = @ParentCode` |
| أصناف تابعة لتصنيف معين | Join `t.Items` | `i.CategoryID = c.CategCode` |

## Grain & keys
- **Grain**: One row per item category code (`CategCode`).
- **Composite PK**: `CompanyID`, `CategCode`.
- **Tenant Key**: `CompanyID`.

## Pipeline
Back Office Catalog Setup / ERP Sync → `ItemsCategories` → Synced to mobile handheld devices via `OT_SendItemsInfo`.

## Related
- [[Items]]
- [[ItemsGroups]]
- [[ItemsClasses]]
- [[TransactionsDetails]]

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| CategCode | nvarchar | YES | ✓ |  |  |
| Parent | nvarchar | YES |  |  |  |
| Name | nvarchar | YES |  |  |  |
| ForeignName | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| Level | int | YES |  |  |  |
| CategSort | int | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
## Primary Key
CompanyID
CategCode
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (134):**
- [[AppDashBoard]]
- [[GetWF_SalesOrderData]]
- [[OT_SendCompData]]
- [[OT_SendItemsInfo]]
- [[Pro_CustomersItemsAssigment]]
- [[Pro_Dashboard_Almalak]]
- [[Pro_ImportData]]
- [[Pro_Items]]
- [[Pro_ItemsCategories]]
- [[Pro_ItemsImageReport]]
- [[Pro_ItemsSalesStats]]
- [[Pro_ItemsSalesStatus]]
- [[Pro_ReturnlineManagerApproval]]
- [[Pro_SalesPersonCustStockItemsAssignment]]
- [[Pro_SalesPersonItemsAssignment]]
- [[Pro_SalespersonsTargetDashboard]]
- [[Pro_Tree]]
- [[RG_Rpt_PromotionInformation]]
- [[RPT_ZalloumReportONE]]
- [[RPT_ZalloumReportTWO]]
- [[Rpt_CategTransaction]]
- [[Rpt_CategoriesSalesPerCustomer]]
- [[Rpt_CategorySalesmanSalesByDay]]
- [[Rpt_CustomerDailySales]]
- [[Rpt_CustomerItemsMonthlySales]]
- [[Rpt_CustomerItemsSales]]
- [[Rpt_CustomerItemsSalesBySelection]]
- [[Rpt_CustomerItemsWeeklySales]]
- [[Rpt_CustomerItemsYearlySales]]
- [[Rpt_CustomerMonthlySales]]
- [[Rpt_CustomerMonthlySalesByArea]]
- [[Rpt_CustomerReturnOrdersDetails]]
- [[Rpt_CustomerSalesByItems]]
- [[Rpt_CustomerSalesByItemsBySelection]]
- [[Rpt_CustomerStockByExpire]]
- [[Rpt_CustomerStockNotExistByDocType]]
- [[Rpt_CustomerStockNotExistByDocType_Summary]]
- [[Rpt_CustomerTypeSalesByItems]]
- [[Rpt_CustomersExpansion]]
- [[Rpt_CustomersSalesDetails]]
- [[Rpt_DailySales]]
- [[Rpt_DailySalesByCateg]]
- [[Rpt_GA_SalesmanAnalysis]]
- [[Rpt_InvoiceDetails]]
- [[Rpt_InvoiceDetailsSummary]]
- [[Rpt_ItemTransaction]]
- [[Rpt_ItemsMonthlySales]]
- [[Rpt_ItemsMonthlySalesBySelection]]
- [[Rpt_ItemsNotSold]]
- [[Rpt_ItemsSalesPerCustomer]]
- [[Rpt_NetSalesBySubCat]]
- [[Rpt_NetSalesItems]]
- [[Rpt_OrdersSalesReportByCategoty]]
- [[Rpt_SalesAmountWithDiscountByCategories]]
- [[Rpt_SalesAreaAndCategoryByCust]]
- [[Rpt_SalesAreaByCategory]]
- [[Rpt_SalesTargetByCustCount_Telegraph]]
- [[Rpt_SalesTransactionByDocumentsTypes]]
- [[Rpt_SalesmanCategorySales]]
- [[Rpt_SalesmanDaySummary]]
- [[Rpt_SalesmanExpansionByItems]]
- [[Rpt_SalesmanItemsSalesSummary]]
- [[Rpt_SalesmanOrdersSummaryByCategory]]
- [[Rpt_SalesmanSalesByCategory]]
- [[Rpt_SalesmanSalesByCategory2]]
- [[Rpt_SalesmanSalesByItems]]
- [[Rpt_SalesmanSalesByItemsBySelection]]
- [[Rpt_SalesmanSalesByTotalCategory]]
- [[Rpt_SalesmanSalesByTotalCategorySama]]
- [[Rpt_SalesmanSalesCashCreditByCateg]]
- [[Rpt_SalesmanSalesCashCreditByCategSeparateTax]]
- [[Rpt_SalesmanSalesComparison]]
- [[Rpt_SalesmanSalesDetails]]
- [[Rpt_SalesmanSalesItemTab]]
- [[Rpt_WF_GeneralSalesByItem]]
- [[Rpt_WareHouse_Category_Balance]]
- [[Rpt_WareHouse_Item_Balance]]
- [[Rpt_WeeklySalesExpansion]]
- [[Rpt_WithdrawalVoucher_Report]]
- [[WF_SelectItemsCategories]]

**Writes (63):**
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[Pro_ImportData]]
- [[Pro_ItemsCategories]]

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
