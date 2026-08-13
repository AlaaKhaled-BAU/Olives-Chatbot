---
type: moc
database: OSFA_DB
name: _MOC-OSFA_DB
tags: [#moc, #mobile]
---

# OSFA_DB — Map of Content

## Key Tables
- [[OT_InvoiceHF]] — Invoice headers (mobile)
- [[OT_InvoiceDF]] — Invoice details (mobile)
- [[OT_OrderHF]] — Order headers (mobile)
- [[OT_OrderDF]] — Order details (mobile)
- [[OT_Payments]] — Payment records (mobile)
- [[OT_COMPANY]] — Company config (mobile)
- [[OT_CustomerMF]] — Customer master (mobile)
- [[OT_ItemsMF]] — Product catalog (mobile)
- [[OT_SalesmanMF]] — Salesperson master (mobile)
- [[OT_CompanyBranches]] — Mobile branch structure
- [[OT_Currency]] — Currency reference (mobile)

## Tables (193)
```dataview
TABLE
  rows.file.link AS Table,
  rows.support_relevance AS Relevance,
  rows.foreign_keys AS FK_Count,
  rows.procedures_reading AS Readers
FROM "OSFA_DB/Tables"
WHERE type = "table"
GROUP BY split(file.folder, "/")[-1]
FLATTEN length(rows) AS Count
SORT Count DESC
```

## Procedures (212)
```dataview
TABLE
  rows.file.link AS Procedure,
  rows.reads_from AS Reads,
  rows.writes_to AS Writes
FROM "OSFA_DB/Procedures"
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
FROM "OSFA_DB/Relations"
WHERE type = "relation"
```

### Relation List
- [[OT_InvoiceDF--OT_InvoiceHF]] — Invoice detail → header
- [[OT_InvoiceDF--OT_Items]] — Invoice detail → item
- [[OT_InvoiceHF--OT_Customers]] — Invoice → customer
- [[OT_LoadOrderHF--OT_SalesPersons]] — Load order → salesperson
- [[OT_OrderDF--OT_OrderHF]] — Order detail → header
- [[OT_OrderHF--OT_Customers]] — Order → customer
- [[OT_Payments--OT_Customers]] — Payment → customer
- [[OT_UnloadOrderHF--OT_SalesPersons]] — Unload order → salesperson
- [[OT_BankDepositDF--OT_BankDepositHF]] — Deposit detail → header

## Connectivity Stats
| Metric | Value |
|--------|-------|
| Tables | 193 |
| Procedures | 212 |
| Relations | 9 |

## Related

- [[OSFA_DB/Tables/OT_BonusItemRanges]]
- [[OSFA_DB/Tables/OT_GeoLevel5]]
- [[OSFA_DB/Tables/OT_BonusItemPriority]]
- [[OSFA_DB/Tables/CompetitiveItemsImage]]
- [[OSFA_DB/Tables/OT_PromotionsRangeInputOutput]]
- [[OSFA_DB/Tables/OT_SystemOptionsLists]]
- [[OSFA_DB/Tables/OT_GeoLevel3]]
- [[OSFA_DB/Tables/OT_CustomerImage]]
- [[OSFA_DB/Tables/OT_CustomersPromotionsExceptions]]
- [[OSFA_DB/Tables/OT_JsonLog_Tmp]]
- [[OSFA_DB/Tables/OT_SystemOptionsTypes]]
- [[OSFA_DB/Tables/Invt_ItemsImage]]
- [[OSFA_DB/Tables/OT_GeoLevel2]]
- [[OSFA_DB/Tables/OT_GeoLevel4]]
- [[OSFA_DB/Tables/OT_PromotionsGroupsCustomersLink]]
- [[OSFA_DB/Tables/OT_Actions]]
- [[OSFA_DB/Tables/OT_Payment_Invoices_Test]]
- [[OSFA_DB/Procedures/OT_Online_RptSalesmenVisitSummaryDetails]]
- [[OSFA_DB/Procedures/GapTransTimeLine_Insert]]
- [[OSFA_DB/Procedures/GapTransImages_Insert]]
- [[OSFA_DB/Procedures/OT_Online_RptSalesmenVisitSummary]]
- [[OSFA_DB/Procedures/OT_ItemsUnitsBarcodes_Insert]]
- [[OSFA_DB/Procedures/GetWF_AttachmentList]]
- [[OSFA_DB/Procedures/OT_Online_Rpt_SalesmenVisitsByRotue]]
- [[OSFA_DB/Procedures/OT_TransAttachment_Insert]]
- [[OSFA_DB/Procedures/OT_LockStock]]
- [[OSFA_DB/Procedures/GapTimeLineImage_Insert]]
- [[OSFA_DB/Procedures/SetRequestCanceled]]
- [[OSFA_DB/Procedures/WF_Attachment_Insert]]
- [[OSFA_DB/Procedures/CustomerSignatureWF_Insert]]
- [[OSFA_DB/Procedures/OT_Online_RptNotSoldCustomersByItemsAndSalesman]]
- [[OSFA_DB/Procedures/OT_DirectInvoice]]
- [[OSFA_DB/Procedures/OT_Online_RptSalesTargetDetails]]
- [[OSFA_DB/Procedures/OT_Hakkak_ShipmentOrders]]
- [[OSFA_DB/Procedures/OT_Online_RptCustomerSalesTargetDetails]]
- [[OSFA_DB/Procedures/InsertOT_ReturnOrderItemsImages]]
- [[OSFA_DB/Procedures/OT_UpdateSalesmanMsgs]]
- [[OSFA_DB/Procedures/UpdateCallsTransactions]]
- [[OSFA_DB/Procedures/OT_Online_RptNotSoldCustomersBySalesman]]
- [[OSFA_DB/Procedures/OT_Online_RptOverDueV]]