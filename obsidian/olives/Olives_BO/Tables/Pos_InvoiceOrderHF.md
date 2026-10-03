---
type: table
database: Olives_BO
name: Pos_InvoiceOrderHF
schema: dbo
tags: [#backoffice, #billing, #order]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# Pos_InvoiceOrderHF


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores pos invoiceorderhf records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| BusUnitID | int | YES |  |  |  |
| CaCr | int | YES |  |  |  |
| CompNo | int | YES |  |  |  |
| CustomerDiscountAmount | float | YES |  |  |  |
| CustomerDiscountPerc | float | YES |  |  |  |
| CustomerName | nchar | YES |  |  |  |
| CustomerNo | int | YES |  |  |  |
| DeliveryLocation | nchar | YES |  |  |  |
| DocType | int | YES |  |  |  |
| ExRate | float | YES |  |  |  |
| ForeignCustomerDiscountAmount | float | YES |  |  |  |
| ForeignCustomerDiscountPerc | float | YES |  |  |  |
| ForeignDiscountAmount | float | YES |  |  |  |
| ForeignDiscountPercent | float | YES |  |  |  |
| GPSX | nchar | YES |  |  |  |
| GPSY | nchar | YES |  |  |  |
| IsProspectiveCustomer | bit | YES |  |  |  |
| IsVoid | int | YES |  |  |  |
| Notes | nchar | YES |  |  |  |
| OrderDate | nchar | YES |  |  |  |
| OrderNo | int | YES |  |  |  |
| OrderYear | int | YES |  |  |  |
| PaymentType | int | YES |  |  |  |
| PrintCopyCount | int | YES |  |  |  |
| PrintOriginalCount | int | YES |  |  |  |
| PrNo | nchar | YES |  |  |  |
| PromisesDate | nchar | YES |  |  |  |
| SalesmanNo | int | YES |  |  |  |
| TrDateTime | nvarchar | YES |  |  |  |
| VouDisc | float | YES |  |  |  |
| VouDiscPer | float | YES |  |  |  |
| GrossTotal | float | YES |  |  |  |
| Discount | float | YES |  |  |  |
| Tax | float | YES |  |  |  |
| GrandTotal | float | YES |  |  |  |
| DiscountType | int | YES |  |  |  |
| DiscountValue | float | YES |  |  |  |
## Primary Key
(none)
## Foreign Keys
(none)
## Impact / Procedures Using This Table

_No procedures reference this table in the dependency graph._

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Orphan lines**: Detail rows without matching header — causes sync failures
- **Posting failure**: IsPosted flag stuck false — check ERP integration log
- **Duplicate vouchers**: Same VouNo generated for different transactions — run dedup check
- **Currency mismatch**: ExRate different from CurrenciesRate table — financial reconciliation off
- **Void inconsistency**: IsVoid flag but original transaction still active — check WF approval

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[ReceiptRequestsInvoicesLink]]
- [[SalesQuotationHeaders]]
- [[PendingOrdersDetails]]
