---
type: procedure
database: Olives_BO
name: Pro_CatalogMedia
schema: dbo
tags: [#backoffice, #log]
reads_from:
  - [[CatalogMedia]]
  - [[Items]]
writes_to:
  - [[CatalogMedia]]
  - [[Items]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CatalogMedia


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CatalogMedia, Items. Writes CatalogMedia, Items. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID int=null
- @PdfFileID int=null
- @VideoFileID int=null
- @FileType smallint=null
- @FileName varchar(max)=null
- @FilePath varchar(max)=null
- @ItemCode varchar(50)=null
- @cmdType varchar(50)=null
## Tables Read
- [[CatalogMedia]]
- [[Items]]
## Tables Written
- [[CatalogMedia]]
- [[Items]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CatalogMedia]]
- [[Items]]

**Tables Written**
- [[CatalogMedia]]
- [[Items]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
