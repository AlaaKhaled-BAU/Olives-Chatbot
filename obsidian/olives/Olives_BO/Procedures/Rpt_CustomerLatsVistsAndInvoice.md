---
type: procedure
database: Olives_BO
name: Rpt_CustomerLatsVistsAndInvoice
schema: dbo
tags: [#backoffice, #billing, #customer, #reporting]
reads_from:
  - [[Customers]]
  - [[LogActionTransaction]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomerLatsVistsAndInvoice


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, LogActionTransaction, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint =1
- @FromCustomer bigint =0
- @ToCustomer bigint = 99999999999999
## Tables Read
- [[Customers]]
- [[LogActionTransaction]]
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
- [[LogActionTransaction]]
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
