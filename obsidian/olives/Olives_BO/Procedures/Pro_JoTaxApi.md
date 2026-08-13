---
type: procedure
database: Olives_BO
name: Pro_JoTaxApi
schema: dbo
tags: [#backoffice, #billing, #integration, #legal]
reads_from:
  - [[Companies]]
  - [[Currencies]]
  - [[Customers]]
  - Fun_GetReturnSalesInfoForTaxAPI
  - [[InvoiceReturnLink]]
  - [[Items]]
  - [[ItemsUnits]]
  - [[JOTaxSettings]]
  - [[JoTaxResult]]
  - [[PriceLists]]
  - [[RoutesInformation]]
  - [[SalesPersons]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
writes_to:
  - [[JoTaxResult]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_JoTaxApi


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, Currencies, Customers, Fun_GetReturnSalesInfoForTaxAPI, InvoiceReturnLink, Items, ItemsUnits, JOTaxSettings, JoTaxResult, PriceLists, RoutesInformation, SalesPersons, TransactionsDetails, TransactionsHeaders. Writes JoTaxResult. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int =1
- @TransactionYear smallint =2025
- @TransactionNo int =1300300010
- @TransactionTypeID smallint =1
- @status nvarchar(max)=null
- @EINV_QR nvarchar(max)=null
- @EINV_INV_UUID nvarchar(max) =null
- @ErrorMessage nvarchar(max)=null
- @UUID nvarchar(max)=null
- @RoundDigit float=9
- @cmdType nvarchar(100)='Select All by ID'
## Tables Read
- [[Companies]]
- [[Currencies]]
- [[Customers]]
- Fun_GetReturnSalesInfoForTaxAPI
- [[InvoiceReturnLink]]
- [[Items]]
- [[ItemsUnits]]
- [[JOTaxSettings]]
- [[JoTaxResult]]
- [[PriceLists]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
## Tables Written
- [[JoTaxResult]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- [[Currencies]]
- [[Customers]]
- Fun_GetReturnSalesInfoForTaxAPI
- [[InvoiceReturnLink]]
- [[Items]]
- [[ItemsUnits]]
- [[JOTaxSettings]]
- [[JoTaxResult]]
- [[PriceLists]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]

**Tables Written**
- [[JoTaxResult]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Shared/Runbooks/ZATCA-Validation]]
