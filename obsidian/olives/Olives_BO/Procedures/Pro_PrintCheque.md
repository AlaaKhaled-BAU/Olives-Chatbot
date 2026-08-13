---
type: procedure
database: Olives_BO
name: Pro_PrintCheque
schema: dbo
tags: [#backoffice]
reads_from:
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_PrintCheque


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=1
- @PayeeName nvarchar(50)='asd'
- @ChequeDate DateTime ='07-28-2024'
- @Amount float =44
- @Note nvarchar(50)='mmmmmm'
- @Crossing nvarchar(50)  ='0'
## Tables Read
_None_
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
_None_

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
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]

- [[Pro_SalesPersonNewCustomersTargets]]
- [[Pro_CompetitveItemsDataHF]]
- [[Pro_MMS_Diagnostic]]
- [[Glossary]]
