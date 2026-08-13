---
type: shared
name: Olives_BO-Vault-Doc-Audit
tags: [#reference, #shared, #audit]
---

# Olives_BO — Vault Documentation Audit

> Generated: 2026-08-05
> Source: DB object lists from `olives_PEEK` (restore of the "105" backup set, SQL Server 2022).
> Vault scope: `Olives_BO/Tables/*.md` and `Olives_BO/Procedures/*.md`.
> Method: case-insensitive name comparison, existence only. No content review.

## Summary

| Objects | DB count | Vault count | Missing in vault | Vault-only |
|---------|----------|-------------|------------------|------------|
| Tables  | 440      | 410         | 30               | 0          |
| Procs   | 1664     | 1503        | 219              | 58         |

> **Status: RESOLVED 2026-08-05** — all 30 missing tables and 219 missing procs have been documented (see [Documentation Generated](#documentation-generated-2026-08-05)). Vault now has 440 tables / 1722 procs.

Vault-only tables: 0. All vault tables exist in the DB.

---

## Tables missing in vault (30)

- BankDepositDF
- BankDepositHF
- CustomersBalanceAging_Inmaa
- DiscountEarlyPayByInvoiceRef
- EfawateercomPayment
- ItemCommissions
- ItemsCategStockDetails
- ItemsCategStockHeader
- ItemsGroups
- ItemsMinimumSales
- ItemsStoreByUser
- JSONDataLog
- MaintinanceOrdersApprove
- MedicalRepCoaching
- MobileVersionSalesmen
- OrdersDetails_Log
- PriceListDetailsFromGCI
- PromotionBudget
- PromptEmbeddings
- RequestToCancelPayment
- SalesPersonCustomerCountTargetsDF
- SalesPersonCustomerCountTargetsHF
- SalesmanVisitsSummary
- SalespersonCustomersVisitsByDate
- SalespersonsPromotionsExceptions
- TechnicalFinancialInsertTable_Temp
- WFMobilePermissionDefinition
- WFMobilePermissionLink
- Widget_Functions
- Widget_User_LogAction

Themes:
- **Payments/EFT**: `BankDepositDF/HF`, `RequestToCancelPayment`, `EfawateercomPayment`
- **Inventory/stock**: `ItemsCategStockDetails/Header`, `ItemsGroups`, `ItemsMinimumSales`, `ItemsStoreByUser`, `ItemCommissions`
- **Targets/promotions**: `PromotionBudget`, `SalesPersonCustomerCountTargetsDF/HF`, `SalespersonsPromotionsExceptions`, `DiscountEarlyPayByInvoiceRef`
- **AI/log** (new): `PromptEmbeddings`, `Widget_Functions`, `Widget_User_LogAction`, `JSONDataLog`, `OrdersDetails_Log`
- **Mobile app**: `WFMobilePermissionDefinition/Link`, `MobileVersionSalesmen`, `MedicalRepCoaching`, `SalesmanVisitsSummary`
- **Temp/other**: `TechnicalFinancialInsertTable_Temp`, `PriceListDetailsFromGCI`, `CustomersBalanceAging_Inmaa`, `MaintinanceOrdersApprove`

---

## Procs missing in vault (219)

High noise. Mostly branded/duplicate copies not documented, and report procs.

### Integration clones (Injaz/Wafi/branded) (~30)
ABS_Integ_GetAllStoresBalances_Injaz · ABS_Integ_GetDataFromAPI_Injaz · ABS_Integ_PostDataToAPI_Injaz · ABS_Integ_SendInvoicesPayment_Injaz · ABS_Integ_SendInvoices_Injaz · ABS_Integ_SendNewCustomer_Injaz · ABS_Integ_SendPaymentCashInvoice_Injaz · ABS_Integ_SendPayment_Injaz · ABS_Integ_SendPayment_Injaz_Draft · ABS_Integ_SendRetInvoices_Injaz · ABS_Integ_SendSalesOrder_Injaz · ABS_Integ_SendTransferOrders_Injaz · ABS_Integration_Injaz · Alpha_Integ_BatchesQty · Commate_Integ_CreateToken · Commate_Integ_PostToAPI · GTS_Integ_CreateToken · Hesabate_Integ_CreateToken · Hesabate_Integ_PostToAPI · Sajaya_Integ_CreateToken · SandIntegration · SoftInteg_SendNewCustomers · SoftInteg_SendNewCustomers_Cash · Soft_Integ_CreateSalesmanStockTaking · Soft_Integ_SendLoadOrder · Soft_Integ_SendReturnSalesInvoices · Soft_Integ_SendSalesInvoices · Soft_Integ_SendSalesOrder · Soft_Integration_Comp1 · SMS_Retaj · Thuraya_SendIncomingPayment_API · Bisan_Integration · OK_ImportInvoiceAndReturnISDT_Integ

### Pro_* feature procs (~35)
Pro_AI · Pro_BankDeposit · Pro_CheckPromotionBudgetValue · Pro_ComboData · Pro_ComboData_Sujab · Pro_ComparisonReport · Pro_ComparisonReportMain · Pro_ConvertQrCodeToImages · Pro_CustomerImages · Pro_DiscountEarlyPayByInvoiceRef · Pro_EfawateercomApi · Pro_GetCustomerStockHistory · Pro_GetCustomersForAllSalesMan · Pro_GetDataList · Pro_GetNetSalesForAPI · Pro_ImportData_Order · Pro_ImportExcelDataRoutes_59 · Pro_ImportPromotionBudgetData · Pro_ImportUnConditionalPromotionData · Pro_ItemsCategStock · Pro_ItemsMinimumSales · Pro_ItemsOrderList · Pro_ItemsStoreByUser · Pro_JoTaxApiFromOSFA_BeforeYAN · Pro_JsonDataLog · Pro_MedicalRepCoaching · Pro_NewCustTransAttachment · Pro_OlivesReportingAPI · Pro_PageToMenu · Pro_PriceListCustomerAssignment · Pro_PromotionBudget · Pro_ReceiptsDetalisBySalesman · Pro_SalesPersonCustomerCountTargets · Pro_SalesmanReceiptsForAlthuraya · Pro_SoftReportOnline · Pro_TransfersOrdersHeaders_Nighthammoudeh · Pro_UpdatePromotionBudgetFromSAP · Pro_WFMobilePermission · Pro_WFReportForMobile · Pro_ZatcaIntegrationApi_____

### Rpt_* reports (~90)
RPT_CoverageandFrequencybysalesman · RPT_CoverageandFrequencybysalesmanByCompany · RPT_CoverageandFrequencybysalesman_BO · RPT_UnVisitedDoctor · RPT_coverageandfrequency · RptOnlineRpt_DeliveryDetailsForWF · RptOnlineRpt_ReturnDetailsForWF · Rpt_AlthurayaTeamACT · Rpt_AvailableStockByCategory · Rpt_BasketQuantity · Rpt_CarExpiredQuantity · Rpt_CompetitveItemsData · Rpt_CoverageAndfrequany · Rpt_CustomerAddressInfoForExcel · Rpt_CustomerBalanceNaqi · Rpt_CustomerRouteVistsList · Rpt_CustomerRouteVistsList_temp · Rpt_CustomerSalesTargetReport · Rpt_CustomerStockTackingDetails · Rpt_CustomerVisitCount · Rpt_DamagedMaterialsHeader · Rpt_DeliveryDetailsForWF · Rpt_DetailedTotalSalesReportBySalesRepresentative · Rpt_GetSalesmanCustomerVisitsCount · Rpt_InvoiceReturnLink · Rpt_ItemBasket · Rpt_ItemSalesCommissionsBySalesman · Rpt_ItemsImageReport · Rpt_ItemsSalesStatus · Rpt_ListInvoices · Rpt_NetsalesAndLoadOrderAndRateByDate · Rpt_NetsalesAndLoadOrderAndRate_Excel · Rpt_NetsalesAndLoadOrderAndRate_Waffir · Rpt_NetsalesAndRateByDate · Rpt_NotSoldCustomerbyClass · Rpt_OrderDetailsSujab · Rpt_OrdersPosted · Rpt_QrVisitsVerification · Rpt_RejectedTrans · Rpt_RouteActualGPSVisitsExcel · Rpt_RouteActualGPSVisitsExcelCompine · Rpt_RouteSummaryByBranch · Rpt_RouteSummaryByBranchCombine · Rpt_RouteSummaryBySalesmanCombine_SukhtianForPWPI_22_BO · Rpt_RouteSummaryBySalesmanCombine_Wafi · Rpt_RouteSummaryBySalesmanCombine_draft · Rpt_RouteSummaryBySalesmanGetImagesVisit · Rpt_RouteSummaryBySalesman_Suktian_Draft22_BO · Rpt_RouteSummaryBySalesman_Wafi · Rpt_RouteUnvisitedGPSCustomers · Rpt_RouteUnvisitedGPSCustomers_ForExcel · Rpt_Route_Visit_Sales_Targets_Report_Lobik · Rpt_SalesAndReturnByBranch · Rpt_SalesByCustomersClass · Rpt_SalesByCustomersCompare · Rpt_SalesByCustomersDiscount · Rpt_SalesManDailyReport · Rpt_SalesOrdersApprovalEnmaa · Rpt_SalesPerBarndOnline · Rpt_SalesPersonStatement_ReportSubJoad · Rpt_Sales_Sv · Rpt_SalesmanCashSales_TahounehCenters · Rpt_SalesmanCreditSales_Military_Institutes · Rpt_SalesmanDetailsDashboardCombine · Rpt_SalesmanSalesRecStatment_TahounehCenters · Rpt_SalesmanTimeSpentPerCustomer3PerCustomer · Rpt_SalesmanVisitsStutas · Rpt_SalespersonsLocationDashboard · Rpt_SummaryRouteVisitOnline · Rpt_SummarySalesAnd CollectionByCustomerTypes · Rpt_SurveyCustomers · Rpt_Surveys_ToExcel · Rpt_TansactionDetails · Rpt_TeamOrderReport · Rpt_TotalsalesSummaryWithTax · Rpt_TransactionsVisitsBySalesPersonID · Rpt_VisitCount · Rpt_VisitsByCustomers · Rpt_WareHouse_Item_Balance_Defaf3_6_2026 · Rpt_WeeklySalesmanVisitsEnmaa · Rpt_WorkingHours · RreportsOnlineForAlthuray · ExcRpt_vw_SalesNetAmount

### OT_* / Technical* / maintenance (~30)
OT_ImportBankDeposit · OT_ImportConsignmentByAllSalesman · OT_ImportInvoiceHistoryFromBonanza · OT_ImportRequestToCancelPayment · OT_ImportUnloadOrderForSalesmanStock_Hammoudeh · OT_ItemsCategStocDF_CheckExist · OT_ItemsCategStockDF_Insert · OT_ItemsCategStockHF_CheckExist · OT_ItemsCategStockHF_Insert · OT_SendSalesmanData_Test · OT_TransfersOrdersData · TechnicalInsertItemsassignment_invoicehistory · TechnicalFillCustomerfinancialdetailsfromcustomers · TechnicalFillUnfilledSalespersonsRoutes · Technical_CheckRouteCount · Technical_CopyRoutesCustomersFromPositiontoposition · Technical_CopyRoutesCustomersFromPositiontoposition_Comp · Technical_CreateCustomersTransferQuery · Technical_CreateRouteBasedonID&ManualrouteName · Technical_CreateRouteBasedonReference1&ManualrouteName · Technical_FillItemsimagesinolivesimages · Technical_InspectTooshortScheduleJobs · Technical_InssertintFinancialfromFirstFinancialLink

### Other
AlthurayRreportsOnline · AppUsers_SyncFromSalesPersons · Create_Directory · FixDuplicate_All2 · GetItems_Salah · GetReturnOrderData · GetWF_TransferOrderData · Hammoudeh_Integ_CreateSalesmanStockTaking · ImportAddPromotionstData · Integ_Insert_Salesorder_New · ItemAuditing_Hamouda · ItemsOrderList_Details_Report · ItemsOrderList_Header_Report · Items_UpdateImageTools · LastVisitandInvAmount · Merchindizre_Daily_Report · Olives_DataRetrieve · OrderList_Details_Report · POADetailsOnlineReport · PRO_Clients · PRO_PostProductionLoadingOrderApproval · PRO_PreProductionLoadingOrderApproval · PerformanceRreportsForAlthuray · Pro_NewCustTransAttachment · Pro_WFReportForMobile · RptOnlineRpt_DeliveryDetailsForWF · SRV_SalespersonRouteByDate · Sap_SalespersonStock_Sama · Tablet_InvoiceHistoryByDate · TechincalInsertRepeatedItemsPromotions · TransactionsBounsBatch · UnsoldCustomersFromDatetoDate_IZ · UnvisitedCustomersFromDatetoDate_IZ · Update_NiroukhNames_For_Lasttargetreport · WF_CancelRequest · WF_OrdersDetails · Write_Files · ZMT_Greading_Tablet_ALL · getallcustomer_Salah · rpt_OlivesApp_Export · rpt_OlivesApp_Export_All · rpt_OlivesApp_Export_ByUser · rpt_althurayaRefrshabel_Excel

---

## Procs in vault but not in DB (58)

Likely renamed/removed in the current DB, docs-only, or planned:

Pro_ApproveNewCustomers · Pro_ApproveSalespersonsImages · Pro_ApproveVoidPayments · Pro_AssignCustomersForSalesman · Pro_AssignItemForReturn · Pro_AssignItemsForStores · Pro_AssignPlanogramForCustomers · Pro_BackOrder · Pro_ChangeCheckStatus · Pro_CollectGPS · Pro_CopyTarget · Pro_CustomerLocationApproval · Pro_CustomersRoutesAssignment · Pro_DashboardProductPerformance · Pro_DashboardSalesAnalysis · Pro_DashboardSalesGrowth · Pro_DashboardSalesmanDashboard · Pro_DashboardSalesmanKPI · Pro_DashboardTargetDashboard · Pro_ImportOrdersIssues · Pro_ItemsImageReport · Pro_ItemsSalesStats · Pro_ItemsSalesStatus · Pro_MoveSalespersonCustomersPerRoutes · Pro_PasswordGenerator · Pro_PaymentAmountDetails · Pro_PaymentsApproval · Pro_PriceListPromotionGroupLink · Pro_Promotions · Pro_PromotionsWFApprove · Pro_ReceiptRequest · Pro_ReceiptRequestSchedule · Pro_ReturnOrderFinalApproval · Pro_ReturnOrdersApproval · Pro_ReturnSalesApproval · Pro_ReturnSalesFinalApproval · Pro_ReturnSalesVoid · Pro_Routes · Pro_SalesInvoiceApproval · Pro_SalesInvoiceVoid · Pro_SalesOrderFinalApproval · Pro_SalesOrdersApproval · Pro_SalesmanAutoUnload · Pro_SalespersonStockTakingApproval · Pro_SalespersonsItemsAssignment · Pro_SendBackOrder · Pro_ShowMultiRouteInMap · Pro_ShowRouteInMap · Pro_SortItems · Pro_TransferCustomersByRoute · Pro_TransferOrdersApproval · Pro_TransferToERP · Pro_UserActivityLog · Pro_WFCustomersAutoApprove · Pro_WFFunctionsReport · Pro_WFSetup · RPT_SUMMARYSALESAND · Rpt_SalesmanTimeSpentPerCustomer3Combine

---

## Notes
- Many "missing" procs are near-duplicates/date-tagged variants (`_Comp`, `_draft`, `Defaf3_6_2026`, `_Salah`) — likely not worth documenting individually.
- `PromptEmbeddings` table suggests an AI/RAG feature with no vault coverage.
- Full machine-readable lists for Olives_BO are in the DB object dumps used to generate this file.
---

## Documentation Generated (2026-08-05)

All objects listed above as missing from the vault have now been documented with full metadata extracted from the DB:

### Created
- **30 table notes** in `Olives_BO/Tables/` — each with columns (type/nullable/PK), primary key, foreign keys (inbound + outbound), procedures that read/write it, estimated row count
- **219 procedure notes** in `Olives_BO/Procedures/` — each with parameters, tables read/written, callers/callees, when-to-run guidance
- **10 relation notes** in `Olives_BO/Relations/` — FK pairs, incl. cross-DB `Items--OT_ItemsMF`

### Linking conventions
- Table notes link to every referencing procedure via `[[ProcName]]`
- Procedure notes link to every referenced table via `[[TableName]]`
- Cross-DB references (BO proc → OSFA table, qualified `OSFA_DB.dbo.*`) link as `[[OSFA_DB/Tables/OT_X|OT_X]]`
- Procedure frontmatter carries `reads_from`, `writes_to`, `called_by` — consumable by Dataview
- Table frontmatter carries `foreign_keys`, `procedures_reading` — consumable by Dataview
- MOC updated: Tables (440), Procedures (1722), Relations (30)

### Generation source
- Metadata extracted live from `olives_PEEK` (snapshot of the 105 backup set): `sys.columns`, `sys.foreign_keys`, `sys.sql_modules`, `sys.sql_expression_dependencies`, `sys.parameters`
- Table↔proc references: token-matched against each procedure body (read vs write classified by INSERT/UPDATE/DELETE/MERGE context), including cross-DB qualified names
- ALL notes are AUTO-GENERATED — verify before trusting
