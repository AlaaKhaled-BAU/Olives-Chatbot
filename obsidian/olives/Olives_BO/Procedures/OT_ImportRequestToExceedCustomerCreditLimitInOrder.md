---
type: procedure
database: Olives_BO
name: OT_ImportRequestToExceedCustomerCreditLimitInOrder
schema: dbo
tags: [#backoffice, #billing, #customer, #mobile, #order, #workflow]
reads_from:
  - ImportRequest
  - [[RequestToExceedCustomerCreditLimitInOrder]]
  - [[WF_MasterLog]]
  - [[WF_SubLog]]
  - `dbo`
writes_to:
  - [[OT_RequestToExceedCustomerCreditLimitInOrder]]
  - [[RequestToExceedCustomerCreditLimitInOrder]]
  - [[WF_MasterLog]]
  - [[WF_SubLog]]
called_by:
  - [[WF_AddWorkFlowLevelOne]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportRequestToExceedCustomerCreditLimitInOrder


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ImportRequest, RequestToExceedCustomerCreditLimitInOrder, WF_MasterLog, WF_SubLog, dbo. Writes OT_RequestToExceedCustomerCreditLimitInOrder, RequestToExceedCustomerCreditLimitInOrder, WF_MasterLog, WF_SubLog. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- ImportRequest
- [[RequestToExceedCustomerCreditLimitInOrder]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
- `dbo`
## Tables Written
- [[OT_RequestToExceedCustomerCreditLimitInOrder]]
- [[RequestToExceedCustomerCreditLimitInOrder]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
## Callers
_None (no known callers)_
## Callees
- [[WF_AddWorkFlowLevelOne]]
## Impact / Dependencies

**Tables Read**
- ImportRequest
- [[RequestToExceedCustomerCreditLimitInOrder]]
- [[WF_MasterLog]]
- [[WF_SubLog]]
- dbo

**Tables Written**
- [[OT_RequestToExceedCustomerCreditLimitInOrder]]
- [[RequestToExceedCustomerCreditLimitInOrder]]
- [[WF_MasterLog]]
- [[WF_SubLog]]

**Callers**
- [[WF_AddWorkFlowLevelOne]]

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
