---
type: table
database: Olives_BO
name: ErrorLog
schema: dbo
tags: [#backoffice, #log]
foreign_keys:
referenced_by:
  - [[Pro_ErrorLog_BO]]
support_relevance: low
last_verified: 2026-07-05
---
# ErrorLog


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores errorlog records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ID | numeric | YES | ✓ |  |  |
| MacAddress | nvarchar | YES |  |  |  |
| IPAddress | nvarchar | YES |  |  |  |
| PCName | nvarchar | YES |  |  |  |
| UserID | nvarchar | YES |  |  |  |
| TrDateTime | datetime | YES |  |  |  |
| CompanyID | smallint | YES |  |  |  |
| Uri | nvarchar | YES |  |  |  |
| ErrorDescription | nvarchar | YES |  |  |  |
## Primary Key
ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_ErrorLog_BO]]

**Writes (1):**
- [[Pro_ErrorLog_BO]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Rapid growth**: Table size growing fast — archive old records periodically
- **Orphan log entries**: No corresponding source transaction — investigate data source
- **No cleanup**: No purge job configured — disk space may fill up

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
