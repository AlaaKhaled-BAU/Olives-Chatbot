---
type: procedure
database: Olives_BO
name: OT_SendSalesmanData
schema: dbo
tags: [#backoffice, #mobile, #sales]
reads_from:
  - [[ClientsActive]]
  - [[CompanyBranches]]
  - [[CustomersFinancialDetails]]
  - DBO
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - [[OT_SendLog]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
  - [[SalesPersonsDevicePermissions]]
  - [[StoresBalances]]
writes_to:
  - [[CompanyParameters]]
  - [[CustomersFinancialDetails]]
  - CustTargetTot
  - HaveTrans
  - [[Items]]
  - [[OrdersHeaders]]
  - [[OT_Banks]]
  - [[OT_BanksAccounts]]
  - [[OT_BatchsInfo]]
  - [[OT_Branchs]]
  - [[OT_BusinessUnitDef]]
  - [[OT_COMPANY]]
  - [[OT_CompanyBranches]]
  - [[OT_CompetitiveItems]]
  - [[OT_ContractItems]]
  - [[OT_Contracts]]
  - [[OT_CouponsInfo]]
  - [[OT_CreditInvoiceList]]
  - [[OT_Currency]]
  - [[OT_CustIssueAmount]]
  - [[OT_CustomerChqList]]
  - [[OT_CustomerMF]]
  - [[OT_CustomerSalesByCategory]]
  - [[OT_CustomersClasses]]
  - [[OT_CustomersGPSLocations]]
  - [[OT_CustomersGroups]]
  - [[OT_CustomersItemQtyLimit]]
  - [[OT_CustomersItemsAssigment]]
  - [[OT_CustomersReturnItemQtyLimit]]
  - [[OT_CustStockHistory]]
  - [[OT_CustType]]
  - [[OT_DocTypes]]
  - [[OT_Drawers]]
  - [[OT_ErrorLog]]
  - [[OT_GeoLevel1]]
  - [[OT_ImageTypes]]
  - [[OT_InvoiceHistoryDF]]
  - [[OT_InvoiceHistoryHF]]
  - [[OT_InvoiceReturnLinkToTab]]
  - [[OT_ItemsCateg]]
  - [[OT_ItemsMF]]
  - [[OT_ItemsPriceExceptions]]
  - [[OT_ItemsPriority]]
  - [[OT_ItemsQtyAvg]]
  - [[OT_ItemsSalesUnits]]
  - [[OT_ItemsSubCateg]]
  - [[OT_ItemsUnitsBarcode]]
  - [[OT_ItemUnits]]
  - [[OT_LinkedSalesman]]
  - [[OT_OrderHistoryDF]]
  - [[OT_OrderHistoryHF]]
  - [[OT_PaymentsTypes]]
  - [[OT_PriceListsMF]]
  - [[OT_PromotionsCondUnCodOutput]]
  - [[OT_ProspectiveCustomer]]
  - [[OT_Reasons]]
  - [[OT_ReceiptRequests]]
  - [[OT_ReceiptRequestsInvoicesLink]]
  - [[OT_ReprintReasons]]
  - [[OT_ReturnChecks]]
  - [[OT_RouteMF]]
  - [[OT_SalesmanGroupItemQtyLimit]]
  - [[OT_SalesmanItemBonusTarget]]
  - [[OT_SalesmanItemBonusTargetByCustomer]]
  - [[OT_SalesmanMF]]
  - [[OT_SalesmanNotebookSerials]]
  - [[OT_SalesmanProcedures]]
  - [[OT_SalesmanRoute]]
  - [[OT_SalesmanTransactionsSerialsMulti]]
  - [[OT_SendLog]]
  - [[OT_StateAccBalance]]
  - [[OT_StoreItemsQty]]
  - [[OT_StoreItemsQty_Main]]
  - [[OT_Stores]]
  - [[OT_Surveys]]
  - [[OT_Surveys_Questions]]
  - [[OT_Surveys_Questions_Options]]
  - [[OT_SystemOptions]]
  - [[Receipts]]
  - Salesman
  - SalesmanBalance
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersonNotbookTransactionsSerials]]
  - [[SalesPersons]]
  - [[SalesPersonTransactionsSerials]]
  - [[SalesPersonTransactionsSerialsMulti]]
  - StartVisitTime
  - TakedSurveyIDs
  - [[TransactionsHeaders]]
  - [[TransfersOrdersHeaders]]
  - Van_StandardStock
  - VisitActivityInOrder
  - [[WF_PositionsVer]]
called_by:
  - 10
  - ABS_Integ_GetItemBalance_AbuOdeh
  - [[Alpha_GetItemBalance]]
  - [[Alpha_GetItemBalance_Zoumt]]
  - Boanza_Morek_GetitembalanceInsert
  - [[DEMOSALESPERSON2]]
  - [[Falcons_GetItemBalance]]
  - [[FixCustomerMFDuplicateError]]
  - [[FixCustomerMFDuplicateError3]]
  - [[FixDuplicate_All]]
  - [[GP_Integration_Wadi_Collect]]
  - [[GP_Integ_GetItemBalance]]
  - [[IscoJordan_Integ_GetItemsBalance]]
  - Mira_Integ_GetItemBalance
  - Mira_Integ_GetItemBalance2022
  - Mira_Integ_GetItemBalance_AlRajwa
  - [[Motakaml_Integ_GetItemBalance]]
  - [[OT_SendCustomersInfo]]
  - [[OT_SendItemsInfo]]
  - [[OT_Send_StatmentOfAccount_Client161]]
  - [[Phenix_Sukhtian_Integ_GetItemsBalance]]
  - [[PrestoSoft_Integ_GetItemBalance]]
  - [[SAP_GetItemBalance]]
  - SAP_GetItemBalance_Humoodoh
  - SAP_GetItemBalance_Malak
  - [[SN_Integ_GetItemBalance]]
  - [[Wings_Integ_GetItemBalance]]
  - Wings_Integ_Send_StatmentOfAccountBySalesman
  - [[X3_Integ_GetItemBalance]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Company-Setup
  - Customer-Setup
  - Daily-Sales-Cycle
  - Data-Sync-Cycle
  - Inventory-Management
  - Items-Master-Data-Setup
  - PriceList-Management
  - Promotion-Setup
  - Route-Planning
  - Salesman-Onboarding
---
# OT_SendSalesmanData


## Purpose

**BO → tablet master-data push** (`@CompNo`, `@SalesmanNo`, `@SendDate`). Run after salesman onboarding or when admin triggers «Send Data to Salesman». The tablet then pulls OSFA `OT_*` tables on «Update Data».

Opposite direction of [[OT_ImportActionLog]] (tablet actions → BO). This proc does **not** import visits; it **ships** catalog, permissions, and the **visit route plan** the tablet will follow.

### What gets pushed (business categories)

| Category | BO reads (main) | OSFA targets (main) |
|----------|-----------------|---------------------|
| Items / prices / van stock | `Items`, assignments, balances, price lists | `OT_ItemsMF`, `OT_ItemsCateg`, `OT_StoreItemsQty`, `OT_PriceListsMF`, … |
| Customers | `Customers`, `CustomersFinancialDetails`, GPS | `OT_CustomerMF`, `OT_CustomersGPSLocations`, … |
| **Route / visit plan** | `SalesPersonsRoutes`, `RoutesInformation`, `CustomersFinancialDetails` (`RouteID`, `VisitOrder`); optional `SalespersonRouteByDate` (some clients) | `OT_RouteMF` (names), **`OT_SalesmanRoute`** (daily customer list from `@SendDate` forward ~1 month) |
| Salesman profile | `SalesPersons`, device permissions, serials | `OT_SalesmanMF`, `OT_SystemOptions`, targets, surveys, … |
| Pending docs | `OrdersHeaders`, `Receipts`, `TransactionsHeaders`, … | staging tables for tablet pickup |

Delegates bulk work to **`OT_SendItemsInfo`** and **`OT_SendCustomersInfo`**.

### Visit plan mechanics (for chatbot notes)

1. Read weekly calendar: **`SalesPersonsRoutes`** (position × `WeekDay` × `Week1`–`Week4`).
2. Resolve week slot via BO logic (`Fun_GetWeekNo` in reports — not naive calendar week).
3. Expand each day from `@SendDate` forward; join **`CustomersFinancialDetails`** on matching `RouteID` + `PositionsID`; order by **`VisitOrder`**.
4. Delete + insert **`OSFA_DB.OT_SalesmanRoute`** per salesman (tablet working copy). Stamp `Visited` from same-day `OT_ActionLog` ActionID=`0` (UX only).
5. **`Tablet_GetSalesmanRoute`** reads BO `SalesPersonsRoutes` directly — BO is the definition source.

Chatbot: query BO calendar tables (`t.SalesPersonsRoutes` + `t.CustomersFinancialDetails` + `t.RoutesInformation`). Never query OSFA `OT_SalesmanRoute` at runtime.
## Parameters
- @CompNo int
- @SalesmanNo int
- @SendDate smalldatetime = null
## Tables Read
- [[ClientsActive]]
- [[CompanyBranches]]
- [[CustomersFinancialDetails]]
- DBO
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[OT_SendLog]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[SalesPersonsDevicePermissions]]
- [[StoresBalances]]
## Tables Written
- [[CompanyParameters]]
- [[CustomersFinancialDetails]]
- CustTargetTot
- HaveTrans
- [[Items]]
- [[OrdersHeaders]]
- [[OT_Banks]]
- [[OT_BanksAccounts]]
- [[OT_BatchsInfo]]
- [[OT_Branchs]]
- [[OT_BusinessUnitDef]]
- [[OT_COMPANY]]
- [[OT_CompanyBranches]]
- [[OT_CompetitiveItems]]
- [[OT_ContractItems]]
- [[OT_Contracts]]
- [[OT_CouponsInfo]]
- [[OT_CreditInvoiceList]]
- [[OT_Currency]]
- [[OT_CustIssueAmount]]
- [[OT_CustomerChqList]]
- [[OT_CustomerMF]]
- [[OT_CustomerSalesByCategory]]
- [[OT_CustomersClasses]]
- [[OT_CustomersGPSLocations]]
- [[OT_CustomersGroups]]
- [[OT_CustomersItemQtyLimit]]
- [[OT_CustomersItemsAssigment]]
- [[OT_CustomersReturnItemQtyLimit]]
- [[OT_CustStockHistory]]
- [[OT_CustType]]
- [[OT_DocTypes]]
- [[OT_Drawers]]
- [[OT_ErrorLog]]
- [[OT_GeoLevel1]]
- [[OT_ImageTypes]]
- [[OT_InvoiceHistoryDF]]
- [[OT_InvoiceHistoryHF]]
- [[OT_InvoiceReturnLinkToTab]]
- [[OT_ItemsCateg]]
- [[OT_ItemsMF]]
- [[OT_ItemsPriceExceptions]]
- [[OT_ItemsPriority]]
- [[OT_ItemsQtyAvg]]
- [[OT_ItemsSalesUnits]]
- [[OT_ItemsSubCateg]]
- [[OT_ItemsUnitsBarcode]]
- [[OT_ItemUnits]]
- [[OT_LinkedSalesman]]
- [[OT_OrderHistoryDF]]
- [[OT_OrderHistoryHF]]
- [[OT_PaymentsTypes]]
- [[OT_PriceListsMF]]
- [[OT_PromotionsCondUnCodOutput]]
- [[OT_ProspectiveCustomer]]
- [[OT_Reasons]]
- [[OT_ReceiptRequests]]
- [[OT_ReceiptRequestsInvoicesLink]]
- [[OT_ReprintReasons]]
- [[OT_ReturnChecks]]
- [[OT_RouteMF]]
- [[OT_SalesmanGroupItemQtyLimit]]
- [[OT_SalesmanItemBonusTarget]]
- [[OT_SalesmanItemBonusTargetByCustomer]]
- [[OT_SalesmanMF]]
- [[OT_SalesmanNotebookSerials]]
- [[OT_SalesmanProcedures]]
- [[OT_SalesmanRoute]]
- [[OT_SalesmanTransactionsSerialsMulti]]
- [[OT_SendLog]]
- [[OT_StateAccBalance]]
- [[OT_StoreItemsQty]]
- [[OT_StoreItemsQty_Main]]
- [[OT_Stores]]
- [[OT_Surveys]]
- [[OT_Surveys_Questions]]
- [[OT_Surveys_Questions_Options]]
- [[OT_SystemOptions]]
- [[Receipts]]
- Salesman
- SalesmanBalance
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalesPersonNotbookTransactionsSerials]]
- [[SalesPersons]]
- [[SalesPersonTransactionsSerials]]
- [[SalesPersonTransactionsSerialsMulti]]
- StartVisitTime
- TakedSurveyIDs
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]
- Van_StandardStock
- VisitActivityInOrder
- [[WF_PositionsVer]]
## Callers
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[Alpha_GetItemBalance]]
- [[Izhiman_SAP_Integ]]
- [[Khobara_Integ]]
- [[MeatLand_Integration]]
- [[MeatLand_Integrationnew]]
- [[Pro_SalesPersons]]
- [[Qerat_Integ]]
- [[Qetaf_Integ]]
- [[RamPharm_SAP_Integ]]
- [[Salbeshian_SAP_Integ]]
- [[SAMA_SAP_Integ]]
- [[Shini_Integ]]
- [[Yolande_Integ_GetItemBalance]]
- [[Zedan_SAP_Integ]]
## Callees
- 10
- ABS_Integ_GetItemBalance_AbuOdeh
- [[Alpha_GetItemBalance]]
- [[Alpha_GetItemBalance_Zoumt]]
- Boanza_Morek_GetitembalanceInsert
- [[DEMOSALESPERSON2]]
- [[Falcons_GetItemBalance]]
- [[FixCustomerMFDuplicateError]]
- [[FixCustomerMFDuplicateError3]]
- [[FixDuplicate_All]]
- [[GP_Integration_Wadi_Collect]]
- [[GP_Integ_GetItemBalance]]
- [[IscoJordan_Integ_GetItemsBalance]]
- Mira_Integ_GetItemBalance
- Mira_Integ_GetItemBalance2022
- Mira_Integ_GetItemBalance_AlRajwa
- [[Motakaml_Integ_GetItemBalance]]
- [[OT_SendCustomersInfo]]
- [[OT_SendItemsInfo]]
- [[OT_Send_StatmentOfAccount_Client161]]
- [[Phenix_Sukhtian_Integ_GetItemsBalance]]
- [[PrestoSoft_Integ_GetItemBalance]]
- [[SAP_GetItemBalance]]
- SAP_GetItemBalance_Humoodoh
- SAP_GetItemBalance_Malak
- [[SN_Integ_GetItemBalance]]
- [[Wings_Integ_GetItemBalance]]
- Wings_Integ_Send_StatmentOfAccountBySalesman
- [[X3_Integ_GetItemBalance]]
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CompanyBranches]]
- [[CustomersFinancialDetails]]
- DBO
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[OT_SendLog]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[SalesPersonsDevicePermissions]]
- [[StoresBalances]]

**Tables Written**
- [[CompanyParameters]]
- [[CustomersFinancialDetails]]
- CustTargetTot
- HaveTrans
- [[Items]]
- [[OrdersHeaders]]
- [[OT_Banks]]
- [[OT_BanksAccounts]]
- [[OT_BatchsInfo]]
- [[OT_Branchs]]
- [[OT_BusinessUnitDef]]
- [[OT_COMPANY]]
- [[OT_CompanyBranches]]
- [[OT_CompetitiveItems]]
- [[OT_ContractItems]]
- [[OT_Contracts]]
- [[OT_CouponsInfo]]
- [[OT_CreditInvoiceList]]
- [[OT_Currency]]
- [[OT_CustIssueAmount]]
- [[OT_CustomerChqList]]
- [[ot_customerMF]]
- [[OT_CustomerSalesByCategory]]
- [[OT_CustomersClasses]]
- [[OT_CustomersGPSLocations]]
- [[OT_CustomersGroups]]
- [[OT_CustomersItemQtyLimit]]
- [[OT_CustomersItemsAssigment]]
- [[OT_CustomersReturnItemQtyLimit]]
- [[OT_CustStockHistory]]
- [[OT_CustType]]
- [[OT_DocTypes]]
- [[OT_Drawers]]
- [[OT_ErrorLog]]
- [[OT_GeoLevel1]]
- [[OT_ImageTypes]]
- [[OT_InvoiceHistoryDF]]
- [[OT_InvoiceHistoryHF]]
- [[OT_InvoiceReturnLinkToTab]]
- [[OT_ItemsCateg]]
- [[OT_ItemsMF]]
- [[OT_ItemsPriceExceptions]]
- [[OT_ItemsPriority]]
- [[OT_ItemsQtyAvg]]
- [[OT_ItemsSalesUnits]]
- [[OT_ItemsSubCateg]]
- [[OT_ItemsUnitsBarcode]]
- [[OT_ItemUnits]]
- [[OT_LinkedSalesman]]
- [[OT_OrderHistoryDF]]
- [[OT_OrderHistoryHF]]
- [[OT_PaymentsTypes]]
- [[OT_PriceListsMF]]
- [[OT_PromotionsCondUnCodOutput]]
- [[OT_ProspectiveCustomer]]
- [[OT_Reasons]]
- [[OT_ReceiptRequests]]
- [[OT_ReceiptRequestsInvoicesLink]]
- [[OT_ReprintReasons]]
- [[OT_ReturnChecks]]
- [[OT_RouteMF]]
- [[OT_SalesmanGroupItemQtyLimit]]
- [[OT_SalesmanItemBonusTarget]]
- [[OT_SalesmanItemBonusTargetByCustomer]]
- [[OT_SalesmanMF]]
- [[OT_SalesmanNotebookSerials]]
- [[OT_SalesmanProcedures]]
- [[OT_SalesmanRoute]]
- [[OT_SalesmanTransactionsSerialsMulti]]
- [[OT_SendLog]]
- [[OT_StateAccBalance]]
- [[OT_StoreItemsQty]]
- [[OT_StoreItemsQty_main]]
- [[OT_Stores]]
- [[OT_Surveys]]
- [[OT_Surveys_Questions]]
- [[OT_Surveys_Questions_Options]]
- [[OT_SystemOptions]]
- [[Receipts]]
- Salesman
- SalesmanBalance
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalesPersonNotbookTransactionsSerials]]
- [[SalesPersons]]
- [[SalesPersonTransactionsSerials]]
- [[SalesPersonTransactionsSerialsMulti]]
- StartVisitTime
- TakedSurveyIDs
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]
- Van_StandardStock
- VisitActivityInOrder
- [[WF_PositionsVer]]

**Callers**
- 10
- ABS_Integ_GetItemBalance_AbuOdeh
- [[Alpha_GetItemBalance]]
- [[Alpha_GetItemBalance_Zoumt]]
- Boanza_Morek_GetitembalanceInsert
- [[DemoSalesperson2]]
- [[Falcons_GetItemBalance]]
- [[FixCustomerMFDuplicateError]]
- [[FixCustomerMFDuplicateError3]]
- [[FixDuplicate_All]]
- [[GP_Integration_Wadi_Collect]]
- [[GP_Integ_GetItemBalance]]
- [[IscoJordan_Integ_GetItemsBalance]]
- Mira_Integ_GetItemBalance
- Mira_Integ_GetItemBalance2022
- Mira_Integ_GetItemBalance_AlRajwa
- [[Motakaml_Integ_GetItemBalance]]
- [[OT_SendCustomersInfo]]
- [[OT_SendItemsInfo]]
- [[OT_Send_StatmentOfAccount_Client161]]
- [[Phenix_Sukhtian_Integ_GetItemsBalance]]
- [[PrestoSoft_Integ_GetItemBalance]]
- [[SAP_GetItemBalance]]
- SAP_GetItemBalance_Humoodoh
- SAP_GetItemBalance_Malak
- [[SN_Integ_GetItemBalance]]
- [[Wings_Integ_GetItemBalance]]
- Wings_Integ_Send_StatmentOfAccountBySalesman
- [[X3_Integ_GetItemBalance]]

**Callees**
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[Alpha_GetItemBalance]]
- [[Izhiman_SAP_Integ]]
- [[Khobara_Integ]]
- [[MeatLand_Integration]]
- [[MeatLand_Integrationnew]]
- [[Pro_SalesPersons]]
- [[Qerat_Integ]]
- [[Qetaf_Integ]]
- [[RamPharm_SAP_Integ]]
- [[Salbeshian_SAP_Integ]]
- [[SAMA_SAP_Integ]]
- [[Shini_Integ]]
- [[Yolande_Integ_GetItemBalance]]
- [[Zedan_SAP_Integ]]


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
