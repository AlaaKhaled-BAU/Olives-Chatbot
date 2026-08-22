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

## Customer ↔ salesperson assignment (CFD / territory)
- `CustomersFinancialDetails` (cfd) ⋈ `Customers` on `CompanyID`, `CustomerID`.
- Territory position: `CustomersFinancialDetails.PositionsID` → `Positions.ID` (live FK — **not** `Positions.PositionID`).
- Salesperson on territory: `Positions.ID` ← `SalesPersons.PositionID` (also `CompanyID` on both sides when composite).
- **Never** join `CustomersFinancialDetails.CustomerID` to `SalesPersons.ID` — that is wrong.
- Static assignment may also appear on `Customers.SalesPersonID` where populated; prefer financial-details/positions path for territory.
- Example (live FKs): for salesperson "أسامة", filter `SalesPersons` then join `Positions` on `sp.PositionID = pos.ID`, then `cfd.PositionsID = pos.ID` — expect multiple CFD rows per territory, not one row per customer naively.
- End-to-end: `Customers` ⋈ `CustomersFinancialDetails` ⋈ `Positions` ⋈ `SalesPersons` via `PositionsID` → `PositionID`.

## Van stock (SalesPersonItemsBalance)
- Van quantity by salesperson + item: `SalesPersonItemsBalance` (live FKs to `SalesPersons`, `Items`, `Companies`).
- Join pattern: `SalesPersonItemsBalance.SalesPersonID` → `SalesPersons.ID` and `SalesPersonItemsBalance.ItemCode` → `Items.ItemCode` (always include `CompanyID` on composite keys).
- Not the same as invoice detail stock or `TransfersOrdersHeaders` — use the table that matches the question (رصيد السيارة vs transfer document).

## ClientsActive
- `(CompanyID, ClientID)` identifies which Olives product fork is active — not a shop or customer row.

## Receipts / checks
- Receipt header: `Receipts`; tie to customers and salespeople via documented FK relation notes in the vault.
- Exclude voided receipts: `ISNULL(Receipts.IsVoid, 0) = 0` — on many tenants `IsVoid` is NULL for all active rows; bare `IsVoid = 0` wrongly drops them.

When vault notes and live `introspect_schema` disagree on a column name, **live schema wins**.
