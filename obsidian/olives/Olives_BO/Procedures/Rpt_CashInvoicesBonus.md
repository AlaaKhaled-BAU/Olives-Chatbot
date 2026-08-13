---
type: procedure
database: Olives_BO
name: Rpt_CashInvoicesBonus
schema: dbo
tags: [#backoffice, #billing, #reporting]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - Fun_GetCompanyBranchesByUser
  - [[Items]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CashInvoicesBonus


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, Fun_GetCompanyBranchesByUser, Items, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID Smallint =1
- @FromDate SmallDateTime ='2021-10-01'
- @ToDate SmallDateTime ='2021-11-29'
- @FromSales int =1
- @ToSales int =9999
- @FromCust BigInt =1
- @ToCust BigInt =9999
- @UserID Nvarchar(50) = 'admin'
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- Fun_GetCompanyBranchesByUser
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
- [[ClientsActive]]
- [[Customers]]
- Fun_GetCompanyBranchesByUser
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
