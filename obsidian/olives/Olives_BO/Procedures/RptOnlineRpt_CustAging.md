---
type: procedure
database: Olives_BO
name: RptOnlineRpt_CustAging
schema: dbo
tags: [#backoffice, #integration, #reporting]
reads_from:
  - [[Customers]]
  - [[CustomersBalanceAging]]
  - [[CustomersFinancialDetails]]
  - [[CustomersPaidTransList]]
  - Fun_GetInvoiceTotalAmount
  - [[Receipts]]
  - [[Receipts_PaidTrans]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# RptOnlineRpt_CustAging


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersBalanceAging, CustomersFinancialDetails, CustomersPaidTransList, Fun_GetInvoiceTotalAmount, Receipts, Receipts_PaidTrans, SalesPersons, TransactionsHeaders, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @SalesmanNo int =3003
- @P1 int = 30
- @P2 int = 60
- @P3 int = 90
- @P4 int = 120
## Tables Read
- [[Customers]]
- [[CustomersBalanceAging]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- Fun_GetInvoiceTotalAmount
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersBalanceAging]]
- [[CustomersFinancialDetails]]
- [[CustomersPaidTransList]]
- Fun_GetInvoiceTotalAmount
- [[Receipts]]
- [[Receipts_PaidTrans]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
