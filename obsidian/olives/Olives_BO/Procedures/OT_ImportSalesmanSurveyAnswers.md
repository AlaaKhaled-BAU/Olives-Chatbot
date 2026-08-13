---
type: procedure
database: Olives_BO
name: OT_ImportSalesmanSurveyAnswers
schema: dbo
tags: [#backoffice, #mobile, #sales, #survey]
reads_from:
  - Survey
  - [[SurveySalesmans]]
  - [[SurveySalesmansAnswers]]
  - `dbo`
writes_to:
  - [[OT_Salesman_Survey]]
  - [[SurveySalesmans]]
  - [[SurveySalesmansAnswers]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportSalesmanSurveyAnswers


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Survey, SurveySalesmans, SurveySalesmansAnswers, dbo. Writes OT_Salesman_Survey, SurveySalesmans, SurveySalesmansAnswers. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- Survey
- [[SurveySalesmans]]
- [[SurveySalesmansAnswers]]
- `dbo`
## Tables Written
- [[OT_Salesman_Survey]]
- [[SurveySalesmans]]
- [[SurveySalesmansAnswers]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Survey
- [[SurveySalesmans]]
- [[SurveySalesmansAnswers]]
- dbo

**Tables Written**
- [[OT_Salesman_Survey]]
- [[SurveySalesmans]]
- [[SurveySalesmansAnswers]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
