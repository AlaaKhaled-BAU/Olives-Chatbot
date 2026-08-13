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
support_relevance: low
last_verified: 2026-07-05
---
# WF_MasterLog


## Business Purpose

Workflow configuration or log table for approval process management.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | YES |  | ✓ | [[Companies]] |
| ReqID | numeric | YES | ✓ |  |  |
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
## Common Issues

- **Rapid growth**: Table size growing fast — archive old records periodically
- **Orphan log entries**: No corresponding source transaction — investigate data source
- **No cleanup**: No purge job configured — disk space may fill up

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
