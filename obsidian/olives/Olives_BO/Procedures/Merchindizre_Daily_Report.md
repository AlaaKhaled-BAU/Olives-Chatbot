---
type: procedure
database: Olives_BO
name: Merchindizre_Daily_Report
schema: dbo
tags: [#reporting]
reads_from:
  - CustomerStockTacking
  - CustomerStockTackingDetails
  - Customers
  - Items
  - ItemsCategories
  - LogActionTransaction
  - SalesPersons
  - SurveySalesmans
  - SurveySalesmansAnswers
writes_to:
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Merchindizre_Daily_Report

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 9 table(s). See sections below for the full dependency map.
## Parameters
- @CompNo int
- @FromSalesMan int
- @ToSalesMan int
- @FromCustomer bigint
- @ToCustomer bigint
- @FromDate datetime
- @ToDate datetime
## Tables Read
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Customers]]
- [[Items]]
- [[ItemsCategories]]
- [[LogActionTransaction]]
- [[SalesPersons]]
- [[SurveySalesmans]]
- [[SurveySalesmansAnswers]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
