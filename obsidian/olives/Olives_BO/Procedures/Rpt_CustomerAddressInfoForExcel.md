---
type: procedure
database: Olives_BO
name: Rpt_CustomerAddressInfoForExcel
schema: dbo
tags: [#reporting]
reads_from:
  - Customers
  - CustomersFinancialDetails
  - SalesPersons
writes_to:
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Rpt_CustomerAddressInfoForExcel

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 3 table(s). See sections below for the full dependency map.
## Parameters
- @CompnyID smallint
- @FromCustomer bigint
- @ToCustomer bigint
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[SalesPersons]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Run when the corresponding report is requested in the UI; supports the listed parameters for filtering.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
