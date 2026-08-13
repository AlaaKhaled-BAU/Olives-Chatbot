---
type: procedure
database: Olives_BO
name: Pro_MonthlySalesPersonsTargets
schema: dbo
tags: [#backoffice, #sales]
reads_from:
writes_to:
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_MonthlySalesPersonsTargets


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID SMALLINT = NULL
- @Year varchar(50)   = NULL
- @Month varchar(50) = NULL
- @FromSalesmanID varchar(50) = NULL
- @ToSalesmanID varchar(50) = NULL
## Tables Read
_None_
## Tables Written
_None_
## Callers
_None (no known callers)_
## Callees
_None_
## Impact / Dependencies

**Tables Read**
_None_

**Tables Written**
_None_

**Callers**
_None_

**Callees**
_None_


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[CustomerTargetsDetails]]
- [[PromotionsApprovalLog]]
- [[SalesQuotationHeaders]]

- [[Pro_SalesPersonNewCustomersTargets]]
- [[Pro_CompetitveItemsDataHF]]
- [[Pro_MMS_Diagnostic]]
- [[Glossary]]
