---
type: procedure
database: Olives_BO
name: Rpt_SalesPersonsName
schema: dbo
tags: [#backoffice, #reporting, #sales]
reads_from:
  - [[CarAndSalespersonLink]]
  - [[CompanyBranches]]
  - [[DeliveryCars]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_SalesPersonsName


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CarAndSalespersonLink, CompanyBranches, DeliveryCars, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID int = null
- @Parent int = null
- @PopulationNo bigint = null
- @Name nvarchar (200)=null
- @ShortName nvarchar (100)=null
- @ForeignName nvarchar (100)=null
- @Reference1 nvarchar (40)=null
- @Reference2 nvarchar (40)=null
- @cmdType varchar(50)=null
- @Loc_Level int = null
- @MacAddress nvarchar(100)=null
- @IPAddress nvarchar(100)=null
- @FromLocation int = null
- @ToLocation int = null
## Tables Read
- [[CarAndSalespersonLink]]
- [[CompanyBranches]]
- [[DeliveryCars]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[CarAndSalespersonLink]]
- [[CompanyBranches]]
- [[DeliveryCars]]
- [[SalesPersons]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Run this report when a user requests this specific sales/operations report. Typically invoked from the reports module or dashboard. No side effects — read-only.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
