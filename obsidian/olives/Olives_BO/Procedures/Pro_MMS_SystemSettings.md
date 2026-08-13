---
type: procedure
database: Olives_BO
name: Pro_MMS_SystemSettings
schema: dbo
tags: [#backoffice, #mms]
reads_from:
  - [[MMS_SystemSettings]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MMS_SystemSettings


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads MMS_SystemSettings. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	= null
- @TechnicianID	int	= null
- @OptionID	int	= null
- @OptionDescription	varchar(50)	= null
- @OptionValue	varchar(50)	= null
- @cmdType varchar(50)=null
## Tables Read
- [[MMS_SystemSettings]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[MMS_SystemSettings]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
