---
type: table
database: Olives_BO
name: CarAndSalespersonLink
schema: dbo
tags: [#backoffice, #sales]
foreign_keys:
referenced_by:
  - [[OT_AppCarAndSalesperson]]
  - [[Pro_CarAndSalespersonLink]]
  - [[Pro_DeliveryCar]]
  - [[Rpt_DeliverySales]]
  - [[Rpt_SalesPersonCarLink]]
  - [[Rpt_SalesPersonsName]]
support_relevance: high
last_verified: 2026-07-05
---
# CarAndSalespersonLink


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores carandsalespersonlink records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompanyID | smallint | YES |  |  |  |
| CarID | int | YES |  |  |  |
| WorkingDate | smalldatetime | YES |  |  |  |
| DriverID | int | YES |  |  |  |
| SalespersonID | int | YES |  |  |  |
| AssistantID | int | YES |  |  |  |
| LocationID | int | YES |  |  |  |
| Barcode | nchar | YES |  |  |  |
| FinishWorkingDate | smalldatetime | YES |  |  |  |
| Note | nvarchar | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (6):**
- [[OT_AppCarAndSalesperson]]
- [[Pro_CarAndSalespersonLink]]
- [[Pro_DeliveryCar]]
- [[Rpt_DeliverySales]]
- [[Rpt_SalesPersonCarLink]]
- [[Rpt_SalesPersonsName]]

**Writes (2):**
- [[OT_AppCarAndSalesperson]]
- [[Pro_CarAndSalespersonLink]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
