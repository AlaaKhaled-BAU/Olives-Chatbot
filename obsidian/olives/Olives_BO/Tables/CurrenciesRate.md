---
type: table
database: Olives_BO
name: CurrenciesRate
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Companies]]
  - [[Currencies]]
referenced_by:
  - [[OT_CustIssueAmount_Update]]
  - [[OT_ImportSalesInvoices]]
  - [[Pro_CurrenciesRate]]
support_relevance: high
last_verified: 2026-07-05
---
# CurrenciesRate


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores currenciesrate records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| CurrencyID | smallint | NO | ✓ | ✓ | [[Currencies]] |
| ExDate | smalldatetime | NO | ✓ |  |  |
| ExRate | float | YES |  |  |  |
| EntryDate | smalldatetime | YES |  |  |  |
## Primary Key
CompanyID
CurrencyID
ExDate
## Foreign Keys
CompanyID -> [[Companies]](ID)
CurrencyID -> [[Currencies]](ID)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_CustIssueAmount_Update]]
- [[OT_ImportSalesInvoices]]
- [[Pro_CurrenciesRate]]

**Writes (1):**
- [[Pro_CurrenciesRate]]

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
