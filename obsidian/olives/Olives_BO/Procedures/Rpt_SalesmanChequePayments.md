---
type: procedure
database: Olives_BO
name: Rpt_SalesmanChequePayments
schema: dbo
tags: [#backoffice, #billing, #reporting, #sales]
reads_from:
  - [[Checks]]
  - [[Customers]]
  - Fun_GetCashInvoicesReceipts
  - Fun_GetCompanyBranchesByUser
  - [[Receipts]]
  - [[SalesPersons]]
  - [[SalesPersonsGroups]]
  - [[TransactionsTypes]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanChequePayments


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, Customers, Fun_GetCashInvoicesReceipts, Fun_GetCompanyBranchesByUser, Receipts, SalesPersons, SalesPersonsGroups, TransactionsTypes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromSalesman int
- @ToSalesman int
- @FromCustomer bigint
- @ToCustomer bigint
- @UserID nvarchar(50)=null
- @FromGroup int = 0
- @ToGroup int = 99999999
## Tables Read
- [[Checks]]
- [[Customers]]
- Fun_GetCashInvoicesReceipts
- Fun_GetCompanyBranchesByUser
- [[Receipts]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TransactionsTypes]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Checks]]
- [[Customers]]
- Fun_GetCashInvoicesReceipts
- Fun_GetCompanyBranchesByUser
- [[Receipts]]
- [[SalesPersons]]
- [[SalesPersonsGroups]]
- [[TransactionsTypes]]

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
