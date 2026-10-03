---
type: table
database: Olives_BO
name: TransactionsHeaders
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[BusinessUnits]]
  - [[Companies]]
  - [[Contracts]]
  - [[Currencies]]
  - [[Customers]]
  - [[DocumentsTypes]]
  - [[PaymentsTypes]]
  - [[PriceLists]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[TransactionsTypes]]
referenced_by:
  - [[BaladInsertrtLoadHeadersintoTransactionstyp6]]
  - [[CalcItemBalance]]
  - [[DA_SalesTarget]]
  - [[Da_ProductPerformance]]
  - [[Da_SalesGrowth]]
  - [[Da_SalesperRep]]
  - [[Da_YearlyCompanyTargetAndSales]]
  - [[DiagnosticTools_CheckSalespersonunpostedOlivesTransactions]]
  - [[GetIssueItemsForOnline]]
  - [[GetTransfersOrdersForOnline]]
  - [[Invoice_Count_Hadara]]
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[OT_FixActionLog]]
  - [[OT_GetOrderInvoiceLinkHistory]]
  - [[OT_ImportActionLog]]
  - [[OT_ImportNewCust]]
  - [[OT_ImportReplacement]]
  - [[OT_ImportSalesInvoices]]
  - [[OT_Online_GetSalesmanSalesByMonths]]
  - [[OT_Online_RptSalesAndReturnPercByCustomer_Supervisor]]
  - [[OT_Online_RptSalesAndReturnPerc_Supervisor]]
  - [[OT_SENDSALESMANDATAFROMORDERS]]
  - [[OT_SendMultiSalesmanData]]
  - [[OT_SendSalesmanData]]
  - [[Pro_CalcSalespersonItemBalance]]
  - [[Pro_CheckItemsInvoiceBarcode]]
  - [[Pro_Checks]]
  - [[Pro_CompanyParameters]]
  - [[Pro_ConvertLoadOrderToTransaction]]
  - [[Pro_ConvertUnloadOrderToTransaction]]
  - [[Pro_DeliveryDashboard]]
  - [[Pro_GetCashCloseTotals]]
  - [[Pro_ImportAlSamahData]]
  - [[Pro_JoTaxApi]]
  - [[Pro_JoTaxResend]]
  - [[Pro_ReturnlineManagerApproval]]
  - [[Pro_RptCashTotalOnline_Android]]
  - [[Pro_RptCashTotalOnline_Android_Naqi]]
  - [[Pro_SalesReport_ItemCode]]
  - [[Pro_SalesmanStockAndReturnLoadOrders]]
  - [[Pro_SalespersonsTargetDashboard]]
  - [[Pro_StockSettlement]]
  - [[Pro_TransactionsHeaders]]
  - [[Pro_TransfersOrdersDetails]]
  - [[Pro_TransfersOrdersHeaders]]
  - [[Pro_TransfersOrdersQtyValidation]]
  - [[RPT_CUSTOMERSALESDETAILSBYITEMANDSALESPERSONNAME]]
  - [[RPT_SALESDETAILSCUSTOMERSBYVALUE]]
  - [[RPT_SUMMARYSALESAND]]
  - [[RPT_ZalloumReportONE]]
  - [[RPT_ZalloumReportTWO]]
  - [[RPT_ZheimanRouteSummaryForExcel]]
  - [[RptOnlineRpt_CustAging]]
  - [[RptOnlineRpt_DamageReturn]]
  - [[RptOnlineRpt_ItemAvgSalesByCustomer]]
  - [[RptOnlineRpt_ReturnDetails]]
  - [[RptOnlineRpt_SalesmanJournySummary]]
  - [[Rpt_AcceptedSalesInvoices]]
  - [[Rpt_ActiveAndInactiveCustomers]]
  - [[Rpt_AnnualTargetAnalysis]]
  - [[Rpt_AreaSalesAnalysis]]
  - [[Rpt_AreaSalesAndSalesmanTarget]]
  - [[Rpt_AssistantsSales]]
  - [[Rpt_AssistantsSalesDaily]]
  - [[Rpt_BasketReport]]
  - [[Rpt_BonusTypeForCustomers]]
  - [[Rpt_CashInvoiceAndReciept]]
  - [[Rpt_CashInvoicesBonus]]
  - [[Rpt_CashSummary]]
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
  - [[Rpt_CustomerLatsVistsAndInvoice]]
  - [[Rpt_CustomerMonthlySales]]
  - [[Rpt_CustomerMonthlySalesByArea]]
  - [[Rpt_CustomerNotSold]]
  - [[Rpt_CustomerNotSoldBySalemanGroup]]
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
  - [[Rpt_DUR]]
  - [[Rpt_DailySales]]
  - [[Rpt_DailySalesByCateg]]
  - [[Rpt_DailySalesSummary]]
  - [[Rpt_DeliverySales]]
  - [[Rpt_ExceededLimit]]
  - [[Rpt_GA_SalesmanAnalysis]]
  - [[Rpt_GpsLocationForTransaction]]
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
  - [[Rpt_LastInvoiceByRoute]]
  - [[Rpt_LiveQty]]
  - [[Rpt_MonthlyCompareSalesTargetWithCustomer]]
  - [[Rpt_MonthlySalesProfit]]
  - [[Rpt_NetSalesBySubCat]]
  - [[Rpt_NetSalesItems]]
  - [[Rpt_NetVisitsTime]]
  - [[Rpt_NetsalesAndLoadOrderAndRate]]
  - [[Rpt_NetsalesAndRate]]
  - [[Rpt_NewCustomersDetails]]
  - [[Rpt_NotSoldPerCateg]]
  - [[Rpt_OSFANewCustomers]]
  - [[Rpt_OrderMaster]]
  - [[Rpt_OrdersAcceptenceStatus]]
  - [[Rpt_PaymentsMappingNew]]
  - [[Rpt_PerformanceMetric]]
  - [[Rpt_Price]]
  - [[Rpt_PromotionCheckReport]]
  - [[Rpt_PromotionsWithDrawalsWithinDate]]
  - [[Rpt_ProposedOrder]]
  - [[Rpt_QuantitiesLoadReport]]
  - [[Rpt_Ransi_LastInvoiceRetInvoice]]
  - [[Rpt_ReasonReprint]]
  - [[Rpt_ReceiptsBySalesman]]
  - [[Rpt_ReprintCount]]
  - [[Rpt_ReturnSalesAmount]]
  - [[Rpt_RoutePerformanceAnalysis]]
  - [[Rpt_RouteScoreBySalesman]]
  - [[Rpt_RouteScoreBySalesman123]]
  - [[Rpt_RouteScoreBySalesmanFromDateToDate]]
  - [[Rpt_RouteSummaryByDelivery]]
  - [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
  - [[Rpt_RouteSummaryBySalesman_Delivery]]
  - [[Rpt_RouteSummaryDeatils]]
  - [[Rpt_RoutesAvg]]
  - [[Rpt_RoutesByPeriod]]
  - [[Rpt_SalesAmountWithDiscountByCategories]]
  - [[Rpt_SalesAndCollectionTargetByLocation]]
  - [[Rpt_SalesAndOrders]]
  - [[Rpt_SalesAndReturnPerc]]
  - [[Rpt_SalesAreaAndCategoryByCust]]
  - [[Rpt_SalesAreaByCategory]]
  - [[Rpt_SalesByLocationsAndRoute]]
  - [[Rpt_SalesByRoute]]
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
  - [[Rpt_SalesmanGeneralDailyVisitsScore]]
  - [[Rpt_SalesmanGroupByUnit]]
  - [[Rpt_SalesmanItemSalesPerRoute]]
  - [[Rpt_SalesmanItemsSales]]
  - [[Rpt_SalesmanItemsSalesSummary]]
  - [[Rpt_SalesmanJourneyPerformance]]
  - [[Rpt_SalesmanOrdersSummary]]
  - [[Rpt_SalesmanRouteAvg]]
  - [[Rpt_SalesmanRouteEfficiency]]
  - [[Rpt_SalesmanRouteEfficiency_SV_LV_TV2]]
  - [[Rpt_SalesmanRoutePerformance]]
  - [[Rpt_SalesmanRouteSummary]]
  - [[Rpt_SalesmanRouteTargetDetails]]
  - [[Rpt_SalesmanSalesByCategory]]
  - [[Rpt_SalesmanSalesByCategory2]]
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
  - [[Rpt_SalesmanTotalCashAndCheck]]
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
  - [[Rpt_SoldUnsoldPerRoute]]
  - [[Rpt_StandCustomersreport]]
  - [[Rpt_StandView]]
  - [[Rpt_StockTakingReportWithPrices]]
  - [[Rpt_SupervisorSalesSummary]]
  - [[Rpt_TotalInvoiceByDocTypes]]
  - [[Rpt_TotalQtyBySalesmanByItems]]
  - [[Rpt_TotalSalesmanRouteSummary]]
  - [[Rpt_TransactionByDate]]
  - [[Rpt_TransactionDateAndTime]]
  - [[Rpt_TransactionRouteAnalysis]]
  - [[Rpt_TransactionSales]]
  - [[Rpt_TransactionsNotes]]
  - [[Rpt_UPriceReport]]
  - [[Rpt_UnloadCustomersPerRoute]]
  - [[Rpt_UnvisitedCustomerDetails]]
  - [[Rpt_VoidedInvoices]]
  - [[Rpt_WFCustomersVisits]]
  - [[Rpt_WareHouse_Category_Balance]]
  - [[Rpt_WareHouse_Item_Balance]]
  - [[Rpt_WeeklySalesExpansion]]
  - [[Rpt_WeeklySalesmanVisits]]
  - [[Rpt_WithdrawalVoucher_Report]]
  - [[Rpt_WorkFlowAnalysis]]
  - [[Rpt_Workflow_ChangePrice]]
  - [[Rpt_first_last_visit_Invoice_TowerExcel]]
  - [[TECHNICAL_CHECKMISSINGSERIAL_OLIVES_BO_ORDER_RECEIPT_INV_RETINV]]
  - [[VoidInvoiceAsReturn]]
  - [[WF_AddWorkFlowLevels]]
  - [[ZeidanCustomersSales0ToMax]]
support_relevance: high
last_verified: 2026-10-03
related_workflows:
  - Daily-Sales-Cycle
  - Data-Sync-Cycle
  - Payments-and-Collections
  - Return-Reversal-Workflow
---
# TransactionsHeaders

## Business Purpose
The primary commercial transactions header table — stores completed sales invoices, return invoices, and credit notes issued by salesmen or back-office operators. Differentiated by `TransactionTypeID` (1 = Sales Invoice, 2 = Return Invoice, etc.). Captures composite PK (`TransactionTypeID`, `TransactionYear`, `TransactionNo`), customer (`CustomerID`), salesman (`SalesPersonID`), date (`TransactionDate`), financial totals (`NetTotal`, `Total`, `DiscountAmount`, `TaxAmount`), and void flags (`IsVoid`). Queryable via `t.TransactionsHeaders`.

## Chatbot semantics
(Query `t.TransactionsHeaders` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| فواتير المبيعات (Sales Invoices) | `TransactionTypeID`, `IsVoid` | `TransactionTypeID = 1 AND (IsVoid = 0 OR IsVoid IS NULL)` | Actual sales invoices issued |
| فواتير الإرجاع / المرتجعات | `TransactionTypeID`, `IsVoid` | `TransactionTypeID = 2 AND (IsVoid = 0 OR IsVoid IS NULL)` | Return sales invoices |
| إجمالي صافي المبيعات | `NetTotal` | `SUM(NetTotal)` with `TransactionTypeID = 1` | Standard sales figure |
| فواتير غير ملغاة | `IsVoid` | `IsVoid = 0 OR IsVoid IS NULL` | Excludes voided bills |
| نوع الدفع (نقدي / آجل) | `CreditCash` | 1 = Cash, 2 = Credit | Payment term classification |
| تفاصيل المواد المباعة | Join `t.TransactionsDetails` | `d.TransactionTypeID = h.TransactionTypeID AND d.TransactionYear = h.TransactionYear AND d.TransactionNo = h.TransactionNo` | Line items, sold quantity, bonuses |

**Do not confuse with:**
- `OrdersHeaders`: Pre-sales orders taken by salesmen before invoice generation. Orders do not establish accounting debt; `TransactionsHeaders` does.
- `Receipts`: Payment receipts collected against invoices or on-account (`t.Receipts`).
- `LogActionTransaction`: ActionID `4` logs the invoice issue *event* (with Data1=Year, Data2=No), but financial totals live here in `TransactionsHeaders`.

## Grain & keys
- **Composite PK**: (`CompanyID`, `TransactionTypeID`, `TransactionYear`, `TransactionNo`)
- **Tenant key**: `CompanyID`
- **FKs**: `CustomerID` → [[Customers]](ID), `SalesPersonID` → [[SalesPersons]](ID), `PriceListID` → [[PriceLists]](ID)

## Pipeline (how rows get here)
Created on mobile devices (direct van sales or delivery invoicing) → uploaded to `OSFA_DB` → imported to BO via `OT_ImportTransactions` / `OT_ImportInvoices`. `LogActionTransaction` ActionID 4/9 logs are created simultaneously.

## Related
- [[TransactionsDetails]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[Customers]]
- [[SalesPersons]]
- [[LogActionTransaction]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[PriceLists]] |
| TransactionTypeID | smallint | NO | ✓ | ✓ | [[TransactionsTypes]] |
| TransactionYear | smallint | NO | ✓ |  |  |
| TransactionNo | int | NO | ✓ |  |  |
| TransactionDate | smalldatetime | YES |  |  |  |
| SalesPersonID | int | YES |  | ✓ | [[SalesPersons]] |
| CustomerID | bigint | YES |  | ✓ | [[Customers]] |
| PriceListID | int | YES |  | ✓ | [[PriceLists]] |
| DocumentTypeID | int | YES |  | ✓ | [[DocumentsTypes]] |
| CreditCash | int | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| ForeignDiscountAmount | float | YES |  |  |  |
| ForeignDiscountPercent | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| CurrencyID | smallint | YES |  | ✓ | [[Currencies]] |
| ExchangeRate | float | YES |  |  |  |
| IsPrinted | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| RouteID | int | YES |  | ✓ | [[RoutesInformation]] |
| PostedToERP | bit | YES |  |  |  |
| IsVoid | bit | YES |  |  |  |
| CustomerName | varchar | YES |  |  |  |
| Approve | bit | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| BusinessUnitID | int | YES |  | ✓ | [[BusinessUnits]] |
| PostedToERP_Rec | bit | YES |  |  |  |
| PaymentType | int | YES |  | ✓ | [[PaymentsTypes]] |
| CustomerDiscountPerc | float | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| IsWFApproved | bit | YES |  |  |  |
| WFApproveDesc | nvarchar | YES |  |  |  |
| IsCheckInvoice | bit | YES |  |  |  |
| ContractID | nvarchar | YES |  | ✓ | [[Contracts]] |
| ForeignCustomerDiscountPerc | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| AcceptDate | smalldatetime | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| IsLinkedWithInv | bit | YES |  |  |  |
| DetailCount | int | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| PayAmount_Curr1 | float | YES |  |  |  |
| PayAmount_Curr2 | float | YES |  |  |  |
| AcceptedBy | nvarchar | YES |  |  |  |
| PatientName | varchar | YES |  |  |  |
| FileNo | varchar | YES |  |  |  |
| LocationLineID | int | YES |  |  |  |
| lineManagerApprove | bit | YES |  |  |  |
| DeliveryOrderYear | smallint | YES |  |  |  |
| DeliveryOrderNo | int | YES |  |  |  |
| InvDueDays | int | YES |  |  |  |
| IsDirectOnline | bit | YES |  |  |  |
| Manual_Disc | float | YES |  |  |  |
| IsLoan | bit | YES |  |  |  |
| LoanApproveBy | nvarchar | YES |  |  |  |
| PostedToERPDateTime | smalldatetime | YES |  |  |  |
| SalesmanStockYear | int | YES |  |  |  |
| SalesmanStockNo | int | YES |  |  |  |
| EINV_QR | nvarchar | YES |  |  |  |
| EINV_INV_UUID | uniqueidentifier | YES |  |  |  |
| IsFromCash | bit | YES |  |  |  |
| IsPostVoid | bit | YES |  |  |  |

## Primary Key
CompanyID
TransactionTypeID
TransactionYear
TransactionNo
## Foreign Keys
CompanyID, BusinessUnitID -> [[BusinessUnits]](CompanyID, ID)
CompanyID -> [[Companies]](ID)
CompanyID, ContractID -> [[Contracts]](CompanyID, ContractID)
CurrencyID -> [[Currencies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, TransactionTypeID, DocumentTypeID -> [[DocumentsTypes]](CompanyID, TransactionTypeID, ID)
CompanyID, PaymentType -> [[PaymentsTypes]](CompanyID, ID)
CompanyID, PriceListID -> [[PriceLists]](CompanyID, ID)
CompanyID, RouteID -> [[RoutesInformation]](CompanyID, ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
TransactionTypeID -> [[TransactionsTypes]](ID)
## Known Circular Dependencies
- Part of a circular FK chain: DocumentsTypes → TransactionsTypes → TransactionsDetails → TransactionsHeaders → DocumentsTypes.
- Part of a circular FK chain: DocumentsTypes → TransactionsTypes → TransactionsHeaders → DocumentsTypes.
- Part of a circular FK chain: TransactionsDetails → TransactionsHeaders → TransactionsTypes → TransactionsDetails.
## Impact / Procedures Using This Table

**Reads (373):**
- [[BaladInsertrtLoadHeadersintoTransactionstyp6]]
- [[CalcItemBalance]]
- [[DA_SalesTarget]]
- [[Da_ProductPerformance]]
- [[Da_SalesGrowth]]
- [[Da_SalesperRep]]
- [[Da_YearlyCompanyTargetAndSales]]
- [[DiagnosticTools_CheckSalespersonunpostedOlivesTransactions]]
- [[GetIssueItemsForOnline]]
- [[GetTransfersOrdersForOnline]]
- [[Invoice_Count_Hadara]]
- [[OT_FixActionLog]]
- [[OT_GetOrderInvoiceLinkHistory]]
- [[OT_ImportNewCust]]
- [[OT_ImportReplacement]]
- [[OT_Online_GetSalesmanSalesByMonths]]
- [[OT_Online_RptSalesAndReturnPercByCustomer_Supervisor]]
- [[OT_Online_RptSalesAndReturnPerc_Supervisor]]
- [[OT_SENDSALESMANDATAFROMORDERS]]
- [[OT_SendMultiSalesmanData]]
- [[Pro_CalcSalespersonItemBalance]]
- [[Pro_CheckItemsInvoiceBarcode]]
- [[Pro_Checks]]
- [[Pro_CompanyParameters]]
- [[Pro_DeliveryDashboard]]
- [[Pro_GetCashCloseTotals]]
- [[Pro_ImportAlSamahData]]
- [[Pro_JoTaxApi]]
- [[Pro_JoTaxResend]]
- [[Pro_ReturnlineManagerApproval]]
- [[Pro_RptCashTotalOnline_Android]]
- [[Pro_RptCashTotalOnline_Android_Naqi]]
- [[Pro_SalesReport_ItemCode]]
- [[Pro_SalesmanStockAndReturnLoadOrders]]
- [[Pro_SalespersonsTargetDashboard]]
- [[Pro_TransfersOrdersDetails]]
- [[Pro_TransfersOrdersHeaders]]
- [[Pro_TransfersOrdersQtyValidation]]
- [[RPT_CUSTOMERSALESDETAILSBYITEMANDSALESPERSONNAME]]
- [[RPT_SALESDETAILSCUSTOMERSBYVALUE]]
- [[RPT_SUMMARYSALESAND]]
- [[RPT_ZalloumReportONE]]
- [[RPT_ZalloumReportTWO]]
- [[RPT_ZheimanRouteSummaryForExcel]]
- [[RptOnlineRpt_CustAging]]
- [[RptOnlineRpt_DamageReturn]]
- [[RptOnlineRpt_ItemAvgSalesByCustomer]]
- [[RptOnlineRpt_ReturnDetails]]
- [[RptOnlineRpt_SalesmanJournySummary]]
- [[Rpt_AcceptedSalesInvoices]]
- [[Rpt_ActiveAndInactiveCustomers]]
- [[Rpt_AnnualTargetAnalysis]]
- [[Rpt_AreaSalesAnalysis]]
- [[Rpt_AreaSalesAndSalesmanTarget]]
- [[Rpt_AssistantsSales]]
- [[Rpt_AssistantsSalesDaily]]
- [[Rpt_BasketReport]]
- [[Rpt_BonusTypeForCustomers]]
- [[Rpt_CashInvoiceAndReciept]]
- [[Rpt_CashInvoicesBonus]]
- [[Rpt_CashSummary]]
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
- [[Rpt_CustomerLatsVistsAndInvoice]]
- [[Rpt_CustomerMonthlySales]]
- [[Rpt_CustomerMonthlySalesByArea]]
- [[Rpt_CustomerNotSold]]
- [[Rpt_CustomerNotSoldBySalemanGroup]]
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
- [[Rpt_DUR]]
- [[Rpt_DailySales]]
- [[Rpt_DailySalesByCateg]]
- [[Rpt_DailySalesSummary]]
- [[Rpt_DeliverySales]]
- [[Rpt_ExceededLimit]]
- [[Rpt_GA_SalesmanAnalysis]]
- [[Rpt_GpsLocationForTransaction]]
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
- [[Rpt_LastInvoiceByRoute]]
- [[Rpt_LiveQty]]
- [[Rpt_MonthlyCompareSalesTargetWithCustomer]]
- [[Rpt_MonthlySalesProfit]]
- [[Rpt_NetSalesBySubCat]]
- [[Rpt_NetSalesItems]]
- [[Rpt_NetVisitsTime]]
- [[Rpt_NetsalesAndLoadOrderAndRate]]
- [[Rpt_NetsalesAndRate]]
- [[Rpt_NewCustomersDetails]]
- [[Rpt_NotSoldPerCateg]]
- [[Rpt_OSFANewCustomers]]
- [[Rpt_OrderMaster]]
- [[Rpt_OrdersAcceptenceStatus]]
- [[Rpt_PaymentsMappingNew]]
- [[Rpt_PerformanceMetric]]
- [[Rpt_Price]]
- [[Rpt_PromotionCheckReport]]
- [[Rpt_PromotionsWithDrawalsWithinDate]]
- [[Rpt_ProposedOrder]]
- [[Rpt_QuantitiesLoadReport]]
- [[Rpt_Ransi_LastInvoiceRetInvoice]]
- [[Rpt_ReasonReprint]]
- [[Rpt_ReceiptsBySalesman]]
- [[Rpt_ReprintCount]]
- [[Rpt_ReturnSalesAmount]]
- [[Rpt_RoutePerformanceAnalysis]]
- [[Rpt_RouteScoreBySalesman]]
- [[Rpt_RouteScoreBySalesman123]]
- [[Rpt_RouteScoreBySalesmanFromDateToDate]]
- [[Rpt_RouteSummaryByDelivery]]
- [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
- [[Rpt_RouteSummaryBySalesman_Delivery]]
- [[Rpt_RouteSummaryDeatils]]
- [[Rpt_RoutesAvg]]
- [[Rpt_RoutesByPeriod]]
- [[Rpt_SalesAmountWithDiscountByCategories]]
- [[Rpt_SalesAndCollectionTargetByLocation]]
- [[Rpt_SalesAndOrders]]
- [[Rpt_SalesAndReturnPerc]]
- [[Rpt_SalesAreaAndCategoryByCust]]
- [[Rpt_SalesAreaByCategory]]
- [[Rpt_SalesByLocationsAndRoute]]
- [[Rpt_SalesByRoute]]
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
- [[Rpt_SalesmanGeneralDailyVisitsScore]]
- [[Rpt_SalesmanGroupByUnit]]
- [[Rpt_SalesmanItemSalesPerRoute]]
- [[Rpt_SalesmanItemsSales]]
- [[Rpt_SalesmanItemsSalesSummary]]
- [[Rpt_SalesmanJourneyPerformance]]
- [[Rpt_SalesmanOrdersSummary]]
- [[Rpt_SalesmanRouteAvg]]
- [[Rpt_SalesmanRouteEfficiency]]
- [[Rpt_SalesmanRouteEfficiency_SV_LV_TV2]]
- [[Rpt_SalesmanRoutePerformance]]
- [[Rpt_SalesmanRouteSummary]]
- [[Rpt_SalesmanRouteTargetDetails]]
- [[Rpt_SalesmanSalesByCategory]]
- [[Rpt_SalesmanSalesByCategory2]]
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
- [[Rpt_SalesmanTotalCashAndCheck]]
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
- [[Rpt_SoldUnsoldPerRoute]]
- [[Rpt_StandCustomersreport]]
- [[Rpt_StandView]]
- [[Rpt_StockTakingReportWithPrices]]
- [[Rpt_SupervisorSalesSummary]]
- [[Rpt_TotalInvoiceByDocTypes]]
- [[Rpt_TotalQtyBySalesmanByItems]]
- [[Rpt_TotalSalesmanRouteSummary]]
- [[Rpt_TransactionByDate]]
- [[Rpt_TransactionDateAndTime]]
- [[Rpt_TransactionRouteAnalysis]]
- [[Rpt_TransactionSales]]
- [[Rpt_TransactionsNotes]]
- [[Rpt_UPriceReport]]
- [[Rpt_UnloadCustomersPerRoute]]
- [[Rpt_UnvisitedCustomerDetails]]
- [[Rpt_VoidedInvoices]]
- [[Rpt_WFCustomersVisits]]
- [[Rpt_WareHouse_Category_Balance]]
- [[Rpt_WareHouse_Item_Balance]]
- [[Rpt_WeeklySalesExpansion]]
- [[Rpt_WeeklySalesmanVisits]]
- [[Rpt_WithdrawalVoucher_Report]]
- [[Rpt_WorkFlowAnalysis]]
- [[Rpt_Workflow_ChangePrice]]
- [[Rpt_first_last_visit_Invoice_TowerExcel]]
- [[TECHNICAL_CHECKMISSINGSERIAL_OLIVES_BO_ORDER_RECEIPT_INV_RETINV]]
- [[VoidInvoiceAsReturn]]
- [[ZeidanCustomersSales0ToMax]]

**Writes (88):**
- [[BaladInsertrtLoadHeadersintoTransactionstyp6]]
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[OT_ImportActionLog]]
- [[OT_ImportReplacement]]
- [[OT_ImportSalesInvoices]]
- [[OT_SendSalesmanData]]
- [[Pro_Checks]]
- [[Pro_ConvertLoadOrderToTransaction]]
- [[Pro_ConvertUnloadOrderToTransaction]]
- [[Pro_ImportAlSamahData]]
- [[Pro_JoTaxResend]]
- [[Pro_ReturnlineManagerApproval]]
- [[Pro_StockSettlement]]
- [[Pro_TransactionsHeaders]]
- [[VoidInvoiceAsReturn]]
- [[WF_AddWorkFlowLevels]]

## Estimated Size / Volatility
Typical business table
## TransactionTypeID catalog (live lookup)

See `TransactionsTypes` lookup table. Values: 1 Sales Invoice · 2 Return Sales Invoice · 3 Receipt Voucher · 4 Customer Stock · 5 Sales Order · 6 Transfer · 7 Unload · 8 Competitive Items · 9 Salesman Stock · 10 Return Order · 11 Sales Quotations · 12 Items Replacement In-Out · 13 Payment Order · 14 Debit Credit Note · 15 Issue Asset · 16 Receive Items · 17 IssueItems · 18 Bank Deposit · 99 Survey.

## Common Issues

- **Posting**: PostedToERP marks ERP export (no IsPosted column here)
- **Numbering**: voucher number columns are TransactionYear/TransactionNo (no VouNo)
- **FX**: exchange rates live in CurrenciesRate; this table has no ExRate column
- **Type filter**: always pair TransactionTypeID with the catalog above when answering "sales" vs "transfer" questions
## Tenancy

Chatbot queries `t.TransactionsHeaders` / `t.TransactionsDetails` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- See also (OSFA counterparts): [[OSFA_DB/Tables/OT_InvoiceHF]] and [[OSFA_DB/Tables/OT_OrderHF]]
