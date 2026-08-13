---
type: table
database: Olives_BO
name: SalespersonsMessagesDefinition
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
referenced_by:
  - [[Pro_SalespersonsMessagesDefinition]]
support_relevance: high
last_verified: 2026-07-05
---
# SalespersonsMessagesDefinition


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores salespersonsmessagesdefinition records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| ID | int | NO | ✓ |  |  |
| MessageTitle | nvarchar | YES |  |  |  |
| MessageText | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (1):**
- [[Pro_SalespersonsMessagesDefinition]]

**Writes (1):**
- [[Pro_SalespersonsMessagesDefinition]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Olives_BO/Tables/CustomerSalesByCategory]]
- [[Olives_BO/Tables/SpecialCustomerTarget]]
