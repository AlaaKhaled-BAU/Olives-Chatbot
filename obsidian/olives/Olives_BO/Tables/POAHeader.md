---
type: table
database: Olives_BO
name: POAHeader
schema: dbo
tags: [#backoffice]
foreign_keys:

referenced_by:
  - [[POAOnlineReport]]
  - [[POA_Save]]
  - [[WF_AddWorkFlowLevelOne]]
  - [[WF_AddWorkFlowLevels]]
support_relevance: high
last_verified: 2026-07-05
---
# POAHeader


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores poaheader records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| POAID | bigint | NO | ✓ |  |  |
| SalesPersonID | int | YES |  |  |  |
| POAYear | int | YES |  |  |  |
| POAMonth | int | YES |  |  |  |
| Approved | bit | YES |  |  |  |
| RejectedNotes | varchar | YES |  |  |  |

## Primary Key
CompanyID
POAID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[POAOnlineReport]]
- [[POA_Save]]
- [[WF_AddWorkFlowLevels]]

**Writes (3):**
- [[POA_Save]]
- [[WF_AddWorkFlowLevelOne]]
- [[WF_AddWorkFlowLevels]]

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
