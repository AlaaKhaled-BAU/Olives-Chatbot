---
type: table
database: Olives_BO
name: Companies
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Currencies]]
referenced_by:
  - [[AX_INTEGRATION]]
  - [[AX_INTEGRATION_WITHLOG]]
  - [[AX_INTEG_SENDORDERS]]
  - [[AX_INTEG_SENDRECEIPTS]]
  - [[AX_INTEG_SENDSALESQUOTATIONS]]
  - [[AX_INTEG_SENDTRANSACTIONS]]
  - [[AX_INTEG_SENDTRANSFERS]]
  - [[AX_INTEG_SENDUNLOADTRANSFERS]]
  - [[AppDashBoard]]
  - [[Awtar_Integ_SendReceipts]]
  - [[CL_Integration]]
  - [[DR_DynamicReports_PRO]]
  - [[Ejabi_Integ_SendInvoices]]
  - [[Ejabi_Integ_SendPayments]]
  - [[Ejabi_Integ_SendReturnInvoices]]
  - [[Falcons_GetItemBalance]]
  - [[Falcons_Integ]]
  - [[NPF_Integration]]
  - [[Niroukh_Integ_SendReceipts]]
  - [[OT_ImportReturnOrder]]
  - [[OT_ImportSalesInvoices]]
  - [[OT_ImportSalesIssueItems]]
  - [[OT_ImportSalesOrders]]
  - [[OT_ImportSalesQuotations]]
  - [[OT_SendCompData]]
  - [[OT_SendCustomersInfo]]
  - [[OT_SendItemsInfo]]
  - [[PRO_GETRECEIPTSFOREMAIL]]
  - [[PRO_GETVOIDEDRECEIPTSFOREMAIL]]
  - [[Phenix_Sukhtian_Integ_SendReceipts]]
  - [[ProTech_Integration]]
  - [[ProTech_Integration_SendOrders]]
  - [[ProTech_Integration_SendPayment]]
  - [[ProTech_Integration_SendReturnInvoice]]
  - [[ProTech_Integration_SendSalesInvoice]]
  - [[Pro_Companies]]
  - [[Pro_CompanyParameters]]
  - [[Pro_DeliveryCarSummaryReport]]
  - [[Pro_DeliveryDashboard]]
  - [[Pro_JoTaxApi]]
  - [[Pro_JoTaxApiFromOSFA]]
  - [[Pro_JoTaxApiFromOSFA____]]
  - [[Pro_MMS_GetDataForAndroid]]
  - [[Pro_MerchandiseDashboard]]
  - [[Pro_ReceiptRequests]]
  - [[Pro_RoutesInformation]]
  - [[Pro_Users]]
  - [[QR_SCAN_OSFA_MOBILE]]
  - [[RPT_RoutesummarybysalesmancompineExcel2]]
  - [[Rpt_CashReceipts]]
  - [[Rpt_CollectedReceiptsByCompany]]
  - [[Rpt_DeliveryCarSummaryReport]]
  - [[Rpt_GpsLocationForTransaction]]
  - [[Rpt_LoadOrderFirstApproval]]
  - [[Rpt_PrintCustomersBarcode]]
  - [[Rpt_PrintInvoices]]
  - [[Rpt_ReceiptVouchers]]
  - [[Rpt_ReceivablesSalesInvoice]]
  - [[Rpt_ReportHeader]]
  - [[Rpt_RoutePerformanceAnalysis]]
  - [[Rpt_RouteSummaryBySalesmanCombine]]
  - [[Rpt_RouteSummaryBySalesmanCombine_New]]
  - [[Rpt_RouteSummaryBySalesmanCombine_Spartan]]
  - [[Rpt_RouteSummaryBySalesmanCombineforExcel]]
  - [[Rpt_RouteSummaryBySalesmanCombineforExcel_Bushnaq]]
  - [[Rpt_RouteVisitsByWeekDay]]
  - [[Rpt_RouteVisitsByWeekDayforExcel]]
  - [[Rpt_SalesQuotation]]
  - [[Rpt_SalesmanExpansionByItems]]
  - [[Rpt_SalesmanRouteDetails_SendToBarcodePrinter]]
  - [[Tax_Integration]]
  - [[X3_INTEGRATIONPROMOTION_WITHLOG]]
  - [[X3_INTEGRATION_WITHLOG]]
  - [[X3_Integ_DeliveryInvoice]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Company-Setup
---
# Companies


## Business Purpose

Multi-company/tenant configuration — name, address, tax info, and branding assets.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ID | smallint | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| Address | nvarchar | YES |  |  |  |
| TelephoneNo | nvarchar | YES |  |  |  |
| FaxNo | nvarchar | YES |  |  |  |
| POBox | nvarchar | YES |  |  |  |
| WebSite | nvarchar | YES |  |  |  |
| Email | nvarchar | YES |  |  |  |
| Logo | image | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| SalesTaxNum | nvarchar | YES |  |  |  |
| CurrencyID | smallint | YES |  | ✓ | [[Currencies]] |
| ServerDate | smalldatetime | YES |  |  |  |
| DataSize | int | YES |  |  |  |
| LogSize | int | YES |  |  |  |
| NullData | int | YES |  |  |  |
| Logo2 | image | YES |  |  |  |
| WaterMarkImage | image | YES |  |  |  |
| CID | int | YES |  |  |  |
| CompanyUID | varchar | YES |  |  |  |
| SalesTaxSerial | nvarchar | YES |  |  |  |
## Primary Key
ID
## Foreign Keys
CurrencyID -> [[Currencies]](ID)
## Impact / Procedures Using This Table

**Reads (74):**
- [[AX_INTEGRATION]]
- [[AX_INTEGRATION_WITHLOG]]
- [[AX_INTEG_SENDORDERS]]
- [[AX_INTEG_SENDRECEIPTS]]
- [[AX_INTEG_SENDSALESQUOTATIONS]]
- [[AX_INTEG_SENDTRANSACTIONS]]
- [[AX_INTEG_SENDTRANSFERS]]
- [[AX_INTEG_SENDUNLOADTRANSFERS]]
- [[AppDashBoard]]
- [[Awtar_Integ_SendReceipts]]
- [[CL_Integration]]
- [[DR_DynamicReports_PRO]]
- [[Ejabi_Integ_SendInvoices]]
- [[Ejabi_Integ_SendPayments]]
- [[Ejabi_Integ_SendReturnInvoices]]
- [[Falcons_GetItemBalance]]
- [[Falcons_Integ]]
- [[NPF_Integration]]
- [[Niroukh_Integ_SendReceipts]]
- [[OT_ImportReturnOrder]]
- [[OT_ImportSalesInvoices]]
- [[OT_ImportSalesIssueItems]]
- [[OT_ImportSalesOrders]]
- [[OT_ImportSalesQuotations]]
- [[OT_SendCompData]]
- [[OT_SendCustomersInfo]]
- [[OT_SendItemsInfo]]
- [[PRO_GETRECEIPTSFOREMAIL]]
- [[PRO_GETVOIDEDRECEIPTSFOREMAIL]]
- [[Phenix_Sukhtian_Integ_SendReceipts]]
- [[ProTech_Integration]]
- [[ProTech_Integration_SendOrders]]
- [[ProTech_Integration_SendPayment]]
- [[ProTech_Integration_SendReturnInvoice]]
- [[ProTech_Integration_SendSalesInvoice]]
- [[Pro_Companies]]
- [[Pro_CompanyParameters]]
- [[Pro_DeliveryCarSummaryReport]]
- [[Pro_DeliveryDashboard]]
- [[Pro_JoTaxApi]]
- [[Pro_JoTaxApiFromOSFA]]
- [[Pro_JoTaxApiFromOSFA____]]
- [[Pro_MMS_GetDataForAndroid]]
- [[Pro_MerchandiseDashboard]]
- [[Pro_ReceiptRequests]]
- [[Pro_RoutesInformation]]
- [[Pro_Users]]
- [[QR_SCAN_OSFA_MOBILE]]
- [[RPT_RoutesummarybysalesmancompineExcel2]]
- [[Rpt_CashReceipts]]
- [[Rpt_CollectedReceiptsByCompany]]
- [[Rpt_DeliveryCarSummaryReport]]
- [[Rpt_GpsLocationForTransaction]]
- [[Rpt_LoadOrderFirstApproval]]
- [[Rpt_PrintCustomersBarcode]]
- [[Rpt_PrintInvoices]]
- [[Rpt_ReceiptVouchers]]
- [[Rpt_ReceivablesSalesInvoice]]
- [[Rpt_ReportHeader]]
- [[Rpt_RoutePerformanceAnalysis]]
- [[Rpt_RouteSummaryBySalesmanCombine]]
- [[Rpt_RouteSummaryBySalesmanCombine_New]]
- [[Rpt_RouteSummaryBySalesmanCombine_Spartan]]
- [[Rpt_RouteSummaryBySalesmanCombineforExcel]]
- [[Rpt_RouteSummaryBySalesmanCombineforExcel_Bushnaq]]
- [[Rpt_RouteVisitsByWeekDay]]
- [[Rpt_RouteVisitsByWeekDayforExcel]]
- [[Rpt_SalesQuotation]]
- [[Rpt_SalesmanExpansionByItems]]
- [[Rpt_SalesmanRouteDetails_SendToBarcodePrinter]]
- [[Tax_Integration]]
- [[X3_INTEGRATIONPROMOTION_WITHLOG]]
- [[X3_INTEGRATION_WITHLOG]]
- [[X3_Integ_DeliveryInvoice]]

**Writes (2):**
- [[ProTech_Integration]]
- [[Pro_Companies]]

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
- [[Olives_BO/Tables/ItemsUnitsDetails_1]]
- [[Olives_BO/Tables/GroupsMenu]]
- [[Olives_BO/Tables/ItemsRelatedToItems]]
- [[Olives_BO/Tables/CustomerTypeTargetsDetails]]
- [[Olives_BO/Tables/ScheduleDeliveryOrders]]
- [[Olives_BO/Tables/UsersGroupsLink]]
- [[Shared/Runbooks/Orphan-Records]]
