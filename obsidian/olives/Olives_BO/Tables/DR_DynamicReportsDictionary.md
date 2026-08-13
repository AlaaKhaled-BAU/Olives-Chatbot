---
type: table
database: Olives_BO
name: DR_DynamicReportsDictionary
schema: dbo
tags: [#backoffice, #reporting]
foreign_keys:
referenced_by:
  - [[DR_DynamicReports_PRO]]
support_relevance: high
last_verified: 2026-07-05
---
# DR_DynamicReportsDictionary


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores dr dynamicreportsdictionary records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| ReportID | bigint | NO | ✓ |  |  |
| DictionaryID | varchar | YES | ✓ |  |  |
| DictionaryText | varchar | YES |  |  |  |
## Primary Key
CompanyID
ReportID
DictionaryID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[DR_DynamicReports_PRO]]

**Writes (0):**
_None_

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
