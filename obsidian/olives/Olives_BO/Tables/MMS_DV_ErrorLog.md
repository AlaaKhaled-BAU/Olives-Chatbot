---
type: table
database: Olives_BO
name: MMS_DV_ErrorLog
schema: dbo
tags: [#backoffice, #log, #mms]
foreign_keys:
referenced_by:
support_relevance: low
last_verified: 2026-07-05
---
# MMS_DV_ErrorLog


## Business Purpose

Maintenance management data — technician, order, and visit records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ID | bigint | YES | ✓ |  |  |
| CompNo | smallint | YES |  |  |  |
| SalesmanNo | int | YES |  |  |  |
| ErrDesc | ntext | YES |  |  |  |
| SysDate | smalldatetime | YES |  |  |  |
## Primary Key
ID
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
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[PromotionsApprovalLog]]
- [[OWGM_LockLog]]
- [[TransfersOrdersDetails_ErrorQty]]

- [[MMS_ItemsCategories]]
- [[MMS_PaymentsChecksDetails]]
- [[MMS_TaxType]]
- [[Glossary]]
