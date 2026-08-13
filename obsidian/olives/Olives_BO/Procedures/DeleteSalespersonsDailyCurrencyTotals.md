---
type: procedure
database: Olives_BO
name: DeleteSalespersonsDailyCurrencyTotals
schema: dbo
tags: [#backoffice, #sales]
reads_from:
  - [[SalespersonsDailyCurrencyTotals]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# DeleteSalespersonsDailyCurrencyTotals


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalespersonsDailyCurrencyTotals. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @SalesPersonID smallint
- @TrDateTime Date
## Tables Read
- [[SalespersonsDailyCurrencyTotals]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalespersonsDailyCurrencyTotals]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Cleanup procedure — removes stale or temporary data. Run during maintenance windows only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
