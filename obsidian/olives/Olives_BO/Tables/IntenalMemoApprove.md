---
type: table
database: Olives_BO
name: IntenalMemoApprove
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[IntenalMemoApprove]]
referenced_by:
  - [[InternalMemo_Insert]]
  - [[Pro_InternalMemo]]
  - [[Rpt_IntenalMemo]]
support_relevance: high
last_verified: 2026-07-05
---
# IntenalMemoApprove


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores intenalmemoapprove records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ | ✓ | [[IntenalMemoApprove]] |
| CompanyID | smallint | NO | ✓ | ✓ | [[IntenalMemoApprove]] |
| IntenalMemoID | numeric | YES |  |  |  |
| UserID | nvarchar | YES |  |  |  |
| AssignDate | smalldatetime | YES |  |  |  |
| Approve | bit | YES |  |  |  |
| ApproveDate | smalldatetime | YES |  |  |  |
| Note | nvarchar | YES |  |  |  |
| IsPosted | bit | YES |  |  |  |
## Primary Key
AutoID
CompanyID
## Foreign Keys
AutoID, CompanyID -> [[IntenalMemoApprove]](AutoID, CompanyID)
## Known Circular Dependencies
- Self-referencing FK (references itself via AutoID/CompanyID).
## Impact / Procedures Using This Table

**Reads (3):**
- [[InternalMemo_Insert]]
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
