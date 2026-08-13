---
type: procedure
database: Olives_BO
name: Pro_ItemBarcodes
schema: dbo
tags: [#backoffice, #inventory, #reference]
reads_from:
  - `dbo`
writes_to:
  - [[ItemsBarcodes]]
  - [[ItemsUnits]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ItemBarcodes


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads dbo. Writes ItemsBarcodes, ItemsUnits. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @ItemNo nvarchar (100) = '0000000552'
- @Barcode nvarchar (200)=null
- @UnitCode nvarchar (100)='Test66'
- @UnitName nvarchar (100)='Test66'
- @BarcodeAutoID bigInt=null
- @IsSuspended bit =null
- @cmdType varchar(50)='Select All Units Item'
## Tables Read
- `dbo`
## Tables Written
- [[ItemsBarcodes]]
- [[ItemsUnits]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- dbo

**Tables Written**
- [[ItemsBarcodes]]
- [[ItemsUnits]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
