---
type: procedure
database: Olives_BO
name: Rpt_CompareCustSalesByCategAndTargetRef
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[CustomerTargetsDetails]]
  - [[Customers]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - [[SalesPersons]]
  - [[TargetsReferences]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CompareCustSalesByCategAndTargetRef


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerTargetsDetails, Customers, InvoiceHistoryDF, InvoiceHistoryHF, Items, SalesPersons, TargetsReferences, TransactionsDetails, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
- @TrYear smallint = 2023
- @TrMonth smallint = 2
- @FromSalesman int = 29
- @ToSalesman int = 29
- @FromTarget int = 0
- @ToTarget int = 9999
- @FromCust bigint = 66
- @ToCust bigint = 66
- @FromCateg nvarchar(50) = '0'
- @ToCateg nvarchar(50) = 'z'
## Tables Read
- [[CustomerTargetsDetails]]
- [[Customers]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[SalesPersons]]
- [[TargetsReferences]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerTargetsDetails]]
- [[Customers]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[SalesPersons]]
- [[TargetsReferences]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

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
