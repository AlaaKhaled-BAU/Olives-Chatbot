---
type: procedure
database: Olives_BO
name: Rpt_InvoiceReturnLink
schema: dbo
tags: [#reporting]
reads_from:
  - InvoiceReturnLink
  - Items
  - ItemsUnits
  - SalesPersons
  - TransactionsDetails
  - TransactionsHeaders
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_InvoiceReturnLink

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 6 table(s); calls 2 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @FromDate datetime
- @ToDate datetime
- @FromTransactionNo bigint
- @ToTransactionNo bigint
- @UserID nvarchar(50)
## Tables Read
- [[InvoiceReturnLink]]
- [[Items]]
- [[ItemsUnits]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_GetCompanyBranchesByUser`
- `GetItemOrgUnitQty`
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
