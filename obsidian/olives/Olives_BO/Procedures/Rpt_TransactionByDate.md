---
type: procedure
database: Olives_BO
name: Rpt_TransactionByDate
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - Fun_GetCompanyBranchesByUser
  - Fun_ReCalcTransactionAmounts
  - [[Items]]
  - [[ItemsUnits]]
  - [[Locations]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[TransactionsTypes]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_TransactionByDate


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, Fun_GetCompanyBranchesByUser, Fun_ReCalcTransactionAmounts, Items, ItemsUnits, Locations, SalesPersons, TransactionsDetails, TransactionsHeaders, TransactionsTypes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FromInvNo bigint=1
- @ToInvNo bigint=1300300061
- @InvYear int=2025
- @FromType int=1
- @ToType int=1
- @FromDate smalldatetime='2025-01-01'
- @ToDate smalldatetime='2025-12-31'
- @FromSalesman int=0
- @ToSalesman int=9999999
- @UserID nvarchar(50)='admin'
- @InvType smallint = -1
- @FromCustomer bigint = 0
- @ToCustomer bigint = 9999999999999
- @Approved bit = null
- @FromApproveDate smalldatetime = null
- @ToApproveDate smalldatetime = null
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- Fun_GetCompanyBranchesByUser
- Fun_ReCalcTransactionAmounts
- [[Items]]
- [[ItemsUnits]]
- [[Locations]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]
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
- Fun_ReCalcTransactionAmounts
- [[Items]]
- [[ItemsUnits]]
- [[Locations]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
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
