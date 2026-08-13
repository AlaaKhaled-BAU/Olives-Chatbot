---
type: procedure
database: Olives_BO
name: Pro_ZatcaIntegrationApi
schema: dbo
tags: [#backoffice, #integration, #legal]
reads_from:
  - [[Branches]]
  - [[Currencies]]
  - [[Customers]]
  - DefaultRow
  - [[InvoiceReturnLink]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[PriceLists]]
  - ResultGenerateXmlZatca
  - [[RoutesInformation]]
  - SalesPerson
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[ZatcaCompany]]
writes_to:
  - ResultGenerateXmlZatca
  - SalesPerson
  - [[ZatcaResultGenerateXml]]
  - [[ZatcaSalesPersons]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ZatcaIntegrationApi


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Branches, Currencies, Customers, DefaultRow, InvoiceReturnLink, Items, ItemsUnits, PriceLists, ResultGenerateXmlZatca, RoutesInformation, SalesPerson, SalesPersons, TransactionsDetails, TransactionsHeaders, ZatcaCompany. Writes ResultGenerateXmlZatca, SalesPerson, ZatcaResultGenerateXml, ZatcaSalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @TransactionTypeID int = 1
- @TransactionNo int = 1300300648
- @TransactionYear smallint = 2024
- @CustomerID bigint = 100288
- @EncodedInvoice nvarchar(max)=null
- @InvoiceHash nvarchar(max)=null
- @UUID nvarchar(max)=null
- @QRCode nvarchar(max)=null
- @IsValid bit=null
- @ErrorMessage nvarchar(max)=null
- @AllowanceTotalAmount nvarchar(max)=null
- @ChargeTotalAmount nvarchar(max)=null
- @LineExtensionAmount nvarchar(max)=null
- @PayableAmount nvarchar(max)=null
- @PrepaidAmount nvarchar(max)=null
- @TaxExclusiveAmount nvarchar(max)=null
- @TaxInclusiveAmount nvarchar(max)=null
- @TaxAmount nvarchar(max)=null
- @StatusCode int=null
- @SendingStatus nvarchar(max)=null
- @IsSent bit=null
- @WarningMessage nvarchar(max)=null
- @ZatcaCallErrorMessage nvarchar(max)=null
- @ClearedInvoice nvarchar(max)=null
- @ZatcaQRCode nvarchar(max)=null
- @SalesPersonID int=null
- @CSID nvarchar(max)=null
- @PrivateKey nvarchar(max)=null
- @Secretkey nvarchar(max)=null
- @CSR nvarchar(max)=null
- @FromDate smalldatetime = null
- @ToDate smalldatetime = null
- @FromCustomer bigint =null
- @ToCustomer bigint =null
- @FromSalesman int =null
- @ToSalesman int =null
- @cmdType varchar(50)='Select Xml Data'
## Tables Read
- [[Branches]]
- [[Currencies]]
- [[Customers]]
- DefaultRow
- [[InvoiceReturnLink]]
- [[Items]]
- [[ItemsUnits]]
- [[PriceLists]]
- ResultGenerateXmlZatca
- [[RoutesInformation]]
- SalesPerson
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[ZatcaCompany]]
## Tables Written
- ResultGenerateXmlZatca
- SalesPerson
- [[ZatcaResultGenerateXml]]
- [[ZatcaSalesPersons]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Branches]]
- [[Currencies]]
- [[Customers]]
- DefaultRow
- [[InvoiceReturnLink]]
- [[Items]]
- [[ItemsUnits]]
- [[PriceLists]]
- ResultGenerateXmlZatca
- [[RoutesInformation]]
- SalesPerson
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[ZatcaCompany]]

**Tables Written**
- ResultGenerateXmlZatca
- SalesPerson
- [[ZatcaResultGenerateXml]]
- [[ZatcaSalesPersons]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Shared/Runbooks/ZATCA-Validation]]
