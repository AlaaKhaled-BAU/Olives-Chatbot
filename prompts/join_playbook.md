# Olives BO — canonical joins (BO names, not OSFA)

Use these patterns when writing `SELECT` on `t.` views. Orders and invoices are **different** tables.

## Invoice (sales transaction)
- Header ⋈ details: `TransactionsHeaders` ⋈ `TransactionsDetails` on `CompanyID`, `TransactionTypeID`, `TransactionYear`, `TransactionNo`.
- **Not every `TransactionsHeaders` row is a sales invoice.** Filter by transaction/document type:
  - Sales invoices: `TransactionTypeID = 1` (confirm IDs in `t.TransactionsTypes` / `t.DocumentsTypes` if unsure).
  - Return invoices: typically `TransactionTypeID = 2` — separate grain from sales.
  - `COUNT(*)` on all headers **without** a type filter mixes sales + returns + other types; never equate that total with “sales invoices”.
- Exclude voids: `ISNULL(TransactionsHeaders.IsVoid, 0) = 0` (never bare `IsVoid = 0` — NULL must count as not void).
- **Line money.** `TransactionsDetails.Price` is the line total and already includes tax. Do not multiply `Price` by `Quantity`. Do not add `TaxAmount` on top of `Price`. `TaxAmount1` and `TaxAmount2` stay unused.
  - Charged total (default, what `run_metric` `net_sales` returns): `ABS(Price) - ABS(DiscountAmount) - ABS(VoucherDiscount) - ABS(ISNULL(CustomerDiscountAmount,0))`, type 1, not void.
  - Before tax, only when the user says قبل الضريبة / بدون ضريبة / before tax: charged total minus `ABS(TaxAmount)`.
  - «صافي» and «بعد المرتجعات» mean the same thing: the charged total minus returns (type 1 minus type 2). In accounting that is net sales. «مبيعات» without those words is the charged total before returns.
- **run_metric `sales` (preferred for مبيعات):** pass `filters.tax` and `filters.returns`:
  - «مبيعات» / general sales → `tax=incl`, `returns=gross`.
  - «صافي» / «بعد المرتجعات» / net of credit notes → `tax=incl`, `returns=net`.
  - «قبل الضريبة» / before tax → `tax=excl` (keep the same `returns` mode unless the user changes it).
  - Invoice **count** = `COUNT(*)` on `t.TransactionsHeaders` only (type 1, non-void). `COUNT(*)` on the join to `t.TransactionsDetails` counts **lines**, not invoice headers.
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

## Deducing Salesperson Operational Mode (Cash Van vs. Order Taking) — Dynamic Inference (NO Hardcoding)
Never hardcode or memorize which salesperson is Cash Van or Order Taking. Deduce dynamically:
- **Call `lookup_hot('SalesPersons')`**: inspect `PositionID`. Do not use `CarID` or `VehicleId` to classify a salesman.
- **Call `lookup_hot('SalesPersonsDevicePermissions')`**: match `PositionsID = sp.PositionID`.
  - **Cash Van (بيع مباشر من السيارة)**: `MakeSalesInvoice = 1`.
    - Sales live in `t.TransactionsHeaders` (`TransactionTypeID = 1`, `ISNULL(IsVoid,0) = 0`).
    - Tablet stock is `OT_StoreItemsQty` (`StoreNo` = salesman number). `t.SalesPersonItemsBalance` is the back-office balance only, not a substitute.
    - Warehouse ↔ van stock movements live in `t.TransfersOrdersHeaders` / `t.TransfersOrdersDetails`. Do not assume a `VouType` number means load or unload.
  - **Order Taking / Pre-Sales (حجز طلبيات لتوصيل المستودع)**: `MakeOrderTaking = 1` AND `ISNULL(MakeSalesInvoice, 0) = 0`.
    - Sales live in `t.OrdersHeaders` + `t.OrdersDetails`. Do not require `WFApproved` or `Approved` unless the user asked for approved or pending orders.
    - Tablet stock is `OT_StoreItemsQty_Main` (main store). Do not answer their stock from `t.StoresBalances` when the tablet table has rows.
  - **Hybrid (مندوب مزدوج)**: `MakeSalesInvoice = 1` AND `MakeOrderTaking = 1`.
    - When asked for "sales", lead with direct field invoices (`TransactionsHeaders`); if booked sales orders (`OrdersHeaders`) matter, show them as a separate labelled line. Never add the two amounts together.
    - When asked for stock, lead with `OT_StoreItemsQty` (his van) and show `OT_StoreItemsQty_Main` (main store) as a second labelled line. Do not add the two quantities.

## Transfers orders
`TransfersOrdersHeaders` / `TransfersOrdersDetails` are stock movements, not sales invoices and not `OrdersHeaders`. Do not map `VouType` or a `TransactionsHeaders.TransactionTypeID` to load or unload; that numbering is client-specific.
Sales questions still require `TransactionTypeID = 1` and `ISNULL(IsVoid, 0) = 0`, because other transaction types share `TransactionsHeaders`.

## Inventory & Stock Tables Matrix
- **`t.SalesPersonItemsBalance`**: Back-office cash-van balance. Primary key: `(CompanyID, SalesPersonID, ItemCode)`.
- **`t.StoresBalances`**: Central warehouse stock. Primary key: `(CompanyID, StoreNo, ItemCode)`.
- Tablet stock, allowed to read. Role comes from `SalesPersonsDevicePermissions`, not from `CarID`:
  - Cash van (`MakeSalesInvoice = 1`): `OT_StoreItemsQty`, where `StoreNo` is the salesman number.
  - Order taking (`MakeOrderTaking = 1`): `OT_StoreItemsQty_Main`, the main-store quantity those reps sell from.
  - If the table for that role has no quantity for him, use `OT_ItemsMF.QtyOH`.
- **`t.SalesPersonStockTacking`**: Physical stock-taking counts submitted by reps to reconcile van shrinkage.

## Van and main-store stock
- Cash van (`MakeSalesInvoice = 1` only): `OT_StoreItemsQty` where `StoreNo` is the salesman number. If that salesman has no rows, use `OT_ItemsMF.QtyOH`.
- Order taker (`MakeOrderTaking = 1` and not `MakeSalesInvoice`): `OT_StoreItemsQty_Main`. If that table has no quantity, use `OT_ItemsMF.QtyOH`.
- Hybrid (both flags): van quantity first, main-store quantity on a second labelled line. Never add them.
- `t.SalesPersonItemsBalance` and `t.StoresBalances` are back-office balances. Use them only when the user asks for the back-office balance, not for tablet stock.

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
