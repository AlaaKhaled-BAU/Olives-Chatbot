---
type: table
database: Olives_BO
name: ZatcaSalesPersons
schema: dbo
tags: [#backoffice, #legal, #sales]
foreign_keys:
referenced_by:
support_relevance: high
last_verified: 2026-07-05
---
# ZatcaSalesPersons


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores zatcasalespersons records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ |  |  |
| ID | int | NO | ✓ |  |  |
| CSID | nvarchar | YES |  |  |  |
| PrivateKey | nvarchar | YES |  |  |  |
| Secretkey | nvarchar | YES |  |  |  |
| OTP | nvarchar | YES |  |  |  |
| CommonName | nvarchar | YES |  |  |  |
| SerialNumber | nvarchar | YES |  |  |  |
| CSR | nvarchar | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (0):**
_None_

**Writes (1):**

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Missing route assignment**: Salesperson has no RouteID — cannot see customers on tablet
- **Item balance mismatch**: Van stock differs from SalesPersonsItemsBalance — run stock-taking proc
- **Device permission missing**: No device permission record — tablet app features unavailable
- **Target not calculated**: Monthly targets missing — dashboard shows zero achievement

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
- [[JoTaxResult]]
- [[CustomersItemsLog]]
- [[CatalogMedia]]
- [[CustomerTargetsDetails]]
- [[PromotionsApprovalLog]]
- [[SalesQuotationHeaders]]

- [[ZatcaMode]]
- [[ZatcaResultGenerateXml]]
- [[ZatcaCustomer]]
