---
type: table
database: Olives_BO
name: RequestToExceedInvoiceCount
schema: dbo
tags: [#backoffice, #billing, #workflow]
foreign_keys:
referenced_by:
  - [[OT_ImportRequestToExceedInvoiceCount]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-07-05
---
# RequestToExceedInvoiceCount


## Business Purpose

Workflow request records for special approvals (credit, discount, exceptions).

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| SalesPersonNo | int | YES |  |  |  |
| CustomerNo | bigint | YES |  |  |  |
| InvoiceCount | int | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| Latitude | nvarchar | YES |  |  |  |
| Longitude | nvarchar | YES |  |  |  |
| OSFA_AutoID | numeric | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_ImportRequestToExceedInvoiceCount]]

**Writes (3):**
- [[OT_ImportRequestToExceedInvoiceCount]]
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
