---
type: procedure
database: Olives_BO
name: Retco_Integ_ItemBal
schema: dbo
tags: [#backoffice, #integration, #inventory]
reads_from:
  - [[Items]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[SalesPersonItemsAssignment]]
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
  - [[SalesPersonsDevicePermissions]]
  - [[TransactionsHeaders]]
writes_to:
  - [[SalesPersonItemsBalance]]
  - [[SalesPersons]]
  - [[TransactionsHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Retco_Integ_ItemBal


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Items, ItemsUnits, ItemsUnitsDetails, SalesPersonItemsAssignment, SalesPersonItemsBalance, SalesPersons, SalesPersonsDevicePermissions, TransactionsHeaders. Writes SalesPersonItemsBalance, SalesPersons, TransactionsHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
- @SalesmanNo int=null
- @CmdType varchar(50)
- @ItemCode varchar(50)=null
- @ItemQuantity float=null
- @UnitCode  varchar(50)=null
## Tables Read
- [[Items]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[SalesPersonsDevicePermissions]]
- [[TransactionsHeaders]]
## Tables Written
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[TransactionsHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Items]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[SalesPersonItemsAssignment]]
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[SalesPersonsDevicePermissions]]
- [[TransactionsHeaders]]

**Tables Written**
- [[SalesPersonItemsBalance]]
- [[SalesPersons]]
- [[TransactionsHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
