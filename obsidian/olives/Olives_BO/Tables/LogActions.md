---
type: table
database: Olives_BO
name: LogActions
schema: dbo
tags: [#backoffice, #log]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-08-28
---
# LogActions


## Business Purpose

L1 codebook for `LogActionTransaction.ActionID` (`lookup_hot` table `LogActions` or `LogActionTransaction`).
`ActionId` + `ActionDesc`: 0 CustEntry, 3 CustLeave, 4 InvoiceIssue, 5 OrderIssue, 7 SystemLogin, 8 NoSaleExit, 9 ReturnInvoiceIssue, 10/11 journey, 12 PaymentIssue, 49 Pending Invoice JSON, plus ~40 other tablet actions.
Join `t.LogActions.ActionId` = log.`ActionID`. This table has no event rows.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ActionId | nvarchar | YES | ✓ |  |  |
| ActionDesc | varchar | YES |  |  |  |
## Primary Key
ActionId
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Rapid growth**: Table size growing fast — archive old records periodically
- **Orphan log entries**: No corresponding source transaction — investigate data source
- **No cleanup**: No purge job configured — disk space may fill up

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[Glossary]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[PromotionsApprovalLog]]
- [[OWGM_LockLog]]
- [[TransfersOrdersDetails_ErrorQty]]
