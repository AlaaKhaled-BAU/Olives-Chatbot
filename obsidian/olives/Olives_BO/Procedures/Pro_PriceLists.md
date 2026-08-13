---
type: procedure
database: Olives_BO
name: Pro_PriceLists
schema: dbo
tags: [#backoffice, #billing]
reads_from:
  - [[PriceLists]]
writes_to:
  - [[PriceLists]]
called_by:
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - PriceList-Management
---
# Pro_PriceLists


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads PriceLists. Writes PriceLists. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID smallint = null
- @Name nvarchar (200)=null
- @StartDate smalldatetime =null
- @EndDate smalldatetime =null
- @Notes nvarchar (200)=null
- @IsSuspended bit = null
- @CurrencyID smallint = null
- @cmdType varchar(50)=null
## Tables Read
- [[PriceLists]]
## Tables Written
- [[PriceLists]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[PriceLists]]

**Tables Written**
- [[PriceLists]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
