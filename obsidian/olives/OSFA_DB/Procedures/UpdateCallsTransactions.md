---
type: procedure
database: OSFA_DB
name: UpdateCallsTransactions
schema: dbo
tags: [#mobile]
reads_from:
  - `dbo`
writes_to:
  - CallsTransactions
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# UpdateCallsTransactions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the OSFA_DB database. Reads dbo. Writes CallsTransactions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @CallID bigint
- @Status int
- @ReplyNotes nvarchar(max)
- @InvoiceNo  nvarchar(max)
## Tables Read
- `dbo`
## Tables Written
- CallsTransactions
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dbo

**Tables Written**
- CallsTransactions

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-OSFA_DB|OSFA_DB MOC]]
