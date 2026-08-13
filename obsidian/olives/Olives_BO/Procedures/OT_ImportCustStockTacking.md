---
type: procedure
database: Olives_BO
name: OT_ImportCustStockTacking
schema: dbo
tags: [#backoffice, #inventory, #mobile]
reads_from:
  - [[ClientsActive]]
  - [[CustomerStockTacking]]
  - `dbo`
writes_to:
  - [[CustomerStockTacking]]
  - [[CustomerStockTackingDetails]]
  - [[Notifications]]
  - [[OT_CustStockDF]]
  - [[OT_CustStockHF]]
  - [[TransactionsBatchsItemsInfo]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportCustStockTacking


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CustomerStockTacking, dbo. Writes CustomerStockTacking, CustomerStockTackingDetails, Notifications, OT_CustStockDF, OT_CustStockHF, TransactionsBatchsItemsInfo. Invoked by 13 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[ClientsActive]]
- [[CustomerStockTacking]]
- `dbo`
## Tables Written
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Notifications]]
- [[OT_CustStockDF]]
- [[OT_CustStockHF]]
- [[TransactionsBatchsItemsInfo]]
## Callers
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[Alpha_SendData]]
- [[Bajali_SAP_Integ]]
- [[ECO_Land_SAP_Integ]]
- [[Izhiman_SAP_Integ]]
- [[Qetaf_Integ]]
- [[RamPharm_SAP_Integ]]
- [[Salbeshian_SAP_Integ]]
- [[SAMA_SAP_Integ]]
- [[Shini_Integ]]
- [[Zedan_SAP_Integ]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CustomerStockTacking]]
- dbo

**Tables Written**
- [[CustomerStockTacking]]
- [[CustomerStockTackingDetails]]
- [[Notifications]]
- [[OT_CustStockDF]]
- [[OT_CustStockHF]]
- [[TransactionsBatchsItemsInfo]]

**Callers**
_None_

**Callees**
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[Alpha_SendData]]
- [[Bajali_SAP_Integ]]
- [[ECO_Land_SAP_Integ]]
- [[Izhiman_SAP_Integ]]
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
