---
type: procedure
database: Olives_BO
name: Rpt_WorkFlowFunctions
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[OrdersHeaders]]
  - [[RequestSalesmanWillNotVisit]]
  - [[RequestToAddDiscount]]
  - [[RequestToAddDiscountInOrder]]
  - [[RequestToAddDrawer]]
  - [[RequestToAddExtraBonus]]
  - [[RequestToAllowTakeChecksFromCustomer]]
  - [[RequestToApprovePromotion]]
  - [[RequestToChangeInvoicePaymentType]]
  - [[RequestToChangeItemSellPrice]]
  - [[RequestToExceedCheckDueDate]]
  - [[RequestToExceedChqLimit]]
  - [[RequestToExceedCustomerCreditLimit]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_WorkFlowFunctions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, OrdersHeaders, RequestSalesmanWillNotVisit, RequestToAddDiscount, RequestToAddDiscountInOrder, RequestToAddDrawer, RequestToAddExtraBonus, RequestToAllowTakeChecksFromCustomer, RequestToApprovePromotion, RequestToChangeInvoicePaymentType, RequestToChangeItemSellPrice, RequestToExceedCheckDueDate, RequestToExceedChqLimit, RequestToExceedCustomerCreditLimit. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID  smallint =1
- @TableID int = 3
- @FromDate datetime = '2019-03-01 15:07:00'
- @ToDate datetime = '2024-03-11  11:46:00'
- @IsApprove smallint =1
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[OrdersHeaders]]
- [[RequestSalesmanWillNotVisit]]
- [[RequestToAddDiscount]]
- [[RequestToAddDiscountInOrder]]
- [[RequestToAddDrawer]]
- [[RequestToAddExtraBonus]]
- [[RequestToAllowTakeChecksFromCustomer]]
- [[RequestToApprovePromotion]]
- [[RequestToChangeInvoicePaymentType]]
- [[RequestToChangeItemSellPrice]]
- [[RequestToExceedCheckDueDate]]
- [[RequestToExceedChqLimit]]
- [[RequestToExceedCustomerCreditLimit]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[OrdersHeaders]]
- [[RequestSalesmanWillNotVisit]]
- [[RequestToAddDiscount]]
- [[RequestToAddDiscountInOrder]]
- [[RequestToAddDrawer]]
- [[RequestToAddExtraBonus]]
- [[RequestToAllowTakeChecksFromCustomer]]
- [[RequestToApprovePromotion]]
- [[RequestToChangeInvoicePaymentType]]
- [[RequestToChangeItemSellPrice]]
- [[RequestToExceedCheckDueDate]]
- [[RequestToExceedChqLimit]]
- [[RequestToExceedCustomerCreditLimit]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
