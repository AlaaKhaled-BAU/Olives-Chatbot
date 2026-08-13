---
type: shared
name: Exceptions
tags: [#reference, #shared]
---

# Exceptions

## Legitimate Standalone Objects
These objects have minimal links by design (lookup tables, log tables, temp tables):

- ActivityList
- ClassTargetRate
- CurrenciesDenominations
- CustomerData_Sample
- ExcelReports
- Language
- LanguageDictionary
- MIMETypes
- Menu
- ProcedureChangeLog
- Table_1

## Notes with Insufficient Connectivity
These notes have only a parent MOC link and need manual review or cross-referencing
from SQL body analysis:

- ABS_Integ_GetDataFromAPI
- ABS_Integ_PostDataToAPI
- Acback_Integ_PostData
- Acback_Integ_PostTransactionsData
- Alpha_GetCurrRate
- Alpha_Integ_GetCurrRate
- Alpha_SendData
- Awtar_Integ_GetDataFromAPI
- Clients
- ClientsWFID
- CompanyParameters
- CompetitiveItemsImage
- CustomerSalesByCategory
- Customers2
- CustomersFinancialDetails2
- CustomersFinancialDetails_Old
- CustomersReturnItemQtyLimit
- DashBoard_ExceptionsIssues
- Ejabi_Integ_GetDataFromAPI
- Ejabi_Integ_PostDataToAPI
- EmpDetails
- EncodeArabicToUTF8DataFromOSFA_API
- Falcons_UpdateItemBalance
- GTS_Integ_GetDataFromAPI
- GapTags
- GapTransTags
- GetCustomerAssets
- Invt_ItemsImage
- ItemsBarcodes
- ItemsInventory
- ItemsSuggestGroupLinkWithItems
- LogActionTransaction_
- LogActions
- MMS_DV_ErrorLog
- MMS_ShowRooms
- MultiTargets
- Niroukh_Integ_GetDataFromAPI
- OT_Actions
- OT_BonusItemPriority
- OT_BonusItemRanges
- OT_CouponsInfo
- OT_CreditInvoiceList
- OT_Currency
- OT_CustIssueAmount
- OT_CustStockHistory
- OT_CustomerChqList
- OT_CustomerImage
- OT_CustomerSalesByCategory
- OT_CustomersClasses
- OT_CustomersGroups
- OT_CustomersItemQtyLimit
- OT_CustomersItemsAssigment
- OT_CustomersPromotionsExceptions
- OT_CustomersReturnItemQtyLimit
- OT_DirectInvoice
- OT_ErrorLogInteg
- OT_GeoLevel1
- OT_GeoLevel2
- OT_GeoLevel3
- OT_GeoLevel4
- OT_GeoLevel5
- OT_ImportSalesIssueItems
- OT_InvoiceReturnLinkToTab
- OT_ItemsPriceExceptions
- OT_ItemsPriority
- OT_ItemsQtyAvg
- OT_ItemsSalesUnits
- OT_ItemsSubCateg
- OT_ItemsUnitsBarcode
- OT_JsonLog
- OT_JsonLog_Tmp
- OT_LinkedSalesman
- OT_OrderHistoryDF
- OT_OrderHistoryHF
- OT_Payment_Invoices_Test
- OT_PaymentsTypes
- OT_PriceList
- OT_PriceListsMF
- OT_PromotionsCondUnCodInput
- OT_PromotionsCondUnCodOutput
- OT_PromotionsCustomersGroupsLink
- OT_PromotionsGroupsCustomersLink
- OT_PromotionsHeaders
- OT_PromotionsRangeInputOutput
- OT_PromotionsSalesmanGroupsLink
- OT_ProspectiveCustomer
- OT_Reasons
- OT_ReceiptRequests
- OT_ReceiptRequestsInvoicesLink
- OT_ReprintReasons
- OT_ReturnChecks
- OT_RouteMF
- OT_SalesmanGroupItemQtyLimit
- OT_SalesmanItemBonusTarget
- OT_SalesmanItemBonusTargetByCustomer
- OT_SalesmanNotebookSerials
- OT_SalesmanProcedures
- OT_SalesmanRoute
- OT_SalesmanTransactionsSerialsMulti
- OT_StoreItemsQty_Main
- OT_Stores
- OT_Surveys
- OT_Surveys_Questions
- OT_Surveys_Questions_Options
- OT_SystemOptionsLists
- OT_SystemOptionsTypes
- PRO_REPORT
- PendingInvoices
- Pos_InvoiceOrderHF
- PriceListQtyRanges
- Pro_MonthlySalesPersonsTargets
- Pro_PrintCheque
- PromotionTypes
- Receipts_Branches
- Rpt_Hakkak_TargetReportFromAlpha
- Rpt_VoidOrder
- RunSQLWebAPI_Integ
- SMSSEND_ZUMOT
- SMS_Niroukh
- SalesPersonItemsBalanceBatches
- Shamel_Integ_GetDataFromAPI
- SpecialCustomerTarget
- Tech_CustomizationPerformedTasks
- Test_Banks
- TransactionsBatchsItemsInvoiceLink
- TransactionsSuggestedItems
- TransfersOrdersDetails_ErrorQty
- WieghtTargets
- ZatcaCustomer
- ZatcaMode
- ZatcaResultGenerateXml
- ZatcaSalesPersons
- forupdateonly


---


# Conflict & Duplicate Relationship Scan

> Generated: 2026-07-05

## Summary
- **Conflicts found**: 18
- **Cross-database name duplicates**: 5

## Issues
  Self-reference: Olives_BO/Tables/Locations -> [[Locations]]
  Self-reference: Olives_BO/Tables/Locations -> [[Locations]]
  Self-reference: Olives_BO/Tables/Locations -> [[Locations]]
  Self-reference: Olives_BO/Tables/IntenalMemoApprove -> [[IntenalMemoApprove]]
  Self-reference: Olives_BO/Tables/IntenalMemoApprove -> [[IntenalMemoApprove]]
  Self-reference: Olives_BO/Tables/IntenalMemoApprove -> [[IntenalMemoApprove]]
  Self-reference: Olives_BO/Tables/Currencies -> [[Currencies]]
  Self-reference: Olives_BO/Tables/Currencies -> [[Currencies]]
  Self-reference: Olives_BO/Tables/Currencies -> [[Currencies]]
  Self-reference: Olives_BO/Tables/Customers -> [[Customers]]
  Self-reference: Olives_BO/Tables/Customers -> [[Customers]]
  Self-reference: Olives_BO/Tables/Customers -> [[Customers]]
  Self-reference: Olives_BO/Tables/SalesPersons -> [[SalesPersons]]
  Self-reference: Olives_BO/Tables/SalesPersons -> [[SalesPersons]]
  Self-reference: Olives_BO/Tables/SalesPersons -> [[SalesPersons]]
  Self-reference: Olives_BO/Procedures/Galaxy_Integration -> [[Galaxy_Integration]]
  Self-reference: Olives_BO/Procedures/Galaxy_Integration -> [[Galaxy_Integration]]
  Self-reference: Olives_BO/Procedures/Galaxy_Integration -> [[Galaxy_Integration]]
  Same procedure name in both databases: OT_GETORDERINVOICELINKHISTORY, OT_ONLINECURRENT_SALESMANBALANCE, PRO_NEWCUSTIMAGES, PRO_OT_LAYOUT_SETTING, RPT_ALLRETURNCHECKS

## Notes
- Self-references indicate notes linking to themselves (non-critical)
- Cross-database duplicate names are acceptable if the objects serve different purposes
