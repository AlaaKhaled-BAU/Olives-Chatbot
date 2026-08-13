---
type: procedure
database: Olives_BO
name: Alpha_SalesmanCustRoute
schema: dbo
tags: [#backoffice, #gps, #sales]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - LogAction
  - [[LogActionTransaction]]
  - RouteInfo
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[SalesPersonsDevicePermissions]]
  - [[SalesPersonsRoutes]]
  - `dbo`
writes_to:
  - AR_SalesManCustomers
  - customer
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - glactmf
  - GLCRBMF
  - [[RoutesInformation]]
  - [[SalesPersonsRoutes]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Alpha_SalesmanCustRoute


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, LogAction, LogActionTransaction, RouteInfo, RoutesInformation, SalesPersons, SalesPersonsDevicePermissions, SalesPersonsRoutes, dbo. Writes AR_SalesManCustomers, customer, Customers, CustomersFinancialDetails, glactmf, GLCRBMF, RoutesInformation, SalesPersonsRoutes. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SalesmanNo int
- @Date smalldatetime
- @CmdType varchar(100)
- @OldCustomerNo bigint = null
- @NewCustomerNo bigint = null
- @CustomerName varchar(200) = null
- @GPSx varchar(200) = null
- @GPSY varchar(200) = null
- @FromCustomer bigint = null
- @ToCustomer bigint = null
- @FromDept int = null
- @ToDept int = null
- @Country int = null
- @Area int = null
- @SArea int = null
- @PriceList int = null
- @CustType int = null
- @InvType int = null
- @NewRouteID int = null
- @AlphaNewCustomerNo bigint = 0 output
- @NewRouteNo int = 0 output
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- LogAction
- [[LogActionTransaction]]
- RouteInfo
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsDevicePermissions]]
- [[SalesPersonsRoutes]]
- `dbo`
## Tables Written
- AR_SalesManCustomers
- customer
- [[Customers]]
- [[CustomersFinancialDetails]]
- glactmf
- GLCRBMF
- [[RoutesInformation]]
- [[SalesPersonsRoutes]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersFinancialDetails]]
- LogAction
- [[LogActionTransaction]]
- RouteInfo
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsDevicePermissions]]
- [[SalesPersonsRoutes]]
- dbo

**Tables Written**
- AR_SalesManCustomers
- customer
- [[Customers]]
- [[CustomersFinancialDetails]]
- glactmf
- GLCRBMF
- [[RoutesInformation]]
- [[SalesPersonsRoutes]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
