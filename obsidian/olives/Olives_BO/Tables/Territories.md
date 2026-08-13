---
type: table
database: Olives_BO
name: Territories
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Pro_Territories]]
  - [[TerritoriesOnlineReport]]
support_relevance: high
last_verified: 2026-07-05
---
# Territories


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores territories records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| TerritoryID | bigint | NO | ✓ |  |  |
| SalesPersonID | int | YES |  |  |  |
| TerritoryType | nvarchar | YES |  |  |  |
| TrDate | smalldatetime | YES |  |  |  |
| Notes | nvarchar | YES |  |  |  |
| TrDateTime | smalldatetime | YES |  |  |  |
## Primary Key
CompanyID
TerritoryID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (2):**
- [[Pro_Territories]]
- [[TerritoriesOnlineReport]]

**Writes (1):**
- [[Pro_Territories]]

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
