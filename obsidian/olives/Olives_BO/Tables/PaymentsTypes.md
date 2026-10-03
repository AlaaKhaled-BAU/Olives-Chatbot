---
type: table
database: Olives_BO
name: PaymentsTypes
schema: dbo
tags: [#backoffice, #billing, #reference]
foreign_keys:
  - [[Companies]]
referenced_by:
  - [[OSFA_SP_Api]]
  - [[OSFA_SP_Api_Jawad]]
  - [[OT_ImportSalesInvoices]]
  - [[Pro_CustomerReceivablesInfo]]
  - [[Pro_GetCashCloseTotals]]
  - [[Pro_ImportData]]
  - [[Pro_OrdersHeaders]]
  - [[Pro_PaymentsTypes]]
  - [[Pro_SalesQuotationHeaders]]
  - [[Pro_SalesTrans]]
  - [[Rpt_CashSummary]]
  - [[Rpt_CustomersVisitsCountByClass]]
  - [[Rpt_DeliveryDetails]]
  - [[Rpt_NewCustomer]]
  - [[Rpt_ProspectiveCustomer]]
support_relevance: high
last_verified: 2026-07-05
---
# PaymentsTypes


## Business Purpose

Reference/lookup table defining paymentstypes categories.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| CompanyID | smallint | NO | ✓ | ✓ | [[Companies]] |
| ID | int | NO | ✓ |  |  |
| Name | nvarchar | YES |  |  |  |
| ShortName | nvarchar | YES |  |  |  |
| Reference1 | nvarchar | YES |  |  |  |
| Reference2 | nvarchar | YES |  |  |  |
| DueDays | int | YES |  |  |  |
## Primary Key
CompanyID
ID
## Foreign Keys
CompanyID -> [[Companies]](ID)
## Impact / Procedures Using This Table

**Reads (50):**
- [[OT_ImportSalesInvoices]]
- [[Pro_CustomerReceivablesInfo]]
- [[Pro_GetCashCloseTotals]]
- [[Pro_ImportData]]
- [[Pro_OrdersHeaders]]
- [[Pro_PaymentsTypes]]
- [[Pro_SalesQuotationHeaders]]
- [[Pro_SalesTrans]]
- [[Rpt_CashSummary]]
- [[Rpt_CustomersVisitsCountByClass]]
- [[Rpt_DeliveryDetails]]
- [[Rpt_NewCustomer]]
- [[Rpt_ProspectiveCustomer]]

**Writes (41):**
- [[OSFA_SP_Api]]
- [[OSFA_SP_Api_Jawad]]
- [[Pro_ImportData]]
- [[Pro_PaymentsTypes]]

## Estimated Size / Volatility
Typical business table
## Common Issues

- **Partial payment not tracked**: Receipt amount less than invoice total — aging report shows incorrect balance
- **Check bounce**: CheckStatus not updated after bank return — customer credit not restored
- **Currency conversion error**: ExRate differs from daily rate — receipt in wrong amount
- **Duplicate receipts**: Same payment applied twice — customer credit balance wrong

## Related

- [[_MOC-Olives_BO|Olives_BO MOC]]
