---
type: procedure
database: Olives_BO
name: WF_AddWorkFlowLevels
schema: dbo
tags: [#auth, #backoffice, #workflow]
reads_from:
  - [[AddDiscountToCustomerOrders]]
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Fun_GetCategoryTree
  - [[OT_SendLog]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[POAHeader]]
  - [[RequestSalesmanWillNotVisit]]
  - [[RequestToAddDiscount]]
  - [[RequestToAddDiscountInOrder]]
  - [[RequestToAddDrawer]]
  - [[RequestToAddExtraBonus]]
writes_to:
  - [[AddDiscountToCustomerOrders]]
  - [[OrdersHeaders]]
  - [[POAHeader]]
  - [[RequestSalesmanWillNotVisit]]
  - [[RequestToAddDiscount]]
  - [[RequestToAddDiscountInOrder]]
  - [[RequestToAddDrawer]]
  - [[RequestToAddExtraBonus]]
  - [[RequestToAddExtraBonusAndDiscount]]
  - [[RequestToAddNewCustomer]]
  - [[RequestToAllowTakeChecksFromCustomer]]
  - [[RequestToApprovePromotion]]
  - [[RequestToApprovePromotionDetails]]
  - [[RequestToChangeDeliveryPaymentType]]
  - [[RequestToChangeInvoicePaymentType]]
  - [[RequestToChangeItemSellPrice]]
  - [[RequestToExceedCheckDueDate]]
  - [[RequestToExceedChqLimit]]
  - [[RequestToExceedCustomerCreditLimit]]
  - [[RequestToExceedCustomerCreditLimitInOrder]]
  - [[RequestToExceedCustomerInvoiceDueDays]]
  - [[RequestToExceedCustomerInvoiceDueDaysInOrder]]
  - [[RequestToExceedCustomerVisitOrder]]
  - [[RequestToExceedFinishAllTasks]]
  - [[RequestToExceedInvoiceAmount]]
  - [[RequestToExceedInvoiceCount]]
  - [[RequestToExceedPayInvoiceDiscount]]
  - [[RequestToExceedPayOverBalance]]
  - [[RequestToExceedSalesmanCreditLimit]]
  - [[RequestToIncreaseCustomerCreditlimit]]
  - [[RequestToLinkCustomerToSalesman]]
  - [[RequestToLoginToCustomerWithoutVerficiation]]
  - [[RequestToMakeTransactionToSuspendedCustomer]]
  - [[RequestToMakeZeroAmountInvoice]]
  - [[RequestToReturnInvoice]]
  - [[RequestToVisitCustomerNotInRoute]]
  - [[RequestToVoidTransaction]]
  - [[ReturnOrdersHeaders]]
  - [[SalesQuotationHeaders]]
  - [[TransactionsHeaders]]
  - [[TransfersOrdersHeaders]]
  - [[Vacations]]
  - [[WF_MasterLog]]
  - [[WF_PositionsVer]]
  - [[WF_SubLog]]
called_by:
  - [[ConvertReturnOrderToInvoiceDelivery]]
  - [[Pro_ConvertLoadOrderToTransaction]]
  - [[Pro_ConvertUnloadOrderToTransaction]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_IsHaveDueBalance]]
support_relevance: high
last_verified: 2026-07-05
---
# WF_AddWorkFlowLevels


## Purpose
Core workflow decision execution procedure in Olives_BO that records an approver's action on a workflow step and transitions the request to the next level or final status.
- **Trigger**: Called when a supervisor or manager acts on an item in their inbox (`Action = 'A'` for Approve, `'R'` for Reject).
- **Outcome**: 
  - Updates the targeted step in `WF_SubLog` with `Action`, `ActionDate`, `Notes`, and `PositionID`.
  - If approved (`'A'`) and further levels exist, creates the next level task in `WF_SubLog` (`ARLevel = ARLevel + 1`).
  - If rejected (`'R'`), marks `WF_MasterLog.LastStatus = 2` (Rejected) and terminates further workflow routing.
  - If approved on the final level (`IsFinalApprove = 1`), updates `WF_MasterLog.LastStatus = 1` (Approved), and executes post-approval business logic on the underlying request table (e.g. Setting `IsAproved = 1` in `RequestTo*`, or releasing hold flags on `OrdersHeaders`).
## Parameters
- @CompanyID smallint
- @SID numeric(30, 0)
- @Action nvarchar(1)
- @ActionDate smalldatetime
- @Notes nvarchar(500)
- @PositionID int
- @SalesmanNo int = 0
- @DtPromotion WFPromotionsDetails Readonly
- @ReAssignSalesmanNo int = 0
## Tables Read
- [[AddDiscountToCustomerOrders]]
- [[ClientsActive]]
- [[CompanyParameters]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetCategoryTree
- [[OT_SendLog]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[POAHeader]]
- [[RequestSalesmanWillNotVisit]]
- [[RequestToAddDiscount]]
- [[RequestToAddDiscountInOrder]]
- [[RequestToAddDrawer]]
- [[RequestToAddExtraBonus]]
## Tables Written
- [[AddDiscountToCustomerOrders]]
- [[OrdersHeaders]]
- [[POAHeader]]
- [[RequestSalesmanWillNotVisit]]
- [[RequestToAddDiscount]]
- [[RequestToAddDiscountInOrder]]
- [[RequestToAddDrawer]]
- [[RequestToAddExtraBonus]]
- [[RequestToAddExtraBonusAndDiscount]]
- [[RequestToAddNewCustomer]]
- [[RequestToAllowTakeChecksFromCustomer]]
- [[RequestToApprovePromotion]]
- [[RequestToApprovePromotionDetails]]
- [[RequestToChangeDeliveryPaymentType]]
- [[RequestToChangeInvoicePaymentType]]
- [[RequestToChangeItemSellPrice]]
- [[RequestToExceedCheckDueDate]]
- [[RequestToExceedChqLimit]]
- [[RequestToExceedCustomerCreditLimit]]
- [[RequestToExceedCustomerCreditLimitInOrder]]
- [[RequestToExceedCustomerInvoiceDueDays]]
- [[RequestToExceedCustomerInvoiceDueDaysInOrder]]
- [[RequestToExceedCustomerVisitOrder]]
- [[RequestToExceedFinishAllTasks]]
- [[RequestToExceedInvoiceAmount]]
- [[RequestToExceedInvoiceCount]]
- [[RequestToExceedPayInvoiceDiscount]]
- [[RequestToExceedPayOverBalance]]
- [[RequestToExceedSalesmanCreditLimit]]
- [[RequestToIncreaseCustomerCreditlimit]]
- [[RequestToLinkCustomerToSalesman]]
- [[RequestToLoginToCustomerWithoutVerficiation]]
- [[RequestToMakeTransactionToSuspendedCustomer]]
- [[RequestToMakeZeroAmountInvoice]]
- [[RequestToReturnInvoice]]
- [[RequestToVisitCustomerNotInRoute]]
- [[RequestToVoidTransaction]]
- [[ReturnOrdersHeaders]]
- [[SalesQuotationHeaders]]
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]
- [[Vacations]]
- [[WF_MasterLog]]
- [[WF_PositionsVer]]
- [[WF_SubLog]]
## Callers
_None (no known callers)_
## Callees
- [[ConvertReturnOrderToInvoiceDelivery]]
- [[Pro_ConvertLoadOrderToTransaction]]
- [[Pro_ConvertUnloadOrderToTransaction]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_IsHaveDueBalance]]
## Impact / Dependencies

**Tables Read**
- [[AddDiscountToCustomerOrders]]
- [[ClientsActive]]
- [[CompanyParameters]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetCategoryTree
- [[OT_SendLog]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[POAHeader]]
- [[RequestSalesmanWillNotVisit]]
- [[RequestToAddDiscount]]
- [[RequestToAddDiscountInOrder]]
- [[RequestToAddDrawer]]
- [[RequestToAddExtraBonus]]

**Tables Written**
- [[AddDiscountToCustomerOrders]]
- [[OrdersHeaders]]
- [[POAHeader]]
- [[RequestSalesmanWillNotVisit]]
- [[RequestToAddDiscount]]
- [[RequestToAddDiscountInOrder]]
- [[RequestToAddDrawer]]
- [[RequestToAddExtraBonus]]
- [[RequestToAddExtraBonusAndDiscount]]
- [[RequestToAddNewCustomer]]
- [[RequestToAllowTakeChecksFromCustomer]]
- [[RequestToApprovePromotion]]
- [[RequestToApprovePromotionDetails]]
- [[RequestToChangeDeliveryPaymentType]]
- [[RequestToChangeInvoicePaymentType]]
- [[RequestToChangeItemSellPrice]]
- [[RequestToExceedCheckDueDate]]
- [[RequestToExceedChqLimit]]
- [[RequestToExceedCustomerCreditLimit]]
- [[RequestToExceedCustomerCreditLimitInOrder]]
- [[RequestToExceedCustomerInvoiceDueDays]]
- [[RequestToExceedCustomerInvoiceDueDaysInOrder]]
- [[RequestToExceedCustomerVisitOrder]]
- [[RequestToExceedFinishAllTasks]]
- [[RequestToExceedInvoiceAmount]]
- [[RequestToExceedInvoiceCount]]
- [[RequestToExceedPayInvoiceDiscount]]
- [[RequestToExceedPayOverBalance]]
- [[RequestToExceedSalesmanCreditLimit]]
- [[RequestToIncreaseCustomerCreditlimit]]
- [[RequestToLinkCustomerToSalesman]]
- [[RequestToLoginToCustomerWithoutVerficiation]]
- [[RequestToMakeTransactionToSuspendedCustomer]]
- [[RequestToMakeZeroAmountInvoice]]
- [[RequestToReturnInvoice]]
- [[RequestToVisitCustomerNotInRoute]]
- [[RequestToVoidTransaction]]
- [[ReturnOrdersHeaders]]
- [[SalesQuotationHeaders]]
- [[TransactionsHeaders]]
- [[TransfersOrdersHeaders]]
- [[Vacations]]
- [[WF_MasterLog]]
- [[WF_PositionsVer]]
- [[WF_SubLog]]

**Callers**
- [[ConvertReturnOrderToInvoiceDelivery]]
- [[Pro_ConvertLoadOrderToTransaction]]
- [[Pro_ConvertUnloadOrderToTransaction]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_IsHaveDueBalance]]

**Callees**
_None_


## When to Run This

Workflow procedure — called automatically by the WF engine when processing approval chains. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
