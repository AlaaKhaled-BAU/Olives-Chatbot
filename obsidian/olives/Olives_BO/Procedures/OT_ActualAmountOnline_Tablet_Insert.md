---
type: procedure
database: Olives_BO
name: OT_ActualAmountOnline_Tablet_Insert
schema: dbo
tags: [#backoffice, #mobile]
reads_from:
  - [[SalespersonsDailyCurrencyTotals]]
writes_to:
  - [[SalespersonsDailyCurrencyTotals]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ActualAmountOnline_Tablet_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SalespersonsDailyCurrencyTotals. Writes SalespersonsDailyCurrencyTotals. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @SalesPersonID smallint
- @TrDateTime datetime
- @CurrencyID smallint
- @ActualAmount float	= null
- @SysCashAmount float	= null
- @ErrNo SmallInt Output
## Tables Read
- [[SalespersonsDailyCurrencyTotals]]
## Tables Written
- [[SalespersonsDailyCurrencyTotals]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SalespersonsDailyCurrencyTotals]]

**Tables Written**
- [[SalespersonsDailyCurrencyTotals]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
