---
type: table
database: Olives_BO
name: OLV_PDC
schema: dbo
tags: [#backoffice]
foreign_keys:
referenced_by:
  - [[CustomersFinancialStatus]]
support_relevance: high
last_verified: 2026-07-05
---
# OLV_PDC


## Business Purpose

- `CheckNum` [int] - `CheckSum` [float] - `RcptDate` [smalldatetime] - `CardCode` [nvarchar](50) - `CardName` [nvarchar](200) - `CheckDate` [smalldatetime] - `BankName` [nvarchar](200) - `SalespersonID` [int] - `SalesmanName` [nvarchar](200)

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CheckNum | int | YES |  |  |  |
| CheckSum | float | YES |  |  |  |
| RcptDate | smalldatetime | YES |  |  |  |
| CardCode | nvarchar | YES |  |  |  |
| CardName | nvarchar | YES |  |  |  |
| CheckDate | smalldatetime | YES |  |  |  |
| BankName | nvarchar | YES |  |  |  |
| SalespersonID | int | YES |  |  |  |
| SalesmanName | nvarchar | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[CustomersFinancialStatus]]

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
