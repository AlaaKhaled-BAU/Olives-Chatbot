---
type: procedure
database: Olives_BO
name: Rpt_CustomerNameByLocation
schema: dbo
tags: [#backoffice, #customer, #gps, #reporting]
reads_from:
  - [[ClientsActive]]
  - [[Customers]]
  - [[CustomersContactPersons]]
  - [[CustomersContactPersonsLink]]
  - [[CustomersFinancialDetails]]
  - [[CustomersGroups]]
  - [[Locations]]
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_CustomerNameByLocation


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads ClientsActive, Customers, CustomersContactPersons, CustomersContactPersonsLink, CustomersFinancialDetails, CustomersGroups, Locations, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=null
- @ID int = null
- @Parent int = null
- @PopulationNo bigint = null
- @Name nvarchar (200)=null
- @FromLocation int = null
- @ToLocation int = null
- @FromCustomer bigint = null
- @ToCustomer bigint = null
## Tables Read
- [[ClientsActive]]
- [[Customers]]
- [[CustomersContactPersons]]
- [[CustomersContactPersonsLink]]
- [[CustomersFinancialDetails]]
- [[CustomersGroups]]
- [[Locations]]
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[ClientsActive]]
- [[Customers]]
- [[CustomersContactPersons]]
- [[CustomersContactPersonsLink]]
- [[CustomersFinancialDetails]]
- [[CustomersGroups]]
- [[Locations]]
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
