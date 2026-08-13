---
type: procedure
database: Olives_BO
name: VoidInvoiceAsReturn
schema: dbo
tags: [#backoffice, #billing, #order]
reads_from:
  - [[SalesPersonTransactionsSerials]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
  - [[OT_InvoiceDF]]
  - [[OT_InvoiceHF]]
  - [[OT_InvoiceReturnLink]]
  - [[TransactionsHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# VoidInvoiceAsReturn


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersonTransactionsSerials, TransactionsHeaders, dbo. Writes OT_InvoiceDF, OT_InvoiceHF, OT_InvoiceReturnLink, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
- @TrTypeID smallint=1
- @TrTypeYear smallint=2025
- @TrTypeNo int=1300300074
## Tables Read
- [[SalesPersonTransactionsSerials]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
- [[OT_InvoiceDF]]
- [[OT_InvoiceHF]]
- [[OT_InvoiceReturnLink]]
- [[TransactionsHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersonTransactionsSerials]]
- [[TransactionsHeaders]]
- dbo

**Tables Written**
- [[OT_InvoiceDF]]
- [[OT_InvoiceHF]]
- [[OT_InvoiceReturnLink]]
- [[TransactionsHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
