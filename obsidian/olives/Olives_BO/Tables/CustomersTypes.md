---
type: table
database: Olives_BO
name: CustomersTypes
schema: dbo
tags: [#backoffice, #customer, #reference]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Customers_By_Type]]
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[OT_SendCompData]]
  - [[Pro_Customers]]
  - [[Pro_CustomersFinancialDetails]]
  - [[Pro_CustomersPromotionsGroupsLink]]
  - [[Pro_CustomersTypes]]
  - [[Pro_DriverDetailsDashboard]]
  - [[Pro_ImportData]]
  - [[Pro_MapTransactionLog]]
  - [[Pro_ProspectiveCustomers]]
  - [[Pro_SalesPersonBonusLimit]]
  - [[Pro_SalesmanDetailsDashboard]]
  - [[Pro_TransactionsHeaders]]
  - [[Pro_WFFunctionsAutoApprove]]
  - [[RPT_LOCATIONS_CUSTOMERTYPE_MAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
  - [[RPT_SUMMARYSALESAND]]
  - [[Rpt_CategoriesSalesPerCustomer]]
  - [[Rpt_CustomerInfoAndRouteDetails]]
  - [[Rpt_CustomerItemsSales]]
  - [[Rpt_CustomerItemsSalesBySelection]]
  - [[Rpt_CustomerItemsWeeklySales]]
  - [[Rpt_CustomerMonthlySalesByArea]]
  - [[Rpt_CustomerSalesSummary]]
  - [[Rpt_CustomerSalesSummary_BySelection]]
  - [[Rpt_CustomerTypeSalesByItems]]
  - [[Rpt_CustomersOrdersSummary]]
  - [[Rpt_CustomersSalesDetails]]
  - [[Rpt_CustomersVisitsCountByCategory]]
  - [[Rpt_InvoiceByDocTypes]]
  - [[Rpt_ItemsSalesPerCustomer]]
  - [[Rpt_LocationWithSalesmanSummary]]
  - [[Rpt_NewCustomer]]
  - [[Rpt_ProspectiveCustomer]]
  - [[Rpt_RouteSummaryByDelivery]]
  - [[Rpt_RouteSummaryBySalesman]]
  - [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
  - [[Rpt_RouteSummaryBySalesman_Delivery]]
  - [[Rpt_RouteSummaryBySalesman_Merchandisers]]
  - [[Rpt_RouteSummaryBySalesman_Sukhtian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
  - [[Rpt_SalesItemsByCustomersType]]
  - [[Rpt_SalesTransactionByDocumentsTypes]]
  - [[Rpt_SalesmanOrders]]
  - [[Rpt_SalesmanSalesDetails]]
  - [[Rpt_SalesmanTimeSpentPerCustomer2]]
  - [[Rpt_SalesmanTimeSpentPerCustomer3]]
  - [[Rpt_SalesmanTimeSpentPerCustomer4]]
  - [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
  - [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
  - [[Rpt_TotalInvoiceByDocTypes]]
  - [[Rpt_TransactionSales]]
  - [[WF_GetCustAgingInfo]]
  - [[WF_IsHaveDueBalance]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Customer-Setup
---
# CustomersTypes


## Business Purpose

Reference/lookup table defining customerstypes categories.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| SalesOrderLimit | float | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (120):**
- [[Customers_By_Type]]
- [[OT_SendCompData]]
- [[Pro_Customers]]
- [[Pro_CustomersFinancialDetails]]
- [[Pro_CustomersPromotionsGroupsLink]]
- [[Pro_CustomersTypes]]
- [[Pro_DriverDetailsDashboard]]
- [[Pro_ImportData]]
- [[Pro_MapTransactionLog]]
- [[Pro_ProspectiveCustomers]]
- [[Pro_SalesPersonBonusLimit]]
- [[Pro_SalesmanDetailsDashboard]]
- [[Pro_TransactionsHeaders]]
- [[Pro_WFFunctionsAutoApprove]]
- [[RPT_LOCATIONS_CUSTOMERTYPE_MAIN_SUBTARGETREPORT_COLLECTIONSPERSALESMAN]]
- [[RPT_SUMMARYSALESAND]]
- [[Rpt_CategoriesSalesPerCustomer]]
- [[Rpt_CustomerInfoAndRouteDetails]]
- [[Rpt_CustomerItemsSales]]
- [[Rpt_CustomerItemsSalesBySelection]]
- [[Rpt_CustomerItemsWeeklySales]]
- [[Rpt_CustomerMonthlySalesByArea]]
- [[Rpt_CustomerSalesSummary]]
- [[Rpt_CustomerSalesSummary_BySelection]]
- [[Rpt_CustomerTypeSalesByItems]]
- [[Rpt_CustomersOrdersSummary]]
- [[Rpt_CustomersSalesDetails]]
- [[Rpt_CustomersVisitsCountByCategory]]
- [[Rpt_InvoiceByDocTypes]]
- [[Rpt_ItemsSalesPerCustomer]]
- [[Rpt_LocationWithSalesmanSummary]]
- [[Rpt_NewCustomer]]
- [[Rpt_ProspectiveCustomer]]
- [[Rpt_RouteSummaryByDelivery]]
- [[Rpt_RouteSummaryBySalesman]]
- [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
- [[Rpt_RouteSummaryBySalesman_Delivery]]
- [[Rpt_RouteSummaryBySalesman_Merchandisers]]
- [[Rpt_RouteSummaryBySalesman_Sukhtian]]
- [[Rpt_RouteSummaryBySalesman_Suktian]]
- [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
- [[Rpt_SalesItemsByCustomersType]]
- [[Rpt_SalesTransactionByDocumentsTypes]]
- [[Rpt_SalesmanOrders]]
- [[Rpt_SalesmanSalesDetails]]
- [[Rpt_SalesmanTimeSpentPerCustomer2]]
- [[Rpt_SalesmanTimeSpentPerCustomer3]]
- [[Rpt_SalesmanTimeSpentPerCustomer4]]
- [[Rpt_SalesmanTimeSpentPerCustomer6_QimaH]]
- [[Rpt_SalesmanTimeSpentPerCustomerQima7]]
- [[Rpt_TotalInvoiceByDocTypes]]
- [[Rpt_TransactionSales]]
- [[WF_GetCustAgingInfo]]
- [[WF_IsHaveDueBalance]]

**Writes (56):**
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[Pro_CustomersTypes]]
- [[Pro_ImportData]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate customers**: Multiple records with same name/phone created during sync — support agent sees duplicate entries in dropdowns
- **Orphan references**: Customer records referenced by transactions that were soft-deleted — causes FK violation on cleanup
- **Balance mismatch**: CustomerBalance field diverges from actual calculated balance — run reconciliation proc
- **Suspend stuck**: IsSuspended flag not clearing after payment — check WF approval chain
- **GPS not collected**: IsCollectedGPS flag false — affects route optimization

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Olives_BO/Tables/CustomerTypeTargetsDetails]]
