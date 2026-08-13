---
type: procedure
database: Olives_BO
name: OT_ImportReplacement
schema: dbo
tags: [#backoffice, #mobile]
reads_from:
  - [[ClientsActive]]
  - GetSalesman
  - Header
  - [[ItemsReplacementHeaders]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
  - [[ItemsReplacementDetails]]
  - [[ItemsReplacementHeaders]]
  - [[OT_ItemsReplacmentHF]]
  - [[TransactionsBatchsItemsInfo]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
called_by:
  - [[Pro_CalcSalespersonItemBalance]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportReplacement


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, GetSalesman, Header, ItemsReplacementHeaders, TransactionsHeaders, dbo. Writes ItemsReplacementDetails, ItemsReplacementHeaders, OT_ItemsReplacmentHF, TransactionsBatchsItemsInfo, TransactionsDetails, TransactionsHeaders. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[ClientsActive]]
- GetSalesman
- Header
- [[ItemsReplacementHeaders]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
- [[ItemsReplacementDetails]]
- [[ItemsReplacementHeaders]]
- [[OT_ItemsReplacmentHF]]
- [[TransactionsBatchsItemsInfo]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Callers
_None (no known callers)_
## Callees
- [[Pro_CalcSalespersonItemBalance]]
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- GetSalesman
- Header
- [[ItemsReplacementHeaders]]
- [[TransactionsHeaders]]
- dbo

**Tables Written**
- [[ItemsReplacementDetails]]
- [[ItemsReplacementHeaders]]
- [[OT_ItemsReplacmentHF]]
- [[TransactionsBatchsItemsInfo]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Callers**
- [[Pro_CalcSalespersonItemBalance]]

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
