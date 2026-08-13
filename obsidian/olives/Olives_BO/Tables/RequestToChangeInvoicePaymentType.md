---
type: table
database: Olives_BO
name: RequestToChangeInvoicePaymentType
schema: dbo
tags: [#backoffice, #billing, #legal, #reference, #workflow]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportRequestToChangeInvoicePaymentType]]
  - [[Rpt_WFFunctionsLog]]
  - [[Rpt_WorkFlowFunctions]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-07-05
---
# RequestToChangeInvoicePaymentType


## Business Purpose

Workflow request records for special approvals (credit, discount, exceptions).

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  | ✓ | [[Companies]] |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| InvoiceAmount | float | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| InvDueDays | int | YES |  |  |  |
| IsCanceled | bit | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (4):**
- [[OT_ImportRequestToChangeInvoicePaymentType]]
- [[Rpt_WFFunctionsLog]]
- [[Rpt_WorkFlowFunctions]]
- [[WF_AddWorkFlowLevelOne]]

**Writes (3):**
- [[OT_ImportRequestToChangeInvoicePaymentType]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Orphan lines**: Detail rows without matching header — causes sync failures
- **Posting failure**: IsPosted flag stuck false — check ERP integration log
- **Duplicate vouchers**: Same VouNo generated for different transactions — run dedup check
- **Currency mismatch**: ExRate different from CurrenciesRate table — financial reconciliation off
- **Void inconsistency**: IsVoid flag but original transaction still active — check WF approval

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[OSFA_DB/Procedures/SetRequestCanceled]]
