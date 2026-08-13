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
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AddDiscountToCustomerOrders, ClientsActive, CompanyParameters, Customers, CustomersFinancialDetails, Fun_GetCategoryTree, OT_SendLog, OrdersDetails, OrdersHeaders, POAHeader, RequestSalesmanWillNotVisit, RequestToAddDiscount, RequestToAddDiscountInOrder, RequestToAddDrawer, RequestToAddExtraBonus. Writes AddDiscountToCustomerOrders, OrdersHeaders, POAHeader, RequestSalesmanWillNotVisit, RequestToAddDiscount, RequestToAddDiscountInOrder, RequestToAddDrawer, RequestToAddExtraBonus, RequestToAddExtraBonusAndDiscount, RequestToAddNewCustomer, RequestToAllowTakeChecksFromCustomer, RequestToApprovePromotion, RequestToApprovePromotionDetails, RequestToChangeDeliveryPaymentType, RequestToChangeInvoicePaymentType, RequestToChangeItemSellPrice, RequestToExceedCheckDueDate, RequestToExceedChqLimit, RequestToExceedCustomerCreditLimit, RequestToExceedCustomerCreditLimitInOrder, RequestToExceedCustomerInvoiceDueDays, RequestToExceedCustomerInvoiceDueDaysInOrder, RequestToExceedCustomerVisitOrder, RequestToExceedFinishAllTasks, RequestToExceedInvoiceAmount, RequestToExceedInvoiceCount, RequestToExceedPayInvoiceDiscount, RequestToExceedPayOverBalance, RequestToExceedSalesmanCreditLimit, RequestToIncreaseCustomerCreditlimit, RequestToLinkCustomerToSalesman, RequestToLoginToCustomerWithoutVerficiation, RequestToMakeTransactionToSuspendedCustomer, RequestToMakeZeroAmountInvoice, RequestToReturnInvoice, RequestToVisitCustomerNotInRoute, RequestToVoidTransaction, ReturnOrdersHeaders, SalesQuotationHeaders, TransactionsHeaders, TransfersOrdersHeaders, Vacations, WF_MasterLog, WF_PositionsVer, WF_SubLog. Calls 5 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
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
