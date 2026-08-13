---
type: procedure
database: Olives_BO
name: OT_ImportSalesIssueItems
schema: dbo
tags: [#backoffice, #inventory, #mobile, #sales]
reads_from:
  - [[BusinessUnits]]
  - [[ClientsActive]]
  - [[Companies]]
  - [[CompanyParameters]]
  - Details
  - GetSalesman
  - Header
  - [[OrdersHeaders]]
  - [[OT_IssueItemsHF]]
  - [[OT_OrderDF]]
writes_to:
  - [[IssueItemsDetails]]
  - [[IssueItemsHeaders]]
  - [[OrdersHeaders]]
  - [[OT_IssueItemsHF]]
called_by:
  - [[Alpha_Integ_GetCurrRate]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportSalesIssueItems


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BusinessUnits, ClientsActive, Companies, CompanyParameters, Details, GetSalesman, Header, OrdersHeaders, OT_IssueItemsHF, OT_OrderDF. Writes IssueItemsDetails, IssueItemsHeaders, OrdersHeaders, OT_IssueItemsHF. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[BusinessUnits]]
- [[ClientsActive]]
- [[Companies]]
- [[CompanyParameters]]
- Details
- GetSalesman
- Header
- [[OrdersHeaders]]
- [[OT_IssueItemsHF]]
- [[OT_OrderDF]]
## Tables Written
- [[IssueItemsDetails]]
- [[IssueItemsHeaders]]
- [[OrdersHeaders]]
- [[OT_IssueItemsHF]]
## Callers
_None (no known callers)_
## Callees
- [[Alpha_Integ_GetCurrRate]]
## Impact / Dependencies

**Tables Read**
- [[BusinessUnits]]
- [[ClientsActive]]
- [[Companies]]
- [[CompanyParameters]]
- Details
- GetSalesman
- Header
- [[OrdersHeaders]]
- [[OT_IssueItemsHF]]
- [[OT_OrderDF]]

**Tables Written**
- [[IssueItemsDetails]]
- [[IssueItemsHeaders]]
- [[OrdersHeaders]]
- [[OT_IssueItemsHF]]

**Callers**
- [[Alpha_Integ_GetCurrRate]]

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[MMS_ItemsCategories]]
- [[IssueItemsDetails]]
- [[SalespersonCustStockItemsAssignment]]
- [[OT_SendLog]]
- [[OT_SendMultiSalesmanData]]
- [[CustomerTargetsDetails]]
- [[PromotionsApprovalLog]]
- [[SalesQuotationHeaders]]

- [[OT_ImportSalesInvoices]]
- [[OT_ImportRequestToExceedChqLimit]]
- [[OT_ImportSalesmanDoneProcedures]]
- [[Glossary]]
