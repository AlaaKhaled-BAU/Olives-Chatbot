---
type: table
database: Olives_BO
name: WF_SubLog
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
  - [[PRO_GETWFLOGFORNOTIFICATION]]
  - [[Pro_Receipts]]
  - [[Rpt_ExceededLimit]]
  - [[Rpt_IncreaseCreditLimit]]
  - [[Rpt_IncreaseCreditLimit_forALPHA]]
  - [[Rpt_OrderLink]]
  - [[Rpt_OrderMaster]]
  - [[Rpt_OrdersAcceptenceStatus]]
  - [[Rpt_ReturnOrdersMaster]]
  - [[Rpt_WFCustomersVisits]]
  - [[Rpt_WFCustomersVisitsCounts]]
  - [[Rpt_WFFunctionsLog]]
  - [[Rpt_WF_SalesOrderStatus]]
  - [[Rpt_WorkFlowExceeds]]
  - [[WF_AddRequestToIncreaseCustomerCreditlimit]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevelOne_Promotions]]
  - [[WF_AddWorkFlowLevels]]
  - [[WF_AlertsRemoveAll]]
  - [[WF_AlertsUpdate]]
  - [[WF_GetCustAgingInfo]]
  - [[WF_GetPositionWFData]]
  - [[WF_GetPositionWFDataByDate_Alerts]]
  - [[WF_GetPositionWFData_Alerts]]
support_relevance: high
last_verified: 2026-10-03
---
# WF_SubLog

## Business Purpose
Per-step workflow log and approval task table — stores one row per approver position, level, or engine notification for each request. Forms the **supervisor inbox** when filtered for pending actions, and forms the audit trail of who approved or rejected each step. Pair with [[WF_MasterLog]] on `ReqID` and company. Queryable via `t.WF_SubLog`.

## Chatbot semantics
(Query `t.WF_SubLog` — scoped by session CompanyID via `t.` views.)

| User / Arabic intent | Column(s) | Filter / rule | Notes |
|----------------------|-----------|---------------|-------|
| بانتظار موافقتي (Supervisor Inbox) | `Action`, `ActionNeed`, `PositionID` | `Action IS NULL AND ActionNeed = N'AR' AND PositionID = @PosID` | Exactly what the tablet inbox displays |
| طلبات وافقت عليها | `Action`, `PositionID`, `ActionDate` | `Action = N'A' AND PositionID = @PosID` | Date range on `ActionDate` |
| طلبات رفضتها | `Action`, `PositionID`, `ActionDate` | `Action = N'R' AND PositionID = @PosID` | Rejection decisions |
| مستوى الموافقة الحالي | `ARLevel` | e.g. `ARLevel = 1` | 1 = first level approver, 2 = second level, etc. |
| تفاصيل الطلب والمندوب | Join `t.WF_MasterLog` | `s.ReqID = m.ReqID AND s.CompanyID = m.CompanyID` | Gives `FunctionID`, `ReqDate`, and `Ref1`..`Ref5` |
| اسم نوع الطلب | Join `t.WF_Functions` | `m.FunctionID = f.ID` | Gives human-readable request name (`ArName` / `EngName`) |

**Do not confuse with:**
- `WF_MasterLog.LastStatus`: Request overall outcome (0=Open, 1=Approved, 2=Rejected, 3=Canceled). An individual approver line having `Action = 'A'` does not mean `LastStatus = 1` if higher approval levels remain.
- `Action = 'N'`: Notification/history line logged by the workflow engine (often with `TrDesc` indicating action at earlier levels); not an inbox action item.
- `LogActionTransaction`: Field activity log (visits, invoices). Approvals are not field actions.

## Grain & keys
- **PK**: `SID` (numeric step ID)
- **Join to Master**: `ReqID` (links to `WF_MasterLog.ReqID`)
- **Tenant key**: `CompanyID`

## Pipeline (how rows get here)
Created by `WF_AddWorkFlowLevelOne` when mobile request arrives. Approver takes action in back-office UI or tablet (`WF_GetPositionWFData`) → invokes `WF_AddWorkFlowLevels` → updates `Action`, `ActionDate`, `Notes`, and if higher levels exist, seeds the next level's `WF_SubLog` row.

## Related
- [[WF_MasterLog]]
- [[WF_Functions]]
- [[Workflow_Approval_Codes]]
- [[WF_GetPositionWFData]]
- [[WF_AddWorkFlowLevels]]


## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| SID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  | ✓ | [[Companies]] |
| ReqID | numeric | YES |  |  |  |
| PositionID | int | YES |  |  |  |
| SalesmanNo | int | YES |  |  |  |
| ReqDate | smalldatetime | YES |  |  |  |
| ActionNeed | nvarchar | YES |  |  |  |
| Action | nvarchar | YES |  |  |  |
| ActionDate | smalldatetime | YES |  |  |  |
| ARLevel | smallint | YES |  |  |  |
| TrDesc | nvarchar | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| Ref1 | nvarchar | YES |  |  |  |
| Ref2 | nvarchar | YES |  |  |  |
| Ref3 | nvarchar | YES |  |  |  |
| Ref4 | nvarchar | YES |  |  |  |
| Ref5 | nvarchar | YES |  |  |  |
| IsPostedNotification | bit | YES |  |  |  |
| IsCanceled | bit | YES |  |  |  |
## Primary Key
SID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (54):**
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
- [[PRO_GETWFLOGFORNOTIFICATION]]
- [[Pro_Receipts]]
- [[Rpt_ExceededLimit]]
- [[Rpt_IncreaseCreditLimit]]
- [[Rpt_IncreaseCreditLimit_forALPHA]]
- [[Rpt_OrderLink]]
- [[Rpt_OrderMaster]]
- [[Rpt_OrdersAcceptenceStatus]]
- [[Rpt_ReturnOrdersMaster]]
- [[Rpt_WFCustomersVisits]]
- [[Rpt_WFCustomersVisitsCounts]]
- [[Rpt_WFFunctionsLog]]
- [[Rpt_WF_SalesOrderStatus]]
- [[Rpt_WorkFlowExceeds]]
- [[WF_AddRequestToIncreaseCustomerCreditlimit]]
- [[WF_AddWorkFlowLevelOne_Promotions]]
- [[WF_AlertsRemoveAll]]
- [[WF_AlertsUpdate]]
- [[WF_GetCustAgingInfo]]
- [[WF_GetPositionWFData]]
- [[WF_GetPositionWFDataByDate_Alerts]]
- [[WF_GetPositionWFData_Alerts]]

**Writes (38):**
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
- [[WF_AlertsRemoveAll]]
- [[WF_AlertsUpdate]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Rapid growth**: Table size growing fast — archive old records periodically
- **Orphan log entries**: No corresponding source transaction — investigate data source
- **No cleanup**: No purge job configured — disk space may fill up

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
