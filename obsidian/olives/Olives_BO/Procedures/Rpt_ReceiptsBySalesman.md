---
type: procedure
database: Olives_BO
name: Rpt_ReceiptsBySalesman
schema: dbo
tags: [#backoffice, #billing, #reporting, #sales]
reads_from:
  - [[Checks]]
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersClasses]]
  - Fun_GetCompanyBranchesByUser
  - [[Receipts]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_ReceiptsBySalesman


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Checks, ClientsActive, Customers, CustomersClasses, Fun_GetCompanyBranchesByUser, Receipts, SalesPersons, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromSalesman int
- @ToSalesman int
- @UserID nvarchar(50)
- @FromCustType int
- @ToCustType int
- @WithReturnedChecks bit = 0
- @FromLocation int =null
- @ToLocation int =null
## Tables Read
- [[Checks]]
- [[ClientsActive]]
- [[Customers]]
- [[CustomersClasses]]
- Fun_GetCompanyBranchesByUser
- [[Receipts]]
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
- [[Checks]]
- [[ClientsActive]]
- [[Customers]]
- [[CustomersClasses]]
- Fun_GetCompanyBranchesByUser
- [[Receipts]]
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
