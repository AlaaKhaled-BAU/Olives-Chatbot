---
type: procedure
database: Olives_BO
name: OT_SendCompData
schema: dbo
tags: [#backoffice, #mobile]
reads_from:
  - [[Banks]]
  - [[BusinessUnits]]
  - [[ClientsActive]]
  - [[Companies]]
  - [[CompanyBranches]]
  - [[CompanyParameters]]
  - [[CompetitiveItems]]
  - [[Currencies]]
  - [[Customers]]
  - [[CustomersTypes]]
  - [[DocumentsTypes]]
  - [[InvoiceHistoryHF]]
  - [[Items]]
  - [[ItemsCategories]]
  - [[ItemsUnits]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# OT_SendCompData


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Banks, BusinessUnits, ClientsActive, Companies, CompanyBranches, CompanyParameters, CompetitiveItems, Currencies, Customers, CustomersTypes, DocumentsTypes, InvoiceHistoryHF, Items, ItemsCategories, ItemsUnits. Invoked by 7 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompNo int
## Tables Read
- [[Banks]]
- [[BusinessUnits]]
- [[ClientsActive]]
- [[Companies]]
- [[CompanyBranches]]
- [[CompanyParameters]]
- [[CompetitiveItems]]
- [[Currencies]]
- [[Customers]]
- [[CustomersTypes]]
- [[DocumentsTypes]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]
## Tables Written
_None_
## Callers
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[Pro_Companies]]
- [[Qetaf_Integ]]
- [[RamPharm_SAP_Integ]]
- [[Shini_Integ]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Banks]]
- [[BusinessUnits]]
- [[ClientsActive]]
- [[Companies]]
- [[CompanyBranches]]
- [[CompanyParameters]]
- [[CompetitiveItems]]
- [[Currencies]]
- [[Customers]]
- [[CustomersTypes]]
- [[DocumentsTypes]]
- [[InvoiceHistoryHF]]
- [[Items]]
- [[ItemsCategories]]
- [[ItemsUnits]]

**Tables Written**
_None_

**Callers**
_None_

**Callees**
- [[AbuOda_BonMarrof_Integ]]
- [[AbuOda_Comp2_Integ]]
- [[AbuOda_Integ]]
- [[Pro_Companies]]
- [[Qetaf_Integ]]
- [[RamPharm_SAP_Integ]]
- [[Shini_Integ]]


## When to Run This
> [!warning] AUTO-GENERATED — verify before trusting

Review procedure definition to determine appropriate use case. Check the tables it reads/writes for business context.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
