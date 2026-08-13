---
type: procedure
database: Olives_BO
name: OT_ImportUploadOrders
schema: dbo
tags: [#backoffice, #mobile, #order]
reads_from:
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - Header
  - [[TransfersOrdersHeaders]]
  - `dbo`
writes_to:
  - [[OT_ConsOrderHF]]
  - [[TransactionsBatchsItemsInfo]]
  - [[TransfersOrdersDetails]]
  - [[TransfersOrdersHeaders]]
  - [[WF_MasterLog]]
  - [[WF_SubLog]]
called_by:
  - [[Pro_ConvertLoadOrderToTransaction]]
  - [[Pro_ConvertUnloadOrderToTransaction]]
  - [[SMS_AnwarMakesTransfer]]
  - [[WF_AddWorkFlowLevelOne]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportUploadOrders


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CompanyParameters, Header, TransfersOrdersHeaders, dbo. Writes OT_ConsOrderHF, TransactionsBatchsItemsInfo, TransfersOrdersDetails, TransfersOrdersHeaders, WF_MasterLog, WF_SubLog. Invoked by 15 procedure(s). Calls 4 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[ClientsActive]]
- [[CompanyParameters]]
- Header
- [[TransfersOrdersHeaders]]
- `dbo`
## Tables Written
- [[OT_ConsOrderHF]]
- [[TransactionsBatchsItemsInfo]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
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
- [[Pro_ConvertLoadOrderToTransaction]]
- [[Pro_ConvertUnloadOrderToTransaction]]
- [[SMS_AnwarMakesTransfer]]
- [[WF_AddWorkFlowLevelOne]]
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CompanyParameters]]
- Header
- [[TransfersOrdersHeaders]]
- dbo

**Tables Written**
- [[OT_ConsOrderHF]]
- [[TransactionsBatchsItemsInfo]]
- [[TransfersOrdersDetails]]
- [[TransfersOrdersHeaders]]
- [[WF_MasterLog]]
- [[WF_SubLog]]

**Callers**
- [[Pro_ConvertLoadOrderToTransaction]]
- [[Pro_ConvertUnloadOrderToTransaction]]
- [[SMS_AnwarMakesTransfer]]
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
