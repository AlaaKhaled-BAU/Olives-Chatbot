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
last_verified: 2026-09-26
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

## Column semantics — DataSize / LogSize / NullData / ServerDate (verified 2026-09-26 vs live DB)

> Verified against live `Olives_BO` via `sp_helptext` + `sys.columns`. Vault previously had no per-column definition.

- `NullData int NULL, no default, not computed` — **salesman-license enforcement flag**. `0` = no enforcement, `1` = enforce salesman-count quotas. Current state: all rows `0` (feature OFF).
- `DataSize int NULL` + `LogSize int NULL` — quota inputs, maintained alongside `NullData`. Current state: all rows `0`.
- `ServerDate smalldatetime NULL` — last-touch timestamp written together with the three columns.
- Writer: `[[Pro_Companies]]` branch `@cmdType='Update Log File'` — `UPDATE Companies SET DataSize=@DataSize, LogSize=@LogSize, NullData=@NullData, ServerDate=GETDATE()` (no `WHERE`, touches every row). `INSERT`/`Update` branches do NOT touch these columns; `SELECT` branches return them.
- Reader: `dbo.GetSalesman()` TVF (no vault note — functions are referenced as plain text, e.g. in `[[OT_ImportSalesOrders]]`). Logic: `SELECT TOP 1 @NullData = ISNULL(NullData,0) FROM Companies`; if `0` returns empty (no blocking). If `1`: quota `(@DataSize+45)/700` / `(@LogSize+45)/700`, counts distinct active salesmen in last 24h (FOC from `OrdersHeaders`+`TransactionsHeaders`+`Receipts`, WFC from `WF_SubLog` where `ActionNeed='AR'`), returns `TOP(actual-quota)` most-recently-active salesmen as overflow list.
- Effect: `OT_Import*` procs (`[[OT_ImportSalesOrders]]`, `[[OT_ImportSalesInvoices]]`, `[[OT_ImportSalesIssueItems]]`, `[[OT_ImportSalesQuotations]]`, `[[OT_ImportReturnOrder]]`) filter `SalesmanNo NOT IN (SELECT SalesMan FROM dbo.GetSalesman() WHERE Company=@CompNo AND TType='FOC')` — over-quota salesmen's tablet data stays in `OSFA_DB`, never posts to `Olives_BO`.
- Quirks: `[[Pro_Companies]]` param is `@NullData bit` while column is `int`; `GetSalesman` uses `TOP 1` with no `WHERE`, so in a multi-company table the flag/quota comes from an arbitrary row.
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
