---
type: procedure
database: Olives_BO
name: Awtar_Integration_SOA
schema: dbo
tags: [#backoffice, #integration]
reads_from:
  - Cur_Custs
  - [[CustomerStatmentOfAccount]]
  - [[Customers]]
  - [[CustomersFinancialDetails]]
  - OPENJSON
  - STRING_SPLIT
writes_to:
  - [[CustomerStatmentOfAccount]]
called_by:
  - [[Niroukh_Integ_GetDataFromAPI]]
support_relevance: high
last_verified: 2026-07-05
---
# Awtar_Integration_SOA


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Cur_Custs, CustomerStatmentOfAccount, Customers, CustomersFinancialDetails, OPENJSON, STRING_SPLIT. Writes CustomerStatmentOfAccount. Invoked by 1 procedure(s). Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID nvarchar(50) = 2
- @APILinkUser nvarchar(100)='UserName=Bahaad&Password=12'
## Tables Read
- Cur_Custs
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- OPENJSON
- STRING_SPLIT
## Tables Written
- [[CustomerStatmentOfAccount]]
## Callers
- [[Awtar_Integ_AllUsers_SOA]]
## Callees
- [[Niroukh_Integ_GetDataFromAPI]]
## Impact / Dependencies

**Tables Read**
- Cur_Custs
- [[CustomerStatmentOfAccount]]
- [[Customers]]
- [[CustomersFinancialDetails]]
- OPENJSON
- STRING_SPLIT

**Tables Written**
- [[CustomerStatmentOfAccount]]

**Callers**
- [[Niroukh_Integ_GetDataFromAPI]]

**Callees**
- [[Awtar_Integ_AllUsers_SOA]]


## When to Run This

Run during ERP integration sync cycles. Monitor IntegrationErrorLog for failures.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
