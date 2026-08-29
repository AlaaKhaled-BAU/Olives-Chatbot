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

## Actual salesman visits (زيارات منفذة)
- Fact table: `LogActionTransaction` (query `t.LogActionTransaction`). CompNo is tenant-scoped by the view.
- Login / visit start: `ActionID = N'0'` (CustEntry). Logout: `ActionID = N'3'` (CustLeave). `Data1` = customer id. `TimeStamp` = when. `SalesmanID` is nvarchar — `TRY_CAST(lat.SalesmanID AS int) = sp.ID`.
- Visit *count* for a period: count logins (`ActionID = N'0'`) only. **`ActionID = N'7'` is SystemLogin (app open), not a visit** — it is often the most common action.
- **Data1 is not always a customer.** Invoice/order/return/payment actions (`4`,`5`,`9`,`12`): `Data1` = document year, `Data2` = document number (`OT_ImportActionLog` stamps those docs' LocationLineID).
- Join customers only for visit-like actions: `TRY_CAST(lat.Data1 AS bigint) = c.ID`.
- Codebook: `lookup_hot` table `LogActions` or `LogActionTransaction` (same L1 snapshot). Do not dump the fact log via lookup_hot.
- Last week: filter `TimeStamp` with tenant `calendar_today`, not invoice max date.

## Planned / future visits (زيارات قادمة — route calendar)

Not in `LogActionTransaction` (history only). Pushed to tablet by `OT_SendSalesmanData` → OSFA `OT_SalesmanRoute`; chatbot reads BO master:

- Calendar: `SalesPersons` → `PositionID` → `SalesPersonsRoutes`.
- `WeekDay`: 1=Saturday … 7=Friday. With SQL Server `DATEFIRST` 7: Olives weekday = `(DATEPART(WEEKDAY, the_date) % 7) + 1`.
- `Week1`–`Week4` are week-of-month route slots — resolve with BO `Fun_GetWeekNo` logic (same as send-data proc); do not blindly `COALESCE(Week1..Week4)`.
- Customers: `CustomersFinancialDetails.RouteID` IN (the day's WeekN) and `cfd.PositionsID = spr.PositionsID`, order by `VisitOrder`.
- Route name: `RoutesInformation`.
- Sparse override (some clients): `SalespersonRouteByDate`.

**Forecast vs plan:** user asks توقع / تحليل / رأيك → historical `LogActionTransaction` + `analyze`, not this calendar.

## Analyst visit forecast (توقع زيارات)

Historical weekly counts from `LogActionTransaction` where `ActionID = N'0'`, GROUP BY week, then `analyze` trend. Label projection تقديري. Compare to plan only when user explicitly asks.

## Van stock (SalesPersonItemsBalance)
- Van quantity by salesperson + item: `SalesPersonItemsBalance` (live FKs to `SalesPersons`, `Items`, `Companies`).
- Join pattern: `SalesPersonItemsBalance.SalesPersonID` → `SalesPersons.ID` and `SalesPersonItemsBalance.ItemCode` → `Items.ItemCode` (always include `CompanyID` on composite keys).
- Not the same as invoice detail stock or `TransfersOrdersHeaders` — use the table that matches the question (رصيد السيارة vs transfer document).

## ClientsActive
- `(CompanyID, ClientID)` identifies which Olives product fork is active — not a shop or customer row.

## Price lists (PriceLists / PriceListDetails)
- Table name is **`PriceListDetails`** (singular *List*), not `PriceListsDetails`.
- Header: `PriceLists` (ID, Name, IsSuspended). L1 snapshot via `lookup_hot` table `PriceLists`.
- Line prices: `PriceListDetails` — PK `(CompanyID, PriceListID, ItemCode, UnitID)`; columns include `Price`, `DiscountPercent`, `UseInSales`, `UseInReturn`.
- Customer's assigned list: `CustomersFinancialDetails.PriceListID` → `PriceLists.ID` (per position/business unit — **not** on `Customers`).
- Order snapshot: `OrdersHeaders.PriceListID` → `PriceLists` when the question is about the list used on an order.
- Join item prices: `PriceListDetails` ⋈ `Items` on `CompanyID` + `ItemCode`; ⋈ `ItemsUnits` on `CompanyID` + `UnitID`.
- Filter active lists: `ISNULL(PriceLists.IsSuspended, 0) = 0` when the user means current pricing.

## Receipts / checks
- Receipt header: `Receipts`; tie to customers and salespeople via documented FK relation notes in the vault.
- Exclude voided receipts: `ISNULL(Receipts.IsVoid, 0) = 0` — on many tenants `IsVoid` is NULL for all active rows; bare `IsVoid = 0` wrongly drops them.

When vault notes and live `introspect_schema` disagree on a column name, **live schema wins**.
