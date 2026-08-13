---
type: procedure
database: Olives_BO
name: Rpt_ChecksByStatus
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[Checks]]
  - [[Customers]]
  - [[CustomersClasses]]
  - Fun_GetCompanyBranchesByUser
  - Fun_ReturnCheckRemaining
  - [[Receipts]]
  - [[Receipts_PaidTransChecks]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_ChecksByStatus


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, Checks, Customers, CustomersClasses, Fun_GetCompanyBranchesByUser, Fun_ReturnCheckRemaining, Receipts, Receipts_PaidTransChecks, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int
- @FromSalesman int =null
- @ToSalesman int=null
- @FromCust bigint=null
- @ToCust bigint =null
- @FromCustClass int=null
- @ToCustClass int=null
- @FromDate Smalldatetime=null
- @ToDate Smalldatetime=null
- @CheckStatus smallint =null
- @CheckType smallint =null
- @RemainingAmount smallint =null, -- 1 = all , 2 = 0 , 3 = greater than 0
- @UserID nvarchar(50) = null
- @FromLocation int =null
- @ToLocation int =null
## Tables Read
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[Customers]]
- [[CustomersClasses]]
- Fun_GetCompanyBranchesByUser
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
