---
type: procedure
database: Olives_BO
name: Rpt_RouteSummaryBySalesmanGetImagesVisit
schema: dbo
tags: [#reporting]
reads_from:
writes_to:
called_by:
support_relevance: low
last_verified: 2026-08-05
status: documented
---
# Rpt_RouteSummaryBySalesmanGetImagesVisit

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — standalone procedure. See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @CustomerID bigint
- @SalespersonID int
- @VouDate date
- @LoginTime time
- @LogoutTime time
## Tables Read
_None_
## Tables Written
_None_
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_CustGalaryImages|OT_CustGalaryImages]]
## Callers
_None_
## Callees
_None_
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
