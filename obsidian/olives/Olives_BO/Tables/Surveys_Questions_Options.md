---
type: table
database: Olives_BO
name: Surveys_Questions_Options
schema: dbo
tags: [#backoffice, #survey]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Pro_Surveys]]
  - [[Pro_Surveys_Questions]]
  - [[Pro_Surveys_Questions_Options]]
  - [[Rpt_SurveryMultiSelection]]
  - [[Rpt_SurveyCustomersAnswerDetails]]
  - [[Rpt_Surveys]]
support_relevance: high
last_verified: 2026-07-05
---
# Surveys_Questions_Options


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores surveys questions options records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| Survey_ID | int | NO | ✓ |  |  |
| Question_No | int | NO | ✓ |  |  |
| Option_No | int | NO | ✓ |  |  |
| Option_Desc | varchar | YES |  |  |  |
| SortID | int | YES |  |  |  |
| OptionImage | image | YES |  |  |  |
## Primary Key
CompanyID
Survey_ID
Question_No
Option_No
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (6):**
- [[Pro_Surveys]]
- [[Pro_Surveys_Questions]]
- [[Pro_Surveys_Questions_Options]]
- [[Rpt_SurveryMultiSelection]]
- [[Rpt_SurveyCustomersAnswerDetails]]
- [[Rpt_Surveys]]

**Writes (1):**
- [[Pro_Surveys_Questions_Options]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing reference values**: Required dropdown items not present — selection fails on tablet
- **Duplicate codes**: Same code used for different descriptions — mapping ambiguity
- **Orphan references**: Referenced by deleted records — FK violation on delete attempt

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
