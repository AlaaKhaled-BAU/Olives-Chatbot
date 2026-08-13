---
type: table
database: Olives_BO
name: ReturnOrdersHeaders
schema: dbo
tags: [#backoffice, #order]
foreign_keys:
  - [[Companies]]
  - [[Currencies]]
  - [[Customers]]
  - [[PriceLists]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
referenced_by:
  - [[Alpha_Integ_SendReturnOrder]]
  - [[Awtar_Integ_SendReturnOrder]]
  - [[Bajali_SAP_Integ]]
  - [[ConvertReturnOrderToInvoiceDelivery]]
  - [[DEMOSALESPERSON]]
  - [[DEMOSALESPERSON2]]
  - [[ECO_Land_SAP_Integ]]
  - [[GArrow_SAP_Integ]]
  - [[Niroukh_Integ_SendReturnOrder]]
  - [[OT_ImportActionLog]]
  - [[OT_ImportReturnOrder]]
  - [[PrestoSoft_Integ_SendReturnOrders]]
  - [[Pro_CompanyParameters]]
  - [[Pro_ReturnOrdersHeaders]]
  - [[Rpt_CustomerReturnOrdersDetails]]
  - [[Rpt_ReturnOrder]]
  - [[Rpt_ReturnOrdersMaster]]
  - [[Rpt_RouteSummaryBySalesman]]
  - [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
  - [[Rpt_RouteSummaryBySalesman_Sukhtian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian]]
  - [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
  - [[Rpt_TransactionDateAndTime]]
  - [[Rpt_TransactionsNotes]]
  - [[SAP_Integ_SendReturnOrder_Karadsheh]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Return-Reversal-Workflow
---
# ReturnOrdersHeaders


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores returnordersheaders records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalesPersons]] |
| TransactionYear | smallint | NO | ✓ |  |  |
| TransactionNo | int | NO | ✓ |  |  |
| TransactionDate | smalldatetime | YES |  |  |  |
| SalesPersonID | int | YES |  | ✓ | [[SalesPersons]] |
| CustomerID | bigint | YES |  | ✓ | [[Customers]] |
| PriceListID | int | YES |  | ✓ | [[PriceLists]] |
| CreditCash | int | YES |  |  |  |
| DiscountAmount | float | YES |  |  |  |
| DiscountPercent | float | YES |  |  |  |
| ForeignDiscountAmount | float | YES |  |  |  |
| ForeignDiscountPercent | float | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| CurrencyID | smallint | YES |  | ✓ | [[Currencies]] |
| ExchangeRate | float | YES |  |  |  |
| IsPrinted | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| RouteID | int | YES |  | ✓ | [[RoutesInformation]] |
| PostedToERP | bit | YES |  |  |  |
| IsVoid | bit | YES |  |  |  |
| CustomerName | varchar | YES |  |  |  |
| WFApproved | bit | YES |  |  |  |
| Approve | bit | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
| CustomerDiscountPerc | float | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| IsWFApproved | bit | YES |  |  |  |
| WFApproveDesc | nvarchar | YES |  |  |  |
| ForeignCustomerDiscountPerc | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| ServerDate | smalldatetime | YES |  |  |  |
| Manual_Disc | float | YES |  |  |  |
| LocationLineID | int | YES |  |  |  |
| FinalApproval | bit | YES |  |  |  |
| DocumentTypeID | int | YES |  |  |  |
| ExtraNotes | varchar | YES |  |  |  |
| Reason | nvarchar | YES |  |  |  |
| PostedToERPDateTime | smalldatetime | YES |  |  |  |
| AcceptDate | smalldatetime | YES |  |  |  |
## Primary Key
CompanyID
TransactionYear
TransactionNo
## Foreign Keys
CompanyID -> [[Companies]](ID)
CurrencyID -> [[Currencies]](ID)
CompanyID, CustomerID -> [[Customers]](CompanyID, ID)
CompanyID, PriceListID -> [[PriceLists]](CompanyID, ID)
CompanyID, RouteID -> [[RoutesInformation]](CompanyID, ID)
CompanyID, SalesPersonID -> [[SalesPersons]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (20):**
- [[Alpha_Integ_SendReturnOrder]]
- [[Awtar_Integ_SendReturnOrder]]
- [[ConvertReturnOrderToInvoiceDelivery]]
- [[DEMOSALESPERSON]]
- [[DEMOSALESPERSON2]]
- [[Niroukh_Integ_SendReturnOrder]]
- [[OT_ImportReturnOrder]]
- [[PrestoSoft_Integ_SendReturnOrders]]
- [[Pro_CompanyParameters]]
- [[Rpt_CustomerReturnOrdersDetails]]
- [[Rpt_ReturnOrder]]
- [[Rpt_ReturnOrdersMaster]]
- [[Rpt_RouteSummaryBySalesman]]
- [[Rpt_RouteSummaryBySalesmanBushnaqExcel]]
- [[Rpt_RouteSummaryBySalesman_Sukhtian]]
- [[Rpt_RouteSummaryBySalesman_Suktian]]
- [[Rpt_RouteSummaryBySalesman_Suktian_Draft]]
- [[Rpt_TransactionDateAndTime]]
- [[Rpt_TransactionsNotes]]
- [[SAP_Integ_SendReturnOrder_Karadsheh]]

**Writes (13):**
- [[Alpha_Integ_SendReturnOrder]]
- [[Awtar_Integ_SendReturnOrder]]
- [[Bajali_SAP_Integ]]
- [[ECO_Land_SAP_Integ]]
- [[GArrow_SAP_Integ]]
- [[Niroukh_Integ_SendReturnOrder]]
- [[OT_ImportActionLog]]
- [[OT_ImportReturnOrder]]
- [[PrestoSoft_Integ_SendReturnOrders]]
- [[Pro_ReturnOrdersHeaders]]
- [[SAP_Integ_SendReturnOrder_Karadsheh]]
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
