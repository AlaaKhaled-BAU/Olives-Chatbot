---
type: procedure
database: Olives_BO
name: OT_ImportSalesQuotations
schema: dbo
tags: [#backoffice, #mobile, #order, #sales]
reads_from:
  - [[Companies]]
  - [[CompanyParameters]]
  - GetSalesman
  - Header
  - [[ProspectiveCustomers]]
  - `dbo`
writes_to:
  - [[OT_SalesQuotationHF]]
  - [[SalesQuotationDetails]]
  - [[SalesQuotationHeaders]]
called_by:
  - [[OT_ImportNewCust_Prospective]]
support_relevance: high
last_verified: 2026-07-05
---
# OT_ImportSalesQuotations


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, CompanyParameters, GetSalesman, Header, ProspectiveCustomers, dbo. Writes OT_SalesQuotationHF, SalesQuotationDetails, SalesQuotationHeaders. Calls 1 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo smallint
## Tables Read
- [[Companies]]
- [[CompanyParameters]]
- GetSalesman
- Header
- [[ProspectiveCustomers]]
- `dbo`
## Tables Written
- [[OT_SalesQuotationHF]]
- [[SalesQuotationDetails]]
- [[SalesQuotationHeaders]]
## Callers
_None (no known callers)_
## Callees
- [[OT_ImportNewCust_Prospective]]
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- [[CompanyParameters]]
- GetSalesman
- Header
- [[ProspectiveCustomers]]
- dbo

**Tables Written**
- [[OT_SalesQuotationHF]]
- [[SalesQuotationDetails]]
- [[SalesQuotationHeaders]]

**Callers**
- [[OT_ImportNewCust_Prospective]]

**Callees**
_None_


## When to Run This

Run to import tablet data into BO during sync. Called by the sync service when OSFA devices push transactions. If this fails, tablet data remains in OSFA_DB and isn't reflected in Olives_BO.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
