---
type: procedure
database: Olives_BO
name: Rpt_PrintCustomersBarcode
schema: dbo
tags: [#backoffice, #customer, #inventory, #reference, #reporting]
reads_from:
  - [[Companies]]
  - [[Customers]]
  - [[DeliveryCars]]
  - Fun_ConvArrayToTable
  - [[SalesPersons]]
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Rpt_PrintCustomersBarcode


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads Companies, Customers, DeliveryCars, Fun_ConvArrayToTable, SalesPersons. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID int = NULL
- @CustomersArray VARCHAR(max)=''
- @Type int = null
## Tables Read
- [[Companies]]
- [[Customers]]
- [[DeliveryCars]]
- Fun_ConvArrayToTable
- [[SalesPersons]]
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- [[Companies]]
- [[Customers]]
- [[DeliveryCars]]
- Fun_ConvArrayToTable
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
