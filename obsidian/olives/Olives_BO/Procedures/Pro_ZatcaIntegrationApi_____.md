---
type: procedure
database: Olives_BO
name: Pro_ZatcaIntegrationApi_____
schema: dbo
tags: [#integration]
reads_from:
  - Branches
  - Currencies
  - Customers
  - InvoiceReturnLink
  - Items
  - ItemsUnits
  - PriceLists
  - RoutesInformation
  - SalesPersons
  - TransactionsDetails
  - TransactionsHeaders
  - ZatcaCompany
  - ZatcaCustomer
  - ZatcaMode
writes_to:
  - ZatcaResultGenerateXml
  - ZatcaSalesPersons
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Pro_ZatcaIntegrationApi_____

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 14 table(s); writes 2; calls 1 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @TransactionTypeID int
- @TransactionNo int
- @TransactionYear smallint
- @CustomerID bigint
- @EncodedInvoice nvarchar(MAX)
- @InvoiceHash nvarchar(MAX)
- @UUID nvarchar(MAX)
- @QRCode nvarchar(MAX)
- @IsValid bit
- @ErrorMessage nvarchar(MAX)
- @AllowanceTotalAmount nvarchar(MAX)
- @ChargeTotalAmount nvarchar(MAX)
- @LineExtensionAmount nvarchar(MAX)
- @PayableAmount nvarchar(MAX)
- @PrepaidAmount nvarchar(MAX)
- @TaxExclusiveAmount nvarchar(MAX)
- @TaxInclusiveAmount nvarchar(MAX)
- @TaxAmount nvarchar(MAX)
- @StatusCode int
- @SendingStatus nvarchar(MAX)
- @IsSent bit
- @WarningMessage nvarchar(MAX)
- @ZatcaCallErrorMessage nvarchar(MAX)
- @ClearedInvoice nvarchar(MAX)
- @ZatcaQRCode nvarchar(MAX)
- @SalesPersonID int
- @CSID nvarchar(MAX)
- @PrivateKey nvarchar(MAX)
- @Secretkey nvarchar(MAX)
- @CSR nvarchar(MAX)
- @FromDate smalldatetime
- @ToDate smalldatetime
- @FromCustomer bigint
- @ToCustomer bigint
- @FromSalesman int
- @ToSalesman int
- @cmdType varchar(50)
## Tables Read
- [[Branches]]
- [[Currencies]]
- [[Customers]]
- [[InvoiceReturnLink]]
- [[Items]]
- [[ItemsUnits]]
- [[PriceLists]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[ZatcaCompany]]
- [[ZatcaCustomer]]
- [[ZatcaMode]]
## Tables Written
- [[ZatcaResultGenerateXml]]
- [[ZatcaSalesPersons]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `GetItemOrgUnitQty`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
