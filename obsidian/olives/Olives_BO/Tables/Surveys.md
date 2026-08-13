---
type: table
database: Olives_BO
name: Surveys
schema: dbo
tags: [#backoffice, #survey]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[Pro_MapTransactionLog]]
  - [[Pro_Surveys]]
  - [[Pro_Surveys_Questions]]
  - [[Rpt_SurveyCustomersAnswerDetails]]
  - [[Rpt_Surveys]]
support_relevance: high
last_verified: 2026-07-05
---
# Surveys


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores surveys records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| Survey_ID | int | NO | ✓ |  |  |
| Survey_Name | varchar | YES |  |  |  |
| Active | bit | YES |  |  |  |
| IsRequired | bit | YES |  |  |  |
| IsSalesmanSurvey | bit | YES |  |  |  |
## Primary Key
CompanyID
Survey_ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (5):**
- [[Pro_MapTransactionLog]]
- [[Pro_Surveys]]
- [[Pro_Surveys_Questions]]
- [[Rpt_SurveyCustomersAnswerDetails]]
- [[Rpt_Surveys]]

**Writes (1):**
- [[Pro_Surveys]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Incomplete surveys**: Questions not answered — survey results incomplete
- **Orphan answers**: Answer records without matching survey header — data integrity issue
- **Wrong survey assigned**: Customer received wrong survey version — reporting mismatch

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
