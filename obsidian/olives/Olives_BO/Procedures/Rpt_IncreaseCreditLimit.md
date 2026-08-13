---
type: procedure
database: Olives_BO
name: Rpt_IncreaseCreditLimit
schema: dbo
tags: [#backoffice, #billing, #reporting]
reads_from:
  - [[CompanyBranches]]
  - [[Customers]]
  - [[OrdersHeaders]]
  - [[RequestToIncreaseCustomerCreditlimit]]
  - [[SalesPersons]]
  - [[WF_MasterLog]]
  - [[WF_SubLog]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_IncreaseCreditLimit


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CompanyBranches, Customers, OrdersHeaders, RequestToIncreaseCustomerCreditlimit, SalesPersons, WF_MasterLog, WF_SubLog. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @FromDate smalldatetime = '2020-01-01'
- @ToDate smalldatetime = '2022-01-01'
- @FromSales int =1
- @ToSales int =9999
- @CompanyID smallint = 1
## Tables Read
- [[CompanyBranches]]
- [[Customers]]
- [[OrdersHeaders]]
- [[RequestToIncreaseCustomerCreditlimit]]
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
- [[CompanyBranches]]
- [[Customers]]
- [[OrdersHeaders]]
- [[RequestToIncreaseCustomerCreditlimit]]
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
