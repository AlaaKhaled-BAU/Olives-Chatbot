---
type: procedure
database: Olives_BO
name: Pro_Contracts
schema: dbo
tags: [#backoffice]
reads_from:
  - Contract
  - [[ContractItems]]
  - [[Contracts]]
  - [[Customers]]
  - [[Items]]
  - [[ItemsUnits]]
writes_to:
  - Contract
  - [[ContractItems]]
  - [[Contracts]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_Contracts


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Contract, ContractItems, Contracts, Customers, Items, ItemsUnits. Writes Contract, ContractItems, Contracts. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = null
- @ContractID varchar(50) = null
- @cmdType varchar(50) = null
- @ContractName varchar(50) = null
- @StartDate datetime = null
- @EndDate datetime = null
- @IsSuspended bit = null
- @CustomerID int = null
- @ItemCode varchar(50) = null
- @UnitID varchar(50) = null
- @MaxQty int = null
## Tables Read
- Contract
- [[ContractItems]]
- [[Contracts]]
- [[Customers]]
- [[Items]]
- [[ItemsUnits]]
## Tables Written
- Contract
- [[ContractItems]]
- [[Contracts]]
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- Contract
- [[ContractItems]]
- [[Contracts]]
- [[Customers]]
- [[Items]]
- [[ItemsUnits]]

**Tables Written**
- Contract
- [[ContractItems]]
- [[Contracts]]

**Callers**
_None_

**Callees**
_None_


## When to Run This

Back-office management procedure. Called from the admin interface for this specific domain.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
