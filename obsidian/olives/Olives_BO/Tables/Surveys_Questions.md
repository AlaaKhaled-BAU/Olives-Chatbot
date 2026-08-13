---
type: table
database: Olives_BO
name: Surveys_Questions
schema: dbo
tags: [#backoffice, #survey]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Pro_Surveys]]
  - [[Pro_Surveys_Questions]]
  - [[Rpt_SurveryAllQuestions]]
  - [[Rpt_SurveryMultiSelection]]
  - [[Rpt_SurveyCustomersAnswerDetails]]
  - [[Rpt_SurveyCustomersSummary]]
  - [[Rpt_Surveys]]
support_relevance: high
last_verified: 2026-07-05
---
# Surveys_Questions


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores surveys questions records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| Survey_ID | int | NO | ✓ |  |  |
| Question_No | int | NO | ✓ |  |  |
| Template_No | int | YES |  |  |  |
| Question_String | varchar | YES |  |  |  |
| SortID | int | YES |  |  |  |
| IsRequired | bit | YES |  |  |  |
## Primary Key
CompanyID
Survey_ID
Question_No
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (7):**
- [[Pro_Surveys]]
- [[Pro_Surveys_Questions]]
- [[Rpt_SurveryAllQuestions]]
- [[Rpt_SurveryMultiSelection]]
- [[Rpt_SurveyCustomersAnswerDetails]]
- [[Rpt_SurveyCustomersSummary]]
- [[Rpt_Surveys]]

**Writes (1):**
- [[Pro_Surveys_Questions]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Incomplete surveys**: Questions not answered — survey results incomplete
- **Orphan answers**: Answer records without matching survey header — data integrity issue
- **Wrong survey assigned**: Customer received wrong survey version — reporting mismatch

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
