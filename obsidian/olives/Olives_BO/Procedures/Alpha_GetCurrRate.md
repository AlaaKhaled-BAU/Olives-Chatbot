---
type: procedure
database: Olives_BO
name: Alpha_GetCurrRate
schema: dbo
tags: [#backoffice]
reads_from:
  - InvCategCodes
  - InvItemsMF
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_GetCurrRate


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads InvCategCodes, InvItemsMF. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo	smallint
- @ItemNo nvarchar(100)
- @ExRate float output
## Tables Read
- InvCategCodes
- InvItemsMF
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- InvCategCodes
- InvItemsMF

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Glossary]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
