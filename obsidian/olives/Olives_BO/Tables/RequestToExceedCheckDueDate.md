---
type: table
database: Olives_BO
name: RequestToExceedCheckDueDate
schema: dbo
tags: [#backoffice, #workflow]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportRequestToExceedCheckDueDate]]
  - [[Rpt_MasterOrders]]
  - [[Rpt_WFFunctionsLog]]
  - [[Rpt_WorkFlowAnalysis]]
  - [[Rpt_WorkFlowExceeds]]
  - [[Rpt_WorkFlowFunctions]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-07-05
---
# RequestToExceedCheckDueDate


## Business Purpose

Workflow request records for special approvals (credit, discount, exceptions).

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  | ✓ | [[Companies]] |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| ReceiptAmount | float | YES |  |  |  |
| ChecksInfo | nvarchar | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| CustomerDueDays | smallint | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (7):**
- [[OT_ImportRequestToExceedCheckDueDate]]
- [[Rpt_MasterOrders]]
- [[Rpt_WFFunctionsLog]]
- [[Rpt_WorkFlowAnalysis]]
- [[Rpt_WorkFlowExceeds]]
- [[Rpt_WorkFlowFunctions]]
- [[WF_AddWorkFlowLevelOne]]

**Writes (3):**
- [[OT_ImportRequestToExceedCheckDueDate]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Partial payment not tracked**: Receipt amount less than invoice total — aging report shows incorrect balance
- **Check bounce**: CheckStatus not updated after bank return — customer credit not restored
- **Currency conversion error**: ExRate differs from daily rate — receipt in wrong amount
- **Duplicate receipts**: Same payment applied twice — customer credit balance wrong

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
