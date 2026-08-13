---
type: procedure
database: Olives_BO
name: OT_ImportReturnOrder
schema: dbo
tags: [#backoffice, #mobile, #order]
reads_from:
  - [[ClientsActive]]
  - [[Companies]]
  - [[CompanyParameters]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - Header
  - [[ReturnOrdersHeaders]]
  - [[SalesPersons]]
  - [[SalespersonsMessages]]
  - `dbo`
writes_to:
  - [[OT_ReturnOrderHF]]
  - [[ReturnOrdersDetails]]
  - [[ReturnOrdersHeaders]]
  - [[SalespersonsMessages]]
  - [[TransactionsBatchsItemsInfo]]
  - [[TransactionsPromotions]]
called_by:
  - [[Alpha_Integ_GetCurrRate]]
  - [[WF_AddWorkFlowLevelOne]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportReturnOrder


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Companies, CompanyParameters, Customers, CustomersFinancialDetails, Header, ReturnOrdersHeaders, SalesPersons, SalespersonsMessages, dbo. Writes OT_ReturnOrderHF, ReturnOrdersDetails, ReturnOrdersHeaders, SalespersonsMessages, TransactionsBatchsItemsInfo, TransactionsPromotions. Calls 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[ClientsActive]]
- [[Companies]]
- [[CompanyParameters]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Header
- [[ReturnOrdersHeaders]]
- [[SalesPersons]]
- [[SalespersonsMessages]]
- `dbo`
## Tables Written
- [[OT_ReturnOrderHF]]
- [[ReturnOrdersDetails]]
- [[ReturnOrdersHeaders]]
- [[SalespersonsMessages]]
- [[TransactionsBatchsItemsInfo]]
- [[TransactionsPromotions]]
## Callers
_None (no known callers)_
## Callees
- [[Alpha_Integ_GetCurrRate]]
- [[WF_AddWorkFlowLevelOne]]
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Companies]]
- [[CompanyParameters]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- Header
- [[ReturnOrdersHeaders]]
- [[SalesPersons]]
- [[SalespersonsMessages]]
- dbo

**Tables Written**
- [[OT_ReturnOrderHF]]
- [[ReturnOrdersDetails]]
- [[ReturnOrdersHeaders]]
- [[SalespersonsMessages]]
- [[TransactionsBatchsItemsInfo]]
- [[TransactionsPromotions]]

**Callers**
- [[Alpha_Integ_GetCurrRate]]
- [[WF_AddWorkFlowLevelOne]]

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
