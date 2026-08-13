---
type: procedure
database: Olives_BO
name: Pro_CurrenciesRate
schema: dbo
tags: [#backoffice]
reads_from:
  - [[Currencies]]
  - [[CurrenciesRate]]
writes_to:
  - [[CurrenciesRate]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CurrenciesRate


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Currencies, CurrenciesRate. Writes CurrenciesRate. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	=null
- @CurrencyID	smallint	=null
- @ExDate	smalldatetime	=null
- @ExRate	float	=null
- @EntryDate	datetime	=null
- @cmdType nvarchar(50) = null
## Tables Read
- [[Currencies]]
- [[CurrenciesRate]]
## Tables Written
- [[CurrenciesRate]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Currencies]]
- [[CurrenciesRate]]

**Tables Written**
- [[CurrenciesRate]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
