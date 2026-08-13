---
type: table
database: Olives_BO
name: SurveySalesmans
schema: dbo
tags: [#backoffice, #sales, #survey]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportSalesmanSurveyAnswers]]
support_relevance: high
last_verified: 2026-07-05
---
# SurveySalesmans


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores surveysalesmans records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| Salesman_Survey_No | bigint | NO | ✓ |  |  |
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| Survey_ID | int | NO | ✓ |  |  |
| Survey_Date | datetime | YES |  |  |  |
| GPSX | varchar | YES |  |  |  |
| GPSY | varchar | YES |  |  |  |
| SalesmanNo | nvarchar | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
| ForSalesmanNo | int | YES |  |  |  |
## Primary Key
Salesman_Survey_No
CompanyID
Survey_ID
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
