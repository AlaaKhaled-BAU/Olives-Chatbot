---
type: moc
database: Olives_BO
name: _MOC-Olives_BO
tags: [#moc, #backoffice]
---

# Olives_BO — Map of Content

## Key Tables
- [[SalesPersons]] — Central hub (1,693 links)
- [[Customers]] — Customer master (1,496 links)
- [[Items]] — Product catalog (907 links)
- [[TransactionsHeaders]] — Transaction hub (776 links)
- [[TransactionsDetails]] — Line items (579 links)
- [[CustomersFinancialDetails]] — Customer financials (553 links)
- [[ClientsActive]] — Active clients (507 links)
- [[OrdersHeaders]] — Sales orders (449 links)
- [[CompanyBranches]] — Branch structure
- [[Companies]] — Company/tenant

## Key Procedures
- [[Pro_CustomersFinancialDetails]] — Customer financial update
- [[Pro_SalesPersons]] — Salesperson management
- [[Pro_TransLock]] — Transaction locking
- [[Pro_BusinessUnits]] — Business unit operations

## Tables (440)
```dataview
TABLE
  rows.file.link AS Table,
  rows.support_relevance AS Relevance,
  rows.foreign_keys AS FK_Count,
  rows.procedures_reading AS Readers
FROM "Olives_BO/Tables"
WHERE type = "table"
GROUP BY split(file.folder, "/")[-1]
FLATTEN length(rows) AS Count
SORT Count DESC
```

## Procedures (1722)
```dataview
TABLE
  rows.file.link AS Procedure,
  rows.reads_from AS Reads,
  rows.writes_to AS Writes
FROM "Olives_BO/Procedures"
WHERE type = "procedure"
GROUP BY split(file.folder, "/")[-1]
FLATTEN length(rows) AS Count
SORT Count DESC
```

## Relations
```dataview
TABLE
  file.link AS Relation,
  file.tags AS Tags
FROM "Olives_BO/Relations"
WHERE type = "relation"
```

### Relation List
- [[Checks--Banks]] — Checks.BankID → Banks.ID
- [[Checks--Currencies]] — Checks → Currencies
- [[Checks--Customers]] — Checks → Customers
- [[Contracts--Customers]] — Contracts → Customers
- [[Customers--PriceLists]] — Customers → PriceLists
- [[Customers--SalesPersons]] — Customers → SalesPersons
- [[IntegrationPostedTransactions--TransactionsHeaders]] — Integration → Transactions
- [[Items--ItemsCategories]] — Items → ItemsCategories
- [[OrdersHeaders--Customers]] — Order → Customer
- [[OrdersHeaders--SalesPersons]] — Order → SalesPerson
- [[PriceListDetails--Items]] — PriceList → Item
- [[PriceListDetails--PriceLists]] — PriceList → PriceList
- [[Receipts--Currencies]] — Receipt → Currency
- [[Receipts--Customers]] — Receipt → Customer
- [[Receipts_PaidTrans--Receipts]] — Receipt → Receipt
- [[Receipts--SalesPersons]] — Receipt → SalesPerson
- [[RequestToExceedCustomerCreditLimit--Customers]] — CreditLimit → Customer
- [[TransactionsDetails--Items]] — TransactionDetail → Item
- [[TransactionsDetails--TransactionsHeaders]] — Detail → Header
- [[TransactionsHeaders--Customers]] — Transaction → Customer
- [[BankDepositDF--BankDepositHF]] — Deposit detail → header
- [[BankDepositDF--Companies]] — Deposit detail → company
- [[BankDepositHF--Banks]] — Deposit header → bank
- [[BankDepositHF--Branches]] — Deposit header → branch
- [[BankDepositHF--Companies]] — Deposit header → company
- [[BankDepositHF--SalesPersons]] — Deposit header → salesperson
- [[ItemsGroups--Companies]] — Item group → company
- [[Items--ItemsGroups]] — Item → item group
- [[Items--OT_ItemsMF]] — BO item → tablet item (cross-DB)
- [[Widget_User_LogAction--Widget_User_LogAction]] — Log action → log action (self-FK)

## Connectivity Stats
| Metric | Value |
|--------|-------|
| Tables | 440 |
| Procedures | 1722 |
| Relations | 30 |

## Related

- [[Olives_BO/Tables/Tech_CustomizationPerformedTasks]]
- [[Olives_BO/Tables/ItemsUnitsDetails_1]]
- [[Olives_BO/Tables/GroupsMenu]]
- [[Olives_BO/Tables/CustomersFinancialDetails2]]
- [[Olives_BO/Tables/forupdateonly]]
- [[Olives_BO/Tables/MultiTargets]]
- [[Olives_BO/Tables/MMS_ShowRooms]]
- [[Olives_BO/Tables/Clients]]
- [[Olives_BO/Tables/Pos_InvoiceOrderHF]]
- [[Olives_BO/Tables/CustomerSalesByCategory]]
- [[Olives_BO/Tables/CustomersReturnItemQtyLimit]]
- [[Olives_BO/Tables/ItemsSuggestGroupLinkWithItems]]
- [[Olives_BO/Tables/ItemsRelatedToItems]]
- [[Olives_BO/Tables/SalesPersonItemsBalanceBatches]]
- [[Olives_BO/Tables/SpecialCustomerTarget]]
- [[Olives_BO/Tables/CustomerTypeTargetsDetails]]
- [[Olives_BO/Tables/Customers2]]
- [[Olives_BO/Tables/EmpDetails]]
- [[Olives_BO/Tables/ClientsWFID]]
- [[Olives_BO/Tables/ItemsInventory]]
- [[Olives_BO/Tables/MMS_DV_ErrorLog]]
- [[Olives_BO/Tables/WieghtTargets]]
- [[Olives_BO/Tables/CustomersFinancialDetails_Old]]
- [[Olives_BO/Tables/PriceListQtyRanges]]
- [[Olives_BO/Tables/ScheduleDeliveryOrders]]
- [[Olives_BO/Tables/LogActions]]
- [[Olives_BO/Tables/PromotionTypes]]
- [[Olives_BO/Tables/UsersGroupsLink]]
- [[Olives_BO/Procedures/GetCustomerAssets]]
- [[Olives_BO/Procedures/Pro_PrintCheque]]
- [[Olives_BO/Procedures/sp_helpdiagramdefinition]]
- [[Olives_BO/Procedures/Rpt_VoidOrder]]
- [[Olives_BO/Procedures/OT_ImportReturnOrderMerch]]
- [[Olives_BO/Procedures/SP_UPGRADDIAGRAMS]]
- [[Olives_BO/Procedures/Pro_MonthlySalesPersonsTargets]]
- [[Olives_BO/Procedures/sp_alterdiagram]]
- [[Olives_BO/Procedures/DashBoard_ExceptionsIssues]]
- [[Olives_BO/Procedures/OWMS]]
- [[Olives_BO/Procedures/RunSQLWebAPI_Integ]]
- [[Olives_BO/Procedures/EncodeArabicToUTF8DataFromOSFA_API]]
- [[Olives_BO/Procedures/SMSSEND_ZUMOT]]
- [[Olives_BO/Procedures/Test_Banks]]
- [[Olives_BO/Procedures/sp_renamediagram]]
- [[Olives_BO/Procedures/Alpha_GetCurrRate]]
- [[Olives_BO/Procedures/Niroukh_VS_MonthlyandQuarter]]
- [[Olives_BO/Procedures/sp_helpdiagrams]]
- [[Olives_BO/Procedures/Niroukh_AllCustomersTargets]]
- [[Olives_BO/Procedures/CopySystemOption]]
- [[Olives_BO/Procedures/Awtar_Integ_GetDataFromAPI]]
- [[Olives_BO/Procedures/PRO_REPORT]]
- [[Olives_BO/Procedures/Rpt_Get_SalesAnalysisPerSalesEmp_Tablet]]
- [[Olives_BO/Procedures/sp_creatediagram]]
- [[Olives_BO/Procedures/GetRouteAndCategoryOnline]]
- [[Olives_BO/Procedures/FIXCORRUPTEDIMAGEGALARY_OSFA]]
- [[Olives_BO/Procedures/CopySystemOption_Delete_Insert_fromsalesmantosalesman]]
- [[Olives_BO/Procedures/sp_dropdiagram]]
- [[Olives_BO/Procedures/Online_RptSalesmanCustomerCategAreaSales_Zumot]]
- [[Olives_BO/Procedures/Technical_Activate_DeactivateLoginbybarcode_Atieh]]
- [[Olives_BO/Procedures/Rpt_Hakkak_TargetReportFromAlpha]]