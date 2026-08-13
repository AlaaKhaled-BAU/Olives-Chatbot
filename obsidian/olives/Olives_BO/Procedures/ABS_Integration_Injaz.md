---
type: procedure
database: Olives_BO
name: ABS_Integration_Injaz
schema: dbo
tags: [#integration]
reads_from:
writes_to:
  - CustomerStatmentOfAccount
  - Customers
  - CustomersPaidTransList
  - CustomersTypes
  - InvoiceHistoryDF
  - InvoiceHistoryHF
  - Items
  - ItemsCategories
  - ItemsUnits
  - ItemsUnitsDetails
  - Positions
  - PriceListDetails
  - PriceLists
  - SalesPersons
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# ABS_Integration_Injaz

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — writes 14. See sections below for the full dependency map.
## Parameters
- @CompanyID nvarchar(50)
## Tables Read
_None_
## Tables Written
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersPaidTransList]]
- [[CustomersTypes]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[Positions]]
- [[PriceListDetails]]
- [[PriceLists]]
- [[SalesPersons]]
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
