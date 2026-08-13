---
type: procedure
database: Olives_BO
name: Phenix_Sukhtian_Integ_GetItemsBalance
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - OPENJSON
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
  - [[Items]]
writes_to:
  - [[SalesPersonItemsBalance]]
called_by:
  - [[Phenix_Sukhtian_Integ_CloseSession]]
  - [[Phenix_Sukhtian_Integ_GetDataFromAPI]]
  - [[Phenix_Sukhtian_Integ_OpenSession]]
support_relevance: high
last_verified: 2026-07-05
---
# Phenix_Sukhtian_Integ_GetItemsBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads OPENJSON, SalesPersonItemsBalance, SalesPersons, Items. Writes SalesPersonItemsBalance. Invoked by 1 procedure(s). Calls 3 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
- @SalesmanNo int = 1
## Tables Read
- OPENJSON
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[Items]]
## Tables Written
- [[SalesPersonItemsBalance]]
## Callers
- [[OT_SendSalesmanData]]
## Callees
- [[Phenix_Sukhtian_Integ_CloseSession]]
- [[Phenix_Sukhtian_Integ_GetDataFromAPI]]
- [[Phenix_Sukhtian_Integ_OpenSession]]
## Impact / Dependencies

**Tables Read**
- OPENJSON
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[items]]

**Tables Written**
- [[SalesPersonItemsBalance]]

**Callers**
- [[Phenix_Sukhtian_Integ_CloseSession]]
- [[Phenix_Sukhtian_Integ_GetDataFromAPI]]
- [[Phenix_Sukhtian_Integ_OpenSession]]

**Callees**
- [[OT_SendSalesmanData]]


## When to Run This

Run when pulling data from an external API/system. Called during sync cycles or on-demand data refresh.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
