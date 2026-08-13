---
type: table
database: Olives_BO
name: SurveyCustomersAnswers
schema: dbo
tags: [#backoffice, #customer, #survey]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OT_ImportCustomerSurveyAnswers]]
  - [[Pro_SurveyCustomersAnswers]]
  - [[Rpt_CompetitveCompanies_ByLocation]]
  - [[Rpt_Customers_Notes]]
  - [[Rpt_SurveryAllQuestions]]
  - [[Rpt_SurveyCustomersAnswerDetails]]
  - [[Rpt_SurveyCustomersSummary]]
  - [[Rpt_Surveys]]
support_relevance: high
last_verified: 2026-07-05
---
# SurveyCustomersAnswers


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores surveycustomersanswers records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| Cust_Survey_No | bigint | NO | ✓ |  |  |
| Question_No | int | NO | ✓ |  |  |
| Answer | varchar | YES |  |  |  |
## Primary Key
CompanyID
Cust_Survey_No
Question_No
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (8):**
- [[OT_ImportCustomerSurveyAnswers]]
- [[Pro_SurveyCustomersAnswers]]
- [[Rpt_CompetitveCompanies_ByLocation]]
- [[Rpt_Customers_Notes]]
- [[Rpt_SurveryAllQuestions]]
- [[Rpt_SurveyCustomersAnswerDetails]]
- [[Rpt_SurveyCustomersSummary]]
- [[Rpt_Surveys]]

**Writes (1):**
- [[OT_ImportCustomerSurveyAnswers]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Duplicate customers**: Multiple records with same name/phone created during sync — support agent sees duplicate entries in dropdowns
- **Orphan references**: Customer records referenced by transactions that were soft-deleted — causes FK violation on cleanup
- **Balance mismatch**: CustomerBalance field diverges from actual calculated balance — run reconciliation proc
- **Suspend stuck**: IsSuspended flag not clearing after payment — check WF approval chain
- **GPS not collected**: IsCollectedGPS flag false — affects route optimization

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
