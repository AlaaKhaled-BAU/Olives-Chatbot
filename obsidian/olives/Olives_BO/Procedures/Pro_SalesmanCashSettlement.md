---
type: procedure
database: Olives_BO
name: Pro_SalesmanCashSettlement
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[Currencies]]
  - Fun_GetReceiptsChecksTotal
  - [[Receipts]]
  - [[SalesPersons]]
  - [[SalesmanCashSettlement]]
writes_to:
  - [[Receipts]]
  - [[SalesmanCashSettlement]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesmanCashSettlement


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Currencies, Fun_GetReceiptsChecksTotal, Receipts, SalesPersons, SalesmanCashSettlement. Writes Receipts, SalesmanCashSettlement. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo SmallInt = 2
- @CurrencyID Int = 1
- @SalesmanID Int = 97
- @TotAmount Float = NULL
- @PaidAmount Float = NULL
- @TrDate SmallDateTime = '2021-12-23'
- @CmdType Nvarchar(50) = 'SelectByID'
## Tables Read
- [[Currencies]]
- Fun_GetReceiptsChecksTotal
- [[Receipts]]
- [[SalesPersons]]
- [[SalesmanCashSettlement]]
## Tables Written
- [[Receipts]]
- [[SalesmanCashSettlement]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Currencies]]
- Fun_GetReceiptsChecksTotal
- [[Receipts]]
- [[SalesPersons]]
- [[SalesmanCashSettlement]]

**Tables Written**
- [[Receipts]]
- [[SalesmanCashSettlement]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
