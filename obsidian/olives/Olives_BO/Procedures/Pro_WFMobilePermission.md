---
type: procedure
database: Olives_BO
name: Pro_WFMobilePermission
schema: dbo
tags: [#workflow]
reads_from:
  - SalesPersons
writes_to:
  - WFMobilePermissionDefinition
  - WFMobilePermissionLink
called_by:
support_relevance: medium
last_verified: 2026-08-05
status: documented
---
# Pro_WFMobilePermission

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 1 table(s); writes 2. See sections below for the full dependency map.
## Parameters
- @CompanyID int
- @PerID int
- @Description nvarchar(100)
- @IsSysOption bit
- @UseMultiselect bit
- @SalesmanNo int
- @PerValue nvarchar(200)
- @Cmd nvarchar(100)
## Tables Read
- [[SalesPersons]]
## Tables Written
- [[WFMobilePermissionDefinition]]
- [[WFMobilePermissionLink]]
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
_None_
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
