---
type: table
database: Olives_BO
name: SurveyProspectiveCustomers
schema: dbo
tags: [#backoffice, #customer, #survey]
foreign_keys:
  - [[Companies]]
  - [[ProspectiveCustomers]]
referenced_by:
  - [[OT_ImportCustomerSurveyAnswers]]
  - [[Pro_CompanyParameters]]
  - [[Rpt_Customers_NotesProcpective]]
support_relevance: high
last_verified: 2026-07-05
---
# SurveyProspectiveCustomers


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores surveyprospectivecustomers records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| Cust_Survey_No | bigint | NO | ✓ |  |  |
| CompanyID | smallint | NO | ✓ | ✓ | [[ProspectiveCustomers]] |
| Survey_ID | int | NO | ✓ |  |  |
| Customer_No | bigint | NO | ✓ | ✓ | [[ProspectiveCustomers]] |
| Survey_Date | datetime | YES |  |  |  |
| GPSX | varchar | YES |  |  |  |
| GPSY | varchar | YES |  |  |  |
| SalesmanNo | nvarchar | YES |  |  |  |
## Primary Key
Cust_Survey_No
CompanyID
Survey_ID
Customer_No
## Foreign Keys
CompanyID -> [[Companies]](ID)
CompanyID, Customer_No -> [[ProspectiveCustomers]](CompanyID, ID)
## Impact / Procedures Using This Table

**Reads (3):**
- [[OT_ImportCustomerSurveyAnswers]]
- [[Pro_CompanyParameters]]
- [[Rpt_Customers_NotesProcpective]]

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
