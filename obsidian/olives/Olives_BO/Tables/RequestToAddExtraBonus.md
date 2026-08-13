---
type: table
database: Olives_BO
name: RequestToAddExtraBonus
schema: dbo
tags: [#backoffice, #workflow]
foreign_keys:
referenced_by:
  - [[OT_ImportRequestToAddExtraBonus]]
  - [[OT_ImportRequestToAddExtraBonusAndDiscount]]
  - [[Rpt_WFFunctionsLog]]
  - [[Rpt_WorkFlowAnalysis]]
  - [[Rpt_WorkFlowFunctions]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-07-05
---
# RequestToAddExtraBonus


## Business Purpose

Workflow request records for special approvals (credit, discount, exceptions).

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| TrType | int | YES |  |  |  |
| CompanyID | smallint | YES |  |  |  |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| InvoiceAmount | float | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| OSFA_AutoID | numeric | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| BonusAmount | float | YES |  |  |  |
| BonusType | nvarchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (6):**
- [[OT_ImportRequestToAddExtraBonus]]
- [[OT_ImportRequestToAddExtraBonusAndDiscount]]
- [[Rpt_WFFunctionsLog]]
- [[Rpt_WorkFlowAnalysis]]
- [[Rpt_WorkFlowFunctions]]
- [[WF_AddWorkFlowLevels]]

**Writes (3):**
- [[OT_ImportRequestToAddExtraBonus]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Stuck in workflow**: WF level not advancing — check WF_SETUPHD and approver chain
- **Missing approver**: No user assigned at workflow level — request never processed
- **Duplicate requests**: Same request submitted multiple times — approve/reject duplicates

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
