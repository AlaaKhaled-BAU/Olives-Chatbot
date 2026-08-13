---
type: procedure
database: Olives_BO
name: OT_ImportSalesInvoices
schema: dbo
tags: [#backoffice, #billing, #mobile, #sales]
reads_from:
  - [[ClientsActive]]
  - [[Companies]]
  - [[CompanyParameters]]
  - [[CurrenciesRate]]
  - GetSalesman
  - Header
  - [[PaymentsTypes]]
  - `dbo`
  - olives_BO
writes_to:
  - [[CouponsBooksDetails]]
  - [[CustomersPaidTransList]]
  - [[OT_ErrorLog]]
  - [[OT_InvoiceDF]]
  - [[OT_InvoiceHF]]
  - [[Receipts_PaidTrans]]
  - [[SalesOrderDeliveryHF]]
  - [[TransactionsBatchsItemsInfo]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[TransactionsImages]]
  - [[TransactionsPromotions]]
  - [[TransactionsSuggestedItems]]
called_by:
  - [[Alpha_Integ_GetCurrRate]]
  - [[Pro_CalcSalespersonItemBalance]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportSalesInvoices


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Companies, CompanyParameters, CurrenciesRate, GetSalesman, Header, PaymentsTypes, dbo, olives_BO. Writes CouponsBooksDetails, CustomersPaidTransList, OT_ErrorLog, OT_InvoiceDF, OT_InvoiceHF, Receipts_PaidTrans, SalesOrderDeliveryHF, TransactionsBatchsItemsInfo, TransactionsDetails, TransactionsHeaders, TransactionsImages, TransactionsPromotions, TransactionsSuggestedItems. Invoked by 15 procedure(s). Calls 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
- @pVouType smallint = 0
- @pVouYear smallint = 0
- @pVouNo int = 0
- @pHaveError int = 0 output
## Tables Read
- [[ClientsActive]]
- [[Companies]]
- [[CompanyParameters]]
- [[CurrenciesRate]]
- GetSalesman
- Header
- [[PaymentsTypes]]
- `dbo`
- olives_BO
## Tables Written
- [[CouponsBooksDetails]]
- [[CustomersPaidTransList]]
- [[OT_ErrorLog]]
- [[OT_InvoiceDF]]
- [[OT_InvoiceHF]]
- [[Receipts_PaidTrans]]
- [[SalesOrderDeliveryHF]]
- [[TransactionsBatchsItemsInfo]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsImages]]
- [[TransactionsPromotions]]
- [[TransactionsSuggestedItems]]
## Callers
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[Alpha_SendData]]
- [[Bajali_SAP_Integ]]
- [[ECO_Land_SAP_Integ]]
- [[Izhiman_SAP_Integ]]
- [[Khobara_Integ]]
- [[Qerat_Integ]]
- [[Qetaf_Integ]]
- [[RamPharm_SAP_Integ]]
- [[Salbeshian_SAP_Integ]]
- [[SAMA_SAP_Integ]]
- [[Shini_Integ]]
- [[Zedan_SAP_Integ]]
## Callees
- [[Alpha_Integ_GetCurrRate]]
- [[Pro_CalcSalespersonItemBalance]]
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Companies]]
- [[CompanyParameters]]
- [[CurrenciesRate]]
- GetSalesman
- Header
- [[PaymentsTypes]]
- dbo
- olives_BO

**Tables Written**
- [[CouponsBooksDetails]]
- [[CustomersPaidTransList]]
- [[OT_ErrorLog]]
- [[OT_InvoiceDF]]
- [[OT_InvoiceHF]]
- [[Receipts_PaidTrans]]
- [[SalesOrderDeliveryHF]]
- [[TransactionsBatchsItemsInfo]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsImages]]
- [[TransactionsPromotions]]
- [[TransactionsSuggestedItems]]

**Callers**
- [[Alpha_Integ_GetCurrRate]]
- [[Pro_CalcSalespersonItemBalance]]

**Callees**
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[Alpha_SendData]]
- [[Bajali_SAP_Integ]]
- [[ECO_Land_SAP_Integ]]
- [[Izhiman_SAP_Integ]]
- [[Khobara_Integ]]
- [[Qerat_Integ]]
- [[Qetaf_Integ]]
- [[RamPharm_SAP_Integ]]
- [[Salbeshian_SAP_Integ]]
- [[SAMA_SAP_Integ]]
- [[Shini_Integ]]
- [[Zedan_SAP_Integ]]


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
