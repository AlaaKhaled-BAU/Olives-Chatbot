---
type: procedure
database: Olives_BO
name: Rpt_CheckStatusDetails
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Banks]]
  - [[Branches]]
  - [[Checks]]
  - [[Customers]]
  - Fun_GetCompanyBranchesByUser
  - [[Receipts]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CheckStatusDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, Branches, Checks, Customers, Fun_GetCompanyBranchesByUser, Receipts, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = null
- @UserID nvarchar(50)=NULL @Checks_Type [dbo].[Checks_Type] readonly
## Tables Read
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[Customers]]
- Fun_GetCompanyBranchesByUser
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
- [[Banks]]
- [[Branches]]
- [[Checks]]
- [[Customers]]
- Fun_GetCompanyBranchesByUser
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
