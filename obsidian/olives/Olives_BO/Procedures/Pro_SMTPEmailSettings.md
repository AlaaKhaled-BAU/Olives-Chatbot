---
type: procedure
database: Olives_BO
name: Pro_SMTPEmailSettings
schema: dbo
tags: [#backoffice]
reads_from:
  - [[SMTPEmailSettings]]
writes_to:
  - [[SMTPEmailSettings]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_SMTPEmailSettings


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads SMTPEmailSettings. Writes SMTPEmailSettings. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID	smallint	 = null
- @FromEmail	varchar(500)	= null
- @FromEmail_PW	varchar(50)	= null
- @SMTP_HOST	varchar(50)	= null
- @SMTP_Port	int	= null
- @cmdType  nvarchar(50) = null
## Tables Read
- [[SMTPEmailSettings]]
## Tables Written
- [[SMTPEmailSettings]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[SMTPEmailSettings]]

**Tables Written**
- [[SMTPEmailSettings]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
