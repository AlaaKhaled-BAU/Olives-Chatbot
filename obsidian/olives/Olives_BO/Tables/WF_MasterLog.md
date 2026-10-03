---
type: table
database: Olives_BO
name: WF_MasterLog
schema: dbo
tags: [#auth, #backoffice, #log, #workflow]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_GetOrderInvoiceLinkHistory]]
  - [[OT_ImportRequestSalesmanWillNotVisit]]
  - [[OT_ImportRequestToAddDiscount]]
  - [[OT_ImportRequestToAddDiscountInOrder]]
  - [[OT_ImportRequestToAddDrawer]]
  - [[OT_ImportRequestToAddExtraBonus]]
  - [[OT_ImportRequestToAddExtraBonusAndDiscount]]
  - [[OT_ImportRequestToAddNewCustomer]]
  - [[OT_ImportRequestToAllowTakeChecksFromCustomer]]
  - [[OT_ImportRequestToApprovePromotion]]
  - [[OT_ImportRequestToChangeDeliveryPaymentType]]
  - [[OT_ImportRequestToChangeInvoicePaymentType]]
  - [[OT_ImportRequestToChangeItemSellPrice]]
  - [[OT_ImportRequestToExceedCheckDueDate]]
  - [[OT_ImportRequestToExceedChqLimit]]
  - [[OT_ImportRequestToExceedCustomerCreditLimit]]
  - [[OT_ImportRequestToExceedCustomerCreditLimitInOrder]]
  - [[OT_ImportRequestToExceedCustomerInvoiceDueDays]]
  - [[OT_ImportRequestToExceedCustomerInvoiceDueDaysInOrder]]
  - [[OT_ImportRequestToExceedCustomerVisitOrder]]
  - [[OT_ImportRequestToExceedFinishAllTasks]]
  - [[OT_ImportRequestToExceedInvoiceAmount]]
  - [[OT_ImportRequestToExceedInvoiceCount]]
  - [[OT_ImportRequestToExceedPayInvoiceDiscount]]
  - [[OT_ImportRequestToExceedPayOverBalance]]
  - [[OT_ImportRequestToExceedSalesmanCreditLimit]]
  - [[OT_ImportRequestToLinkCustomerToSalesman]]
  - [[OT_ImportRequestToLoginToCustomerWithoutVerficiation]]
  - [[OT_ImportRequestToMakeTransactionToSuspendedCustomer]]
  - [[OT_ImportRequestToMakeZeroAmountInvoice]]
  - [[OT_ImportRequestToReturnInvoice]]
  - [[OT_ImportRequestToVisitCustomerNotInRoute]]
  - [[OT_ImportSalesOrders]]
  - [[OT_ImportUploadOrders]]
  - [[Rpt_IncreaseCreditLimit]]
  - [[Rpt_IncreaseCreditLimit_forALPHA]]
  - [[Rpt_OrdersAcceptenceStatus]]
  - [[Rpt_WFCustomersVisits]]
  - [[Rpt_WFCustomersVisitsCounts]]
  - [[Rpt_WFFunctionsLog]]
  - [[Rpt_WF_SalesOrderStatus]]
  - [[WF_AddRequestToIncreaseCustomerCreditlimit]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevelOne_Promotions]]
  - [[WF_AddWorkFlowLevels]]
  - [[WF_AlertsRemoveAll]]
  - [[WF_AlertsUpdate]]
  - [[WF_GetPositionWFData]]
  - [[WF_GetPositionWFDataByDate_Alerts]]
  - [[WF_GetPositionWFData_Alerts]]
support_relevance: high
last_verified: 2026-10-03
---
# WF_MasterLog

## Business Purpose
The central workflow master header — one row per approval request raised by mobile salesmen (e.g. credit limit exceptions, extra discounts, out-of-route visits) or generated for orders. Tracks overall request lifecycle via `LastStatus`, request category via `FunctionID`, applicant via `PositionID` / `ReqBy`, and links to the underlying business record via `Ref1`..`Ref5`. Queryable as `t.WF_MasterLog` scoped by company.

## Chatbot semantics
(Query `t.WF_MasterLog` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| طلبات معلّقة / قيد الإجراء | `LastStatus` | `LastStatus = N'0'` | Request is still open in workflow |
| طلبات تمت الموافقة عليها | `LastStatus` | `LastStatus = N'1'` | Final approval granted |
| طلبات مرفوضة | `LastStatus` | `LastStatus = N'2'` | Request rejected |
| طلبات ملغاة من التابلت | `LastStatus` | `LastStatus = N'3'` | Canceled before completion |
| نوع الطلب (حد ائتمان، خصم، خارج المسار...) | `FunctionID` | Join `t.WF_Functions` on `FunctionID = WF_Functions.ID` | Key IDs: 2 (Credit Limit), 5 (Off-Route), 6 (Sales Order), 11 (Discount), 28 (Promotion) |
| تاريخ ووقت الطلب | `ReqDate` | e.g. `CAST(ReqDate AS date) = '...'` | Submission timestamp |
| مقدم الطلب (المندوب) | `PositionID`, `ReqBy` | Link to `SalesPersons` | Position of the salesman submitting the request |

**Do not confuse with:**
- `WF_SubLog.Action`: Individual approver step action (`A` Approved, `R` Rejected, `NULL` Pending). A request can have `WF_MasterLog.LastStatus = 0` (Open) while several levels have already marked `Action = 'A'`.
- `LogActionTransaction.ActionID`: Actual field visits/log actions. Workflow requests do not represent store visits.
- `SystemCodes`: Approval codes are NOT in `SystemCodes` (see [[Workflow_Approval_Codes]]).

## Ref1..Ref5 Joins to Request Details
- **FunctionID = 2** (RequestToExceedCustomerCreditLimit): `TRY_CAST(Ref1 AS numeric) = RequestToExceedCustomerCreditLimit.AutoID`
- **FunctionID = 4** (RequestToExceedCustomerInvoiceDueDays): `TRY_CAST(Ref1 AS numeric) = RequestToExceedCustomerInvoiceDueDays.AutoID`
- **FunctionID = 5** (RequestToVisitCustomerNotInRoute): `TRY_CAST(Ref1 AS numeric) = RequestToVisitCustomerNotInRoute.AutoID`
- **FunctionID = 6** (Sales Orders): `TRY_CAST(Ref1 AS int) = OrdersHeaders.OrderYear AND TRY_CAST(Ref2 AS numeric) = OrdersHeaders.OrderNo`
- **FunctionID = 7** (Load Orders): `TRY_CAST(Ref1 AS int) = TransfersOrdersHeaders.TrYear AND TRY_CAST(Ref2 AS numeric) = TransfersOrdersHeaders.TrNo`
- **FunctionID = 11** (RequestToAddDiscount): `TRY_CAST(Ref1 AS numeric) = RequestToAddDiscount.AutoID`
- **FunctionID = 14** (RequestToApproveChqLimit): `TRY_CAST(Ref1 AS numeric) = RequestToExceedChqLimit.AutoID`
- **FunctionID = 15** (RequestToExceedCustomerCreditLimitInOrder): `TRY_CAST(Ref1 AS numeric) = RequestToExceedCustomerCreditLimitInOrder.AutoID`
- **FunctionID = 21** (RequestToAddNewCustomer): `TRY_CAST(Ref1 AS numeric) = RequestToAddNewCustomer.AutoID`
- **FunctionID = 23** (RequestSalesmanWillNotVisit): `TRY_CAST(Ref1 AS numeric) = RequestSalesmanWillNotVisit.AutoID`
- **FunctionID = 28** (Promo): `TRY_CAST(Ref1 AS numeric) = RequestToApprovePromotion.AutoID`

## Grain & keys
- **PK**: `ReqID` (numeric identity, 1 row = 1 request)
- **Tenant key**: `CompanyID`

## Pipeline (how rows get here)
Tablet/OSFA sync → `OT_ImportRequestTo*` procs → calls `WF_AddWorkFlowLevelOne` (inserts master row with `LastStatus = 0`, populates `Ref1`..`Ref5`, and seeds `WF_SubLog` approval chain). `WF_AddWorkFlowLevels` updates `LastStatus` to 1 (Approved) or 2 (Rejected).

## Related
- [[WF_SubLog]]
- [[WF_Functions]]
- [[Workflow_Approval_Codes]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]
- [[WF_GetPositionWFData]]
- [[_RequestTo-Join-Conventions]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | YES |  | ✓ | [[Companies]] |
| ReqID | numeric | NO | ✓ |  |  |
| FunctionID | smallint | YES |  |  |  |
| PositionID | int | YES |  |  |  |
| ReqDate | smalldatetime | YES |  |  |  |
| GPSx | nvarchar | YES |  |  |  |
| GPSy | nvarchar | YES |  |  |  |
| LastStatus | nvarchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| Ref1 | nvarchar | YES |  |  |  |
| Ref2 | nvarchar | YES |  |  |  |
| Ref3 | nvarchar | YES |  |  |  |
| Ref4 | nvarchar | YES |  |  |  |
| Ref5 | nvarchar | YES |  |  |  |
| ReqBy | nvarchar | YES |  |  |  |
## Primary Key
ReqID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (46):**
- [[OT_GetOrderInvoiceLinkHistory]]
- [[OT_ImportRequestSalesmanWillNotVisit]]
- [[OT_ImportRequestToAddDiscount]]
- [[OT_ImportRequestToAddDiscountInOrder]]
- [[OT_ImportRequestToAddDrawer]]
- [[OT_ImportRequestToAddExtraBonus]]
- [[OT_ImportRequestToAddExtraBonusAndDiscount]]
- [[OT_ImportRequestToAddNewCustomer]]
- [[OT_ImportRequestToAllowTakeChecksFromCustomer]]
- [[OT_ImportRequestToApprovePromotion]]
- [[OT_ImportRequestToChangeDeliveryPaymentType]]
- [[OT_ImportRequestToChangeInvoicePaymentType]]
- [[OT_ImportRequestToChangeItemSellPrice]]
- [[OT_ImportRequestToExceedCheckDueDate]]
- [[OT_ImportRequestToExceedChqLimit]]
- [[OT_ImportRequestToExceedCustomerCreditLimit]]
- [[OT_ImportRequestToExceedCustomerCreditLimitInOrder]]
- [[OT_ImportRequestToExceedCustomerInvoiceDueDays]]
- [[OT_ImportRequestToExceedCustomerInvoiceDueDaysInOrder]]
- [[OT_ImportRequestToExceedCustomerVisitOrder]]
- [[OT_ImportRequestToExceedFinishAllTasks]]
- [[OT_ImportRequestToExceedInvoiceAmount]]
- [[OT_ImportRequestToExceedInvoiceCount]]
- [[OT_ImportRequestToExceedPayInvoiceDiscount]]
- [[OT_ImportRequestToExceedPayOverBalance]]
- [[OT_ImportRequestToExceedSalesmanCreditLimit]]
- [[OT_ImportRequestToLinkCustomerToSalesman]]
- [[OT_ImportRequestToLoginToCustomerWithoutVerficiation]]
- [[OT_ImportRequestToMakeTransactionToSuspendedCustomer]]
- [[OT_ImportRequestToMakeZeroAmountInvoice]]
- [[OT_ImportRequestToReturnInvoice]]
- [[OT_ImportRequestToVisitCustomerNotInRoute]]
- [[Rpt_IncreaseCreditLimit]]
- [[Rpt_IncreaseCreditLimit_forALPHA]]
- [[Rpt_OrdersAcceptenceStatus]]
- [[Rpt_WFCustomersVisits]]
- [[Rpt_WFCustomersVisitsCounts]]
- [[Rpt_WFFunctionsLog]]
- [[Rpt_WF_SalesOrderStatus]]
- [[WF_AddRequestToIncreaseCustomerCreditlimit]]
- [[WF_AddWorkFlowLevelOne_Promotions]]
- [[WF_AlertsRemoveAll]]
- [[WF_AlertsUpdate]]
- [[WF_GetPositionWFData]]
- [[WF_GetPositionWFDataByDate_Alerts]]
- [[WF_GetPositionWFData_Alerts]]

**Writes (36):**
- [[OT_ImportRequestToAddDiscount]]
- [[OT_ImportRequestToAddDiscountInOrder]]
- [[OT_ImportRequestToAddDrawer]]
- [[OT_ImportRequestToAddExtraBonus]]
- [[OT_ImportRequestToAddExtraBonusAndDiscount]]
- [[OT_ImportRequestToAddNewCustomer]]
- [[OT_ImportRequestToAllowTakeChecksFromCustomer]]
- [[OT_ImportRequestToApprovePromotion]]
- [[OT_ImportRequestToChangeDeliveryPaymentType]]
- [[OT_ImportRequestToChangeInvoicePaymentType]]
- [[OT_ImportRequestToChangeItemSellPrice]]
- [[OT_ImportRequestToExceedCheckDueDate]]
- [[OT_ImportRequestToExceedChqLimit]]
- [[OT_ImportRequestToExceedCustomerCreditLimit]]
- [[OT_ImportRequestToExceedCustomerCreditLimitInOrder]]
- [[OT_ImportRequestToExceedCustomerInvoiceDueDays]]
- [[OT_ImportRequestToExceedCustomerInvoiceDueDaysInOrder]]
- [[OT_ImportRequestToExceedCustomerVisitOrder]]
- [[OT_ImportRequestToExceedFinishAllTasks]]
- [[OT_ImportRequestToExceedInvoiceAmount]]
- [[OT_ImportRequestToExceedInvoiceCount]]
- [[OT_ImportRequestToExceedPayInvoiceDiscount]]
- [[OT_ImportRequestToExceedPayOverBalance]]
- [[OT_ImportRequestToExceedSalesmanCreditLimit]]
- [[OT_ImportRequestToLinkCustomerToSalesman]]
- [[OT_ImportRequestToLoginToCustomerWithoutVerficiation]]
- [[OT_ImportRequestToMakeTransactionToSuspendedCustomer]]
- [[OT_ImportRequestToMakeZeroAmountInvoice]]
- [[OT_ImportRequestToReturnInvoice]]
- [[OT_ImportRequestToVisitCustomerNotInRoute]]
- [[OT_ImportSalesOrders]]
- [[OT_ImportUploadOrders]]
- [[WF_AddRequestToIncreaseCustomerCreditlimit]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevelOne_Promotions]]
- [[WF_AddWorkFlowLevels]]

## Estimated Size / Volatility
Typical business table
## Status codes (LastStatus)

Decode **`0` open / `1` approved / `2` rejected / `3` canceled** — full tables, inbox rules, and Arabic labels: [[Workflow_Approval_Codes]]. Not `SystemCodes` type `Status`.

## Common Issues

- **Approver resolution**: FunctionID joins [[WF_Functions]].ID by convention (no declared FK); PositionID -> Positions
- **Volume**: append-only log — always bound queries by date
## Tenancy

Chatbot queries `t.WF_MasterLog` only — auto-scoped by `SESSION_CONTEXT(N'CompanyID')`. Raw dbo access is blocked for `chatbot_ro`.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
