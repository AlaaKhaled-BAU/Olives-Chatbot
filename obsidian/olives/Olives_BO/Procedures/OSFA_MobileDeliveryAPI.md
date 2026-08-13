---
type: procedure
database: Olives_BO
name: OSFA_MobileDeliveryAPI
schema: dbo
tags: [#backoffice, #integration, #mobile, #order]
reads_from:
  - [[Customers]]
  - [[DeliveryCars]]
  - Fun_GetOrdersDeliveredQtyTot
  - Fun_GetOrdersDeliveryTrans
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[Items]]
  - [[OrdersDetails]]
  - [[OrdersHeaders]]
  - [[SalesPersons]]
  - [[Users]]
  - `dbo`
writes_to:
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[OrdersHeaders]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OSFA_MobileDeliveryAPI


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, DeliveryCars, Fun_GetOrdersDeliveredQtyTot, Fun_GetOrdersDeliveryTrans, InvoiceDeliveryDF, InvoiceDeliveryHF, Items, OrdersDetails, OrdersHeaders, SalesPersons, Users, dbo. Writes InvoiceDeliveryDF, InvoiceDeliveryHF, OrdersHeaders. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CmdType nvarchar(100)='GetOrdersForAssignment'
- @CompanyID smallint=1
- @username nvarchar(500)=null
- @password nvarchar(500)=null
- @TransactionYear int=2023
- @TransactionNo bigint=1300300002
- @TabletSysID varchar(100)='3003_2023042611225988'
- @ItemCode  varchar(100)=''
- @ItemUnit  varchar(100)=''
- @DeliveryCarID int=0
- @AssignDateTime smalldatetime=null
- @Qty float=0
- @Stat int=0
## Tables Read
- [[Customers]]
- [[DeliveryCars]]
- Fun_GetOrdersDeliveredQtyTot
- Fun_GetOrdersDeliveryTrans
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[Users]]
- `dbo`
## Tables Written
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[OrdersHeaders]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[DeliveryCars]]
- Fun_GetOrdersDeliveredQtyTot
- Fun_GetOrdersDeliveryTrans
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Items]]
- [[OrdersDetails]]
- [[OrdersHeaders]]
- [[SalesPersons]]
- [[Users]]
- dbo

**Tables Written**
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[OrdersHeaders]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
