---
type: table
database: Olives_BO
name: SalespersonsAssistants
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Pro_SalespersonsAssistants]]
  - [[Rpt_Assistants]]
  - [[Rpt_AssistantsSales]]
  - [[Rpt_AssistantsSalesDaily]]
support_relevance: high
last_verified: 2026-07-05
---
# SalespersonsAssistants


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonsassistants records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| Tel | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| NationalID | nvarchar | YES |  |  |  |
| Nationality | nvarchar | YES |  |  |  |
| IsSuspended | bit | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (4):**
- [[Pro_SalespersonsAssistants]]
- [[Rpt_Assistants]]
- [[Rpt_AssistantsSales]]
- [[Rpt_AssistantsSalesDaily]]

**Writes (1):**
- [[Pro_SalespersonsAssistants]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
