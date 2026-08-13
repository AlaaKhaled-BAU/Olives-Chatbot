---
type: table
database: Olives_BO
name: POADetails
schema: dbo
tags: [#backoffice]
foreign_keys:
referenced_by:
  - [[POAOnlineReport]]
  - [[POA_Save]]
support_relevance: high
last_verified: 2026-07-05
---
# POADetails


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores poadetails records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| POAID | bigint | NO | ✓ |  |  |
| CustomerID | bigint | NO | ✓ |  |  |
| VisitCount | int | YES |  |  |  |
## Primary Key
CompanyID
POAID
CustomerID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (2):**
- [[POAOnlineReport]]
- [[POA_Save]]

**Writes (1):**
- [[POA_Save]]

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
