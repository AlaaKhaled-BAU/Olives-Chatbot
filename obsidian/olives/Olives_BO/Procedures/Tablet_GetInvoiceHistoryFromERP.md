---
type: procedure
database: Olives_BO
name: Tablet_GetInvoiceHistoryFromERP
schema: dbo
tags: [#backoffice, #billing, #integration, #log, #mobile]
reads_from:
  - [[ClientsActive]]
  - [[InvoiceHistoryDF]]
  - [[InvoiceHistoryHF]]
  - OPENJSON
writes_to:
called_by:
  - [[Niroukh_Integ_GetDataFromAPI]]
support_relevance: high
last_verified: 2026-07-05
---
# Tablet_GetInvoiceHistoryFromERP


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, InvoiceHistoryDF, InvoiceHistoryHF, OPENJSON. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=2
- @InvYear int =4
- @InvNo bigint=1844
- @Header bit=1
## Tables Read
- [[ClientsActive]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- OPENJSON
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[Niroukh_Integ_GetDataFromAPI]]
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[InvoiceHistoryDF]]
- [[InvoiceHistoryHF]]
- OPENJSON

**Tables Written**
_None_

**Callers**
- [[Niroukh_Integ_GetDataFromAPI]]

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
