---
type: procedure
database: Olives_BO
name: Pro_DeliveryAssigning
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - [[Customers]]
  - [[DeliveryCars]]
  - [[DeliveryProvaD]]
  - [[DeliveryProvaH]]
  - Fun_GetAssignedDeliveryItems
  - [[Items]]
  - [[ItemsUnits]]
  - [[Locations]]
  - [[SalesOrderHistoryDF]]
  - [[SalesOrderHistoryHF]]
  - [[SalesPersons]]
  - [[SystemCodes]]
writes_to:
  - [[DeliveryProvaD]]
  - [[DeliveryProvaH]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_DeliveryAssigning


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, DeliveryCars, DeliveryProvaD, DeliveryProvaH, Fun_GetAssignedDeliveryItems, Items, ItemsUnits, Locations, SalesOrderHistoryDF, SalesOrderHistoryHF, SalesPersons, SystemCodes. Writes DeliveryProvaD, DeliveryProvaH. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
- @OrderYear smallint = 1
- @ProvaNo Bigint = 0
- @OrderNo int = 1
- @SalesmanNo int = 1
- @CarID int = 1
- @ItemCode nvarchar(100)=NULL
- @UnitID nvarchar(50)=NULL
- @Quantity float= null
- @Weight float= null
- @DeliveryDate SmallDateTime = '2021-09-16'
- @UserID Nvarchar(50) = NULL
- @cmdType Nvarchar(50) = NULL
## Tables Read
- [[Customers]]
- [[DeliveryCars]]
- [[DeliveryProvaD]]
- [[DeliveryProvaH]]
- Fun_GetAssignedDeliveryItems
- [[Items]]
- [[ItemsUnits]]
- [[Locations]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]
- [[SalesPersons]]
- [[SystemCodes]]
## Tables Written
- [[DeliveryProvaD]]
- [[DeliveryProvaH]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[DeliveryCars]]
- [[DeliveryProvaD]]
- [[DeliveryProvaH]]
- Fun_GetAssignedDeliveryItems
- [[Items]]
- [[ItemsUnits]]
- [[Locations]]
- [[SalesOrderHistoryDF]]
- [[SalesOrderHistoryHF]]
- [[SalesPersons]]
- [[SystemCodes]]

**Tables Written**
- [[DeliveryProvaD]]
- [[DeliveryProvaH]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
