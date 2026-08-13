---
type: procedure
database: Olives_BO
name: OT_ImportCustomerSurveyAnswers
schema: dbo
tags: [#backoffice, #customer, #mobile, #survey]
reads_from:
  - [[ClientsActive]]
  - [[CustomersVisitActivity]]
  - [[ProspectiveCustomers]]
  - Survey
  - [[SurveyCustomers]]
  - [[SurveyCustomersAnswers]]
  - [[SurveyProspectiveCustomers]]
  - [[SurveyProspectiveCustomersAnswers]]
  - `dbo`
writes_to:
  - [[OT_Cust_Survey]]
  - [[SurveyCustomers]]
  - [[SurveyCustomersAnswers]]
  - [[SurveyProspectiveCustomers]]
  - [[SurveyProspectiveCustomersAnswers]]
called_by:
  - [[OT_ImportNewCust_Prospective]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportCustomerSurveyAnswers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, CustomersVisitActivity, ProspectiveCustomers, Survey, SurveyCustomers, SurveyCustomersAnswers, SurveyProspectiveCustomers, SurveyProspectiveCustomersAnswers, dbo. Writes OT_Cust_Survey, SurveyCustomers, SurveyCustomersAnswers, SurveyProspectiveCustomers, SurveyProspectiveCustomersAnswers. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
## Tables Read
- [[ClientsActive]]
- [[CustomersVisitActivity]]
- [[ProspectiveCustomers]]
- Survey
- [[SurveyCustomers]]
- [[SurveyCustomersAnswers]]
- [[SurveyProspectiveCustomers]]
- [[SurveyProspectiveCustomersAnswers]]
- `dbo`
## Tables Written
- [[OT_Cust_Survey]]
- [[SurveyCustomers]]
- [[SurveyCustomersAnswers]]
- [[SurveyProspectiveCustomers]]
- [[SurveyProspectiveCustomersAnswers]]
## Callers
_None (no known callers)_
## Callees
- [[OT_ImportNewCust_Prospective]]
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[CustomersVisitActivity]]
- [[ProspectiveCustomers]]
- Survey
- [[SurveyCustomers]]
- [[SurveyCustomersAnswers]]
- [[SurveyProspectiveCustomers]]
- [[SurveyProspectiveCustomersAnswers]]
- dbo

**Tables Written**
- [[OT_Cust_Survey]]
- [[SurveyCustomers]]
- [[SurveyCustomersAnswers]]
- [[SurveyProspectiveCustomers]]
- [[SurveyProspectiveCustomersAnswers]]

**Callers**
- [[OT_ImportNewCust_Prospective]]

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
