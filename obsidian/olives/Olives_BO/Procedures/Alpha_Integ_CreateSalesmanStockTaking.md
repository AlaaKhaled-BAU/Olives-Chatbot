---
type: procedure
database: Olives_BO
name: Alpha_Integ_CreateSalesmanStockTaking
schema: dbo
tags: [#backoffice, #integration, #inventory, #sales]
reads_from:
  - Cur_HF
  - [[SalesPersonStockTacking]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[OT_InvoiceDF]]
  - [[OT_InvoiceHF]]
  - [[SalesPersonStockTacking]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_Integ_CreateSalesmanStockTaking


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Cur_HF, SalesPersonStockTacking, SalesPersons, dbo. Writes OT_InvoiceDF, OT_InvoiceHF, SalesPersonStockTacking. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
## Tables Read
- Cur_HF
- [[SalesPersonStockTacking]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[OT_InvoiceDF]]
- [[OT_InvoiceHF]]
- [[SalesPersonStockTacking]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Cur_HF
- [[SalesPersonStockTacking]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[OT_InvoiceDF]]
- [[OT_InvoiceHF]]
- [[SalesPersonStockTacking]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
