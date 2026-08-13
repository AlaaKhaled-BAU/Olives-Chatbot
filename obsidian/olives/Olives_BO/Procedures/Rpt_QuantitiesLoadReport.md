---
type: procedure
database: Olives_BO
name: Rpt_QuantitiesLoadReport
schema: dbo
tags: [#backoffice, #order, #reporting]
reads_from:
  - [[ClientsActive]]
  - [[Items]]
  - [[PriceListDetails]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_QuantitiesLoadReport


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Items, PriceListDetails, SalesPersons, TransactionsDetails, TransactionsHeaders, TransfersOrdersDetails, TransfersOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromItem varchar(100)
- @ToItem varchar(100)
- @FromSalesman int
- @ToSalesman int
- @UserID nvarchar(50)=null
- @FromPriceList varchar(100)
- @ToPriceList varchar(100)
## Tables Read
- [[ClientsActive]]
- [[Items]]
- [[PriceListDetails]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
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
- [[ClientsActive]]
- [[Items]]
- [[PriceListDetails]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
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
