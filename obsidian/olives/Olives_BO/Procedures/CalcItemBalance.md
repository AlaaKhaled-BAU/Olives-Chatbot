---
type: procedure
database: Olives_BO
name: CalcItemBalance
schema: dbo
tags: [#backoffice, #inventory]
reads_from:
  - [[SalesPersonItemsBalance]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
  - [[SalesPersonItemsBalance]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# CalcItemBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersonItemsBalance, TransactionsDetails, TransactionsHeaders. Writes SalesPersonItemsBalance. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo  Smallint
- @SalesmanNo int
## Tables Read
- [[SalesPersonItemsBalance]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
- [[SalesPersonItemsBalance]]
## Callers
- [[Pro_Auto_Unload]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersonItemsBalance]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
- [[SalesPersonItemsBalance]]

**Callers**
_None_

**Callees**
- [[Pro_Auto_Unload]]


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
