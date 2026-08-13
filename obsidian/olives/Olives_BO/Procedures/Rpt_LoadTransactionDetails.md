---
type: procedure
database: Olives_BO
name: Rpt_LoadTransactionDetails
schema: dbo
tags: [#backoffice, #order, #reporting]
reads_from:
  - [[Items]]
  - [[ItemsUnits]]
  - [[PriceListDetails]]
  - [[SalesPersons]]
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_LoadTransactionDetails


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, ItemsUnits, PriceListDetails, SalesPersons, TransfersOrdersDetails, TransfersOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID SMALLINT = 1
- @FromSalesPerson BIGINT = 0
- @ToSalesPerson INT = 999999
- @FromDate DATETIME = '2020-02-02'
- @ToDate DATETIME = '2024-08-15'
## Tables Read
- [[Items]]
- [[ItemsUnits]]
- [[PriceListDetails]]
- [[SalesPersons]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[ItemsUnits]]
- [[PriceListDetails]]
- [[SalesPersons]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]

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
