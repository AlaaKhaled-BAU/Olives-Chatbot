---
type: table
database: Olives_BO
name: RequestToIncreaseCustomerCreditlimit
schema: dbo
tags: [#backoffice, #billing, #customer, #workflow]
foreign_keys:
referenced_by:
  - [[Rpt_IncreaseCreditLimit]]
  - [[Rpt_IncreaseCreditLimit_forALPHA]]
  - [[WF_AddRequestToIncreaseCustomerCreditlimit]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-07-05
---
# RequestToIncreaseCustomerCreditlimit


## Business Purpose

Workflow request records for special approvals (credit, discount, exceptions).

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| OrderYear | smallint | YES |  |  |  |
| OrderNo | int | YES |  |  |  |
| IsAproved | bit | YES |  |  |  |
| CustomerCreditLimit | float | YES |  |  |  |
| CustomerBanalce | float | YES |  |  |  |
| CustomerChqBanalce | float | YES |  |  |  |
| OrderAmount | float | YES |  |  |  |
| ExceedAmount | float | YES |  |  |  |
| DueDays | int | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| SID | numeric | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[Rpt_IncreaseCreditLimit]]
- [[Rpt_IncreaseCreditLimit_forALPHA]]
- [[WF_AddRequestToIncreaseCustomerCreditlimit]]

**Writes (3):**
- [[WF_AddRequestToIncreaseCustomerCreditlimit]]
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
