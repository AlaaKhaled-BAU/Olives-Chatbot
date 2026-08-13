---
type: procedure
database: Olives_BO
name: Pro_ComboData_Sujab
schema: dbo
tags: [#backoffice]
reads_from:
  - ClientsActive
  - Customers
  - CustomersClasses
  - CustomersFinancialDetails
  - CustomersGroups
  - CustomersTypes
  - Items
  - ItemsCategories
  - Locations
  - RoutesInformation
  - SalesPersons
  - SalespersonsAssistants
writes_to:
called_by:
support_relevance: high
last_verified: 2026-08-05
status: documented
---
# Pro_ComboData_Sujab

## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Stored procedure in Olives_BO — reads 12 table(s); calls 2 proc(s). See sections below for the full dependency map.
## Parameters
- @CompanyID smallint
- @SalesPersonType int
- @Search nvarchar(200)
- @UserIDLog nvarchar(100)
- @cmdType varchar(50)
- @Fillter nvarchar(200)
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersClasses]]
- [[CustomersFinancialDetails]]
- [[CustomersGroups]]
- [[CustomersTypes]]
- [[Items]]
- [[ItemsCategories]]
- [[Locations]]
- [[RoutesInformation]]
- [[SalesPersons]]
- [[SalespersonsAssistants]]
## Tables Written
_None_
## Cross-DB Tables
_None_
## Callers
_None_
## Callees
- `Fun_ConvArrayToTable`
- `Fun_GetCompanyBranchesByUser`
## When to Run

Scheduled or on-demand per business cycle; inspect body (columns read/written) for exact trigger.

## Related
- [[_MOC-Olives_BO|Olives_BO MOC]]
