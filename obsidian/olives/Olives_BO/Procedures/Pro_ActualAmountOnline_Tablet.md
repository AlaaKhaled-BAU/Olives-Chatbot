---
type: procedure
database: Olives_BO
name: Pro_ActualAmountOnline_Tablet
schema: dbo
tags: [#backoffice, #mobile]
reads_from:
  - [[Currencies]]
  - Fun_GetReceiptsChecksTotal
  - [[Receipts]]
  - [[SalespersonsDailyCurrencyTotals]]
  - [[TransactionsHeaders]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ActualAmountOnline_Tablet


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Currencies, Fun_GetReceiptsChecksTotal, Receipts, SalespersonsDailyCurrencyTotals, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @SalesPersonID smallint=11
- @TrDate date = '2023-09-24'
## Tables Read
- [[Currencies]]
- Fun_GetReceiptsChecksTotal
- [[Receipts]]
- [[SalespersonsDailyCurrencyTotals]]
- [[TransactionsHeaders]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Currencies]]
- Fun_GetReceiptsChecksTotal
- [[Receipts]]
- [[SalespersonsDailyCurrencyTotals]]
- [[TransactionsHeaders]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
