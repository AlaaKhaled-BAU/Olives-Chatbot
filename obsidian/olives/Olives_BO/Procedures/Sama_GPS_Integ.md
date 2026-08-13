---
type: procedure
database: Olives_BO
name: Sama_GPS_Integ
schema: dbo
tags: [#backoffice, #gps, #integration]
reads_from:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[SalesPersonsRoutes]]
  - [[Users]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Sama_GPS_Integ


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, CustomersFinancialDetails, RoutesInformation, SalesPersons, SalesPersonsRoutes, Users. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint
- @cmdType varchar(50)
- @UserName varchar(50)=null
- @PW varchar(50) =null
- @VehicleId varchar(100)=null
- @RouteDate smalldatetime=null
## Tables Read
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[Users]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalesPersonsRoutes]]
- [[Users]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
