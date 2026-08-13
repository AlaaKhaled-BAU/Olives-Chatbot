---
type: procedure
database: Olives_BO
name: Pro_Auto_Unload
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - AutoUnload
  - [[SalesPersonItemsBalance]]
  - [[SalesPersonTransactionsSerials]]
  - [[TransfersOrdersHeaders]]
writes_to:
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
called_by:
  - [[CalcItemBalance]]
support_relevance: high
last_verified: 2026-07-05
---
# Pro_Auto_Unload


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads AutoUnload, SalesPersonItemsBalance, SalesPersonTransactionsSerials, TransfersOrdersHeaders. Writes TransfersOrdersDetails, TransfersOrdersHeaders. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesmanNo int
## Tables Read
- AutoUnload
- [[SalesPersonItemsBalance]]
- [[SalesPersonTransactionsSerials]]
- [[TransfersOrdersHeaders]]
## Tables Written
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
- [[CalcItemBalance]]
## Impact / Dependencies

**Tables Read**
- AutoUnload
- [[SalesPersonItemsBalance]]
- [[SalesPersonTransactionsSerials]]
- [[TransfersOrdersHeaders]]

**Tables Written**
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]

**Callers**
- [[CalcItemBalance]]

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
