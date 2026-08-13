---
type: table
database: Olives_BO
name: SalespersonsDailyCurrencyTotals
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
referenced_by:
  - [[DeleteSalespersonsDailyCurrencyTotals]]
  - [[OT_ActualAmountOnline_Tablet_Insert]]
  - [[Pro_ActualAmountOnline_Tablet]]
support_relevance: high
last_verified: 2026-07-05
---
# SalespersonsDailyCurrencyTotals


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonsdailycurrencytotals records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| SalesPersonID | int | NO | ✓ |  |  |
| TrDateTime | date | NO | ✓ |  |  |
| CurrencyID | int | NO | ✓ |  |  |
| ActualAmount | float | YES |  |  |  |
| SysCashAmount | float | YES |  |  |  |
## Primary Key
CompanyID
SalesPersonID
TrDateTime
CurrencyID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (3):**
- [[DeleteSalespersonsDailyCurrencyTotals]]
- [[OT_ActualAmountOnline_Tablet_Insert]]
- [[Pro_ActualAmountOnline_Tablet]]

**Writes (1):**
- [[OT_ActualAmountOnline_Tablet_Insert]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
