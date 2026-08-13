---
type: procedure
database: Olives_BO
name: Pro_CalcSalespersonItemBalance
schema: dbo
tags: [#backoffice, #inventory, #sales]
reads_from:
  - CalcItemQty
  - [[ClientsActive]]
  - [[CompanyParameters]]
  - [[SalesPersonItemsBalance]]
  - [[TransactionsDetails]]
  - [[TransactionsHeaders]]
  - `dbo`
writes_to:
  - [[SalesPersonItemsBalance]]
called_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pro_CalcSalespersonItemBalance


## Purpose
> [!warning] AUTO-GENERATED — verify before trusting
Automatically documented procedure in the Olives_BO database. Reads CalcItemQty, ClientsActive, CompanyParameters, SalesPersonItemsBalance, TransactionsDetails, TransactionsHeaders, dbo. Writes SalesPersonItemsBalance. Invoked by 8 procedure(s). See Tables Read/Written and Callers/Callees below for the full dependency map.
## Parameters
- @CompanyID smallint
- @TrType smallint
- @TrYear smallint
- @TrNo int
- @ModType smallint
- @ErrorNo int output
## Tables Read
- CalcItemQty
- [[ClientsActive]]
- [[CompanyParameters]]
- [[SalesPersonItemsBalance]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- `dbo`
## Tables Written
- [[SalesPersonItemsBalance]]
## Callers
- [[Defaf_Integration]]
- [[OT_ImportReplacement]]
- [[OT_ImportSalesInvoices]]
- [[Pro_ConvertLoadOrderToTransaction]]
- [[Pro_ConvertUnloadOrderToTransaction]]
- [[Pro_ReturnOrdersDetails]]
- [[Pro_TransactionsDetails]]
- [[Pro_TransactionsHeaders]]
## Callees
_None_
## Impact / Dependencies

**Tables Read**
- CalcItemQty
- [[ClientsActive]]
- [[CompanyParameters]]
- [[SalesPersonItemsBalance]]
- [[TransactionsDetails]]
- [[TransactionsHeaders]]
- dbo

**Tables Written**
- [[SalesPersonItemsBalance]]

**Callers**
_None_

**Callees**
- [[Defaf_Integration]]
- [[OT_ImportReplacement]]
- [[OT_ImportSalesInvoices]]
- [[Pro_ConvertLoadOrderToTransaction]]
- [[Pro_ConvertUnloadOrderToTransaction]]
- [[Pro_ReturnOrdersDetails]]
- [[Pro_TransactionsDetails]]
- [[Pro_TransactionsHeaders]]


## When to Run This

CRUD procedure for maintaining master data. Called from the back-office UI when users create/update/delete records. Not typically run manually.

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Shared/Runbooks/Van-Stock-Mismatch]]
