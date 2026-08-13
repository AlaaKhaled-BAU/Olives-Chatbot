---
type: procedure
database: Olives_BO
name: Rpt_ExceededLimit
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Customers]]
  - [[OrdersHeaders]]
  - [[RequestToExceedCustomerCreditLimit]]
  - [[RequestToExceedCustomerCreditLimitInOrder]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
  - [[WF_SubLog]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_ExceededLimit


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, OrdersHeaders, RequestToExceedCustomerCreditLimit, RequestToExceedCustomerCreditLimitInOrder, SalesPersons, TransactionsHeaders, WF_SubLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @FromDate smalldatetime = '2021-1-1'
- @ToDate smalldatetime = '2022-04-25'
- @CompanyID smallint=1
## Tables Read
- [[Customers]]
- [[OrdersHeaders]]
- [[RequestToExceedCustomerCreditLimit]]
- [[RequestToExceedCustomerCreditLimitInOrder]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- [[WF_SubLog]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[OrdersHeaders]]
- [[RequestToExceedCustomerCreditLimit]]
- [[RequestToExceedCustomerCreditLimitInOrder]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
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
