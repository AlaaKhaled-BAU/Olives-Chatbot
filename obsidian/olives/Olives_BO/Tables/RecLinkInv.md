---
type: table
database: Olives_BO
name: RecLinkInv
schema: dbo
tags: [#backoffice]
foreign_keys:
referenced_by:
  - [[Rpt_OutStandingInvoices_online]]
support_relevance: high
last_verified: 2026-07-05
---
# RecLinkInv


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores reclinkinv records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| FatherCode | nvarchar | YES |  |  |  |
| DocDueDate | smalldatetime | YES |  |  |  |
| DocDate | smalldatetime | YES |  |  |  |
| SAPInvoiceID | int | YES |  |  |  |
| InvoiceNumber | int | YES |  |  |  |
| InvoiceClientID | int | YES |  |  |  |
| InvoiceFinalAmount | float | YES |  |  |  |
| InvoiceRemainingAmount | float | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Rpt_OutStandingInvoices_online]]

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
