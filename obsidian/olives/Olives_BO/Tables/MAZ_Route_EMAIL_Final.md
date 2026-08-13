---
type: table
database: Olives_BO
name: MAZ_Route_EMAIL_Final
schema: dbo
tags: [#backoffice, #gps, #sales]
foreign_keys:
referenced_by:
  - [[TotalSummaryReport_AbuODeh]]
support_relevance: high
last_verified: 2026-07-05
---
# MAZ_Route_EMAIL_Final


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores maz route email final records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| SalesmanName | nvarchar | YES |  |  |  |
| RouteDate | smalldatetime | YES |  |  |  |
| RouteCount | int | YES |  |  |  |
| PositiveCall | int | YES |  |  |  |
| NegativeCall | int | YES |  |  |  |
| OutOfRoute | int | YES |  |  |  |
| NotVIsited | int | YES |  |  |  |
| NOInvoices | int | YES |  |  |  |
| TotalCollection | float | YES |  |  |  |
| TotalAmount | float | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[TotalSummaryReport_AbuODeh]]

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
