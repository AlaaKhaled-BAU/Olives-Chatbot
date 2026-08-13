---
type: procedure
database: Olives_BO
name: Pro_MMS_TaxType
schema: dbo
tags: [#backoffice, #billing, #legal, #mms, #reference]
reads_from:
  - [[MMS_TaxType]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_TaxType


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_TaxType. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompayID	smallint	= null
- @TaxTypeID	int	= null
- @Name	nvarchar(100)	= null
- @ForeignName	nvarchar(100)	= null
- @TaxPercent	float	= null
- @Reference1	nvarchar(100)	= null
- @Reference2	nvarchar(100)	= null
- @cmdType nvarchar(50)	= null
## Tables Read
- [[MMS_TaxType]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_TaxType]]

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
