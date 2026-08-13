---
type: procedure
database: Olives_BO
name: Rpt_WFFunctionsLog
schema: dbo
tags: [#backoffice, #log, #reporting]
reads_from:
  - [[RequestToAddDiscountInOrder]]
  - [[RequestToAddExtraBonus]]
  - [[RequestToChangeInvoicePaymentType]]
  - [[RequestToExceedCheckDueDate]]
  - [[RequestToExceedCustomerCreditLimitInOrder]]
  - [[RequestToExceedCustomerInvoiceDueDays]]
  - [[SalesPersons]]
  - [[WF_MasterLog]]
  - [[WF_SubLog]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_WFFunctionsLog


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads RequestToAddDiscountInOrder, RequestToAddExtraBonus, RequestToChangeInvoicePaymentType, RequestToExceedCheckDueDate, RequestToExceedCustomerCreditLimitInOrder, RequestToExceedCustomerInvoiceDueDays, SalesPersons, WF_MasterLog, WF_SubLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromCustomer bigint
- @ToCustomer bigint
- @FromSalesman int
- @ToSalesman int
- @WFFunID int
## Tables Read
- [[RequestToAddDiscountInOrder]]
- [[RequestToAddExtraBonus]]
- [[RequestToChangeInvoicePaymentType]]
- [[RequestToExceedCheckDueDate]]
- [[RequestToExceedCustomerCreditLimitInOrder]]
- [[RequestToExceedCustomerInvoiceDueDays]]
- [[SalesPersons]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[RequestToAddDiscountInOrder]]
- [[RequestToAddExtraBonus]]
- [[RequestToChangeInvoicePaymentType]]
- [[RequestToExceedCheckDueDate]]
- [[RequestToExceedCustomerCreditLimitInOrder]]
- [[RequestToExceedCustomerInvoiceDueDays]]
- [[SalesPersons]]
- [[WF_MasterLog]]
- [[WF_SubLog]]

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
