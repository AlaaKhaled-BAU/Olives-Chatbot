---
type: procedure
database: Olives_BO
name: DR_DynamicReports_PRO
schema: dbo
tags: [#backoffice, #reporting]
reads_from:
  - [[Companies]]
  - [[DR_DynamicReports]]
  - [[DR_DynamicReportsDictionary]]
  - [[DR_DynamicReportsParameters]]
  - [[Users]]
writes_to:
  - [[DR_DynamicReports]]
  - [[DR_DynamicReportsParameters]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# DR_DynamicReports_PRO


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, DR_DynamicReports, DR_DynamicReportsDictionary, DR_DynamicReportsParameters, Users. Writes DR_DynamicReports, DR_DynamicReportsParameters. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @cmdType varchar(50)=null
- @ReportID int=null
- @UserID varchar(500)=null
- @UserPWD varchar(500)=null
- @ReportNameAR varchar(500)=null
- @ReportNameEN varchar(500)=null
- @ReportFileName varchar(500)=null
- @SpName varchar(500)=null
- @AllowTranslate bit=null
- @ParamID int=null
- @ParamCaption varchar(500)=null
- @ParamSQLName varchar(500)=null
- @ParamType varchar(500)=null
- @DropDownSource varchar(500)=null
## Tables Read
- [[Companies]]
- [[DR_DynamicReports]]
- [[DR_DynamicReportsDictionary]]
- [[DR_DynamicReportsParameters]]
- [[Users]]
## Tables Written
- [[DR_DynamicReports]]
- [[DR_DynamicReportsParameters]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- [[DR_DynamicReports]]
- [[DR_DynamicReportsDictionary]]
- [[DR_DynamicReportsParameters]]
- [[Users]]

**Tables Written**
- [[DR_DynamicReports]]
- [[DR_DynamicReportsParameters]]

**Callers**
_None_

**Callees**
_None_


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
