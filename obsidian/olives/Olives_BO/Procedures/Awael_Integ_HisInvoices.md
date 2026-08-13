---
type: procedure
database: Olives_BO
name: Awael_Integ_HisInvoices
schema: dbo
tags: [#backoffice, #billing, #integration]
reads_from:
  - [[BatchsItemsInfo]]
  - [[Customers]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - `dbo`
writes_to:
  - [[BatchsItemsInfo]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Awael_Integ_HisInvoices


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BatchsItemsInfo, Customers, InvoiceHistoryDF, InvoiceHistoryHF, Items, dbo. Writes BatchsItemsInfo, InvoiceHistoryDF, InvoiceHistoryHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- [[BatchsItemsInfo]]
- [[Customers]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- `dbo`
## Tables Written
- [[BatchsItemsInfo]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[BatchsItemsInfo]]
- [[Customers]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[Items]]
- dbo

**Tables Written**
- [[BatchsItemsInfo]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
