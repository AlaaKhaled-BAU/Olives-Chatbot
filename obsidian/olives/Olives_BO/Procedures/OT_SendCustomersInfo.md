---
type: procedure
database: Olives_BO
name: OT_SendCustomersInfo
schema: dbo
tags: [#backoffice, #customer, #mobile]
reads_from:
  - [[Companies]]
  - Cust_summary
  - [[Customers]]
  - [[CustomersClasses]]
  - [[CustomersFinancialDetails]]
  - CustomersTaxExclude
  - [[DeliveryManifest]]
  - [[DeliveryRoute]]
  - Fun_GetSalesmanTreeByID
  - [[InvoiceDeliveryHF]]
  - [[Locations]]
  - OSFA_DB
  - [[OrdersDeliveryDetails]]
  - [[OrdersHeaders]]
  - [[SalesOrderDeliveryHF]]
writes_to:
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - [[DeliveryRoute]]
  - [[OT_CustomerMF]]
  - [[OT_RouteMF]]
  - [[OT_SalesmanRoute]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_SendCustomersInfo


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, Cust_summary, Customers, CustomersClasses, CustomersFinancialDetails, CustomersTaxExclude, DeliveryManifest, DeliveryRoute, Fun_GetSalesmanTreeByID, InvoiceDeliveryHF, Locations, OSFA_DB, OrdersDeliveryDetails, OrdersHeaders, SalesOrderDeliveryHF. Writes Customers, CustomersFinancialDetails, DeliveryRoute, OT_CustomerMF, OT_RouteMF, OT_SalesmanRoute. Invoked by 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @SendDate smalldatetime
- @ClientActive smallint
- @SalesmanNo int
- @PositionsID int
- @OnlyCustomersOnRoutes bit
- @SalesPersonType int
- @GroupCustByRelatedSalespersons int
- @SalesmanCarID int
## Tables Read
- [[Companies]]
- Cust_summary
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- CustomersTaxExclude
- [[DeliveryManifest]]
- [[DeliveryRoute]]
- Fun_GetSalesmanTreeByID
- [[InvoiceDeliveryHF]]
- [[Locations]]
- OSFA_DB
- [[OrdersDeliveryDetails]]
- [[OrdersHeaders]]
- [[SalesOrderDeliveryHF]]
## Tables Written
- [[Customers]]
- [[CustomersFinancialDetails]]
- [[DeliveryRoute]]
- [[OT_CustomerMF]]
- [[OT_RouteMF]]
- [[OT_SalesmanRoute]]
## Callers
- [[OT_SendSalesmanData]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- Cust_summary
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- CustomersTaxExclude
- [[DeliveryManifest]]
- [[DeliveryRoute]]
- Fun_GetSalesmanTreeByID
- [[InvoiceDeliveryHF]]
- [[Locations]]
- OSFA_DB
- [[OrdersDeliveryDetails]]
- [[OrdersHeaders]]
- [[SalesOrderDeliveryHF]]

**Tables Written**
- [[customers]]
- [[CustomersFinancialDetails]]
- [[DeliveryRoute]]
- [[OT_CustomerMF]]
- [[OT_RouteMF]]
- [[OT_SalesmanRoute]]

**Callers**
_None_

**Callees**
- [[OT_SendSalesmanData]]


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
