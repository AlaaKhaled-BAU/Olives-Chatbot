# Olives BO — canonical joins (BO names, not OSFA)

Use these patterns when writing `SELECT` on `t.` views. Orders and invoices are **different** tables.

## Invoice (sales transaction)
- Header ⋈ details: `TransactionsHeaders` ⋈ `TransactionsDetails` on `CompanyID`, `TransactionTypeID`, `TransactionYear`, `TransactionNo`.
- **Not every `TransactionsHeaders` row is a sales invoice.** Filter by transaction/document type:
  - Sales invoices: `TransactionTypeID = 1` (confirm IDs in `t.TransactionsTypes` / `t.DocumentsTypes` if unsure).
  - Return invoices: typically `TransactionTypeID = 2` — separate grain from sales.
  - `COUNT(*)` on all headers **without** a type filter mixes sales + returns + other types; never equate that total with “sales invoices”.
- Exclude voids: `ISNULL(TransactionsHeaders.IsVoid, 0) = 0` (never bare `IsVoid = 0` — NULL must count as not void).
- Customer: `TransactionsHeaders.CustomerID` → `Customers.ID`.
- Salesperson **on the invoice document**: `TransactionsHeaders.SalesPersonID` → `SalesPersons.ID` (who issued the invoice).
- Salesperson **territory assignment** (which customers belong to whom): via `CustomersFinancialDetails` / `Positions` — not `cfd.CustomerID = sp.ID`.

## Order (not an invoice)
- `OrdersHeaders` ⋈ `OrdersDetails` on `CompanyID`, year, and order number — **not** the same grain as invoices.
- Order customer: `OrdersHeaders.CustomerID` → `Customers.ID`.
- Order salesperson: `OrdersHeaders.SalesPersonID` → `SalesPersons.ID`.

## Customer ↔ salesperson assignment
- `Customers` ⋈ `CustomersFinancialDetails` ⋈ `SalesPersons` via `PositionsID` → `PositionID`.
- **Never** join `CustomersFinancialDetails.CustomerID` to `SalesPersons.ID` — that is wrong.
- Static assignment may also appear on `Customers.SalesPersonID` where populated; prefer financial-details/positions path for territory.

## ClientsActive
- `(CompanyID, ClientID)` identifies which Olives product fork is active — not a shop or customer row.

## Receipts / checks
- Receipt header: `Receipts`; tie to customers and salespeople via documented FK relation notes in the vault.
- Exclude voided receipts: `ISNULL(Receipts.IsVoid, 0) = 0` — on many tenants `IsVoid` is NULL for all active rows; bare `IsVoid = 0` wrongly drops them.

When vault notes and live `introspect_schema` disagree on a column name, **live schema wins**.
