---
type: procedure
database: Olives_BO
name: OT_ImportSalesOrders
schema: dbo
tags: [#backoffice, #mobile, #order, #sales]
reads_from:
  - [[BusinessUnits]]
  - [[ClientsActive]]
  - [[Companies]]
  - [[CompanyParameters]]
  - GetSalesman
  - Header
  - `dbo`
writes_to:
  - [[OrdersDeliveryInfo]]
  - [[OrdersDetails]]
  - OrdersDetailsLog
  - [[OrdersHeaders]]
  - OrdersHeadersLog
  - [[OT_ErrorLog]]
  - [[OT_OrderHF]]
  - [[TransactionsBatchsItemsInfo]]
  - [[TransactionsPromotions]]
  - [[TransactionsSuggestedItems]]
  - [[WF_MasterLog]]
  - [[WF_SubLog]]
called_by:
  - [[Alpha_Integ_GetCurrRate]]
  - [[WF_AddWorkFlowLevelOne]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportSalesOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads BusinessUnits, ClientsActive, Companies, CompanyParameters, GetSalesman, Header, dbo. Writes OrdersDeliveryInfo, OrdersDetails, OrdersDetailsLog, OrdersHeaders, OrdersHeadersLog, OT_ErrorLog, OT_OrderHF, TransactionsBatchsItemsInfo, TransactionsPromotions, TransactionsSuggestedItems, WF_MasterLog, WF_SubLog. Invoked by 15 procedure(s). Calls 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[BusinessUnits]]
- [[ClientsActive]]
- [[Companies]]
- [[CompanyParameters]]
- GetSalesman
- Header
- `dbo`
## Tables Written
- [[OrdersDeliveryInfo]]
- [[OrdersDetails]]
- OrdersDetailsLog
- [[OrdersHeaders]]
- OrdersHeadersLog
- [[OT_ErrorLog]]
- [[OT_OrderHF]]
- [[TransactionsBatchsItemsInfo]]
- [[TransactionsPromotions]]
- [[TransactionsSuggestedItems]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
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
- [[WF_AddWorkFlowLevelOne]]
## Impact / Dependencies

**Tables Read**
- [[BusinessUnits]]
- [[ClientsActive]]
- [[Companies]]
- [[CompanyParameters]]
- GetSalesman
- Header
- dbo

**Tables Written**
- [[OrdersDeliveryInfo]]
- [[OrdersDetails]]
- OrdersDetailsLog
- [[OrdersHeaders]]
- OrdersHeadersLog
- [[OT_ErrorLog]]
- [[OT_OrderHF]]
- [[TransactionsBatchsItemsInfo]]
- [[TransactionsPromotions]]
- [[TransactionsSuggestedItems]]
- [[WF_MasterLog]]
- [[WF_SubLog]]

**Callers**
- [[Alpha_Integ_GetCurrRate]]
- [[WF_AddWorkFlowLevelOne]]

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
