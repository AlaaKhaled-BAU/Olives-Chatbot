---
type: procedure
database: Olives_BO
name: Rpt_InvoiceByCustomerAndSalesmanAndItem
schema: dbo
tags: [#backoffice, #billing, #customer, #inventory, #reporting, #sales]
reads_from:
  - [[Items]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_InvoiceByCustomerAndSalesmanAndItem


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromItem varchar(100) = '0'
- @ToItem varchar(100)= 'zzzzzzzzzzzzz'
- @FromSalesman int=1
- @ToSalesman int=999999
- @FromCustomer bigint=1
- @ToCustomer bigint =999999999999
## Tables Read
- [[Items]]
- [[SalesPersons]]
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
- [[Items]]
- [[SalesPersons]]
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
