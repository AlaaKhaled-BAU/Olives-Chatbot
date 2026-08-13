---
type: shared
name: Cross-DB-Links
tags: [#reference, #shared]
---

# Cross-Database Links

## Data Flow
```
Olives_BO (Server)  ←→  OSFA_DB (Tablet)
```

## Key Mapping Patterns
- Olives_BO `SalesPersons` → OSFA_DB `OT_SalesPersons`
- Olives_BO `Customers` → OSFA_DB `OT_Customers`
- Olives_BO `Items` → OSFA_DB `OT_Items`
- Olives_BO `TransactionsHeaders` → OSFA_DB `OT_InvoiceHF` / `OT_OrderHF`
- Olives_BO `TransactionsDetails` → OSFA_DB `OT_InvoiceDF`
- Olives_BO `Receipts` → OSFA_DB `OT_Payments`
- System Options: `CompanyParameters` (BO) → `OT_SystemOptions` (tablet)

## Sync Direction
| Data Type | Direction | Mechanism |
|---|---|---|
| Master data (customers, items, prices) | BO → OSFA | Sync stored procedures |
| Transactions (invoices, orders) | OSFA → BO | Posting procedures |
| Payments (receipts, checks) | OSFA → BO | Posting procedures |
| System options | BO → OSFA | `COPYSYSTEMOPTIONS` procedures |
