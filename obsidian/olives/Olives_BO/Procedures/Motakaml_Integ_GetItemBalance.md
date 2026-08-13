---
type: procedure
database: Olives_BO
name: Motakaml_Integ_GetItemBalance
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - [[CompanyBranches]]
  - OLIV
  - [[SalesPersons]]
  - [[TransactionsBatchsItemsInfo]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Motakaml_Integ_GetItemBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CompanyBranches, OLIV, SalesPersons, TransactionsBatchsItemsInfo, TransactionsDetails, TransactionsHeaders, dbo. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int = 1
- @SalesmanNo int = 1002
## Tables Read
- [[CompanyBranches]]
- OLIV
- [[SalesPersons]]
- [[TransactionsBatchsItemsInfo]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
_None_
## Callers
- [[OT_SendSalesmanData]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CompanyBranches]]
- OLIV
- [[SalesPersons]]
- [[TransactionsBatchsItemsInfo]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- dbo

**Tables Written**
_None_

**Callers**
_None_

**Callees**
- [[OT_SendSalesmanData]]


## When to Run This

Run when pulling data from an external API/system. Called during sync cycles or on-demand data refresh.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
