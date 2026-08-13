---
type: procedure
database: Olives_BO
name: Niroukh_AllCustomersTargets
schema: dbo
tags: [#backoffice, #customer, #sales]
reads_from:
  - Fun_Niroukh_VS_MonthlyandQuarter_Achievment
  - Fun_Niroukh_VS_MonthlyandQuarter_Targets
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Niroukh_AllCustomersTargets


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Fun_Niroukh_VS_MonthlyandQuarter_Achievment, Fun_Niroukh_VS_MonthlyandQuarter_Targets. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @compno int=2
- @year int =2024
- @quarter int =2
- @AchievementType bit=1
- @byamount bit=1
## Tables Read
- Fun_Niroukh_VS_MonthlyandQuarter_Achievment
- Fun_Niroukh_VS_MonthlyandQuarter_Targets
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Fun_Niroukh_VS_MonthlyandQuarter_Achievment
- Fun_Niroukh_VS_MonthlyandQuarter_Targets

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
