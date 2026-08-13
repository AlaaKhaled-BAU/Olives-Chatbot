---
type: procedure
database: Olives_BO
name: Rpt_CollectedReceiptsByCompany
schema: dbo
tags: [#backoffice, #billing, #reporting]
reads_from:
  - [[Checks]]
  - [[Companies]]
  - [[CompanyBranches]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Fun_GetCompanyBranchesByUser
  - Fun_GetReceiptsChecksTotal
  - [[Receipts]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CollectedReceiptsByCompany


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, Companies, CompanyBranches, Customers, CustomersFinancialDetails, Fun_GetCompanyBranchesByUser, Fun_GetReceiptsChecksTotal, Receipts, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @FilteredCompanyID smallint
- @FromSales int=0
- @ToSales int=99999999
- @FromDate smalldatetime='2015-1-1'
- @ToDate smalldatetime='2020-1-1'
- @UserID nvarchar(50)='admin'
## Tables Read
- [[Checks]]
- [[Companies]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetCompanyBranchesByUser
- Fun_GetReceiptsChecksTotal
- [[Receipts]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Checks]]
- [[Companies]]
- [[CompanyBranches]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Fun_GetCompanyBranchesByUser
- Fun_GetReceiptsChecksTotal
- [[Receipts]]
- [[SalesPersons]]

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
