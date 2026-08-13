---
type: procedure
database: Olives_BO
name: Pro_SalesPersonItemsBalance
schema: dbo
tags: [#backoffice, #inventory, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
writes_to:
  - [[SalesPersonItemsBalance]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SalesPersonItemsBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Items, ItemsUnits, SalesPersonItemsBalance, SalesPersons. Writes SalesPersonItemsBalance. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @SalesPersonID int = 3003
- @ItemCode nvarchar (20)=null
- @ItemQuantity float =null
- @cmdType varchar(50)='Select All'
## Tables Read
- [[ClientsActive]]
- [[Items]]
- [[ItemsUnits]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
## Tables Written
- [[SalesPersonItemsBalance]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Items]]
- [[ItemsUnits]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]

**Tables Written**
- [[SalesPersonItemsBalance]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
