---
type: table
database: Olives_BO
name: SurveySalesmansAnswers
schema: dbo
tags: [#backoffice, #sales, #survey]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportSalesmanSurveyAnswers]]
support_relevance: high
last_verified: 2026-07-05
---
# SurveySalesmansAnswers


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores surveysalesmansanswers records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| Salesman_Survey_No | bigint | NO | ✓ |  |  |
| Question_No | int | NO | ✓ |  |  |
| Answer | varchar | YES |  |  |  |
## Primary Key
CompanyID
Salesman_Survey_No
Question_No
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (1):**
- [[OT_ImportSalesmanSurveyAnswers]]

**Writes (1):**
- [[OT_ImportSalesmanSurveyAnswers]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
