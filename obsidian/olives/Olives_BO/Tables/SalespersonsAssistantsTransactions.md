---
type: table
database: Olives_BO
name: SalespersonsAssistantsTransactions
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
  - [[SalesPersons]]
  - [[SalespersonsAssistants]]
referenced_by:
  - [[OT_ImportActionLog]]
  - [[Pro_SalespersonsAssistants]]
  - [[Rpt_Assistants]]
  - [[Rpt_AssistantsSales]]
  - [[Rpt_AssistantsSalesDaily]]
support_relevance: high
last_verified: 2026-07-05
---
# SalespersonsAssistantsTransactions


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonsassistantstransactions records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[SalespersonsAssistants]] |
| TrDate | smalldatetime | NO | ✓ |  |  |
| SalespersonID | int | NO | ✓ | ✓ | [[SalesPersons]] |
| AssistantID | int | NO | ✓ | ✓ | [[SalespersonsAssistants]] |
## Primary Key
CompanyID
TrDate
SalespersonID
AssistantID
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, SalespersonID -> [[SalesPersons]](CompanyID, ID)
CompanyID, AssistantID -> [[SalespersonsAssistants]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (4):**
- [[Pro_SalespersonsAssistants]]
- [[Rpt_Assistants]]
- [[Rpt_AssistantsSales]]
- [[Rpt_AssistantsSalesDaily]]

**Writes (2):**
- [[OT_ImportActionLog]]
- [[Pro_SalespersonsAssistants]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Orphan lines**: Detail rows without matching header — causes sync failures
- **Posting failure**: IsPosted flag stuck false — check ERP integration log
- **Duplicate vouchers**: Same VouNo generated for different transactions — run dedup check
- **Currency mismatch**: ExRate different from CurrenciesRate table — financial reconciliation off
- **Void inconsistency**: IsVoid flag but original transaction still active — check WF approval

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
