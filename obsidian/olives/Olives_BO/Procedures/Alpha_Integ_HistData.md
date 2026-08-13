---
type: procedure
database: Olives_BO
name: Alpha_Integ_HistData
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[CustomerChqList]]
  - [[CustomerStatmentOfAccount]]
  - [[Customers]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[SalesOrderHistoryDF]]
  - [[SalesOrderHistoryHF]]
  - `dbo`
writes_to:
  - [[CustomerChqList]]
  - [[CustomerStatmentOfAccount]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - [[SalesOrderHistoryDF]]
  - [[SalesOrderHistoryHF]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_Integ_HistData


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CustomerChqList, CustomerStatmentOfAccount, Customers, InvoiceHistoryDF, InvoiceHistoryHF, SalesOrderHistoryDF, SalesOrderHistoryHF, dbo. Writes CustomerChqList, CustomerStatmentOfAccount, InvoiceHistoryDF, InvoiceHistoryHF, SalesOrderHistoryDF, SalesOrderHistoryHF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[CustomerChqList]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]
- `dbo`
## Tables Written
- [[CustomerChqList]]
- [[CustomerStatmentOfAccount]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CustomerChqList]]
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]
- dbo

**Tables Written**
- [[CustomerChqList]]
- [[CustomerStatmentOfAccount]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
