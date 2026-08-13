---
type: procedure
database: Olives_BO
name: Tablet_GetPendingOrdersTotals
schema: dbo
tags: [#backoffice, #mobile, #order]
reads_from:
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[PendingOrdersDetails]]
  - [[PendingOrdersHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Tablet_GetPendingOrdersTotals


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads InvoiceHistoryDF, InvoiceHistoryHF, OrdersDetails, OrdersHeaders, PendingOrdersDetails, PendingOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @compno int=1
- @salesmanno int=3003
- @FromDate smalldatetime='2014-01-01'
- @ToDate Smalldatetime= '2023-04-03'
## Tables Read
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PendingOrdersDetails]]
- [[PendingOrdersHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[PendingOrdersdetails]]
- [[PendingOrdersheaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
