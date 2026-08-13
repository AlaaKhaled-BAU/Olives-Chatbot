---
type: table
database: Olives_BO
name: RequestToExceedCustomerCreditLimitInOrder
schema: dbo
tags: [#backoffice, #billing, #customer, #order, #workflow]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportRequestToExceedCustomerCreditLimitInOrder]]
  - [[Rpt_ExceededLimit]]
  - [[Rpt_MasterOrders]]
  - [[Rpt_WFFunctionsLog]]
  - [[Rpt_WorkFlowAnalysis]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-07-05
---
# RequestToExceedCustomerCreditLimitInOrder


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
| OSFA_AutoID | numeric | YES |  |  |  |
| TabletSysID | varchar | YES |  |  |  |
| CustomerCreditLimit | float | YES |  |  |  |
| CustomerBanalce | float | YES |  |  |  |
| CustomerChqBanalce | float | YES |  |  |  |
| ExceedAmount | float | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (5):**
- [[OT_ImportRequestToExceedCustomerCreditLimitInOrder]]
- [[Rpt_ExceededLimit]]
- [[Rpt_MasterOrders]]
- [[Rpt_WFFunctionsLog]]
- [[Rpt_WorkFlowAnalysis]]

**Writes (3):**
- [[OT_ImportRequestToExceedCustomerCreditLimitInOrder]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate customers**: Multiple records with same name/phone created during sync — support agent sees duplicate entries in dropdowns
- **Orphan references**: Customer records referenced by transactions that were soft-deleted — causes FK violation on cleanup
- **Balance mismatch**: CustomerBalance field diverges from actual calculated balance — run reconciliation proc
- **Suspend stuck**: IsSuspended flag not clearing after payment — check WF approval chain
- **GPS not collected**: IsCollectedGPS flag false — affects route optimization

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
