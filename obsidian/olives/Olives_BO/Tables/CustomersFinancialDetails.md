---
type: table
database: Olives_BO
name: CustomersFinancialDetails
schema: dbo
tags: [#backoffice, #customer]
foreign_keys:
  - [[BusinessUnits]]
  - [[Companies]]
  - [[CompanyBranches]]
  - [[Customers]]
  - [[CustomersClasses]]
  - [[CustomersPromotionsGroups]]
  - [[PaymentsTypes]]
  - [[Positions]]
  - [[PriceLists]]
  - [[RoutesInformation]]
referenced_by:
  - [[All_Visits]]
  - [[AppDashBoard]]
  - [[BO_Online_RptCustomerSalesTargetDetails]]
  - [[CustPricelistD_TMP]]
  - [[CustomersInvoicesPayOnlineReport]]
  - [[DA_SalesTarget]]
  - [[FixCustomerMFDuplicateError]]
  - [[FixCustomerMFDuplicateError3]]
  - [[FixDuplicate_All]]
  - [[GetSalesOrdersForApiReport_GCI]]
  - [[GetSalesOrdersForEdit]]
  - [[GetSalesOrdersForOnlineReport]]
  - [[GetSalesOrdersForOnlineReport_GCI]]
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[OT_FixDuplicateCustomers]]
  - [[OT_ImportNewCust]]
  - [[OT_ImportNewCust_145]]
  - [[OT_ImportReturnOrder]]
  - [[OT_SendCustomersInfo]]
  - [[OT_SendItemsInfo]]
  - [[OT_SendSalesmanData]]
  - [[OT_WF_SalesmanVisits]]
  - [[Online_RptSalesOrderStatusInERP]]
  - [[Pro_CustomerReceivablesInfo]]
  - [[Pro_Customers]]
  - [[Pro_CustomersFinancialDetails]]
  - [[Pro_CustomersGPS]]
  - [[Pro_CustomersItemsAssigment]]
  - [[Pro_CustomersPromotionsGroupsLink]]
  - [[Pro_CustomersTypes]]
  - [[Pro_Dashboard_Almalak]]
  - [[Pro_DriverDetailsDashboard]]
  - [[Pro_ImportData]]
  - [[Pro_ImportPriceListData]]
  - [[Pro_ImportRouteInfoFromExcel]]
  - [[Pro_ImportRouteInfoFromExcel2]]
  - [[Pro_Locations]]
  - [[Pro_LocationsAndSalespersonsLink]]
  - [[Pro_MapTransactionLog]]
  - [[Pro_MerchandiseDashboard]]
  - [[Pro_OrdersHeaders]]
  - [[Pro_PriceList_PromGroup_SalesLink]]
  - [[Pro_ReceiptRequests]]
  - [[Pro_RoutesInformation]]
  - [[Pro_SalesPersons]]
  - [[Pro_SalesmanClassTarget]]
  - [[Pro_SalesmanDetailsDashboard]]
  - [[RPT_Salesman_Routes_Customers_MonthlyCountandVisits]]
  - [[RPT_ZalloumReportONE]]
  - [[RPT_ZheimanRouteSummaryForExcel]]
  - [[RouteCoverageSummary_New_Excel]]
  - [[RptOnlineRpt_CustAging]]
  - [[RptOnlineRpt_ReturnDetails]]
  - [[Rpt_ActiveAndInactiveCustomers]]
  - [[Rpt_Balance_Credit_Cutomer_Deviation]]
  - [[Rpt_CheckCustomers]]
  - [[Rpt_ChequeInfrmation]]
  - [[Rpt_CollectedReceipts]]
  - [[Rpt_CollectedReceiptsByCompany]]
  - [[Rpt_Coverage]]
  - [[Rpt_CustGpsWithVisits]]
  - [[Rpt_CustomerAccountStatement_Sukhtian]]
  - [[Rpt_CustomerClassesByRoute]]
  - [[Rpt_CustomerInfoAndRouteDetails]]
  - [[Rpt_CustomerNameByLocation]]
  - [[Rpt_CustomerNotSold]]
  - [[Rpt_CustomerNotSoldBySalemanGroup]]
  - [[Rpt_CustomerSalesByUnit]]
  - [[Rpt_CustomersAvgPerClass]]
  - [[Rpt_CustomersExpansion]]
  - [[Rpt_CustomersPriceLists]]
  - [[Rpt_CustomersSalesByRoute]]
  - [[Rpt_CustomersUnAssignedWithRoutes]]
  - [[Rpt_CustomersVisitsCountByCategory]]
  - [[Rpt_CustomersVisitsCountByClass]]
  - [[Rpt_CustomersWithOutGPS]]
  - [[Rpt_DUR]]
  - [[Rpt_DaliyRouteForExcel]]
  - [[Rpt_GetAssignedRoutesDataforReport]]
  - [[Rpt_GetGapTrans]]
  - [[Rpt_ItemsCustomersNotSold]]
  - [[Rpt_ItemsCustomersNotSoldBySelection]]
  - [[Rpt_ItemsNotSold]]
  - [[Rpt_LastInvoiceByRoute]]
  - [[Rpt_LinkedCallCenter]]
  - [[Rpt_MerchSummary_Excel]]
  - [[Rpt_NewCustomers]]
  - [[Rpt_NewCustomersDetails]]
  - [[Rpt_NotSoldPerCateg]]
  - [[Rpt_NumericDistribution]]
  - [[Rpt_PerformanceMetric]]
  - [[Rpt_RoutePerformanceAnalysis]]
  - [[Rpt_RouteScoreBySalesman]]
  - [[Rpt_RouteScoreBySalesman123]]
  - [[Rpt_RouteScoreBySalesmanFromDateToDate]]
  - [[Rpt_RouteSummaryByDelivery]]
  - [[Rpt_RouteSummaryBySalesman]]
  - [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
  - [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
  - [[Rpt_RouteSummaryBySalesman_Delivery]]
  - [[Rpt_RouteSummaryBySalesman_Merchandisers]]
  - [[Rpt_RouteSummaryBySalesman_Sukhtian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
  - [[Rpt_RouteSummaryDeatils]]
  - [[Rpt_RoutesAvg]]
  - [[Rpt_RoutesByPeriod]]
  - [[Rpt_RoutesforExcel]]
  - [[Rpt_SalesAndOrders]]
  - [[Rpt_SalesAreaAndCategoryByCust]]
  - [[Rpt_SalesPerRoute]]
  - [[Rpt_SalesPerRouteWithSalesman]]
  - [[Rpt_SalesPersonAndCustomer]]
  - [[Rpt_SalesPersonSpecialTargets]]
  - [[Rpt_SalesTargetByCustCount_Telegraph]]
  - [[Rpt_SalesmanAnalysisDashBoard]]
  - [[Rpt_SalesmanCustRoutes]]
  - [[Rpt_SalesmanDailyActivities]]
  - [[Rpt_SalesmanDailyRoute]]
  - [[Rpt_SalesmanDaySummary]]
  - [[Rpt_SalesmanGeneralDailyVisitsScore]]
  - [[Rpt_SalesmanItemSalesPerRoute]]
  - [[Rpt_SalesmanRouteAssignment]]
  - [[Rpt_SalesmanRouteAvg]]
  - [[Rpt_SalesmanRouteDetails]]
  - [[Rpt_SalesmanRouteDetails_SendToBarcodePrinter]]
  - [[Rpt_SalesmanRouteEfficiency]]
  - [[Rpt_SalesmanRouteEfficiency_SV_LV_TV2]]
  - [[Rpt_SalesmanRouteSummary]]
  - [[Rpt_SalesmanRouteTargetDetails]]
  - [[Rpt_SalesmanSalesByItemClass_Online]]
  - [[Rpt_SalesmanSalesRecStatment]]
  - [[Rpt_SalesmanSalesTotal]]
  - [[Rpt_SalesmanSalesTotal_BO]]
  - [[Rpt_SalesmanSoldAndNoSoldCustomers]]
  - [[Rpt_SalesmanSoldAndNoSoldCustomers_BO]]
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
  - [[Rpt_SalesmanVisitAnalysis]]
  - [[Rpt_SalesmanVisitsRoute]]
  - [[Rpt_Salesman_Collections]]
  - [[Rpt_SalespersonsDailyVisits]]
  - [[Rpt_SoldUnsoldPerRoute]]
  - [[Rpt_StandView]]
  - [[Rpt_SurverySingleSelection]]
  - [[Rpt_SuspendedCustomers]]
  - [[Rpt_TargetSpartan]]
  - [[Rpt_TotalSalesmanRouteSummary]]
  - [[Rpt_TowerTargets]]
  - [[Rpt_TowerTargetsBO]]
  - [[Rpt_TowerTargets_Distribution]]
  - [[Rpt_TransactionRouteAnalysis]]
  - [[Rpt_UnloadCustomersPerRoute]]
  - [[Rpt_UnvisitedCustomerDetails]]
  - [[Rpt_UnvisitedCustomer_WF]]
  - [[Rpt_UnvisitedCustomersByDate]]
  - [[Rpt_UnvisitedRouteCustomers]]
  - [[Rpt_WF_FinancialAging]]
  - [[Rpt_WF_SalesmanVisits]]
  - [[Rpt_WF_UnvisitedCustomer]]
  - [[Rpt_WeeklySalesmanVisits]]
  - [[Rpt_customersbarcodes]]
  - [[SalesmanInfo]]
  - [[Technical_Atieh_copyCustomers]]
  - [[Technical_CopyfrompositiontoPostition]]
  - [[Technical_CreateRouteBasedonID]]
  - [[Technical_CreateRouteBasedonID_ForPageOnly]]
  - [[Technical_CreateRouteBasedonReference1]]
  - [[Technical_CreateRouteBasedonReference1_UpdateOnly]]
  - [[Technical_RestoreRoutefromlogaction]]
  - [[Technical_UpdateTempCFD_temp_forRouteCreation]]
  - [[Tower_Visits_Coverage_Percentage]]
  - [[WF_AddRequestToIncreaseCustomerCreditlimit]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
  - [[WF_FiltterCustomers]]
  - [[WF_IsHaveDueBalance]]
support_relevance: high
last_verified: 2026-10-03
related_workflows:
  - Customer-Setup
  - Daily-Sales-Cycle
  - Payments-and-Collections
  - PriceList-Management
  - Salesman-Onboarding
---
# CustomersFinancialDetails

## Business Purpose
The customer position, territory, and credit profile table — maps each customer to a sales position (`PositionsID`), assigned planned route (`RouteID`), stop sequence order (`VisitOrder`), price list (`PriceListID`), payment terms, and credit limits (`CreditLimit`, `CustomerBalance`, `ChqBalance`). One customer may have different records for different business units or sales positions. Queryable via `t.CustomersFinancialDetails`.

## Chatbot semantics
(Query `t.CustomersFinancialDetails` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| زبائن المندوب / المسار المخطط | `CustomerID`, `PositionsID`, `RouteID`, `VisitOrder` | Filter by `PositionsID` or `RouteID` | ORDER BY `VisitOrder` gives journey plan sequence |
| سقف الائتمان ورصيد العميل | `CreditLimit`, `CustomerBalance`, `ChqBalance` | Numeric fields | Financial exposure and current balance |
| قائمة أسعار العميل | `PriceListID` | Join `t.PriceLists` on `ID` | Price tier applied to customer |
| شروط الدفع وفترة السماح | `PaymentTypeID`, `DueDays`, `ChqsDueDays` | Link to `PaymentsTypes` | Days permitted before invoice is overdue |
| عميل موقوف عن البيع | `IsSuspended` | `IsSuspended = 1` | Blocks sales transactions |
| ترتيب الزيارة في المسار | `VisitOrder` | Ascending sort | Customer visit priority on the route |

**Do not confuse with:**
- `Customers`: General master data (Name, Phone, Address). `CustomersFinancialDetails` holds the position/financial parameters.
- `SalesPersonsRoutes`: The weekly day-to-route template. Join `SalesPersonsRoutes` with `CustomersFinancialDetails` on `RouteID` and `PositionsID` to see planned customers for a given day.
- `LogActionTransaction`: Actual visit logs. `CustomersFinancialDetails` defines the plan; `LogActionTransaction` proves the execution.

## Grain & keys
- **Composite PK**: (`CompanyID`, `CustomerID`, `PositionsID`, `BusinessUnitID`)
- **Tenant key**: `CompanyID`
- **FKs**: `CustomerID` → [[Customers]](ID), `PositionsID` → [[Positions]](ID), `RouteID` → [[RoutesInformation]](ID), `PriceListID` → [[PriceLists]](ID)

## Pipeline
Maintained in Back Office customer setup screens. Read by `OT_SendCustomersInfo` and `OT_SendSalesmanData` to configure mobile device database and validate credit / route constraints.

## Related
- [[Customers]]
- [[SalesPersonsRoutes]]
- [[RoutesInformation]]
- [[Positions]]
- [[PriceLists]]
- [[LogActionTransaction]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[RoutesInformation]] |
| CustomerID | bigint | NO | ✓ | ✓ | [[Customers]] |
| PositionsID | int | NO | ✓ | ✓ | [[Positions]] |
| BusinessUnitID | int | NO | ✓ | ✓ | [[BusinessUnits]] |
| PaymentTypeID | int | YES |  | ✓ | [[PaymentsTypes]] |
| PriceListID | int | YES |  | ✓ | [[PriceLists]] |
| RouteID | int | YES |  | ✓ | [[RoutesInformation]] |
| CustomersPromotionsGroupsID | int | YES |  | ✓ | [[CustomersPromotionsGroups]] |
| CreditLimit | float | YES |  |  |  |
| DueDays | smallint | YES |  |  |  |
| ChqsDueDays | smallint | YES |  |  |  |
| AllowChqs | bit | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| FavouriteVisitTime | smalldatetime | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| TaxInclude | bit | YES |  |  |  |
| DiscountPerc | float | YES |  |  |  |
| CreditCash | int | YES |  |  |  |
| CustomerBalance | float | YES |  |  |  |
| ChqBalance | float | YES |  |  |  |
| VisitOrder | int | YES |  |  |  |
| MaxInvoiceValue | float | YES |  |  |  |
| MaxInvoiceCount | int | YES |  |  |  |
| ChqLimit | float | YES |  |  |  |
| Tax_1_Include | bit | YES |  |  |  |
| Tax_2_Include | bit | YES |  |  |  |
| AllowManualDiscount | bit | YES |  |  |  |
| CompanyBrancheID | int | YES |  | ✓ | [[CompanyBranches]] |
| EarlyRepaymentDiscountPerc | float | YES |  |  |  |
| ClassID | int | YES |  | ✓ | [[CustomersClasses]] |
| DiscountEarlyPayDays | int | YES |  |  |  |
| LocationLineID | int | YES |  |  |  |
| DeliveryDays | int | YES |  |  |  |
| OrderCashDiscount | float | YES |  |  |  |
| CurrencyID | int | YES |  |  |  |
| ReturnCreditLimit | float | YES |  |  |  |
| ReturnBalance | float | YES |  |  |  |
| LocationID | int | YES |  |  |  |
| SalesOrderLimit | float | YES |  |  |  |
## Primary Key
CompanyID
CustomerID
PositionsID
BusinessUnitID
## Foreign Keys
CompanyID, BusinessUnitID -> [[BusinessUnits]](CompanyID, ID)
CompanyID -> [[Companies]](ID)
CompanyID, CompanyBrancheID -> [[CompanyBranches]](CompanyID, ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, ClassID -> [[CustomersClasses]](CompanyID, ID)
CompanyID, CustomersPromotionsGroupsID -> [[CustomersPromotionsGroups]](CompanyID, ID)
CompanyID, PaymentTypeID -> [[PaymentsTypes]](CompanyID, ID)
CompanyID, PositionsID -> [[Positions]](CompanyID, ID)
CompanyID, PriceListID -> [[PriceLists]](CompanyID, ID)
CompanyID, RouteID -> [[RoutesInformation]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (264):**
- [[All_Visits]]
- [[AppDashBoard]]
- [[BO_Online_RptCustomerSalesTargetDetails]]
- [[CustPricelistD_TMP]]
- [[CustomersInvoicesPayOnlineReport]]
- [[DA_SalesTarget]]
- [[FixCustomerMFDuplicateError]]
- [[FixCustomerMFDuplicateError3]]
- [[FixDuplicate_All]]
- [[GetSalesOrdersForApiReport_GCI]]
- [[GetSalesOrdersForEdit]]
- [[GetSalesOrdersForOnlineReport]]
- [[GetSalesOrdersForOnlineReport_GCI]]
- [[OT_FixDuplicateCustomers]]
- [[OT_ImportNewCust]]
- [[OT_ImportReturnOrder]]
- [[OT_SendCustomersInfo]]
- [[OT_SendItemsInfo]]
- [[OT_SendSalesmanData]]
- [[OT_WF_SalesmanVisits]]
- [[Online_RptSalesOrderStatusInERP]]
- [[Pro_CustomerReceivablesInfo]]
- [[Pro_Customers]]
- [[Pro_CustomersFinancialDetails]]
- [[Pro_CustomersGPS]]
- [[Pro_CustomersItemsAssigment]]
- [[Pro_CustomersPromotionsGroupsLink]]
- [[Pro_CustomersTypes]]
- [[Pro_Dashboard_Almalak]]
- [[Pro_DriverDetailsDashboard]]
- [[Pro_ImportData]]
- [[Pro_ImportPriceListData]]
- [[Pro_ImportRouteInfoFromExcel]]
- [[Pro_ImportRouteInfoFromExcel2]]
- [[Pro_Locations]]
- [[Pro_LocationsAndSalespersonsLink]]
- [[Pro_MapTransactionLog]]
- [[Pro_MerchandiseDashboard]]
- [[Pro_OrdersHeaders]]
- [[Pro_PriceList_PromGroup_SalesLink]]
- [[Pro_ReceiptRequests]]
- [[Pro_RoutesInformation]]
- [[Pro_SalesPersons]]
- [[Pro_SalesmanClassTarget]]
- [[Pro_SalesmanDetailsDashboard]]
- [[RPT_Salesman_Routes_Customers_MonthlyCountandVisits]]
- [[RPT_ZalloumReportONE]]
- [[RPT_ZheimanRouteSummaryForExcel]]
- [[RouteCoverageSummary_New_Excel]]
- [[RptOnlineRpt_CustAging]]
- [[RptOnlineRpt_ReturnDetails]]
- [[Rpt_ActiveAndInactiveCustomers]]
- [[Rpt_Balance_Credit_Cutomer_Deviation]]
- [[Rpt_CheckCustomers]]
- [[Rpt_ChequeInfrmation]]
- [[Rpt_CollectedReceipts]]
- [[Rpt_CollectedReceiptsByCompany]]
- [[Rpt_Coverage]]
- [[Rpt_CustGpsWithVisits]]
- [[Rpt_CustomerAccountStatement_Sukhtian]]
- [[Rpt_CustomerClassesByRoute]]
- [[Rpt_CustomerInfoAndRouteDetails]]
- [[Rpt_CustomerNameByLocation]]
- [[Rpt_CustomerNotSold]]
- [[Rpt_CustomerNotSoldBySalemanGroup]]
- [[Rpt_CustomerSalesByUnit]]
- [[Rpt_CustomersAvgPerClass]]
- [[Rpt_CustomersExpansion]]
- [[Rpt_CustomersPriceLists]]
- [[Rpt_CustomersSalesByRoute]]
- [[Rpt_CustomersUnAssignedWithRoutes]]
- [[Rpt_CustomersVisitsCountByCategory]]
- [[Rpt_CustomersVisitsCountByClass]]
- [[Rpt_CustomersWithOutGPS]]
- [[Rpt_DUR]]
- [[Rpt_DaliyRouteForExcel]]
- [[Rpt_GetAssignedRoutesDataforReport]]
- [[Rpt_GetGapTrans]]
- [[Rpt_ItemsCustomersNotSold]]
- [[Rpt_ItemsCustomersNotSoldBySelection]]
- [[Rpt_ItemsNotSold]]
- [[Rpt_LastInvoiceByRoute]]
- [[Rpt_LinkedCallCenter]]
- [[Rpt_MerchSummary_Excel]]
- [[Rpt_NewCustomers]]
- [[Rpt_NewCustomersDetails]]
- [[Rpt_NotSoldPerCateg]]
- [[Rpt_NumericDistribution]]
- [[Rpt_PerformanceMetric]]
- [[Rpt_RoutePerformanceAnalysis]]
- [[Rpt_RouteScoreBySalesman]]
- [[Rpt_RouteScoreBySalesman123]]
- [[Rpt_RouteScoreBySalesmanFromDateToDate]]
- [[Rpt_RouteSummaryByDelivery]]
- [[Rpt_RouteSummaryBySalesman]]
- [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
- [[Rpt_RouteSummaryBySalesmanByCustomerClass]]
- [[Rpt_RouteSummaryBySalesman_Delivery]]
- [[Rpt_RouteSummaryBySalesman_Merchandisers]]
- [[Rpt_RouteSummaryBySalesman_Sukhtian]]
- [[Rpt_RouteSummaryBySalesman_Suktian]]
- [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
- [[Rpt_RouteSummaryDeatils]]
- [[Rpt_RoutesAvg]]
- [[Rpt_RoutesByPeriod]]
- [[Rpt_RoutesforExcel]]
- [[Rpt_SalesAndOrders]]
- [[Rpt_SalesAreaAndCategoryByCust]]
- [[Rpt_SalesPerRoute]]
- [[Rpt_SalesPerRouteWithSalesman]]
- [[Rpt_SalesPersonAndCustomer]]
- [[Rpt_SalesPersonSpecialTargets]]
- [[Rpt_SalesTargetByCustCount_Telegraph]]
- [[Rpt_SalesmanAnalysisDashBoard]]
- [[Rpt_SalesmanCustRoutes]]
- [[Rpt_SalesmanDailyActivities]]
- [[Rpt_SalesmanDailyRoute]]
- [[Rpt_SalesmanDaySummary]]
- [[Rpt_SalesmanGeneralDailyVisitsScore]]
- [[Rpt_SalesmanItemSalesPerRoute]]
- [[Rpt_SalesmanRouteAssignment]]
- [[Rpt_SalesmanRouteAvg]]
- [[Rpt_SalesmanRouteDetails]]
- [[Rpt_SalesmanRouteDetails_SendToBarcodePrinter]]
- [[Rpt_SalesmanRouteEfficiency]]
- [[Rpt_SalesmanRouteEfficiency_SV_LV_TV2]]
- [[Rpt_SalesmanRouteSummary]]
- [[Rpt_SalesmanRouteTargetDetails]]
- [[Rpt_SalesmanSalesByItemClass_Online]]
- [[Rpt_SalesmanSalesRecStatment]]
- [[Rpt_SalesmanSalesTotal]]
- [[Rpt_SalesmanSalesTotal_BO]]
- [[Rpt_SalesmanSoldAndNoSoldCustomers]]
- [[Rpt_SalesmanSoldAndNoSoldCustomers_BO]]
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
- [[Rpt_SalesmanVisitAnalysis]]
- [[Rpt_SalesmanVisitsRoute]]
- [[Rpt_Salesman_Collections]]
- [[Rpt_SalespersonsDailyVisits]]
- [[Rpt_SoldUnsoldPerRoute]]
- [[Rpt_StandView]]
- [[Rpt_SurverySingleSelection]]
- [[Rpt_SuspendedCustomers]]
- [[Rpt_TargetSpartan]]
- [[Rpt_TotalSalesmanRouteSummary]]
- [[Rpt_TowerTargets]]
- [[Rpt_TowerTargetsBO]]
- [[Rpt_TowerTargets_Distribution]]
- [[Rpt_TransactionRouteAnalysis]]
- [[Rpt_UnloadCustomersPerRoute]]
- [[Rpt_UnvisitedCustomerDetails]]
- [[Rpt_UnvisitedCustomer_WF]]
- [[Rpt_UnvisitedCustomersByDate]]
- [[Rpt_UnvisitedRouteCustomers]]
- [[Rpt_WF_FinancialAging]]
- [[Rpt_WF_SalesmanVisits]]
- [[Rpt_WF_UnvisitedCustomer]]
- [[Rpt_WeeklySalesmanVisits]]
- [[Rpt_customersbarcodes]]
- [[SalesmanInfo]]
- [[Technical_Atieh_copyCustomers]]
- [[Technical_CopyfrompositiontoPostition]]
- [[Technical_CreateRouteBasedonID]]
- [[Technical_CreateRouteBasedonID_ForPageOnly]]
- [[Technical_CreateRouteBasedonReference1]]
- [[Technical_CreateRouteBasedonReference1_UpdateOnly]]
- [[Technical_RestoreRoutefromlogaction]]
- [[Technical_UpdateTempCFD_temp_forRouteCreation]]
- [[Tower_Visits_Coverage_Percentage]]
- [[WF_AddRequestToIncreaseCustomerCreditlimit]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]
- [[WF_FiltterCustomers]]
- [[WF_IsHaveDueBalance]]

**Writes (94):**
- [[FixCustomerMFDuplicateError]]
- [[FixCustomerMFDuplicateError3]]
- [[FixDuplicate_All]]
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[OT_FixDuplicateCustomers]]
- [[OT_ImportNewCust]]
- [[OT_ImportNewCust_145]]
- [[OT_SendCustomersInfo]]
- [[OT_SendSalesmanData]]
- [[Pro_CustomerReceivablesInfo]]
- [[Pro_CustomersFinancialDetails]]
- [[Pro_CustomersTypes]]
- [[Pro_ImportData]]
- [[Pro_ImportPriceListData]]
- [[Pro_ImportRouteInfoFromExcel2]]
- [[Pro_LocationsAndSalespersonsLink]]
- [[Pro_PriceList_PromGroup_SalesLink]]
- [[Technical_Atieh_copyCustomers]]
- [[Technical_CopyfrompositiontoPostition]]
- [[Technical_CreateRouteBasedonID]]
- [[Technical_CreateRouteBasedonID_ForPageOnly]]
- [[Technical_CreateRouteBasedonReference1]]
- [[Technical_CreateRouteBasedonReference1_UpdateOnly]]
- [[Technical_RestoreRoutefromlogaction]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Multi-row**: one customer can hold several term rows (per Position/BusinessUnit) — aggregate credit headroom as SUM(CreditLimit)-SUM(CustomerBalance) across positions
- **Stale snapshots**: CustomerBalance/ChqBalance/ReturnBalance here are cached; reconcile against CustomerStatmentOfAccount ledger when precision matters
- **Template bleed**: older copies of this block cited IsCollectedGPS — that column lives on Customers, not here
## Tenancy

Chatbot queries `t.CustomersFinancialDetails` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
