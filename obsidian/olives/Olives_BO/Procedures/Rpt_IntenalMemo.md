---
type: procedure
database: Olives_BO
name: Rpt_IntenalMemo
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[IntenalMemoApprove]]
  - [[InternalMemo]]
  - [[SalesPersons]]
  - [[Users]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_IntenalMemo


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads IntenalMemoApprove, InternalMemo, SalesPersons, Users. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = 1
- @FromDate datetime
- @ToDate datetime
- @FromSalesman int
- @ToSalesman int
- @FromTransactionNo int =null
- @ToTransactionNo int=null
- @UserID nvarchar(50)
## Tables Read
- [[IntenalMemoApprove]]
- [[InternalMemo]]
- [[SalesPersons]]
- [[Users]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[IntenalMemoApprove]]
- [[InternalMemo]]
- [[SalesPersons]]
- [[users]]

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
