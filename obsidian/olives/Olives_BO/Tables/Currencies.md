---
type: table
database: Olives_BO
name: Currencies
schema: dbo
tags: [#backoffice]
foreign_keys:
  - [[Currencies]]
referenced_by:
  - [[OT_SendCompData]]
  - [[Pro_Checks]]
  - [[Pro_Currencies]]
  - [[Pro_CurrenciesRate]]
  - [[Pro_DeliveryDashboard]]
  - [[Pro_JoTaxApi]]
  - [[Pro_JoTaxApiFromOSFA]]
  - [[Pro_JoTaxApiFromOSFA____]]
  - [[Pro_MerchandiseDashboard]]
  - [[Pro_OrdersHeaders]]
  - [[Pro_Receipts]]
  - [[Pro_ReturnOrdersHeaders]]
  - [[Pro_SalesQuotationHeaders]]
  - [[Pro_SalesmanCashSettlement]]
  - [[Pro_TransactionsHeaders]]
  - [[Rpt_AcceptedSalesInvoices]]
  - [[Rpt_LoadOrderFirstApproval]]
  - [[Rpt_ReceiptVouchers]]
  - [[Rpt_ReceivablesSalesInvoice]]
support_relevance: high
last_verified: 2026-07-05
related_workflows:
  - Company-Setup
---
# Currencies


## Business Purpose
> [!warning] AUTO-GENERATED — verify before trusting

Core data table in the Back Office (server-side) — stores currencies records.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| ID | smallint | NO | ✓ | ✓ | [[Currencies]] |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| Fraction | smallint | YES |  |  |  |
| CashBox | varchar | YES |  |  |  |
| ChqBox | varchar | YES |  |  |  |
## Primary Key
ID
## Foreign Keys
ID -> [[Currencies]](ID)
## Known Circular Dependencies
- Self-referencing FK (references itself via ID).
## Impact / Procedures Using This Table

**Reads (30):**
- [[OT_SendCompData]]
- [[Pro_Checks]]
- [[Pro_Currencies]]
- [[Pro_CurrenciesRate]]
- [[Pro_DeliveryDashboard]]
- [[Pro_JoTaxApi]]
- [[Pro_JoTaxApiFromOSFA]]
- [[Pro_JoTaxApiFromOSFA____]]
- [[Pro_MerchandiseDashboard]]
- [[Pro_OrdersHeaders]]
- [[Pro_Receipts]]
- [[Pro_ReturnOrdersHeaders]]
- [[Pro_SalesQuotationHeaders]]
- [[Pro_SalesmanCashSettlement]]
- [[Pro_TransactionsHeaders]]
- [[Rpt_AcceptedSalesInvoices]]
- [[Rpt_LoadOrderFirstApproval]]
- [[Rpt_ReceiptVouchers]]
- [[Rpt_ReceivablesSalesInvoice]]

**Writes (2):**
- [[Pro_Currencies]]

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
- See also (OSFA counterpart): [[OSFA_DB/Tables/OT_Currency]]
