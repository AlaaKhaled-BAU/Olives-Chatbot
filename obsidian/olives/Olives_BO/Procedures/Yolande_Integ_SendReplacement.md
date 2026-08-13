---
type: procedure
database: Olives_BO
name: Yolande_Integ_SendReplacement
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - [[Customers]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
  - [[OT_ItemsReplacmentDF]]
  - [[OT_ItemsReplacmentHF]]
  - [[TransactionsHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Yolande_Integ_SendReplacement


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, SalesPersons, TransactionsHeaders, dbo. Writes OT_ItemsReplacmentDF, OT_ItemsReplacmentHF, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Customers]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
- [[OT_ItemsReplacmentDF]]
- [[OT_ItemsReplacmentHF]]
- [[TransactionsHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
- dbo

**Tables Written**
- [[OT_ItemsReplacmentDF]]
- [[OT_ItemsReplacmentHF]]
- [[TransactionsHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
