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
support_relevance: low
last_verified: 2026-07-05
---
# WF_SubLog


## Business Purpose

Per-step workflow log for tablet **approval requests** (one row per approver position / engine step). Pair with [[WF_MasterLog]] on `ReqID`.

**Code columns** (`Action`, `ActionNeed`) and supervisor inbox filters: [[Workflow_Approval_Codes]]. Pending on you: `Action IS NULL` and `ActionNeed = N'AR'` (see [[WF_GetPositionWFData]]).

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
- [[OSFA_DB/Procedures/SetRequestCanceled]]
