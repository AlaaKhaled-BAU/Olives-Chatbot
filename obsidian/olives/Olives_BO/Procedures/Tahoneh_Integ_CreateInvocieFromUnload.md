---
type: procedure
database: Olives_BO
name: Tahoneh_Integ_CreateInvocieFromUnload
schema: dbo
tags: [#backoffice, #integration, #legal, #order]
reads_from:
  - Cur_HF
  - [[SalesPersons]]
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
  - `dbo`
writes_to:
  - [[OT_InvoiceDF]]
  - [[OT_InvoiceHF]]
  - [[TransfersOrdersHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Tahoneh_Integ_CreateInvocieFromUnload


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Cur_HF, SalesPersons, TransfersOrdersDetails, TransfersOrdersHeaders, dbo. Writes OT_InvoiceDF, OT_InvoiceHF, TransfersOrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint = 1
## Tables Read
- Cur_HF
- [[SalesPersons]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
- `dbo`
## Tables Written
- [[OT_InvoiceDF]]
- [[OT_InvoiceHF]]
- [[TransfersOrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Cur_HF
- [[SalesPersons]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
- dbo

**Tables Written**
- [[OT_InvoiceDF]]
- [[OT_InvoiceHF]]
- [[TransfersOrdersHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
