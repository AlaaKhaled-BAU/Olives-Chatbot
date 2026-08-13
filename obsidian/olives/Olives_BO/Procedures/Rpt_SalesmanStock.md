---
type: procedure
database: Olives_BO
name: Rpt_SalesmanStock
schema: dbo
tags: [#backoffice, #inventory, #reporting, #sales]
reads_from:
  - [[Items]]
  - [[PriceListDetails]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesmanStock


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, PriceListDetails, TransactionsDetails, TransactionsHeaders, TransfersOrdersDetails, TransfersOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @ToDate smalldatetime='2025-1-1'
- @FromSalesman int=0
- @ToSalesman int=999999
- @FromItem nvarchar(100) = '0'
- @ToItem nvarchar(100) = 'zzzzzzzzz'
## Tables Read
- [[Items]]
- [[PriceListDetails]]
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
- [[Items]]
- [[PriceListDetails]]
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
