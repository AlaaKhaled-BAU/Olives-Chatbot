---
type: procedure
database: Olives_BO
name: JoTaxValidation
schema: dbo
tags: [#backoffice, #billing, #legal]
reads_from:
  - Fun_GetInvoiceTotalAmount
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# JoTaxValidation


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_GetInvoiceTotalAmount. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @Invoices dbo.JoTaxInvoiceTableType READONLY
- @CompNo int=1
## Tables Read
- Fun_GetInvoiceTotalAmount
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Fun_GetInvoiceTotalAmount

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
