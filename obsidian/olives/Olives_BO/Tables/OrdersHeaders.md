---
type: table
database: Olives_BO
name: OrdersHeaders
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
  - [[BusinessUnits]]
  - [[Companies]]
  - [[Contracts]]
  - [[Currencies]]
  - [[Customers]]
  - [[PriceLists]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
referenced_by:
  - [[All_Visits]]
  - [[BO_Online_RptCustomerSalesTargetDetails]]
  - [[DEMOSALESPERSON]]
  - [[DEMOSALESPERSON2]]
  - [[DiagnosticTools_CheckSalespersonunpostedOlivesTransactions]]
  - [[GetOrderHistoryStatus_Online]]
  - [[GetSalesOrdersForEdit]]
  - [[GetSalesOrdersForOnlineReport]]
  - [[GetWF_SalesOrderData]]
  - [[MedicalEfficiencyOnlineReport]]
  - [[OSFA_MobileDeliveryAPI]]
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[OT_FixActionLog]]
  - [[OT_GetOrderInvoiceLinkHistory]]
  - [[OT_ImportActionLog]]
  - [[OT_ImportSalesIssueItems]]
  - [[OT_ImportSalesOrders]]
  - [[OT_SendCustomersInfo]]
  - [[OT_SendMultiSalesmanData]]
  - [[OT_SendSalesmanData]]
  - [[Pro_ApprovedOrder]]
  - [[Pro_BackOrderItems]]
  - [[Pro_CompanyParameters]]
  - [[Pro_Dashboard_Almalak]]
  - [[Pro_DriverDetailsDashboard]]
  - [[Pro_ItemsSalesStats]]
  - [[Pro_ItemsSalesStatus]]
  - [[Pro_MapTransactionLog]]
  - [[Pro_MerchandiseDashboard]]
  - [[Pro_OrdersDetails]]
  - [[Pro_OrdersHeaders]]
  - [[Pro_SalesOrdersQtyValidation]]
  - [[Pro_SalesmanDetailsDashboard]]
  - [[Pro_SalespersonsTargetDashboard]]
  - [[RouteCoverageSummary_New_Excel]]
  - [[Rpt_ActiveAndInactiveCustomers]]
  - [[Rpt_ApprovedOrder]]
  - [[Rpt_BackOrder]]
  - [[Rpt_BackOrderItems]]
  - [[Rpt_CompareCustomerStockWithOrder]]
  - [[Rpt_ConcreteOperationManager]]
  - [[Rpt_ConcreteVehicleTransactions]]
  - [[Rpt_CustomerStockNotExistByDocType]]
  - [[Rpt_CustomerStockNotExistByDocType_Summary]]
  - [[Rpt_CustomersOrderbyItemReport]]
  - [[Rpt_CustomersOrdersSummary]]
  - [[Rpt_CustomersPromotionLog]]
  - [[Rpt_CustomersVisitsCount]]
  - [[Rpt_DUR]]
  - [[Rpt_DailyConcrete]]
  - [[Rpt_DailyConcreteSalesAndCollection]]
  - [[Rpt_DeliveryBatchHeader]]
  - [[Rpt_DeliveryBatchSummery]]
  - [[Rpt_ExceededLimit]]
  - [[Rpt_GA_SalesmanAnalysis]]
  - [[Rpt_IncreaseCreditLimit]]
  - [[Rpt_IncreaseCreditLimit_forALPHA]]
  - [[Rpt_ItemsSalesPerCustomer]]
  - [[Rpt_ItemsStockStatement]]
  - [[Rpt_LoadOrderFirstApproval]]
  - [[Rpt_MasterOrders]]
  - [[Rpt_MonthlyCompareSalesTargetWithCustomer]]
  - [[Rpt_MonthlyCompareSalesTargetWithSales]]
  - [[Rpt_NetVisitsTime]]
  - [[Rpt_OrderHeader]]
  - [[Rpt_OrderLink]]
  - [[Rpt_OrderMaster]]
  - [[Rpt_OrdersAcceptenceStatus]]
  - [[Rpt_OrdersDeliveryDrivers]]
  - [[Rpt_OrdersModificationsLog]]
  - [[Rpt_OrdersSalesReport]]
  - [[Rpt_OrdersSalesReportByCategoty]]
  - [[Rpt_PrintOrdersBatches]]
  - [[Rpt_ReasonReprint]]
  - [[Rpt_ReprintCount]]
  - [[Rpt_RoutePerformanceAnalysis]]
  - [[Rpt_RouteScoreBySalesman]]
  - [[Rpt_RouteScoreBySalesman123]]
  - [[Rpt_RouteScoreBySalesmanFromDateToDate]]
  - [[Rpt_RouteSummaryBySalesman]]
  - [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
  - [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
  - [[Rpt_RouteSummaryBySalesman_Merchandisers]]
  - [[Rpt_RouteSummaryBySalesman_Sukhtian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
  - [[Rpt_RouteSummaryDeatils]]
  - [[Rpt_RoutesAvg]]
  - [[Rpt_RoutesByPeriod]]
  - [[Rpt_SalesAndOrders]]
  - [[Rpt_SalesManRouteSalesComparison]]
  - [[Rpt_SalesOrderPerformance]]
  - [[Rpt_SalesOrdersSummaryBySalesman]]
  - [[Rpt_SalesPersonItemBonusTarget]]
  - [[Rpt_Sales_Statistics]]
  - [[Rpt_SalesmanAnalysisDashBoard]]
  - [[Rpt_SalesmanCategorySales]]
  - [[Rpt_SalesmanDailyActivities]]
  - [[Rpt_SalesmanDaySummary]]
  - [[Rpt_SalesmanGeneralDailyVisitsScore]]
  - [[Rpt_SalesmanOrders]]
  - [[Rpt_SalesmanOrdersSummary]]
  - [[Rpt_SalesmanOrdersSummaryByCategory]]
  - [[Rpt_SalesmanOrdersSummaryByTargetRef]]
  - [[Rpt_SalesmanRouteAvg]]
  - [[Rpt_SalesmanRouteEfficiency]]
  - [[Rpt_SalesmanRouteEfficiency_SV_LV_TV2]]
  - [[Rpt_SalesmanRouteSummary]]
  - [[Rpt_SalesmanRouteTargetDetails]]
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
  - [[Rpt_TransactionDateAndTime]]
  - [[Rpt_TransactionsNotes]]
  - [[Rpt_UnloadOrder]]
  - [[Rpt_WFCustomersVisits]]
  - [[Rpt_WF_GeneralSalesByItem]]
  - [[Rpt_WF_SalesOrderStatus]]
  - [[Rpt_WorkFlowAnalysis]]
  - [[Rpt_WorkFlowFunctions]]
  - [[SendEmailSalesOrder_Tower]]
  - [[TECHNICAL_CHECKMISSINGSERIAL_OLIVES_BO_ORDER_RECEIPT_INV_RETINV]]
  - [[WF_AddRequestToIncreaseCustomerCreditlimit]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
  - [[WF_GetCustAgingInfo]]
  - [[WF_GetPositionWFData]]
  - [[WF_GetPositionWFData_Alerts]]
support_relevance: high
last_verified: 2026-10-03
---
# OrdersHeaders

## Business Purpose
The sales orders header table — stores pre-sales orders taken by salesmen on mobile devices or entered in the back office. Key columns include composite PK (`OrderYear`, `OrderNo`), ordering customer (`CustomerID`), salesman (`SalesPersonID`), date (`OrderDate`), financial totals (`NetTotal`, `Total`, `DiscountAmount`, `TaxAmount`), and status flags (`IsVoid`). Queryable via `t.OrdersHeaders`.

## Chatbot semantics
(Query `t.OrdersHeaders` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| طلبيات البيع / طلبات المندوب | `CustomerID`, `SalesPersonID`, `OrderDate` | Filter by salesman, customer, or date | Pre-sales order documents |
| الطلبيات غير الملغاة | `IsVoid` | `IsVoid = 0` (or `IS NULL`) | Excludes voided/cancelled orders |
| إجمالي قيمة الطلبية | `NetTotal` | Sum or select | Final invoiceable amount after discounts & taxes |
| تفاصيل المواد في الطلبية | Join `t.OrdersDetails` | `d.OrderYear = o.OrderYear AND d.OrderNo = o.OrderNo` | Items, quantities, prices, bonus |
| ربط الطلبية بسير الموافقات | Join `t.WF_MasterLog` | `m.FunctionID = 6 AND TRY_CAST(m.Ref1 AS int) = o.OrderYear AND TRY_CAST(m.Ref2 AS numeric) = o.OrderNo` | Approval state of high-value/credit-exceeding orders |

**Do not confuse with:**
- `TransactionsHeaders`: Actual delivered sales invoices (`TransactionTypeID = 1`). Orders represent pre-sales requests; invoices represent delivered goods and debt.
- `ReturnOrdersHeaders`: Return orders (goods returned from customers).
- `PendingInvoices`: Invoices waiting for upload/approval.

## Grain & keys
- **Composite PK**: (`CompanyID`, `OrderYear`, `OrderNo`)
- **Tenant key**: `CompanyID`
- **FKs**: `CustomerID` → [[Customers]](ID), `SalesPersonID` → [[SalesPersons]](ID), `PriceListID` → [[PriceLists]](ID)

## Pipeline (how rows get here)
Salesman enters order on mobile device → `OT_ImportSalesOrders` or `OT_ImportUploadOrders` copies into `OrdersHeaders` and `OrdersDetails`. If workflow approval required, generates `WF_MasterLog` (`FunctionID = 6`).

## Related
- [[OrdersDetails]]
- [[Customers]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[WF_MasterLog]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Contracts]] |
| OrderYear | int | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| OrderDate | smalldatetime | YES |  |  |  |
| PromisesDate | smalldatetime | YES |  |  |  |
| CustomerID | bigint | YES |  | ✓ | [[Customers]] |
| SalesPersonID | int | YES |  | ✓ | [[SalesPersons]] |
| PriceListID | int | YES |  | ✓ | [[PriceLists]] |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| ForeignDiscountAmount | float | YES |  |  |  |
| ForeignDiscountPercent | float | YES |  |  |  |
| CurrencyID | smallint | YES |  | ✓ | [[Currencies]] |
| ExchangeRate | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
| RouteID | int | YES |  | ✓ | [[RoutesInformation]] |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| PaymentType | int | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| WFApproved | bit | YES |  |  |  |
| Approved | bit | YES |  |  |  |
| DocumentsTypesID | int | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| BusinessUnitID | int | YES |  | ✓ | [[BusinessUnits]] |
| CustomerDiscountPerc | float | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| IsVoid | bit | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| ContractID | nvarchar | YES |  | ✓ | [[Contracts]] |
| ForeignCustomerDiscountPerc | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| IsPostBackOrder | bit | YES |  |  |  |
| IsPostBackOrderToERP | bit | YES |  |  |  |
| CreditCash | int | YES |  |  |  |
| PostedByEmail | bit | YES |  |  |  |
| AcceptDate | smalldatetime | YES |  |  |  |
| DetailCount | int | YES |  |  |  |
| DeliveryBatchID | int | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| ExtraNote | nvarchar | YES |  |  |  |
| IsDelivered | bit | YES |  |  |  |
| Manual_Disc | float | YES |  |  |  |
| BackOrderYear | smallint | YES |  |  |  |
| BackOrderNo | bigint | YES |  |  |  |
| FinalApproval | bit | YES |  |  |  |
| PostedToERPDateTime | smalldatetime | YES |  |  |  |
| UsedInAutoUploadOrder | bit | YES |  |  |  |
| LocationLineID | int | YES |  |  |  |
| MakeCashDiscount | bit | YES |  |  |  |
| QuotationYear | smallint | YES |  |  |  |
| QuotationNo | int | YES |  |  |  |
| NeedApproval | bit | YES |  |  |  |
| DriverNo | int | YES |  |  |  |
| NoNeedCreditCheck | bit | YES |  |  |  |
| TransFees | float | YES |  |  |  |
| ForeignTransFees | float | YES |  |  |  |
| CheckInTime | smalldatetime | YES |  |  |  |
| CustomerName | nvarchar | YES |  |  |  |
| Address | nvarchar | YES |  |  |  |

## Primary Key
CompanyID
OrderYear
OrderNo
## Foreign Keys
CompanyID, BusinessUnitID -> [[BusinessUnits]](CompanyID, ID)
CompanyID -> [[Companies]](ID)
CompanyID, ContractID -> [[Contracts]](CompanyID, ContractID)
CurrencyID -> [[Currencies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, PriceListID -> [[PriceLists]](CompanyID, ID)
CompanyID, RouteID -> [[RoutesInformation]](CompanyID, ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (214):**
- [[All_Visits]]
- [[BO_Online_RptCustomerSalesTargetDetails]]
- [[DEMOSALESPERSON]]
- [[DEMOSALESPERSON2]]
- [[DiagnosticTools_CheckSalespersonunpostedOlivesTransactions]]
- [[GetOrderHistoryStatus_Online]]
- [[GetSalesOrdersForEdit]]
- [[GetSalesOrdersForOnlineReport]]
- [[GetWF_SalesOrderData]]
- [[MedicalEfficiencyOnlineReport]]
- [[OSFA_MobileDeliveryAPI]]
- [[OT_FixActionLog]]
- [[OT_GetOrderInvoiceLinkHistory]]
- [[OT_ImportSalesIssueItems]]
- [[OT_SendCustomersInfo]]
- [[OT_SendMultiSalesmanData]]
- [[OT_SendSalesmanData]]
- [[Pro_ApprovedOrder]]
- [[Pro_BackOrderItems]]
- [[Pro_CompanyParameters]]
- [[Pro_Dashboard_Almalak]]
- [[Pro_DriverDetailsDashboard]]
- [[Pro_ItemsSalesStats]]
- [[Pro_ItemsSalesStatus]]
- [[Pro_MapTransactionLog]]
- [[Pro_MerchandiseDashboard]]
- [[Pro_OrdersDetails]]
- [[Pro_OrdersHeaders]]
- [[Pro_SalesOrdersQtyValidation]]
- [[Pro_SalesmanDetailsDashboard]]
- [[Pro_SalespersonsTargetDashboard]]
- [[RouteCoverageSummary_New_Excel]]
- [[Rpt_ActiveAndInactiveCustomers]]
- [[Rpt_ApprovedOrder]]
- [[Rpt_BackOrder]]
- [[Rpt_BackOrderItems]]
- [[Rpt_CompareCustomerStockWithOrder]]
- [[Rpt_ConcreteOperationManager]]
- [[Rpt_ConcreteVehicleTransactions]]
- [[Rpt_CustomerStockNotExistByDocType]]
- [[Rpt_CustomerStockNotExistByDocType_Summary]]
- [[Rpt_CustomersOrderbyItemReport]]
- [[Rpt_CustomersOrdersSummary]]
- [[Rpt_CustomersPromotionLog]]
- [[Rpt_CustomersVisitsCount]]
- [[Rpt_DUR]]
- [[Rpt_DailyConcrete]]
- [[Rpt_DailyConcreteSalesAndCollection]]
- [[Rpt_DeliveryBatchHeader]]
- [[Rpt_DeliveryBatchSummery]]
- [[Rpt_ExceededLimit]]
- [[Rpt_GA_SalesmanAnalysis]]
- [[Rpt_IncreaseCreditLimit]]
- [[Rpt_IncreaseCreditLimit_forALPHA]]
- [[Rpt_ItemsSalesPerCustomer]]
- [[Rpt_ItemsStockStatement]]
- [[Rpt_LoadOrderFirstApproval]]
- [[Rpt_MasterOrders]]
- [[Rpt_MonthlyCompareSalesTargetWithCustomer]]
- [[Rpt_MonthlyCompareSalesTargetWithSales]]
- [[Rpt_NetVisitsTime]]
- [[Rpt_OrderHeader]]
- [[Rpt_OrderLink]]
- [[Rpt_OrderMaster]]
- [[Rpt_OrdersAcceptenceStatus]]
- [[Rpt_OrdersDeliveryDrivers]]
- [[Rpt_OrdersModificationsLog]]
- [[Rpt_OrdersSalesReport]]
- [[Rpt_OrdersSalesReportByCategoty]]
- [[Rpt_PrintOrdersBatches]]
- [[Rpt_ReasonReprint]]
- [[Rpt_ReprintCount]]
- [[Rpt_RoutePerformanceAnalysis]]
- [[Rpt_RouteScoreBySalesman]]
- [[Rpt_RouteScoreBySalesman123]]
- [[Rpt_RouteScoreBySalesmanFromDateToDate]]
- [[Rpt_RouteSummaryBySalesman]]
- [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
- [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
- [[Rpt_RouteSummaryBySalesman_Merchandisers]]
- [[Rpt_RouteSummaryBySalesman_Sukhtian]]
- [[Rpt_RouteSummaryBySalesman_Suktian]]
- [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
- [[Rpt_RouteSummaryDeatils]]
- [[Rpt_RoutesAvg]]
- [[Rpt_RoutesByPeriod]]
- [[Rpt_SalesAndOrders]]
- [[Rpt_SalesManRouteSalesComparison]]
- [[Rpt_SalesOrderPerformance]]
- [[Rpt_SalesOrdersSummaryBySalesman]]
- [[Rpt_SalesPersonItemBonusTarget]]
- [[Rpt_Sales_Statistics]]
- [[Rpt_SalesmanAnalysisDashBoard]]
- [[Rpt_SalesmanCategorySales]]
- [[Rpt_SalesmanDailyActivities]]
- [[Rpt_SalesmanDaySummary]]
- [[Rpt_SalesmanGeneralDailyVisitsScore]]
- [[Rpt_SalesmanOrders]]
- [[Rpt_SalesmanOrdersSummary]]
- [[Rpt_SalesmanOrdersSummaryByCategory]]
- [[Rpt_SalesmanOrdersSummaryByTargetRef]]
- [[Rpt_SalesmanRouteAvg]]
- [[Rpt_SalesmanRouteEfficiency]]
- [[Rpt_SalesmanRouteEfficiency_SV_LV_TV2]]
- [[Rpt_SalesmanRouteSummary]]
- [[Rpt_SalesmanRouteTargetDetails]]
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
- [[Rpt_TransactionDateAndTime]]
- [[Rpt_TransactionsNotes]]
- [[Rpt_UnloadOrder]]
- [[Rpt_WFCustomersVisits]]
- [[Rpt_WF_GeneralSalesByItem]]
- [[Rpt_WF_SalesOrderStatus]]
- [[Rpt_WorkFlowAnalysis]]
- [[Rpt_WorkFlowFunctions]]
- [[SendEmailSalesOrder_Tower]]
- [[TECHNICAL_CHECKMISSINGSERIAL_OLIVES_BO_ORDER_RECEIPT_INV_RETINV]]
- [[WF_AddRequestToIncreaseCustomerCreditlimit]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]
- [[WF_GetCustAgingInfo]]
- [[WF_GetPositionWFData]]
- [[WF_GetPositionWFData_Alerts]]

**Writes (64):**
- [[OSFA_MobileDeliveryAPI]]
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[OT_ImportActionLog]]
- [[OT_ImportSalesIssueItems]]
- [[OT_ImportSalesOrders]]
- [[OT_SendSalesmanData]]
- [[Pro_OrdersHeaders]]
- [[SendEmailSalesOrder_Tower]]
- [[WF_AddRequestToIncreaseCustomerCreditlimit]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Olives_BO/Tables/ScheduleDeliveryOrders]]
