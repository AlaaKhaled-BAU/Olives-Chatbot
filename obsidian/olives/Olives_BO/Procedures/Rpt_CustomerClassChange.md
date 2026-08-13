---
type: procedure
database: Olives_BO
name: Rpt_CustomerClassChange
schema: dbo
tags: [#backoffice, #customer, #reference, #reporting]
reads_from:
  - [[Customers]]
  - [[CustomersClasses]]
  - Fun_GetCompanyBranchesByUser
  - [[SalesPersons]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomerClassChange


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersClasses, Fun_GetCompanyBranchesByUser, SalesPersons, dbo. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromCust bigint
- @Tocust bigint
- @UserID nvarchar(50)
## Tables Read
- [[Customers]]
- [[CustomersClasses]]
- Fun_GetCompanyBranchesByUser
- [[SalesPersons]]
- `dbo`
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersClasses]]
- Fun_GetCompanyBranchesByUser
- [[SalesPersons]]
- dbo

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
