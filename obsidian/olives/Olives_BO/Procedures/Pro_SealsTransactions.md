---
type: procedure
database: Olives_BO
name: Pro_SealsTransactions
schema: dbo
tags: [#backoffice]
reads_from:
  - [[SalesPersons]]
  - [[SealsTransactions]]
writes_to:
  - [[SealsTransactions]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SealsTransactions


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalesPersons, SealsTransactions. Writes SealsTransactions. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID SMALLINT=null
- @SalespersonID INT = null
- @TrDateTime SmallDateTime = null
- @SealNo1 VARCHAR(100)=null
- @SealNo2 VARCHAR(100)=null
- @cmdtype VARCHAR(60)=null
## Tables Read
- [[SalesPersons]]
- [[SealsTransactions]]
## Tables Written
- [[SealsTransactions]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalesPersons]]
- [[SealsTransactions]]

**Tables Written**
- [[SealsTransactions]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
