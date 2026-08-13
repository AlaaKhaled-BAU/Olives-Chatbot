---
type: procedure
database: Olives_BO
name: Pro_DeliveryCar
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - [[CarAndSalespersonLink]]
  - [[CompanyBranches]]
  - [[Customers]]
  - [[DeliveryCars]]
  - [[DeliveryManifest]]
  - [[InvoiceDeliveryDF]]
  - [[InvoiceDeliveryHF]]
  - [[Items]]
  - [[Locations]]
  - [[NoTransactionsReasons]]
  - [[SalesOrderDeliveryHF]]
  - [[SalesPersons]]
  - [[SalespersonsMessages]]
  - [[SystemCodes]]
  - TransactionsHeaders_Type
writes_to:
  - [[DeliveryCars]]
  - [[DeliveryManifest]]
  - [[InvoiceDeliveryHF]]
  - InvoiceDeliveryLog
  - [[SalesOrderDeliveryHF]]
  - [[SalespersonsMessages]]
  - TransactionsHeaders_Type
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_DeliveryCar


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CarAndSalespersonLink, CompanyBranches, Customers, DeliveryCars, DeliveryManifest, InvoiceDeliveryDF, InvoiceDeliveryHF, Items, Locations, NoTransactionsReasons, SalesOrderDeliveryHF, SalesPersons, SalespersonsMessages, SystemCodes, TransactionsHeaders_Type. Writes DeliveryCars, DeliveryManifest, InvoiceDeliveryHF, InvoiceDeliveryLog, SalesOrderDeliveryHF, SalespersonsMessages, TransactionsHeaders_Type. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @ID smallint = null
- @Name nvarchar (200)=null
- @LoadWieght float =null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @cmdType varchar(max)='SelectInvoiceDeliverdData'
- @UserID nvarchar(100)=null
- @FromCustomer Bigint= 0
- @ToCustomer Bigint= 999999999999
- @FromSalesMan int= 0
- @ToSalesMan int= 999999999
- @AssistantID int= null
- @DeliveryCarID int=null
- @RouteID nvarchar(max)= null
- @AssignDate SmallDatetime = null
- @FromDate Datetime= '2014-01-01'
- @ToDate Datetime= '2024-11-26'
- @IsDelivered bit=null
- @InvoiceNumber int=null
- @InvoiceYear int=null
- @InvoiceType int=null
- @CarType int = null
- @NoOfPackages int = null
- @ManifestID int=null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @PCName varchar(100)=null
- @UserID_Log nvarchar(100)=null
- @BranchID smallint = NULL
- @Prm_TransactionsHeaders_Type  TransactionsHeaders_Type   READONLY
## Tables Read
- [[CarAndSalespersonLink]]
- [[CompanyBranches]]
- [[Customers]]
- [[DeliveryCars]]
- [[DeliveryManifest]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Items]]
- [[Locations]]
- [[NoTransactionsReasons]]
- [[SalesOrderDeliveryHF]]
- [[SalesPersons]]
- [[SalespersonsMessages]]
- [[SystemCodes]]
- TransactionsHeaders_Type
## Tables Written
- [[DeliveryCars]]
- [[DeliveryManifest]]
- [[InvoiceDeliveryHF]]
- InvoiceDeliveryLog
- [[SalesOrderDeliveryHF]]
- [[SalespersonsMessages]]
- TransactionsHeaders_Type
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CarAndSalespersonLink]]
- [[CompanyBranches]]
- [[Customers]]
- [[DeliveryCars]]
- [[DeliveryManifest]]
- [[InvoiceDeliveryDF]]
- [[InvoiceDeliveryHF]]
- [[Items]]
- [[Locations]]
- [[NoTransactionsReasons]]
- [[SalesOrderDeliveryHF]]
- [[SalesPersons]]
- [[SalespersonsMessages]]
- [[SystemCodes]]
- TransactionsHeaders_Type

**Tables Written**
- [[DeliveryCars]]
- [[DeliveryManifest]]
- [[InvoiceDeliveryHF]]
- InvoiceDeliveryLog
- [[SalesOrderDeliveryHF]]
- [[SalespersonsMessages]]
- TransactionsHeaders_Type

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
