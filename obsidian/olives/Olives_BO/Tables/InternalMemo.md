---
type: table
database: Olives_BO
name: InternalMemo
schema: dbo
tags: [#backoffice]
foreign_keys:
referenced_by:
  - [[InternalMemo_Insert]]
  - [[OLIVES_INTEG_INTERNALMEMO]]
  - [[Pro_InternalMemo]]
  - [[Rpt_IntenalMemo]]
support_relevance: high
last_verified: 2026-07-05
---
# InternalMemo


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores internalmemo records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| TrDateTime | datetime | YES |  |  |  |
| SalesmanNo | int | YES |  |  |  |
| MemoSubject | nvarchar | YES |  |  |  |
| MemoDepartment | nvarchar | YES |  |  |  |
| MemoDescription | nvarchar | YES |  |  |  |
| FirstApproval | bit | YES |  |  |  |
| FirstApprovalDescription | nvarchar | YES |  |  |  |
| FirstApprovalUserID | varchar | YES |  |  |  |
| SecondApproval | bit | YES |  |  |  |
| SecondApprovalDescription | nvarchar | YES |  |  |  |
| SecondApprovalUserID | varchar | YES |  |  |  |
| DeviceSysID | varchar | YES |  |  |  |
| SendToUserID | varchar | YES |  |  |  |
| CustID | varchar | YES |  |  |  |
| MerchAutoID | numeric | YES |  |  |  |
| UserID | varchar | YES |  |  |  |
| CreatedBy | varchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (4):**
- [[InternalMemo_Insert]]
- [[OLIVES_INTEG_INTERNALMEMO]]
- [[Pro_InternalMemo]]
- [[Rpt_IntenalMemo]]

**Writes (2):**
- [[InternalMemo_Insert]]
- [[Pro_InternalMemo]]

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
