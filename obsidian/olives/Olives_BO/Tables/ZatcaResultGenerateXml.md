---
type: table
database: Olives_BO
name: ZatcaResultGenerateXml
schema: dbo
tags: [#backoffice, #legal]
foreign_keys:
referenced_by:
  - [[Pro_ZatcaIntegrationApi]]
support_relevance: high
last_verified: 2026-07-05
---
# ZatcaResultGenerateXml


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores zatcaresultgeneratexml records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| TransactionTypeID | smallint | NO | ✓ |  |  |
| TransactionYear | smallint | NO | ✓ |  |  |
| TransactionNo | int | NO | ✓ |  |  |
| EncodedInvoice | nvarchar | YES |  |  |  |
| InvoiceHash | nvarchar | YES |  |  |  |
| UUID | nvarchar | YES |  |  |  |
| QRCode | nvarchar | YES |  |  |  |
| IsValid | bit | YES |  |  |  |
| ErrorMessage | nvarchar | YES |  |  |  |
| AllowanceTotalAmount | nvarchar | YES |  |  |  |
| ChargeTotalAmount | nvarchar | YES |  |  |  |
| LineExtensionAmount | nvarchar | YES |  |  |  |
| PayableAmount | nvarchar | YES |  |  |  |
| PrepaidAmount | nvarchar | YES |  |  |  |
| TaxExclusiveAmount | nvarchar | YES |  |  |  |
| TaxInclusiveAmount | nvarchar | YES |  |  |  |
| TaxAmount | nvarchar | YES |  |  |  |
| StatusCode | int | YES |  |  |  |
| SendingStatus | nvarchar | YES |  |  |  |
| IsSent | bit | YES |  |  |  |
| WarningMessage | nvarchar | YES |  |  |  |
| ZatcaCallErrorMessage | nvarchar | YES |  |  |  |
| ClearedInvoice | nvarchar | YES |  |  |  |
| ZatcaQRCode | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
TransactionTypeID
TransactionYear
TransactionNo
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (0):**
_None_

**Writes (1):**
- [[Pro_ZatcaIntegrationApi]]

## Estimated Size / Volatility
Typical business table
## Common Issues
> [!warning] AUTO-GENERATED — verify before trusting

- **Orphan records**: Missing parent references cause query failures
- **Duplicate entries**: Duplicate keys cause sync/import errors
- **Data integrity**: Missing required fields block related transactions
- **Stale data**: Records not updated — may cause reporting inaccuracies

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[MMS_TaxType]]
- [[JOTaxSettings]]

- [[ZatcaMode]]
- [[ZatcaCustomer]]
- [[ZatcaCompany]]
- [[Glossary]]
