---
type: procedure
database: Olives_BO
name: OT_ImportReceipts
schema: dbo
tags: [#backoffice, #billing, #mobile]
reads_from:
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - GetSalesman
  - Header
  - `dbo`
writes_to:
  - [[Checks]]
  - [[CustomersPaidTransList]]
  - [[Drawers]]
  - [[OT_ErrorLog]]
  - [[OT_Payments]]
  - [[ReceiptRequests]]
  - [[Receipts]]
  - [[Receipts_Branches]]
  - [[Receipts_PaidTrans]]
  - [[Receipts_PaidTransChecks]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportReceipts


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CompanyParameters, GetSalesman, Header, dbo. Writes Checks, CustomersPaidTransList, Drawers, OT_ErrorLog, OT_Payments, ReceiptRequests, Receipts, Receipts_Branches, Receipts_PaidTrans, Receipts_PaidTransChecks. Invoked by 15 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[ClientsActive]]
- [[CompanyParameters]]
- GetSalesman
- Header
- `dbo`
## Tables Written
- [[Checks]]
- [[CustomersPaidTransList]]
- [[Drawers]]
- [[OT_ErrorLog]]
- [[OT_Payments]]
- [[ReceiptRequests]]
- [[Receipts]]
- [[Receipts_Branches]]
- [[Receipts_PaidTrans]]
- [[Receipts_PaidTransChecks]]
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
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CompanyParameters]]
- GetSalesman
- Header
- dbo

**Tables Written**
- [[Checks]]
- [[CustomersPaidTransList]]
- [[Drawers]]
- [[OT_ErrorLog]]
- [[OT_Payments]]
- [[ReceiptRequests]]
- [[receipts]]
- [[Receipts_Branches]]
- [[Receipts_PaidTrans]]
- [[Receipts_PaidTransChecks]]

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
