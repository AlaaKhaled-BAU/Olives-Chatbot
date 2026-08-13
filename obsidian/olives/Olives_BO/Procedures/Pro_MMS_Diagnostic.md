---
type: procedure
database: Olives_BO
name: Pro_MMS_Diagnostic
schema: dbo
tags: [#backoffice, #mms]
reads_from:
  - [[MMS_Diagnostic]]
writes_to:
  - [[MMS_Diagnostic]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_Diagnostic


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_Diagnostic. Writes MMS_Diagnostic. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint = null
- @DiagnosticID	int	  = null
- @Name	nvarchar(200)	  = null
- @ForeignName	nvarchar(200)	  = null
- @Reference1	nvarchar(100)	  = null
- @Reference2	nvarchar(100)	  = null
- @IsSuspended	bit	  = null
- @IsUnderWarranty	bit	  = null
- @cmdType varchar(50)=null
## Tables Read
- [[MMS_Diagnostic]]
## Tables Written
- [[MMS_Diagnostic]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_Diagnostic]]

**Tables Written**
- [[MMS_Diagnostic]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Olives_BO/Procedures/Pro_PrintCheque]]
- [[Olives_BO/Procedures/Pro_MonthlySalesPersonsTargets]]
- [[Olives_BO/Procedures/PRO_REPORT]]
