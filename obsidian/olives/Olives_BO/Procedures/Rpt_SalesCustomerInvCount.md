---
type: procedure
database: Olives_BO
name: Rpt_SalesCustomerInvCount
schema: dbo
tags: [#backoffice, #customer, #reporting, #sales]
reads_from:
  - [[Customers]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesCustomerInvCount


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @FromDate smalldatetime = '2019-01-01'
- @ToDate smalldatetime = '2019-04-22'
- @FromSalesman int = 0
- @ToSalesman int = 999999
- @FromCustomer bigint = 0
- @ToCustomer bigint = 999999999999
- @WithTax bit = 0
## Tables Read
- [[Customers]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

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
