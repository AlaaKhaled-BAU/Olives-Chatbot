---
type: table
database: Olives_BO
name: SalesmanVisitsSummary
schema: dbo
tags: [#backoffice]
foreign_keys: 0
procedures_reading: 0
support_relevance: low
last_verified: 2026-08-05
---
# SalesmanVisitsSummary

## Business Purpose

Back-office table in Olives_BO.
No procedures or foreign keys reference it in the dependency graph — likely a temp/utility table.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| VisitIDAutoID | numeric(30,0) | NO | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| TabSysID_Visit | nvarchar(50) | YES |  |  |  |
| SalesmanID | int | YES |  |  |  |
| CustomerID | bigint | YES |  |  |  |
| VisitDate | smalldatetime | YES |  |  |  |
| StartTime | datetime | YES |  |  |  |
| EndTime | datetime | YES |  |  |  |
| RouteID | int | YES |  |  |  |
| InOrOutRoute | bit | YES |  |  |  |
| IsActualVisit | bit | YES |  |  |  |
| IsWithSalesmanVisit | bit | YES |  |  |  |
| ExitNote | nvarchar(2000) | YES |  |  |  |
| IsSuccsessVisit | bit | YES |  |  |  |
| StartLogID | numeric(30,0) | YES |  |  |  |
| StartData1 | nvarchar(MAX) | YES |  |  |  |
| StartData2 | nvarchar(MAX) | YES |  |  |  |
| StartData3 | nvarchar(MAX) | YES |  |  |  |
| StartData4 | nvarchar(MAX) | YES |  |  |  |
| StartData5 | nvarchar(MAX) | YES |  |  |  |
| EndLogID | numeric(30,0) | YES |  |  |  |
| EndData1 | nvarchar(MAX) | YES |  |  |  |
| EndData2 | nvarchar(MAX) | YES |  |  |  |
| EndData3 | nvarchar(MAX) | YES |  |  |  |
| EndData4 | nvarchar(MAX) | YES |  |  |  |
| EndData5 | nvarchar(MAX) | YES |  |  |  |
| LoginMethod | nvarchar(50) | YES |  |  |  |
| LogoutMethod | nvarchar(50) | YES |  |  |  |
| LoginGPSX | nvarchar(50) | YES |  |  |  |
| LoginGPSY | nvarchar(50) | YES |  |  |  |
| LogOutGPSX | nvarchar(50) | YES |  |  |  |
| LogOutGPSY | nvarchar(50) | YES |  |  |  |
| LogInDistance | float | YES |  |  |  |
| LogOutDistance | float | YES |  |  |  |
| StartBatteryPerc | float | YES |  |  |  |
| EndBattaryPerc | float | YES |  |  |  |
## Primary Key
VisitIDAutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

Referenced by 0 procedure(s): 0 writing, 0 reading.
_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
~0 rows (estimate from sys.partitions).
## Common Issues

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
