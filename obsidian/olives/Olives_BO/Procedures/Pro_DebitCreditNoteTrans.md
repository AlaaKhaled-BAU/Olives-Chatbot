---
type: procedure
database: Olives_BO
name: Pro_DebitCreditNoteTrans
schema: dbo
tags: [#backoffice, #billing]
reads_from:
  - [[Customers]]
  - [[DebitCreditNoteTrans]]
  - [[SalesPersonTransactionsSerials]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - [[DebitCreditNoteTrans]]
  - [[OT_DebitCreditNoteTrans]]
  - [[SalesPersonTransactionsSerials]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_DebitCreditNoteTrans


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, DebitCreditNoteTrans, SalesPersonTransactionsSerials, SalesPersons, dbo. Writes DebitCreditNoteTrans, OT_DebitCreditNoteTrans, SalesPersonTransactionsSerials. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo SmallInt=1
- @VouYear SmallInt=2022
- @Customer BigInt=1
- @Salesman Int=1
- @VouType Int=1
- @VouNo Int=1
- @VouDate SmallDateTime = '2021-11-01'
- @InvNo Varchar(50) = null
- @InvAmount FLOAT=1
- @TotDisccount FLOAT=1
- @Tax FLOAT=1
- @NetDisccount FLOAT=1
- @Notes Nvarchar(200) = null
- @cmdType Nvarchar(50) = null
## Tables Read
- [[Customers]]
- [[DebitCreditNoteTrans]]
- [[SalesPersonTransactionsSerials]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- [[DebitCreditNoteTrans]]
- [[OT_DebitCreditNoteTrans]]
- [[SalesPersonTransactionsSerials]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[DebitCreditNoteTrans]]
- [[SalesPersonTransactionsSerials]]
- [[SalesPersons]]
- dbo

**Tables Written**
- [[DebitCreditNoteTrans]]
- [[OT_DebitCreditNoteTrans]]
- [[SalesPersonTransactionsSerials]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
