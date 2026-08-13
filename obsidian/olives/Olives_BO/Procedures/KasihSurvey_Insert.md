---
type: procedure
database: Olives_BO
name: KasihSurvey_Insert
schema: dbo
tags: [#backoffice, #survey]
reads_from:
  - [[KasihSurvey]]
writes_to:
  - [[KasihSurvey]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# KasihSurvey_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads KasihSurvey. Writes KasihSurvey. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CmdType nvarchar(100) = ''
- @AutoID numeric(30,0) = null
- @CustomerName nvarchar (500) = null
- @CustomerImage image = null
- @CustomerImage1 image = null
- @CustomerImage2 image = null
- @CustomerImage3 image = null
- @CustomerImage4 image = null
- @ShelfImageBefore image = null
- @ShelfImageBefore1 image = null
- @ShelfImageBefore2 image = null
- @ShelfImageBefore3 image = null
- @ShelfImageBefore4 image = null
- @ShelfImageAfter image = null
- @ShelfImageAfter1 image = null
- @ShelfImageAfter2 image = null
- @ShelfImageAfter3 image = null
- @ShelfImageAfter4 image = null
- @ExistingPlace nvarchar (500) = null
- @Notes nvarchar (max) = null
- @ItemAvailability nvarchar (500) = null
- @ItemMovement nvarchar (500) = null
- @NeedOrder nvarchar (500) = null
- @ItemShownByTransmed nvarchar (500) = null
- @UpdateCustomerImage bit = null
- @UpdateCustomerImage1 bit = null
- @UpdateCustomerImage2 bit = null
- @UpdateCustomerImage3 bit = null
- @UpdateCustomerImage4 bit = null
- @UpdateBeforeImage4 bit = null
- @UpdateBeforeImage1 bit = null
- @UpdateBeforeImage2 bit = null
- @UpdateBeforeImage3 bit = null
- @UpdateBeforeImage bit = null
- @UpdateAfterImage bit = null
- @UpdateAfterImage1 bit = null
- @UpdateAfterImage2 bit = null
- @UpdateAfterImage3 bit = null
- @UpdateAfterImage4 bit = null
- @ErrNo SmallInt = 0 Output
## Tables Read
- [[KasihSurvey]]
## Tables Written
- [[KasihSurvey]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[KasihSurvey]]

**Tables Written**
- [[KasihSurvey]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
