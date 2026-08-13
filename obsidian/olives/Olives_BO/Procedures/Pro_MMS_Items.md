---
type: procedure
database: Olives_BO
name: Pro_MMS_Items
schema: dbo
tags: [#backoffice, #inventory, #mms]
reads_from:
  - [[MMS_Items]]
writes_to:
  - [[MMS_Items]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_Items


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_Items. Writes MMS_Items. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint = null
- @ItemNo	nvarchar(100)	= null
- @Name	nvarchar(500)	= null
- @ForeignName	nvarchar(500)	= null
- @ItemType	int	= null
- @CategoryID	int	= null
- @UnitPrice	float	= null
- @Barcode	nvarchar(200)	= null
- @IsRequiredBarcode	bit	= null
- @IsRequiredSerialNo	bit	= null
- @IsSuspended	bit	= null
- @cmdType varchar(50)=null
## Tables Read
- [[MMS_Items]]
## Tables Written
- [[MMS_Items]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_Items]]

**Tables Written**
- [[MMS_Items]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
