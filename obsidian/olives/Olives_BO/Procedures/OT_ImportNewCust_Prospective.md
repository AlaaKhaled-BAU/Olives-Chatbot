---
type: procedure
database: Olives_BO
name: OT_ImportNewCust_Prospective
schema: dbo
tags: [#backoffice, #mobile]
reads_from:
  - [[ClientsActive]]
  - [[ProspectiveCustomers]]
  - `dbo`
  - olives_BO
writes_to:
  - [[OT_NewCustomers]]
  - [[ProspectiveCustomers]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportNewCust_Prospective


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, ProspectiveCustomers, dbo, olives_BO. Writes OT_NewCustomers, ProspectiveCustomers. Invoked by 2 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint=1
## Tables Read
- [[ClientsActive]]
- [[ProspectiveCustomers]]
- `dbo`
- olives_BO
## Tables Written
- [[OT_NewCustomers]]
- [[ProspectiveCustomers]]
## Callers
- [[OT_ImportCustomerSurveyAnswers]]
- [[OT_ImportSalesQuotations]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[ProspectiveCustomers]]
- dbo
- olives_BO

**Tables Written**
- [[OT_NewCustomers]]
- [[ProspectiveCustomers]]

**Callers**
_None_

**Callees**
- [[OT_ImportCustomerSurveyAnswers]]
- [[OT_ImportSalesQuotations]]


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
