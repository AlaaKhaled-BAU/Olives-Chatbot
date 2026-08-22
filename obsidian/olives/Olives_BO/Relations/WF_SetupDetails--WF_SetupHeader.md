---
type: relation
database: Olives_BO
name: WF_SetupDetails--WF_SetupHeader
tags: [#fk, #workflow, #backoffice]
support_relevance: high
parent_table: [[WF_SetupDetails]]
referenced_table: [[WF_SetupHeader]]
columns: "WF_SetupDetails.AutoID → WF_SetupHeader.AutoID"
last_verified: 2026-08-22
verified_source: work/morec/schema_cache.json
---

# WF_SetupDetails → WF_SetupHeader

**FK**: WF_SetupDetails.AutoID → [[WF_SetupHeader]].AutoID

**Business meaning**: Approval levels under a workflow setup: LevelID ordering, IsFinalApprove, SeeAllRequest. Header defines which function/object the workflow governs (FunctionID, FromType/FromID).

## Tenancy

Chatbot queries `t.WF_SetupDetails` and `t.WF_SetupHeader` only; both views auto-filter `SESSION_CONTEXT(N'CompanyID')`. On raw dbo tables always include the CompanyID half shown above.

## See also

- [[WF_SetupDetails]]
- [[WF_SetupHeader]]
- [[WF_SetupHeader]]
- [[_RequestTo-Join-Conventions]]
