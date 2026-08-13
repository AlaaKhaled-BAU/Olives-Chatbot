---
type: procedure
database: Olives_BO
name: Pro_CompanyParameters
schema: dbo
tags: [#backoffice, #reference]
reads_from:
  - [[ClientsActive]]
  - [[Companies]]
  - [[CompanyParameters]]
  - [[CompetitveItemsDataHF]]
  - [[CustomerStockTacking]]
  - [[LogActionTransaction]]
  - [[OrdersHeaders]]
  - [[Receipts]]
  - [[ReturnOrdersHeaders]]
  - [[SalesPersonStockTacking]]
  - [[SalesPersons]]
  - [[SalesQuotationHeaders]]
  - [[SurveyCustomers]]
  - [[SurveyProspectiveCustomers]]
  - [[TransactionsHeaders]]
writes_to:
  - [[CompanyParameters]]
called_by:
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Company-Setup
---
# Pro_CompanyParameters


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Companies, CompanyParameters, CompetitveItemsDataHF, CustomerStockTacking, LogActionTransaction, OrdersHeaders, Receipts, ReturnOrdersHeaders, SalesPersonStockTacking, SalesPersons, SalesQuotationHeaders, SurveyCustomers, SurveyProspectiveCustomers, TransactionsHeaders. Writes CompanyParameters. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int=null
- @SerialType int=null
- @AutoSendInvoiceToERP bit=null
- @AutoSendReturnInvoiceToERP bit=null
- @AutoSendReceiptsToERP bit=null
- @AutoSendOrderToERP bit=null
- @CalcItemBalance bit=null
- @UseRangePrice bit=null
- @PassLength int=null
- @MaxLoadOrderConfirm int = null
- @MaxLogin int=null
- @TimeOutLoginOnBackOffice int=null
- @PassExpiryDays int=null
- @ActivationCodeDays int=null
- @EnablePassPolicy bit=null
- @EnableVerificationCode bit=null
- @EnableMacAddressOnTab bit=null
- @cmdType varchar(50)=null
- @CID int =null
## Tables Read
- [[ClientsActive]]
- [[Companies]]
- [[CompanyParameters]]
- [[CompetitveItemsDataHF]]
- [[CustomerStockTacking]]
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[ReturnOrdersHeaders]]
- [[SalesPersonStockTacking]]
- [[SalesPersons]]
- [[SalesQuotationHeaders]]
- [[SurveyCustomers]]
- [[SurveyProspectiveCustomers]]
- [[TransactionsHeaders]]
## Tables Written
- [[CompanyParameters]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Companies]]
- [[CompanyParameters]]
- [[CompetitveItemsDataHF]]
- [[CustomerStockTacking]]
- [[LogActionTransaction]]
- [[OrdersHeaders]]
- [[Receipts]]
- [[ReturnOrdersHeaders]]
- [[SalesPersonStockTacking]]
- [[SalesPersons]]
- [[SalesQuotationHeaders]]
- [[SurveyCustomers]]
- [[SurveyProspectiveCustomers]]
- [[TransactionsHeaders]]

**Tables Written**
- [[CompanyParameters]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
