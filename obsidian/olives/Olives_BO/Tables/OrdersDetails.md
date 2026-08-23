---
type: table
database: Olives_BO
name: OrdersDetails
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
  - [[Companies]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[OrdersHeaders]]
referenced_by:
  - [[ABS_Integ_SendSalesOrder]]
  - [[ABS_Integ_SendSalesOrder_Jebrene]]
  - [[AX_INTEG_SENDORDERS]]
  - [[AbuOda_BonMarrof_Integ]]
  - [[AbuOda_Comp2_Integ]]
  - [[AbuOda_Integ]]
  - [[AccPack_Integ_SendSalesOrders]]
  - [[AccPack_Integ_SendSalesOrdersLuxuryItemstest]]
  - [[AccPack_Integ_SendSalesOrders_LuxuryItems]]
  - [[Awa2el_Integ_SendSalesOrders]]
  - [[Awtar_Integ_AllUsers]]
  - [[Awtar_Integ_SendSalesOrder]]
  - [[BO_Online_RptCustomerSalesTargetDetails]]
  - [[GP_Integ]]
  - [[GP_Integ_SendBackSalesOrder_Wadi]]
  - [[GP_Integ_SendSalesOrder_Wadi]]
  - [[GP_Integ_SendSalesOrder_Zumot]]
  - [[GP_Integ_SendSalesOrder_Zumot_Aqaba]]
  - [[GP_Integ_Wadi]]
  - [[Galaxy_Integ_SendSalesOrder]]
  - [[GetSalesOrdersForEdit]]
  - [[GetSalesOrdersForOnlineReport]]
  - [[GetWF_SalesOrderData]]
  - [[Integ_Normal_DeliveryOrder]]
  - [[Integ_SendSalesOrders_CB]]
  - [[IscoJordan_Integ_SendOrders]]
  - [[Izhiman_SAP_Integ]]
  - [[Khobara_Integ]]
  - [[MeatLand_Integrationnew]]
  - [[Motakaml_Integ_SendSalesOrders]]
  - [[NPF_Integ_SendSalesOrders]]
  - [[Niroukh_Integ_AllUsers]]
  - [[Niroukh_Integ_SendSalesOrder]]
  - [[OSFA_MobileDeliveryAPI]]
  - [[OT_GetOrderInvoiceLinkHistory]]
  - [[OT_ImportSalesOrders]]
  - [[PRESTOSOFT_INTEG_SENDORDERS_COMP2]]
  - [[Phenix_Sukhtian_Integ_SendSalesOrder]]
  - [[PrestoSoft_Integ_SendOrders]]
  - [[ProTech_Integration_SendOrders]]
  - [[Pro_BackOrderItems]]
  - [[Pro_Dashboard_Almalak]]
  - [[Pro_DriverDetailsDashboard]]
  - [[Pro_Items]]
  - [[Pro_ItemsSalesStats]]
  - [[Pro_ItemsSalesStatus]]
  - [[Pro_ItemsUnitsDetails]]
  - [[Pro_MapTransactionLog]]
  - [[Pro_MerchandiseDashboard]]
  - [[Pro_OrdersDetails]]
  - [[Pro_OrdersHeaders]]
  - [[Pro_SalesOrdersQtyValidation]]
  - [[Pro_SalesmanDetailsDashboard]]
  - [[Pro_SalespersonsTargetDashboard]]
  - [[Qerat_Integ]]
  - [[Qetaf_Integ]]
  - [[RouteCoverageSummary_New_Excel]]
  - [[Rpt_ApprovedOrder]]
  - [[Rpt_BackOrder]]
  - [[Rpt_BackOrderItems]]
  - [[Rpt_CompareCustomerStockWithOrder]]
  - [[Rpt_ConcreteOperationManager]]
  - [[Rpt_ConcreteVehicleTransactions]]
  - [[Rpt_CustomerSalesOrderByClassTablet]]
  - [[Rpt_CustomerSalesTablet]]
  - [[Rpt_CustomerStockNotExistByDocType]]
  - [[Rpt_CustomerStockNotExistByDocType_Summary]]
  - [[Rpt_CustomersOrderbyItemReport]]
  - [[Rpt_CustomersOrdersSummary]]
  - [[Rpt_CustomersPromotionLog]]
  - [[Rpt_CustomersVisitsCount]]
  - [[Rpt_DailyConcrete]]
  - [[Rpt_DailyConcreteSalesAndCollection]]
  - [[Rpt_DeliveryBatchHeader]]
  - [[Rpt_DeliveryBatchSummery]]
  - [[Rpt_GA_SalesmanAnalysis]]
  - [[Rpt_ItemsSalesPerCustomer]]
  - [[Rpt_ItemsStockStatement]]
  - [[Rpt_LoadOrderFirstApproval]]
  - [[Rpt_MasterOrders]]
  - [[Rpt_MonthlyCompareSalesTargetWithCustomer]]
  - [[Rpt_MonthlyCompareSalesTargetWithSales]]
  - [[Rpt_MonthlyCompareSalesTargetWithSales_Spartan]]
  - [[Rpt_NetVisitsTime]]
  - [[Rpt_OrderLink]]
  - [[Rpt_OrderMaster]]
  - [[Rpt_OrdersModificationsLog]]
  - [[Rpt_OrdersSalesReport]]
  - [[Rpt_OrdersSalesReportByCategoty]]
  - [[Rpt_PrintOrdersBatches]]
  - [[Rpt_ReceivablesSalesInvoice]]
  - [[Rpt_RoutePerformanceAnalysis]]
  - [[Rpt_RoutePerformanceAnalysis_Spartan]]
  - [[Rpt_RouteSummaryBySalesman]]
  - [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
  - [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
  - [[Rpt_RouteSummaryBySalesman_Merchandisers]]
  - [[Rpt_RouteSummaryBySalesman_Spartan]]
  - [[Rpt_RouteSummaryBySalesman_Sukhtian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
  - [[Rpt_RouteSummaryDeatils]]
  - [[Rpt_SalesAndOrders]]
  - [[Rpt_SalesManRouteSalesComparison]]
  - [[Rpt_SalesOrderPerformance]]
  - [[Rpt_SalesOrdersSummaryBySalesman]]
  - [[Rpt_SalesPersonItemBonusTarget]]
  - [[Rpt_SalesPersonItemBonusTarget_Tablet]]
  - [[Rpt_Sales_Statistics]]
  - [[Rpt_SalesmanAnalysisDashBoard]]
  - [[Rpt_SalesmanCategorySales]]
  - [[Rpt_SalesmanDailyActivities]]
  - [[Rpt_SalesmanDaySummary]]
  - [[Rpt_SalesmanOrders]]
  - [[Rpt_SalesmanOrdersSummary]]
  - [[Rpt_SalesmanOrdersSummaryByCategory]]
  - [[Rpt_SalesmanOrdersSummaryByTargetRef]]
  - [[Rpt_SalesmanRouteAvg]]
  - [[Rpt_SalesmanSalesByItems]]
  - [[Rpt_SalesmanSalesByTotalCategory]]
  - [[Rpt_SalesmanSalesItemTab]]
  - [[Rpt_SalesmanSalesSummary]]
  - [[Rpt_SalesmanSummaryRoute]]
  - [[Rpt_SalesmanSummaryRoute_60]]
  - [[Rpt_SalesmanSummaryRoute_Atieh]]
  - [[Rpt_SalesmanSummaryRoute_Dandana]]
  - [[Rpt_SalesmanSummaryRoute_zz]]
  - [[Rpt_SalesmanTimeSpentPerCustomer]]
  - [[Rpt_SalesmanTimeSpentPerCustomer2]]
  - [[Rpt_SalesmanTimeSpentPerCustomer3]]
  - [[Rpt_SalesmanTimeSpentPerCustomer4]]
  - [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
  - [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
  - [[Rpt_SalesmanTimeSpentPerCustomerQima8]]
  - [[Rpt_SalesmanVisitsRoute]]
  - [[Rpt_Salesman_Collections]]
  - [[Rpt_SalespersonsDailyVisits]]
  - [[Rpt_TargetSpartan]]
  - [[Rpt_TotalSalesmanRouteSummary]]
  - [[Rpt_UnloadOrder]]
  - [[Rpt_WFCustomersVisits]]
  - [[Rpt_WF_GeneralSalesByItem]]
  - [[Rpt_WorkFlowAnalysis]]
  - [[SAP_Tyconz_Integ_SendSalesOrders]]
  - [[SMS_Almobhiron]]
  - [[SMS_Bostangy]]
  - [[SMS_Lamis]]
  - [[SMS_SpartenNew]]
  - [[SMS_Wales]]
  - [[SN_Integ_SendOrders]]
  - [[Salbeshian_SAP_Integ]]
  - [[Shamel_Integ_SendSalesOrders]]
  - [[Shini_Integ]]
  - [[Spartan_SAP_Integ_draft]]
  - [[TECHNICAL_CHECKMISSINGSERIAL_OLIVES_BO_ORDER_RECEIPT_INV_RETINV]]
  - [[Tablet_GetPendingOrdersTotals]]
  - [[WF_AddRequestToIncreaseCustomerCreditlimit]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
  - [[Wings_Integ_SendSalesOrder]]
  - [[Zedan_SAP_Integ]]
support_relevance: high
last_verified: 2026-07-05
---
# OrdersDetails


## Business Purpose

Line-item details for sales orders — products, quantities, prices, and discounts per order.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[OrdersHeaders]] |
| OrderYear | int | NO | ✓ | ✓ | [[OrdersHeaders]] |
| OrderNo | int | NO | ✓ | ✓ | [[OrdersHeaders]] |
| ItemCode | nvarchar | NO | ✓ | ✓ | [[Items]] |
| UnitID | nvarchar | NO | ✓ | ✓ | [[ItemsUnits]] |
| Quantity | float | YES |  |  |  |
| Bonus | float | YES |  |  |  |
| PromisesDate | smalldatetime | YES |  |  |  |
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
| CustomerDiscountAmount | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| OrginalQty | float | YES |  |  |  |
| OrginalBonus | float | YES |  |  |  |
| UPrice | float | YES |  |  |  |
| TaxType1 | smallint | YES |  |  |  |
| TaxPercent1 | float | YES |  |  |  |
| TaxAmount1 | float | YES |  |  |  |
| TaxType2 | smallint | YES |  |  |  |
| TaxPercent2 | float | YES |  |  |  |
| TaxAmount2 | float | YES |  |  |  |
| Manual_Bonus | float | YES |  |  |  |
| ExchangeRate | float | YES |  |  |  |
| Manual_Disc | float | YES |  |  |  |
| QtyAsBonus | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| BonusTax | float | YES |  |  |  |
| BonusAmount | float | YES |  |  |  |
| LineSort | smallint | YES |  |  |  |
| Ref1 | varchar | YES |  |  |  |
| Ref2 | varchar | YES |  |  |  |
| Ref3 | varchar | YES |  |  |  |
| TotalPrice | float | YES |  |  |  |
| SysCodeTypeID | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
ItemCode
UnitID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, ItemCode -> [[Items]](CompanyID, ItemCode)
CompanyID, UnitID -> [[ItemsUnits]](CompanyID, ID)
CompanyID, OrderYear, OrderNo -> [[OrdersHeaders]](CompanyID, OrderYear, OrderNo)
## Impact / Procedures Using This Table

**Reads (160):**
- [[ABS_Integ_SendSalesOrder]]
- [[ABS_Integ_SendSalesOrder_Jebrene]]
- [[AX_INTEG_SENDORDERS]]
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[AccPack_Integ_SendSalesOrders]]
- [[AccPack_Integ_SendSalesOrdersLuxuryItemstest]]
- [[AccPack_Integ_SendSalesOrders_LuxuryItems]]
- [[Awa2el_Integ_SendSalesOrders]]
- [[Awtar_Integ_AllUsers]]
- [[Awtar_Integ_SendSalesOrder]]
- [[BO_Online_RptCustomerSalesTargetDetails]]
- [[GP_Integ]]
- [[GP_Integ_SendBackSalesOrder_Wadi]]
- [[GP_Integ_SendSalesOrder_Wadi]]
- [[GP_Integ_SendSalesOrder_Zumot]]
- [[GP_Integ_SendSalesOrder_Zumot_Aqaba]]
- [[GP_Integ_Wadi]]
- [[Galaxy_Integ_SendSalesOrder]]
- [[GetSalesOrdersForEdit]]
- [[GetSalesOrdersForOnlineReport]]
- [[GetWF_SalesOrderData]]
- [[Integ_Normal_DeliveryOrder]]
- [[Integ_SendSalesOrders_CB]]
- [[IscoJordan_Integ_SendOrders]]
- [[Izhiman_SAP_Integ]]
- [[Khobara_Integ]]
- [[MeatLand_Integrationnew]]
- [[Motakaml_Integ_SendSalesOrders]]
- [[NPF_Integ_SendSalesOrders]]
- [[Niroukh_Integ_AllUsers]]
- [[Niroukh_Integ_SendSalesOrder]]
- [[OSFA_MobileDeliveryAPI]]
- [[OT_GetOrderInvoiceLinkHistory]]
- [[PRESTOSOFT_INTEG_SENDORDERS_COMP2]]
- [[Phenix_Sukhtian_Integ_SendSalesOrder]]
- [[PrestoSoft_Integ_SendOrders]]
- [[ProTech_Integration_SendOrders]]
- [[Pro_BackOrderItems]]
- [[Pro_Dashboard_Almalak]]
- [[Pro_DriverDetailsDashboard]]
- [[Pro_Items]]
- [[Pro_ItemsSalesStats]]
- [[Pro_ItemsSalesStatus]]
- [[Pro_ItemsUnitsDetails]]
- [[Pro_MapTransactionLog]]
- [[Pro_MerchandiseDashboard]]
- [[Pro_OrdersDetails]]
- [[Pro_OrdersHeaders]]
- [[Pro_SalesOrdersQtyValidation]]
- [[Pro_SalesmanDetailsDashboard]]
- [[Pro_SalespersonsTargetDashboard]]
- [[Qerat_Integ]]
- [[Qetaf_Integ]]
- [[RouteCoverageSummary_New_Excel]]
- [[Rpt_ApprovedOrder]]
- [[Rpt_BackOrder]]
- [[Rpt_BackOrderItems]]
- [[Rpt_CompareCustomerStockWithOrder]]
- [[Rpt_ConcreteOperationManager]]
- [[Rpt_ConcreteVehicleTransactions]]
- [[Rpt_CustomerSalesOrderByClassTablet]]
- [[Rpt_CustomerSalesTablet]]
- [[Rpt_CustomerStockNotExistByDocType]]
- [[Rpt_CustomerStockNotExistByDocType_Summary]]
- [[Rpt_CustomersOrderbyItemReport]]
- [[Rpt_CustomersOrdersSummary]]
- [[Rpt_CustomersPromotionLog]]
- [[Rpt_CustomersVisitsCount]]
- [[Rpt_DailyConcrete]]
- [[Rpt_DailyConcreteSalesAndCollection]]
- [[Rpt_DeliveryBatchHeader]]
- [[Rpt_DeliveryBatchSummery]]
- [[Rpt_GA_SalesmanAnalysis]]
- [[Rpt_ItemsSalesPerCustomer]]
- [[Rpt_ItemsStockStatement]]
- [[Rpt_LoadOrderFirstApproval]]
- [[Rpt_MasterOrders]]
- [[Rpt_MonthlyCompareSalesTargetWithCustomer]]
- [[Rpt_MonthlyCompareSalesTargetWithSales]]
- [[Rpt_MonthlyCompareSalesTargetWithSales_Spartan]]
- [[Rpt_NetVisitsTime]]
- [[Rpt_OrderLink]]
- [[Rpt_OrderMaster]]
- [[Rpt_OrdersModificationsLog]]
- [[Rpt_OrdersSalesReport]]
- [[Rpt_OrdersSalesReportByCategoty]]
- [[Rpt_PrintOrdersBatches]]
- [[Rpt_ReceivablesSalesInvoice]]
- [[Rpt_RoutePerformanceAnalysis]]
- [[Rpt_RoutePerformanceAnalysis_Spartan]]
- [[Rpt_RouteSummaryBySalesman]]
- [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
- [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
- [[Rpt_RouteSummaryBySalesman_Merchandisers]]
- [[Rpt_RouteSummaryBySalesman_Spartan]]
- [[Rpt_RouteSummaryBySalesman_Sukhtian]]
- [[Rpt_RouteSummaryBySalesman_Suktian]]
- [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
- [[Rpt_RouteSummaryDeatils]]
- [[Rpt_SalesAndOrders]]
- [[Rpt_SalesManRouteSalesComparison]]
- [[Rpt_SalesOrderPerformance]]
- [[Rpt_SalesOrdersSummaryBySalesman]]
- [[Rpt_SalesPersonItemBonusTarget]]
- [[Rpt_SalesPersonItemBonusTarget_Tablet]]
- [[Rpt_Sales_Statistics]]
- [[Rpt_SalesmanAnalysisDashBoard]]
- [[Rpt_SalesmanCategorySales]]
- [[Rpt_SalesmanDailyActivities]]
- [[Rpt_SalesmanDaySummary]]
- [[Rpt_SalesmanOrders]]
- [[Rpt_SalesmanOrdersSummary]]
- [[Rpt_SalesmanOrdersSummaryByCategory]]
- [[Rpt_SalesmanOrdersSummaryByTargetRef]]
- [[Rpt_SalesmanRouteAvg]]
- [[Rpt_SalesmanSalesByItems]]
- [[Rpt_SalesmanSalesByTotalCategory]]
- [[Rpt_SalesmanSalesItemTab]]
- [[Rpt_SalesmanSalesSummary]]
- [[Rpt_SalesmanSummaryRoute]]
- [[Rpt_SalesmanSummaryRoute_60]]
- [[Rpt_SalesmanSummaryRoute_Atieh]]
- [[Rpt_SalesmanSummaryRoute_Dandana]]
- [[Rpt_SalesmanSummaryRoute_zz]]
- [[Rpt_SalesmanTimeSpentPerCustomer]]
- [[Rpt_SalesmanTimeSpentPerCustomer2]]
- [[Rpt_SalesmanTimeSpentPerCustomer3]]
- [[Rpt_SalesmanTimeSpentPerCustomer4]]
- [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
- [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
- [[Rpt_SalesmanTimeSpentPerCustomerQima8]]
- [[Rpt_SalesmanVisitsRoute]]
- [[Rpt_Salesman_Collections]]
- [[Rpt_SalespersonsDailyVisits]]
- [[Rpt_TargetSpartan]]
- [[Rpt_TotalSalesmanRouteSummary]]
- [[Rpt_UnloadOrder]]
- [[Rpt_WFCustomersVisits]]
- [[Rpt_WF_GeneralSalesByItem]]
- [[Rpt_WorkFlowAnalysis]]
- [[SAP_Tyconz_Integ_SendSalesOrders]]
- [[SMS_Almobhiron]]
- [[SMS_Bostangy]]
- [[SMS_Lamis]]
- [[SMS_SpartenNew]]
- [[SMS_Wales]]
- [[SN_Integ_SendOrders]]
- [[Salbeshian_SAP_Integ]]
- [[Shamel_Integ_SendSalesOrders]]
- [[Shini_Integ]]
- [[Spartan_SAP_Integ_draft]]
- [[TECHNICAL_CHECKMISSINGSERIAL_OLIVES_BO_ORDER_RECEIPT_INV_RETINV]]
- [[Tablet_GetPendingOrdersTotals]]
- [[WF_AddRequestToIncreaseCustomerCreditlimit]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]
- [[Wings_Integ_SendSalesOrder]]
- [[Zedan_SAP_Integ]]

**Writes (2):**
- [[OT_ImportSalesOrders]]
- [[Pro_OrdersDetails]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
