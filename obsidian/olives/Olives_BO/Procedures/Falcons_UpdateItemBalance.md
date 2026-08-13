---
type: procedure
database: Olives_BO
name: Falcons_UpdateItemBalance
schema: dbo
tags: [#backoffice, #inventory]
reads_from:
writes_to:
called_by:
  - [[Falcons_GetItemBalance]]
support_relevance: high
last_verified: 2026-07-05
---
# Falcons_UpdateItemBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
- @SalesmanNo int
## Tables Read
_None_
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
- [[Falcons_GetItemBalance]]
## Impact / Dependencies

**Tables Read**
_None_

**Tables Written**
_None_

**Callers**
- [[Falcons_GetItemBalance]]

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
- [[MMS_ItemsCategories]]
- [[IssueItemsDetails]]
- [[SalespersonCustStockItemsAssignment]]
