---
type: procedure
database: Olives_BO
name: Retco_Edit_Integ_SalesOrders
schema: dbo
tags: [#backoffice, #integration, #order, #sales]
reads_from:
  - [[Customers]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[ItemsUnitsDetails]]
  - [[SalesPersons]]
  - `dbo`
writes_to:
  - SalesOrders
  - SalesOrdersItems
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Retco_Edit_Integ_SalesOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, Items, ItemsUnits, ItemsUnitsDetails, SalesPersons, dbo. Writes SalesOrders, SalesOrdersItems. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID SMALLINT = NULL
- @OrderYear SMALLINT = NULL
- @OrderNo NVARCHAR(50) = NULL
- @ItemCode varchar(50) = NULL
- @Quantity float= null
- @UnitID nvarchar(50)=NULL
- @CmdType NVARCHAR(50) = NULL
- @IsDeleteHeader bit = null
## Tables Read
- [[Customers]]
- [[Items]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[SalesPersons]]
- `dbo`
## Tables Written
- SalesOrders
- SalesOrdersItems
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[Items]]
- [[ItemsUnits]]
- [[ItemsUnitsDetails]]
- [[SalesPersons]]
- dbo

**Tables Written**
- SalesOrders
- SalesOrdersItems

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
