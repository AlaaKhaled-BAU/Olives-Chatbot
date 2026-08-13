---
type: procedure
database: Olives_BO
name: Pro_ConvertUnloadOrderToTransaction
schema: dbo
tags: [#backoffice, #order]
reads_from:
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - [[TransactionsTypes]]
  - [[TransfersOrdersHeaders]]
writes_to:
  - [[DocumentsTypes]]
  - [[Notifications]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - [[TransactionsTypes]]
  - [[TransfersOrdersDetails_ErrorQty]]
  - [[TransfersOrdersHeaders]]
called_by:
  - [[Pro_CalcSalespersonItemBalance]]
support_relevance: high
last_verified: 2026-07-05
---
# Pro_ConvertUnloadOrderToTransaction


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CompanyParameters, TransactionsTypes, TransfersOrdersHeaders. Writes DocumentsTypes, Notifications, TransactionsDetails, TransactionsHeaders, TransactionsTypes, TransfersOrdersDetails_ErrorQty, TransfersOrdersHeaders. Invoked by 4 procedure(s). Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
- @OrderYear int
- @OrderNo int
- @ErrorNo int output
- @UserID Nvarchar (50) = null
## Tables Read
- [[ClientsActive]]
- [[CompanyParameters]]
- [[TransactionsTypes]]
- [[TransfersOrdersHeaders]]
## Tables Written
- [[DocumentsTypes]]
- [[Notifications]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]
- [[TransfersOrdersDetails_ErrorQty]]
- [[TransfersOrdersHeaders]]
## Callers
- [[OT_ImportUploadOrders]]
- [[Pro_TransfersOrdersHeaders]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]
## Callees
- [[Pro_CalcSalespersonItemBalance]]
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CompanyParameters]]
- [[TransactionsTypes]]
- [[TransfersOrdersHeaders]]

**Tables Written**
- [[DocumentsTypes]]
- [[Notifications]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- [[TransactionsTypes]]
- [[TransfersOrdersDetails_ErrorQty]]
- [[TransfersOrdersHeaders]]

**Callers**
- [[Pro_CalcSalespersonItemBalance]]

**Callees**
- [[OT_ImportUploadOrders]]
- [[Pro_TransfersOrdersHeaders]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
