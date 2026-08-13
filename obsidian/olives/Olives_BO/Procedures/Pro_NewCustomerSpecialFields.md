---
type: procedure
database: Olives_BO
name: Pro_NewCustomerSpecialFields
schema: dbo
tags: [#backoffice, #customer]
reads_from:
  - [[NewCustomerSpecialFields_Def]]
writes_to:
  - [[NewCustomerSpecialFields_Def]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_NewCustomerSpecialFields


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads NewCustomerSpecialFields_Def. Writes NewCustomerSpecialFields_Def. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @cmdType Varchar(50)=null
- @FieldID int = null
- @FieldCaption Varchar(100) = null
- @FieldForeignCaption Varchar(100) = null
- @IsRequired bit = null
## Tables Read
- [[NewCustomerSpecialFields_Def]]
## Tables Written
- [[NewCustomerSpecialFields_Def]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[NewCustomerSpecialFields_Def]]

**Tables Written**
- [[NewCustomerSpecialFields_Def]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
