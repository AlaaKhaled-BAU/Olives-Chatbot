---
type: procedure
database: Olives_BO
name: Pro_SoftReportOnline
schema: dbo
tags: [#reporting]
reads_from:
  - Customers
  - CustomersFinancialDetails
  - Items
  - ItemsCategories
  - ItemsUnits
  - OrdersDetails
  - OrdersHeaders
  - SalesPersons
  - TransactionsDetails
  - TransactionsHeaders
writes_to:
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Pro_SoftReportOnline

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 10 table(s). See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @FromDate datetime
- @ToDate datetime
- @SalesmanNo int
- @FromSalesmanNo int
- @CmdType nvarchar(200)
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Cross-DB Tables
References tables in **OSFA_DB** (qualified as `OSFA_DB.dbo.*`):
- [[OSFA_DB/Tables/OT_ActionLog|OT_ActionLog]]
## Callers
_None_
## Callees
_None_
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
