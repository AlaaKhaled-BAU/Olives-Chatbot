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
  - [[ConvertReturnOrderToInvoiceDelivery]]
  - [[DEMOSALESPERSON]]
  - [[DEMOSALESPERSON2]]
  - [[OT_ImportActionLog]]
  - [[OT_ImportReturnOrder]]
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
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-10-03
related_workflows:
  - Return-Reversal-Workflow
---
# ReturnOrdersHeaders

## Business Purpose
The return orders header table — stores customer return requests/orders created on mobile devices before warehouse receipt or approval. Corresponds to workflow `FunctionID = 22` ("Request To Approve Return Order"). Captures composite PK (`TransactionYear`, `TransactionNo`), customer (`CustomerID`), salesman (`SalesPersonID`), date (`OrderDate`), totals, and void flags (`IsVoid`). Queryable via `t.ReturnOrdersHeaders`.

## Chatbot semantics
(Query `t.ReturnOrdersHeaders` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| طلبيات الإرجاع / المرتجع | `CustomerID`, `SalesPersonID`, `OrderDate` | Direct filters | Return order requests |
| طلبيات غير ملغاة | `IsVoid` | `IsVoid = 0 OR IsVoid IS NULL` | Active return orders |
| إجمالي قيمة طلب الإرجاع | `NetTotal` | Numeric | Net value of return order |
| تفاصيل المواد المرتجعة | Join `t.ReturnOrdersDetails` | Join on (`TransactionYear`, `TransactionNo`) | Items, quantities, reasons |
| ربط بطلب الموافقة على المرتجع | Join `t.WF_MasterLog` | `m.FunctionID = 22 AND TRY_CAST(m.Ref1 AS int) = r.TransactionYear AND TRY_CAST(m.Ref2 AS numeric) = r.TransactionNo` | Approval state of return order |

**Do not confuse with:**
- `TransactionsHeaders` (with `TransactionTypeID = 2`): Completed return *invoices* that credit the customer's ledger immediately. Return orders require approval before conversion to return invoices.

## Grain & keys
- **Composite PK**: (`CompanyID`, `TransactionYear`, `TransactionNo`)
- **Tenant key**: `CompanyID`
- **FKs**: `CustomerID` → [[Customers]](ID), `SalesPersonID` → [[SalesPersons]](ID), `RouteID` → [[RoutesInformation]](ID)

## Pipeline (how rows get here)
Created on mobile devices when returning goods → imported via `OT_ImportReturnOrders` → enters workflow (`FunctionID = 22`). Upon approval, converted to return invoice or processed by warehouse.

## Related
- [[ReturnOrdersDetails]]
- [[TransactionsHeaders]]
- [[Customers]]
- [[SalesPersons]]
- [[WF_MasterLog]]


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
- [[ConvertReturnOrderToInvoiceDelivery]]
- [[DEMOSALESPERSON]]
- [[DEMOSALESPERSON2]]
- [[OT_ImportReturnOrder]]
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

**Writes (13):**
- [[OT_ImportActionLog]]
- [[OT_ImportReturnOrder]]
- [[Pro_ReturnOrdersHeaders]]
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
