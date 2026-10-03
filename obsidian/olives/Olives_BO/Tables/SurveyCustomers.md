---
type: table
database: Olives_BO
name: SurveyCustomers
schema: dbo
tags: [#backoffice, #customer, #survey]
foreign_keys:
  - [[Companies]]
  - [[Customers]]
referenced_by:
  - [[OT_ImportCustomerSurveyAnswers]]
  - [[Pro_CompanyParameters]]
  - [[Pro_MapTransactionLog]]
  - [[Pro_SurveyCustomers]]
  - [[Rpt_CompetitveCompanies_ByLocation]]
  - [[Rpt_Customers_Notes]]
  - [[Rpt_SurveryAllQuestions]]
  - [[Rpt_SurveryMultiSelection]]
  - [[Rpt_SurveyCustomersAnswerDetails]]
  - [[Rpt_SurveyCustomersSummary]]
  - [[Rpt_Surveys]]
support_relevance: high
last_verified: 2026-07-05
---
# SurveyCustomers


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores surveycustomers records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| Cust_Survey_No | bigint | NO | ✓ |  |  |
| CompanyID | smallint | NO | ✓ | ✓ | [[Customers]] |
| Survey_ID | int | NO | ✓ |  |  |
| Customer_No | bigint | NO | ✓ | ✓ | [[Customers]] |
| Survey_Date | datetime | YES |  |  |  |
| GPSX | varchar | YES |  |  |  |
| GPSY | varchar | YES |  |  |  |
| SalesmanNo | nvarchar | YES |  |  |  |
| PostedToERP | bit | YES |  |  |  |
| ItemCode | nvarchar | YES |  |  |  |
## Primary Key
Cust_Survey_No
CompanyID
Survey_ID
Customer_No
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, Customer_No -> [[Customers]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (12):**
- [[OT_ImportCustomerSurveyAnswers]]
- [[Pro_CompanyParameters]]
- [[Pro_MapTransactionLog]]
- [[Pro_SurveyCustomers]]
- [[Rpt_CompetitveCompanies_ByLocation]]
- [[Rpt_Customers_Notes]]
- [[Rpt_SurveryAllQuestions]]
- [[Rpt_SurveryMultiSelection]]
- [[Rpt_SurveyCustomersAnswerDetails]]
- [[Rpt_SurveyCustomersSummary]]
- [[Rpt_Surveys]]

**Writes (3):**
- [[OT_ImportCustomerSurveyAnswers]]
- [[Pro_SurveyCustomers]]

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
