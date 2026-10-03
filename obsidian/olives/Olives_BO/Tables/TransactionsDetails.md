---
type: table
database: Olives_BO
name: TransactionsDetails
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[TransactionsHeaders]]
  - [[TransactionsTypes]]
referenced_by:
  - [[BO_Online_RptCustomerSalesTargetDetails]]
  - [[BaladInsertrtLoadDetailsintoTransactionstyp6]]
  - [[CalcItemBalance]]
  - [[DA_SalesTarget]]
  - [[Da_ProductPerformance]]
  - [[Da_SalesGrowth]]
  - [[Da_SalesperRep]]
  - [[Da_YearlyCompanyTargetAndSales]]
  - [[OT_ImportReplacement]]
  - [[OT_ImportSalesInvoices]]
  - [[OT_Online_GetSalesmanSalesByMonths]]
  - [[OT_Online_RptSalesAndReturnPercByCustomer_Supervisor]]
  - [[OT_Online_RptSalesAndReturnPerc_Supervisor]]
  - [[Pro_CalcSalespersonItemBalance]]
  - [[Pro_CheckItemsInvoiceBarcode]]
  - [[Pro_ConvertLoadOrderToTransaction]]
  - [[Pro_ConvertUnloadOrderToTransaction]]
  - [[Pro_DeliveryDashboard]]
  - [[Pro_ImportAlSamahData]]
  - [[Pro_ItemsUnitsDetails]]
  - [[Pro_JoTaxApi]]
  - [[Pro_ReturnOrdersDetails]]
  - [[Pro_ReturnlineManagerApproval]]
  - [[Pro_RptCashTotalOnline_Android]]
  - [[Pro_RptCashTotalOnline_Android_Naqi]]
  - [[Pro_SalesReport_ItemCode]]
  - [[Pro_SalesmanDetailsDashboard]]
  - [[Pro_SalesmanStockAndReturnLoadOrders]]
  - [[Pro_SalespersonsTargetDashboard]]
  - [[Pro_TransactionsDetails]]
  - [[Pro_TransfersOrdersHeaders]]
  - [[Pro_TransfersOrdersQtyValidation]]
  - [[RPT_CUSTOMERSALESDETAILSBYITEMANDSALESPERSONNAME]]
  - [[RPT_SALESDETAILSCUSTOMERSBYVALUE]]
  - [[RPT_SUMMARYSALESAND]]
  - [[RPT_ZalloumReportONE]]
  - [[RPT_ZalloumReportTWO]]
  - [[RptOnlineRpt_DamageReturn]]
  - [[RptOnlineRpt_ItemAvgSalesByCustomer]]
  - [[RptOnlineRpt_ReturnDetails]]
  - [[RptOnlineRpt_SalesmanJournySummary]]
  - [[Rpt_AcceptedSalesInvoices]]
  - [[Rpt_AnnualTargetAnalysis]]
  - [[Rpt_AreaSalesAnalysis]]
  - [[Rpt_AreaSalesAndSalesmanTarget]]
  - [[Rpt_AssistantsSales]]
  - [[Rpt_AssistantsSalesDaily]]
  - [[Rpt_BasketReport]]
  - [[Rpt_BonusTypeForCustomers]]
  - [[Rpt_CashInvoicesBonus]]
  - [[Rpt_Cashier]]
  - [[Rpt_CategTransaction]]
  - [[Rpt_CategoriesSalesPerCustomer]]
  - [[Rpt_CategorySalesmanSalesByDay]]
  - [[Rpt_CompareCustSalesByCategAndTargetRef]]
  - [[Rpt_CustomerAndReturnPerc]]
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
  - [[Rpt_CustomerSalesByUnit]]
  - [[Rpt_CustomerSalesSummary]]
  - [[Rpt_CustomerSalesSummary_BySelection]]
  - [[Rpt_CustomerTypeSalesByItems]]
  - [[Rpt_CustomersAvgPerClass]]
  - [[Rpt_CustomersCountVisitByWeek]]
  - [[Rpt_CustomersExpansion]]
  - [[Rpt_CustomersPromotionLog]]
  - [[Rpt_CustomersSalesAndVisits]]
  - [[Rpt_CustomersSalesAndVisits2]]
  - [[Rpt_CustomersSalesByRoute]]
  - [[Rpt_CustomersSalesDetails]]
  - [[Rpt_CustomersSalesReturnCollectionMatching]]
  - [[Rpt_CustomersVisitsCount]]
  - [[Rpt_CustomersVisitsPerRoute]]
  - [[Rpt_CustomersVisitsPerRoute_SUP]]
  - [[Rpt_DailySales]]
  - [[Rpt_DailySalesByCateg]]
  - [[Rpt_DailySalesSummary]]
  - [[Rpt_DeliverySales]]
  - [[Rpt_GA_SalesmanAnalysis]]
  - [[Rpt_InvoiceByCustomerAndSalesmanAndItem]]
  - [[Rpt_InvoiceByDocTypes]]
  - [[Rpt_InvoiceDetails]]
  - [[Rpt_InvoiceDetailsSummary]]
  - [[Rpt_InvoiceQty]]
  - [[Rpt_InvoicesSummaryWithTax]]
  - [[Rpt_ItemCountEachCustomer]]
  - [[Rpt_ItemSalesSummary]]
  - [[Rpt_ItemSalesSummaryBySelection]]
  - [[Rpt_ItemTransaction]]
  - [[Rpt_ItemsMonthlySales]]
  - [[Rpt_ItemsMonthlySalesBySelection]]
  - [[Rpt_ItemsNotSold]]
  - [[Rpt_ItemsSalesPerCustomer]]
  - [[Rpt_ItemsSalesPerRoute]]
  - [[Rpt_ItemsStockStatement]]
  - [[Rpt_LiveQty]]
  - [[Rpt_MonthlyCompareSalesTargetWithCustomer]]
  - [[Rpt_MonthlySalesProfit]]
  - [[Rpt_NetSalesBySubCat]]
  - [[Rpt_NetSalesItems]]
  - [[Rpt_NetVisitsTime]]
  - [[Rpt_NetsalesAndLoadOrderAndRate]]
  - [[Rpt_NetsalesAndRate]]
  - [[Rpt_NotSoldPerCateg]]
  - [[Rpt_OrderMaster]]
  - [[Rpt_PerformanceMetric]]
  - [[Rpt_Price]]
  - [[Rpt_PromotionsWithDrawalsWithinDate]]
  - [[Rpt_ProposedOrder]]
  - [[Rpt_QuantitiesLoadReport]]
  - [[Rpt_ReceiptsBySalesman]]
  - [[Rpt_ReturnSalesAmount]]
  - [[Rpt_RoutePerformanceAnalysis]]
  - [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
  - [[Rpt_RouteSummaryDeatils]]
  - [[Rpt_SalesAmountWithDiscountByCategories]]
  - [[Rpt_SalesAndCollectionTargetByLocation]]
  - [[Rpt_SalesAndOrders]]
  - [[Rpt_SalesAndReturnPerc]]
  - [[Rpt_SalesAreaAndCategoryByCust]]
  - [[Rpt_SalesAreaByCategory]]
  - [[Rpt_SalesByLocationsAndRoute]]
  - [[Rpt_SalesCollcetionsTargets]]
  - [[Rpt_SalesCustomerInvCount]]
  - [[Rpt_SalesDifferencePerRoute]]
  - [[Rpt_SalesItemsByCustomersType]]
  - [[Rpt_SalesManRouteSalesComparison]]
  - [[Rpt_SalesPerRoute]]
  - [[Rpt_SalesPerRouteWithSalesman]]
  - [[Rpt_SalesPersonItemBonusTarget]]
  - [[Rpt_SalesPersonSpecialTargets]]
  - [[Rpt_SalesPersonTarget]]
  - [[Rpt_SalesTransactionByDocumentsTypes]]
  - [[Rpt_SalesWithSpecialQty]]
  - [[Rpt_Sales_SummeryBySupervisor]]
  - [[Rpt_SalesbyItemsbyCustomers]]
  - [[Rpt_SalesmanAnalysisDashBoard]]
  - [[Rpt_SalesmanCashAndChequesSales]]
  - [[Rpt_SalesmanCashSales]]
  - [[Rpt_SalesmanCategorySales]]
  - [[Rpt_SalesmanCreditSales]]
  - [[Rpt_SalesmanCustRoutes]]
  - [[Rpt_SalesmanDailyActivities]]
  - [[Rpt_SalesmanDaySummary]]
  - [[Rpt_SalesmanDifferences]]
  - [[Rpt_SalesmanExpansion]]
  - [[Rpt_SalesmanExpansionByItems]]
  - [[Rpt_SalesmanGroupByUnit]]
  - [[Rpt_SalesmanItemSalesPerRoute]]
  - [[Rpt_SalesmanItemsSales]]
  - [[Rpt_SalesmanItemsSalesSummary]]
  - [[Rpt_SalesmanJourneyPerformance]]
  - [[Rpt_SalesmanOrdersSummary]]
  - [[Rpt_SalesmanRouteAvg]]
  - [[Rpt_SalesmanRoutePerformance]]
  - [[Rpt_SalesmanRouteSummary]]
  - [[Rpt_SalesmanSalesByCategory]]
  - [[Rpt_SalesmanSalesByItemClass_Online]]
  - [[Rpt_SalesmanSalesByItems]]
  - [[Rpt_SalesmanSalesByItemsBySelection]]
  - [[Rpt_SalesmanSalesByTotalCategory]]
  - [[Rpt_SalesmanSalesByTotalCategorySama]]
  - [[Rpt_SalesmanSalesCashCreditByCateg]]
  - [[Rpt_SalesmanSalesCashCreditByCategSeparateTax]]
  - [[Rpt_SalesmanSalesComparison]]
  - [[Rpt_SalesmanSalesDetails]]
  - [[Rpt_SalesmanSalesInPeriod]]
  - [[Rpt_SalesmanSalesItemTab]]
  - [[Rpt_SalesmanSalesRecStatment]]
  - [[Rpt_SalesmanSalesSummary]]
  - [[Rpt_SalesmanSalesSummaryByCustomer]]
  - [[Rpt_SalesmanSalesSummaryByCustomerBySelection]]
  - [[Rpt_SalesmanSalesSummaryBySelection]]
  - [[Rpt_SalesmanSalesTargetByDay]]
  - [[Rpt_SalesmanSalesTotal]]
  - [[Rpt_SalesmanSalesTotal_BO]]
  - [[Rpt_SalesmanSales_ByMonths]]
  - [[Rpt_SalesmanSoldAndNoSoldCustomers]]
  - [[Rpt_SalesmanSoldAndNoSoldCustomers_BO]]
  - [[Rpt_SalesmanStock]]
  - [[Rpt_SalesmanStockAndReturn]]
  - [[Rpt_SalesmanSummaryRoute]]
  - [[Rpt_SalesmanSummaryRoute_60]]
  - [[Rpt_SalesmanSummaryRoute_Atieh]]
  - [[Rpt_SalesmanSummaryRoute_Dandana]]
  - [[Rpt_SalesmanSummaryRoute_zz]]
  - [[Rpt_SalesmanTargetCommission]]
  - [[Rpt_SalesmanTargetbyParent]]
  - [[Rpt_SalesmanTimeSpentPerCustomer]]
  - [[Rpt_SalesmanTimeSpentPerCustomer2]]
  - [[Rpt_SalesmanTimeSpentPerCustomer3]]
  - [[Rpt_SalesmanTimeSpentPerCustomer4]]
  - [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
  - [[Rpt_SalesmanTransactionDetails]]
  - [[Rpt_SalesmanVisitAnalysis]]
  - [[Rpt_SalesmanVisitsRoute]]
  - [[Rpt_SalesmenSales_DateToDate]]
  - [[Rpt_SalesmenSales_M]]
  - [[Rpt_SalesmenSales_Year]]
  - [[Rpt_SalesmenVisitsDetails]]
  - [[Rpt_Salesmensales2]]
  - [[Rpt_SalespersonTargetComparison]]
  - [[Rpt_SalespersonsDailyVisits]]
  - [[Rpt_StandCustomersreport]]
  - [[Rpt_StandView]]
  - [[Rpt_StockTakingReportWithPrices]]
  - [[Rpt_SupervisorSalesSummary]]
  - [[Rpt_TargetSpartan]]
  - [[Rpt_TotalInvoiceByDocTypes]]
  - [[Rpt_TotalQtyBySalesmanByItems]]
  - [[Rpt_TotalSalesmanRouteSummary]]
  - [[Rpt_TransactionByDate]]
  - [[Rpt_TransactionSales]]
  - [[Rpt_UPriceReport]]
  - [[Rpt_VoidedInvoices]]
  - [[Rpt_WFCustomersVisits]]
  - [[Rpt_WareHouse_Category_Balance]]
  - [[Rpt_WareHouse_Item_Balance]]
  - [[Rpt_WeeklySalesExpansion]]
  - [[Rpt_WeeklySalesmanVisits]]
  - [[Rpt_WithdrawalVoucher_Report]]
  - [[Rpt_WorkFlowAnalysis]]
  - [[Rpt_Workflow_ChangePrice]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Daily-Sales-Cycle
---
# TransactionsDetails


## Business Purpose
Line-item detail for posted sales invoices and return transactions (`TransactionsHeaders`). Records the exact billed items, units, quantities, bonus/promotional items, prices, discounts, and line taxes.
- **Transaction Types**: Governed by `TransactionTypeID`:
  - `1` = Sales Invoice line (فاتورة مبيعات).
  - `2` = Return Sales Invoice line (مرتجع مبيعات).
- **Header Link**: Pairs with `TransactionsHeaders` on `TransactionTypeID`, `TransactionYear`, and `TransactionNo`.
- **Net Sales Calculation**: Line net before tax is `(Quantity * Price) - DiscountAmount - VoucherDiscount`. Line net after tax includes `TaxAmount`.

## Chatbot semantics
(Query `t.TransactionsDetails` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule |
|----------------------|-----------|---------------|
| بنود الفاتورة / أصناف المبيعات | `ItemCode`, `Quantity`, `Bonus`, `Price` | Join `t.TransactionsHeaders h ON d.TransactionTypeID = h.TransactionTypeID AND d.TransactionYear = h.TransactionYear AND d.TransactionNo = h.TransactionNo WHERE d.TransactionTypeID = 1` |
| بنود مرتجع المبيعات | `ItemCode`, `Quantity`, `Price`, `ReturnReason` | `d.TransactionTypeID = 2` |
| الكمية المباعة الفعلية | `Quantity` | `Quantity > 0` |
| البونص الممنوح | `Bonus`, `QtyAsBonus` | أصناف مجانية ممنوحة مع الفاتورة |
| صافي قيمة الصنف | Calculated | `(d.Quantity * d.Price) - ISNULL(d.DiscountAmount, 0)` |
| خصم الصنف | `DiscountAmount`, `DiscountPercent` | الخصم المباشر الممنوح على مستوى السطر |
| سبب الإرجاع | `ReturnReason` | يحدد سبب إرجاع الصنف في فواتير المرتجع |

**Do not confuse with:**
- `t.OrdersDetails` (unbilled pre-sales demand / orders).
- `t.ReturnOrdersDetails` (unapproved / pre-invoice return requests).

## Grain & keys
- **Grain**: One row per item serial within a transaction header (`TransactionTypeID`, `TransactionYear`, `TransactionNo`, `ItemSerial`).
- **Composite PK**: `CompanyID`, `TransactionTypeID`, `TransactionYear`, `TransactionNo`, `ItemSerial`.
- **Tenant Key**: `CompanyID`.

## Pipeline
Mobile Van/Presales Tablet → `OT_ImportSalesInvoices` (or direct BO billing) → `TransactionsHeaders` + `TransactionsDetails`.

## Related
- [[TransactionsHeaders]]
- [[Items]]
- [[ItemsUnits]]
- [[OrdersDetails]]

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[TransactionsHeaders]] |
| TransactionTypeID | smallint | NO | ✓ | ✓ | [[TransactionsTypes]] |
| TransactionYear | smallint | NO | ✓ | ✓ | [[TransactionsHeaders]] |
| TransactionNo | int | NO | ✓ | ✓ | [[TransactionsHeaders]] |
| ItemCode | nvarchar | YES | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | YES | ✓ | ✓ | [[ItemsUnits]] |
| ItemSerial | int | NO | ✓ |  |  |
| Quantity | float | YES |  |  |  |
| Bonus | float | YES |  |  |  |
| Price | float | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| VoucherDiscount | float | YES |  |  |  |
| TaxType | smallint | YES |  |  |  |
| TaxPercent | float | YES |  |  |  |
| TaxAmount | float | YES |  |  |  |
| ForeignPrice | float | YES |  |  |  |
| ForeignDiscountAmount | float | YES |  |  |  |
| ForeignDiscountPercent | float | YES |  |  |  |
| ForeignVouDiscount | float | YES |  |  |  |
| ForeignTaxPercent | float | YES |  |  |  |
| ForeignTaxAmount | float | YES |  |  |  |
| ItemStatus | smallint | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| UPrice | float | YES |  |  |  |
| TaxType1 | smallint | YES |  |  |  |
| TaxPercent1 | float | YES |  |  |  |
| TaxAmount1 | float | YES |  |  |  |
| TaxType2 | smallint | YES |  |  |  |
| TaxPercent2 | float | YES |  |  |  |
| TaxAmount2 | float | YES |  |  |  |
| Approve | bit | YES |  |  |  |
| Manual_Bonus | float | YES |  |  |  |
| ExchangeRate | float | YES |  |  |  |
| SP_Qty | float | YES |  |  |  |
| ItemBarcode | varchar | YES |  |  |  |
| Manual_Disc | float | YES |  |  |  |
| QtyAsBonus | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| ReturnReason | int | YES |  |  |  |
| BonusTax | float | YES |  |  |  |
| BonusAmount | float | YES |  |  |  |
| LineSort | smallint | YES |  |  |  |
| CurrentQty | float | YES |  |  |  |
| IsInventoried | bit | YES |  |  |  |
## Primary Key
CompanyID
TransactionTypeID
TransactionYear
TransactionNo
ItemCode
UnitID
ItemSerial
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
CompanyID, TransactionTypeID, TransactionYear, TransactionNo -> [[TransactionsHeaders]](CompanyID, TransactionTypeID, TransactionYear, TransactionNo)
TransactionTypeID -> [[TransactionsTypes]](ID)
## Known Circular Dependencies
- Part of a circular FK chain: DocumentsTypes → TransactionsTypes → TransactionsDetails → TransactionsHeaders → DocumentsTypes.
- Part of a circular FK chain: TransactionsDetails → TransactionsHeaders → TransactionsTypes → TransactionsDetails.
## Impact / Procedures Using This Table

**Reads (283):**
- [[BO_Online_RptCustomerSalesTargetDetails]]
- [[BaladInsertrtLoadDetailsintoTransactionstyp6]]
- [[CalcItemBalance]]
- [[DA_SalesTarget]]
- [[Da_ProductPerformance]]
- [[Da_SalesGrowth]]
- [[Da_SalesperRep]]
- [[Da_YearlyCompanyTargetAndSales]]
- [[OT_Online_GetSalesmanSalesByMonths]]
- [[OT_Online_RptSalesAndReturnPercByCustomer_Supervisor]]
- [[OT_Online_RptSalesAndReturnPerc_Supervisor]]
- [[Pro_CalcSalespersonItemBalance]]
- [[Pro_CheckItemsInvoiceBarcode]]
- [[Pro_DeliveryDashboard]]
- [[Pro_ImportAlSamahData]]
- [[Pro_ItemsUnitsDetails]]
- [[Pro_JoTaxApi]]
- [[Pro_ReturnOrdersDetails]]
- [[Pro_ReturnlineManagerApproval]]
- [[Pro_RptCashTotalOnline_Android]]
- [[Pro_RptCashTotalOnline_Android_Naqi]]
- [[Pro_SalesReport_ItemCode]]
- [[Pro_SalesmanDetailsDashboard]]
- [[Pro_SalesmanStockAndReturnLoadOrders]]
- [[Pro_SalespersonsTargetDashboard]]
- [[Pro_TransactionsDetails]]
- [[Pro_TransfersOrdersHeaders]]
- [[Pro_TransfersOrdersQtyValidation]]
- [[RPT_CUSTOMERSALESDETAILSBYITEMANDSALESPERSONNAME]]
- [[RPT_SALESDETAILSCUSTOMERSBYVALUE]]
- [[RPT_SUMMARYSALESAND]]
- [[RPT_ZalloumReportONE]]
- [[RPT_ZalloumReportTWO]]
- [[RptOnlineRpt_DamageReturn]]
- [[RptOnlineRpt_ItemAvgSalesByCustomer]]
- [[RptOnlineRpt_ReturnDetails]]
- [[RptOnlineRpt_SalesmanJournySummary]]
- [[Rpt_AcceptedSalesInvoices]]
- [[Rpt_AnnualTargetAnalysis]]
- [[Rpt_AreaSalesAnalysis]]
- [[Rpt_AreaSalesAndSalesmanTarget]]
- [[Rpt_AssistantsSales]]
- [[Rpt_AssistantsSalesDaily]]
- [[Rpt_BasketReport]]
- [[Rpt_BonusTypeForCustomers]]
- [[Rpt_CashInvoicesBonus]]
- [[Rpt_Cashier]]
- [[Rpt_CategTransaction]]
- [[Rpt_CategoriesSalesPerCustomer]]
- [[Rpt_CategorySalesmanSalesByDay]]
- [[Rpt_CompareCustSalesByCategAndTargetRef]]
- [[Rpt_CustomerAndReturnPerc]]
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
- [[Rpt_CustomerSalesByUnit]]
- [[Rpt_CustomerSalesSummary]]
- [[Rpt_CustomerSalesSummary_BySelection]]
- [[Rpt_CustomerTypeSalesByItems]]
- [[Rpt_CustomersAvgPerClass]]
- [[Rpt_CustomersCountVisitByWeek]]
- [[Rpt_CustomersExpansion]]
- [[Rpt_CustomersPromotionLog]]
- [[Rpt_CustomersSalesAndVisits]]
- [[Rpt_CustomersSalesAndVisits2]]
- [[Rpt_CustomersSalesByRoute]]
- [[Rpt_CustomersSalesDetails]]
- [[Rpt_CustomersSalesReturnCollectionMatching]]
- [[Rpt_CustomersVisitsCount]]
- [[Rpt_CustomersVisitsPerRoute]]
- [[Rpt_CustomersVisitsPerRoute_SUP]]
- [[Rpt_DailySales]]
- [[Rpt_DailySalesByCateg]]
- [[Rpt_DailySalesSummary]]
- [[Rpt_DeliverySales]]
- [[Rpt_GA_SalesmanAnalysis]]
- [[Rpt_InvoiceByCustomerAndSalesmanAndItem]]
- [[Rpt_InvoiceByDocTypes]]
- [[Rpt_InvoiceDetails]]
- [[Rpt_InvoiceDetailsSummary]]
- [[Rpt_InvoiceQty]]
- [[Rpt_InvoicesSummaryWithTax]]
- [[Rpt_ItemCountEachCustomer]]
- [[Rpt_ItemSalesSummary]]
- [[Rpt_ItemSalesSummaryBySelection]]
- [[Rpt_ItemTransaction]]
- [[Rpt_ItemsMonthlySales]]
- [[Rpt_ItemsMonthlySalesBySelection]]
- [[Rpt_ItemsNotSold]]
- [[Rpt_ItemsSalesPerCustomer]]
- [[Rpt_ItemsSalesPerRoute]]
- [[Rpt_ItemsStockStatement]]
- [[Rpt_LiveQty]]
- [[Rpt_MonthlyCompareSalesTargetWithCustomer]]
- [[Rpt_MonthlySalesProfit]]
- [[Rpt_NetSalesBySubCat]]
- [[Rpt_NetSalesItems]]
- [[Rpt_NetVisitsTime]]
- [[Rpt_NetsalesAndLoadOrderAndRate]]
- [[Rpt_NetsalesAndRate]]
- [[Rpt_NotSoldPerCateg]]
- [[Rpt_OrderMaster]]
- [[Rpt_PerformanceMetric]]
- [[Rpt_Price]]
- [[Rpt_PromotionsWithDrawalsWithinDate]]
- [[Rpt_ProposedOrder]]
- [[Rpt_QuantitiesLoadReport]]
- [[Rpt_ReceiptsBySalesman]]
- [[Rpt_ReturnSalesAmount]]
- [[Rpt_RoutePerformanceAnalysis]]
- [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
- [[Rpt_RouteSummaryDeatils]]
- [[Rpt_SalesAmountWithDiscountByCategories]]
- [[Rpt_SalesAndCollectionTargetByLocation]]
- [[Rpt_SalesAndOrders]]
- [[Rpt_SalesAndReturnPerc]]
- [[Rpt_SalesAreaAndCategoryByCust]]
- [[Rpt_SalesAreaByCategory]]
- [[Rpt_SalesByLocationsAndRoute]]
- [[Rpt_SalesCollcetionsTargets]]
- [[Rpt_SalesCustomerInvCount]]
- [[Rpt_SalesDifferencePerRoute]]
- [[Rpt_SalesItemsByCustomersType]]
- [[Rpt_SalesManRouteSalesComparison]]
- [[Rpt_SalesPerRoute]]
- [[Rpt_SalesPerRouteWithSalesman]]
- [[Rpt_SalesPersonItemBonusTarget]]
- [[Rpt_SalesPersonSpecialTargets]]
- [[Rpt_SalesPersonTarget]]
- [[Rpt_SalesTransactionByDocumentsTypes]]
- [[Rpt_SalesWithSpecialQty]]
- [[Rpt_Sales_SummeryBySupervisor]]
- [[Rpt_SalesbyItemsbyCustomers]]
- [[Rpt_SalesmanAnalysisDashBoard]]
- [[Rpt_SalesmanCashAndChequesSales]]
- [[Rpt_SalesmanCashSales]]
- [[Rpt_SalesmanCategorySales]]
- [[Rpt_SalesmanCreditSales]]
- [[Rpt_SalesmanCustRoutes]]
- [[Rpt_SalesmanDailyActivities]]
- [[Rpt_SalesmanDaySummary]]
- [[Rpt_SalesmanDifferences]]
- [[Rpt_SalesmanExpansion]]
- [[Rpt_SalesmanExpansionByItems]]
- [[Rpt_SalesmanGroupByUnit]]
- [[Rpt_SalesmanItemSalesPerRoute]]
- [[Rpt_SalesmanItemsSales]]
- [[Rpt_SalesmanItemsSalesSummary]]
- [[Rpt_SalesmanJourneyPerformance]]
- [[Rpt_SalesmanOrdersSummary]]
- [[Rpt_SalesmanRouteAvg]]
- [[Rpt_SalesmanRoutePerformance]]
- [[Rpt_SalesmanRouteSummary]]
- [[Rpt_SalesmanSalesByCategory]]
- [[Rpt_SalesmanSalesByItemClass_Online]]
- [[Rpt_SalesmanSalesByItems]]
- [[Rpt_SalesmanSalesByItemsBySelection]]
- [[Rpt_SalesmanSalesByTotalCategory]]
- [[Rpt_SalesmanSalesByTotalCategorySama]]
- [[Rpt_SalesmanSalesCashCreditByCateg]]
- [[Rpt_SalesmanSalesCashCreditByCategSeparateTax]]
- [[Rpt_SalesmanSalesComparison]]
- [[Rpt_SalesmanSalesDetails]]
- [[Rpt_SalesmanSalesInPeriod]]
- [[Rpt_SalesmanSalesItemTab]]
- [[Rpt_SalesmanSalesRecStatment]]
- [[Rpt_SalesmanSalesSummary]]
- [[Rpt_SalesmanSalesSummaryByCustomer]]
- [[Rpt_SalesmanSalesSummaryByCustomerBySelection]]
- [[Rpt_SalesmanSalesSummaryBySelection]]
- [[Rpt_SalesmanSalesTargetByDay]]
- [[Rpt_SalesmanSalesTotal]]
- [[Rpt_SalesmanSalesTotal_BO]]
- [[Rpt_SalesmanSales_ByMonths]]
- [[Rpt_SalesmanSoldAndNoSoldCustomers]]
- [[Rpt_SalesmanSoldAndNoSoldCustomers_BO]]
- [[Rpt_SalesmanStock]]
- [[Rpt_SalesmanStockAndReturn]]
- [[Rpt_SalesmanSummaryRoute]]
- [[Rpt_SalesmanSummaryRoute_60]]
- [[Rpt_SalesmanSummaryRoute_Atieh]]
- [[Rpt_SalesmanSummaryRoute_Dandana]]
- [[Rpt_SalesmanSummaryRoute_zz]]
- [[Rpt_SalesmanTargetCommission]]
- [[Rpt_SalesmanTargetbyParent]]
- [[Rpt_SalesmanTimeSpentPerCustomer]]
- [[Rpt_SalesmanTimeSpentPerCustomer2]]
- [[Rpt_SalesmanTimeSpentPerCustomer3]]
- [[Rpt_SalesmanTimeSpentPerCustomer4]]
- [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
- [[Rpt_SalesmanTransactionDetails]]
- [[Rpt_SalesmanVisitAnalysis]]
- [[Rpt_SalesmanVisitsRoute]]
- [[Rpt_SalesmenSales_DateToDate]]
- [[Rpt_SalesmenSales_M]]
- [[Rpt_SalesmenSales_Year]]
- [[Rpt_SalesmenVisitsDetails]]
- [[Rpt_Salesmensales2]]
- [[Rpt_SalespersonTargetComparison]]
- [[Rpt_SalespersonsDailyVisits]]
- [[Rpt_StandCustomersreport]]
- [[Rpt_StandView]]
- [[Rpt_StockTakingReportWithPrices]]
- [[Rpt_SupervisorSalesSummary]]
- [[Rpt_TargetSpartan]]
- [[Rpt_TotalInvoiceByDocTypes]]
- [[Rpt_TotalQtyBySalesmanByItems]]
- [[Rpt_TotalSalesmanRouteSummary]]
- [[Rpt_TransactionByDate]]
- [[Rpt_TransactionSales]]
- [[Rpt_UPriceReport]]
- [[Rpt_VoidedInvoices]]
- [[Rpt_WFCustomersVisits]]
- [[Rpt_WareHouse_Category_Balance]]
- [[Rpt_WareHouse_Item_Balance]]
- [[Rpt_WeeklySalesExpansion]]
- [[Rpt_WeeklySalesmanVisits]]
- [[Rpt_WithdrawalVoucher_Report]]
- [[Rpt_WorkFlowAnalysis]]
- [[Rpt_Workflow_ChangePrice]]

**Writes (10):**
- [[BaladInsertrtLoadDetailsintoTransactionstyp6]]
- [[OT_ImportReplacement]]
- [[OT_ImportSalesInvoices]]
- [[Pro_ConvertLoadOrderToTransaction]]
- [[Pro_ConvertUnloadOrderToTransaction]]
- [[Pro_ImportAlSamahData]]
- [[Pro_ReturnlineManagerApproval]]
- [[Pro_TransactionsDetails]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Qty semantics**: Quantity sign/units depend on TransactionTypeID (issue vs receipt vs transfer) — resolve type first via header join
- **No void flag**: IsVoid lives on the HEADER table only; do not filter IsVoid here
## Tenancy

Chatbot queries `t.TransactionsDetails` / `t.TransactionsHeaders` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
