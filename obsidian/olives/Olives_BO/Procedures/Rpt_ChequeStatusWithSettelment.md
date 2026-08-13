---
type: procedure
database: Olives_BO
name: Rpt_ChequeStatusWithSettelment
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[Checks]]
  - [[Customers]]
  - [[CustomersClasses]]
  - Fun_GetCompanyBranchesByUser
  - Fun_ReturnCheckClosed
  - Fun_ReturnCheckRemaining
  - [[Receipts]]
  - [[Receipts_PaidTransChecks]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_ChequeStatusWithSettelment


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, Checks, Customers, CustomersClasses, Fun_GetCompanyBranchesByUser, Fun_ReturnCheckClosed, Fun_ReturnCheckRemaining, Receipts, Receipts_PaidTransChecks, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int  =1
- @FromSalesman int =1
- @ToSalesman int=99999
- @FromCust bigint=1
- @ToCust bigint =999999999999
- @FromCustClass int=1
- @ToCustClass int=99999999
- @FromDate Smalldatetime=null
- @ToDate Smalldatetime=null
- @UserID nvarchar(50) = 'admin'
- @FromLocation int =1
- @ToLocation int =9999999
- @CheckStatus smallint =null
- @CheckType smallint =null
## Tables Read
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[Customers]]
- [[CustomersClasses]]
- Fun_GetCompanyBranchesByUser
- Fun_ReturnCheckClosed
- Fun_ReturnCheckRemaining
- [[Receipts]]
- [[Receipts_PaidTransChecks]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[Customers]]
- [[CustomersClasses]]
- Fun_GetCompanyBranchesByUser
- Fun_ReturnCheckClosed
- Fun_ReturnCheckRemaining
- [[Receipts]]
- [[Receipts_PaidTransChecks]]
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
