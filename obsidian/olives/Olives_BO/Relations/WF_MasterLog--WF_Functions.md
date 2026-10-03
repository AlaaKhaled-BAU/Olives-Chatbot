---
type: relation
database: Olives_BO
name: WF_MasterLog--WF_Functions
tags: [#fk, #workflow, #catalog]
support_relevance: high
parent_table: [[WF_MasterLog]]
referenced_table: [[WF_Functions]]
columns: "WF_MasterLog.FunctionID → WF_Functions.FunctionID"
last_verified: 2026-10-03
verified_source: live Olives_BO
---

# WF_MasterLog → WF_Functions

**Join Key**: `WF_MasterLog.FunctionID = WF_Functions.FunctionID`

**Business meaning**: Identifies the business document or request type governed by the workflow request (e.g. FunctionID 2 = Credit Limit, 5 = Out of Route Visit, 6 = Sales Order, 11 = Discount).

## Tenancy
`t.WF_MasterLog` is company-scoped. `t.WF_Functions` is a system catalog table of workflow types.

## See also
- [[WF_MasterLog]]
- [[WF_Functions]]
- [[Workflow_Approval_Codes]]
