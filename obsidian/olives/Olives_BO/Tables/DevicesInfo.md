---
type: table
database: Olives_BO
name: DevicesInfo
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Pro_DevicesInfo]]
support_relevance: high
last_verified: 2026-07-05
---
# DevicesInfo


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores devicesinfo records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | YES |  | ✓ | [[Companies]] |
| AutoID | numeric | YES | ✓ |  |  |
| DeviceName | nvarchar | YES |  |  |  |
| MacAddress | nvarchar | YES |  |  |  |
| CreateDate | smalldatetime | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_DevicesInfo]]

**Writes (1):**
- [[Pro_DevicesInfo]]

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
