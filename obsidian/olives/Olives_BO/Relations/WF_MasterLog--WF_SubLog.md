---
type: relation
database: Olives_BO
name: WF_MasterLog--WF_SubLog
tags: [#fk, #workflow, #approval]
support_relevance: high
parent_table: [[WF_SubLog]]
referenced_table: [[WF_MasterLog]]
columns: "WF_SubLog.ReqID → WF_MasterLog.ReqID"
last_verified: 2026-10-03
verified_source: live Olives_BO & WF_AddWorkFlowLevels
---

# WF_SubLog → WF_MasterLog

**Join Key**: `WF_SubLog.ReqID = WF_MasterLog.ReqID`

**Business meaning**: Connects granular supervisor approval decisions/levels (`WF_SubLog`) to the overall workflow master request lifecycle (`WF_MasterLog`). Each master workflow request has one or more approval levels / approvers recorded in sub log.

## Cardinality & Filtering
- **1-to-many**: One `WF_MasterLog` row can have multiple `WF_SubLog` rows (one per approval level or assigned position).
- **Supervisor inbox join**:
```sql
SELECT m.ReqID, m.FunctionID, m.Ref1, m.LastStatus, s.ActionNeed, s.Action, s.ARLevel
FROM t.WF_MasterLog m
INNER JOIN t.WF_SubLog s ON m.ReqID = s.ReqID
WHERE s.PositionID = @PositionID
  AND s.ActionNeed = N'AR'
  AND s.Action IS NULL;
```

## Tenancy
Chatbot queries `t.WF_MasterLog` and `t.WF_SubLog`. Both tenant views filter automatically by `SESSION_CONTEXT(N'CompanyID')`.

## See also
- [[WF_MasterLog]]
- [[WF_SubLog]]
- [[WF_Functions]]
- [[Workflow_Approval_Codes]]
