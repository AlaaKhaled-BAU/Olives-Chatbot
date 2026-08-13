---
type: procedure
database: Olives_BO
name: MaintinanceOrdersImages_Insert
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - [[MaintinanceOrders]]
  - Olives_Images
writes_to:
  - MaintinanceOrdersImages
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# MaintinanceOrdersImages_Insert


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MaintinanceOrders, Olives_Images. Writes MaintinanceOrdersImages. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @OrderDeviceSysID varchar (50)
- @LineID int=0
- @CompanyID smallint
- @ImageType smallint
- @Image image
- @DeviceSysID varchar (50)
- @ErrNo SmallInt Output
## Tables Read
- [[MaintinanceOrders]]
- Olives_Images
## Tables Written
- MaintinanceOrdersImages
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MaintinanceOrders]]
- Olives_Images

**Tables Written**
- MaintinanceOrdersImages

**Callers**
_None_

**Callees**
_None_


## When to Run This

Data insertion procedure — called automatically when a new record is created via the API or UI. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
