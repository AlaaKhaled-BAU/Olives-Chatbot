---
type: procedure
database: Olives_BO
name: Rpt_AssetsByLocation
schema: dbo
tags: [#assets, #backoffice, #gps, #reporting]
reads_from:
  - [[Assets]]
  - [[AssetsCustomerLink]]
  - [[Customers]]
  - [[CustomersContactPersons]]
  - [[CustomersGPSLocations]]
  - [[Locations]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_AssetsByLocation


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Assets, AssetsCustomerLink, Customers, CustomersContactPersons, CustomersGPSLocations, Locations. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint=1
- @ID int = null
- @Parent int = null
- @PopulationNo bigint = null
- @Name nvarchar (200)=null
- @FromLocation int = 1
- @ToLocation int = 999999999
- @FromCustomer bigint = 1
- @ToCustomer bigint = 999999999
- @ToAsset int = 1
- @FromAsset int = 999999
## Tables Read
- [[Assets]]
- [[AssetsCustomerLink]]
- [[Customers]]
- [[CustomersContactPersons]]
- [[CustomersGPSLocations]]
- [[Locations]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Assets]]
- [[AssetsCustomerLink]]
- [[Customers]]
- [[CustomersContactPersons]]
- [[CustomersGPSLocations]]
- [[Locations]]

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
