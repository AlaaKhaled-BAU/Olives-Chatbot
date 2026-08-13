---
type: procedure
database: Olives_BO
name: Rpt_QrVisitsVerification
schema: dbo
tags: [#reporting]
reads_from:
  - Customers
  - LogActionTransaction
  - RoutesInformation
  - SalesPersons
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_QrVisitsVerification

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 4 table(s); calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompNo smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromSalesmanNo int
- @ToSalesmanNo int
- @UserID nvarchar(50)
## Tables Read
- [[Customers]]
- [[LogActionTransaction]]
- [[RoutesInformation]]
- [[SalesPersons]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_GetCompanyBranchesByUser`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
