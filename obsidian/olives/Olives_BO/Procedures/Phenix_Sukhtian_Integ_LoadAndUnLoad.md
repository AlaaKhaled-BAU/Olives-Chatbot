---
type: procedure
database: Olives_BO
name: Phenix_Sukhtian_Integ_LoadAndUnLoad
schema: dbo
tags: [#backoffice, #integration, #order]
reads_from:
  - Curs_Vou
  - [[IntegrationErrorLog]]
  - [[Items]]
  - OPENJSON
  - [[SalesPersons]]
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
writes_to:
  - [[TransfersOrdersHeaders]]
called_by:
  - [[Phenix_Sukhtian_Integ_CloseSession]]
  - [[Phenix_Sukhtian_Integ_GetDataFromAPI]]
  - [[Phenix_Sukhtian_Integ_OpenSession]]
support_relevance: high
last_verified: 2026-07-05
---
# Phenix_Sukhtian_Integ_LoadAndUnLoad


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Curs_Vou, IntegrationErrorLog, Items, OPENJSON, SalesPersons, TransfersOrdersDetails, TransfersOrdersHeaders. Writes TransfersOrdersHeaders. Calls 3 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
## Tables Read
- Curs_Vou
- [[IntegrationErrorLog]]
- [[Items]]
- OPENJSON
- [[SalesPersons]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
## Tables Written
- [[TransfersOrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
- [[Phenix_Sukhtian_Integ_CloseSession]]
- [[Phenix_Sukhtian_Integ_GetDataFromAPI]]
- [[Phenix_Sukhtian_Integ_OpenSession]]
## Impact / Dependencies

**Tables Read**
- Curs_Vou
- [[IntegrationErrorLog]]
- [[Items]]
- OPENJSON
- [[SalesPersons]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]

**Tables Written**
- [[TransfersOrdersHeaders]]

**Callers**
- [[Phenix_Sukhtian_Integ_CloseSession]]
- [[Phenix_Sukhtian_Integ_GetDataFromAPI]]
- [[Phenix_Sukhtian_Integ_OpenSession]]

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
