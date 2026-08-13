---
type: procedure
database: Olives_BO
name: SAP_Tyconz_Integ_SendSurveys
schema: dbo
tags: [#backoffice, #integration, #survey]
reads_from:
  - [[Customers]]
  - [[SalesPersons]]
  - [[SurveyCustomers]]
  - `dbo`
writes_to:
  - Survey
  - [[SurveyCustomers]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# SAP_Tyconz_Integ_SendSurveys


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Customers, SalesPersons, SurveyCustomers, dbo. Writes Survey, SurveyCustomers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint = 1
## Tables Read
- [[Customers]]
- [[SalesPersons]]
- [[SurveyCustomers]]
- `dbo`
## Tables Written
- Survey
- [[SurveyCustomers]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Customers]]
- [[SalesPersons]]
- [[SurveyCustomers]]
- dbo

**Tables Written**
- Survey
- [[SurveyCustomers]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run when pushing data to an external ERP/system. Triggered after transactions are posted and ready for sync. Check IntegrationPostedTransactions for errors if this fails.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
