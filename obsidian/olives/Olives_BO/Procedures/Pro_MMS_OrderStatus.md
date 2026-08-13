---
type: procedure
database: Olives_BO
name: Pro_MMS_OrderStatus
schema: dbo
tags: [#backoffice, #mms, #order]
reads_from:
  - [[MMS_OrderStatus]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_OrderStatus


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_OrderStatus. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @OrderStatusID	int	 = null
- @OrderStatusDesc	varchar(150)	 = null
- @OrderStatusForeignDesc	varchar(150)	 = null
- @UseInDevice	bit	 = null
## Tables Read
- [[MMS_OrderStatus]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_OrderStatus]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
