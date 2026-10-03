---
type: table
database: Olives_BO
name: TransfersOrdersDetails_ErrorQty
schema: dbo
tags: [#backoffice, #log, #order]
foreign_keys:
referenced_by:
  - [[Pro_ConvertUnloadOrderToTransaction]]
support_relevance: low
last_verified: 2026-07-05
---
# TransfersOrdersDetails_ErrorQty


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores transfersordersdetails errorqty records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| OrderYear | smallint | NO | ✓ |  |  |
| OrderNo | int | NO | ✓ |  |  |
| VouType | int | NO | ✓ |  |  |
| ItemCode | nvarchar | YES | ✓ |  |  |
| UnitID | nvarchar | YES | ✓ |  |  |
| Quantity | float | YES |  |  |  |
| DateTime | smalldatetime | YES |  |  |  |
| Desc | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
OrderYear
OrderNo
VouType
ItemCode
UnitID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (0):**
_None_

**Writes (1):**
- [[Pro_ConvertUnloadOrderToTransaction]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Pending orders stuck**: WF approval not progressing — check WF_SETUP and approver assignment
- **Qty mismatch**: Order qty differs from delivered qty — check delivery confirmation step
- **Duplicate items**: Same item appears twice in order details — causes pricing errors
- **Route mismatch**: Customer on wrong route assigned in order — delivery driver skips stop

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[PromotionsApprovalLog]]
- [[OWGM_LockLog]]
- [[LogActionTransaction_]]
- [[SalesQuotationHeaders]]
- [[PendingOrdersDetails]]
- [[Olives_BO/Tables/LogActions]]
