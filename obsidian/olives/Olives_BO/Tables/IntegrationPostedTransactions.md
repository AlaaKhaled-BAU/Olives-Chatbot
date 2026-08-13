---
type: table
database: Olives_BO
name: IntegrationPostedTransactions
schema: dbo
tags: [#backoffice, #integration]
foreign_keys:
referenced_by:
  - [[ABS_Integ_SendInvoices]]
  - [[ABS_Integ_SendInvoices_Jebrene]]
  - [[ABS_Integ_SendPayment_Jebrene]]
  - [[ABS_Integ_SendPayment_Sokhtian]]
  - [[ABS_Integ_SendReturnInvoices_Jebrene]]
  - [[ABS_Integ_SendSalesOrder]]
  - [[ABS_Integ_SendSalesOrder_Jebrene]]
  - [[ABS_Integ_SendTransferOrders]]
  - [[ABS_Integ_SendTransferOrders_Jebrene]]
  - [[ABS_Integ_SendUnloadOrders_Jebrene]]
  - [[Acback_Integ_SendInvoices]]
  - [[Acback_Integ_SendPayments]]
  - [[Acback_Integ_SendReturnInvoices]]
  - [[Acback_Integ_SendTransfer]]
  - [[Ejabi_Integ_SendInvoices]]
  - [[Ejabi_Integ_SendPayments]]
  - [[Ejabi_Integ_SendReturnInvoices]]
  - [[Ejabi_Integ_SendTransferOrders]]
support_relevance: high
last_verified: 2026-07-05
---
# IntegrationPostedTransactions


## Business Purpose

Integration data store for syncing sales transactions with external systems.

## Columns
| Column | Type | Nullable | PK | FK | References |
|--------|------|----------|----|----|------------|
| AutoID | numeric | YES | ✓ |  |  |
| CompNo | smallint | YES |  |  |  |
| TableName | nvarchar | YES |  |  |  |
| JSONData | nvarchar | YES |  |  |  |
| Result | nvarchar | YES |  |  |  |
| PostedDateTime | datetime | YES |  |  |  |
## Primary Key
AutoID
## Foreign Keys
(none)
## Impact / Procedures Using This Table

**Reads (18):**
- [[ABS_Integ_SendInvoices]]
- [[ABS_Integ_SendInvoices_Jebrene]]
- [[ABS_Integ_SendPayment_Jebrene]]
- [[ABS_Integ_SendPayment_Sokhtian]]
- [[ABS_Integ_SendReturnInvoices_Jebrene]]
- [[ABS_Integ_SendSalesOrder]]
- [[ABS_Integ_SendSalesOrder_Jebrene]]
- [[ABS_Integ_SendTransferOrders]]
- [[ABS_Integ_SendTransferOrders_Jebrene]]
- [[ABS_Integ_SendUnloadOrders_Jebrene]]
- [[Acback_Integ_SendInvoices]]
- [[Acback_Integ_SendPayments]]
- [[Acback_Integ_SendReturnInvoices]]
- [[Acback_Integ_SendTransfer]]
- [[Ejabi_Integ_SendInvoices]]
- [[Ejabi_Integ_SendPayments]]
- [[Ejabi_Integ_SendReturnInvoices]]
- [[Ejabi_Integ_SendTransferOrders]]

**Writes (17):**
- [[ABS_Integ_SendInvoices_Jebrene]]
- [[ABS_Integ_SendPayment_Jebrene]]
- [[ABS_Integ_SendPayment_Sokhtian]]
- [[ABS_Integ_SendReturnInvoices_Jebrene]]
- [[ABS_Integ_SendSalesOrder]]
- [[ABS_Integ_SendSalesOrder_Jebrene]]
- [[ABS_Integ_SendTransferOrders]]
- [[ABS_Integ_SendTransferOrders_Jebrene]]
- [[ABS_Integ_SendUnloadOrders_Jebrene]]
- [[Acback_Integ_SendInvoices]]
- [[Acback_Integ_SendPayments]]
- [[Acback_Integ_SendReturnInvoices]]
- [[Acback_Integ_SendTransfer]]
- [[Ejabi_Integ_SendInvoices]]
- [[Ejabi_Integ_SendPayments]]
- [[Ejabi_Integ_SendReturnInvoices]]
- [[Ejabi_Integ_SendTransferOrders]]

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
- [[Shared/Runbooks/Duplicate-Keys]]
- [[Shared/Runbooks/Invoice-Posting-Failure]]
- [[Shared/Runbooks/Sync-Conflict]]
