# OSFA ↔ Olives_BO Table Mapping Summary

> **OSFA_DB** = Field/tablet database (OT_ prefix). **Olives_BO** = Back Office.
> Transaction tables: OSFA → BO. Master data tables: BO → OSFA.

---

## 1. `OT_InvoiceHF` ↔ `TransactionsHeaders`

**Flow Direction:** OSFA → BO (transaction pull)

**Description:** Invoice headers created by the salesperson on the tablet. Each invoice represents a sales transaction (cash or credit) with a customer. Posted flag controls sync.

| Side | Table | PK Columns |
|---|---|---|
| OSFA | `OT_InvoiceHF` | `CompNo`, `VouType`, `VouYear`, `VouNo` |
| BO | `TransactionsHeaders` | `CompanyID`, `TransactionTypeID`, `TransactionYear`, `TransactionNo` |

**Main Columns:**

| OSFA (OT_InvoiceHF) | BO (TransactionsHeaders) | Notes |
|---|---|---|
| CompNo | CompanyID | Company |
| VouType | TransactionTypeID | Document type (invoice/return) |
| VouYear | TransactionYear | Fiscal year |
| VouNo | TransactionNo | Sequential document number |
| SalesmanNo | SalesPersonID | Salesperson who created it |
| CustomerNo | CustomerID | Customer |
| VouDate | TransactionDate | Transaction date |
| CaCr | CreditCash | 1=Cash, 0=Credit |
| DocType | DocumentTypeID | Sub-type of transaction |
| DiscountAmount | DiscountAmount | Total discount value |
| DiscountPercent | DiscountPercent | Total discount % |
| Currency | CurrencyID | Currency |
| ExRate | ExchangeRate | Exchange rate |
| RouteID | RouteID | Sales route |
| IsVoid | IsVoid | 1=Cancelled/voided |
| PaymentType | PaymentType | Payment method (cheque, cash, etc.) |
| BusUnitID | BusinessUnitID | Business unit |
| IsPosted | (sync flag) | 1=Ready to sync to BO |
| GPSX / GPSY | Latitude / Longitude | GPS coordinates |
| CustomerName | CustomerName | Denormalized customer name |
| DiscountAmount | DiscountAmount | |
| IsWFApproved | IsWFApproved | Workflow approval |
| ContractID | ContractID | Contract reference |
| DeliveryOrderYear | DeliveryOrderYear | Linked delivery order |
| DeliveryOrderNo | DeliveryOrderNo | |
| DetailCount | DetailCount | Number of detail lines |
| TabletSysID | TabletSysID | Unique tablet system ID |
| IsLoan | IsLoan | Loan flag |
| SalesmanStockYear | SalesmanStockYear | Van stock reference |
| SalesmanStockNo | SalesmanStockNo | |
| InvDueDays | InvDueDays | Invoice due days |

**Key behavior:**
- BO reads `OT_InvoiceHF` where `IsPosted = 0`, inserts/updates `TransactionsHeaders`, then sets `IsPosted = 1`.
- `TransactionsHeaders` has additional BO-only fields: `PostedToERP`, `EINV_QR`, `EINV_INV_UUID` (Zatca e-invoicing), `IsFromCash`, `IsPostVoid`.
- FK relationships: `SalesPersons`, `Customers`, `BusinessUnits`, `RoutesInformation`, `Currencies`, `PriceLists`, `Contracts`, `DocumentsTypes`, `PaymentsTypes`, `TransactionsTypes`, `Companies`.

---

## 2. `OT_InvoiceDF` ↔ `TransactionsDetails`

**Flow Direction:** OSFA → BO

**Description:** Invoice line items (products sold). Each row is one item with quantity, price, discounts, taxes, and bonus.

| Side | Table | PK Columns |
|---|---|---|
| OSFA | `OT_InvoiceDF` | `CompNo`, `VouType`, `VouYear`, `VouNo`, `ItemNo`, `Unit` |
| BO | `TransactionsDetails` | `CompanyID`, `TransactionTypeID`, `TransactionYear`, `TransactionNo`, `ItemCode`, `UnitID`, `ItemSerial` |

**Main Columns:**

| OSFA (OT_InvoiceDF) | BO (TransactionsDetails) | Notes |
|---|---|---|
| CompNo | CompanyID | |
| VouType | TransactionTypeID | |
| VouYear | TransactionYear | |
| VouNo | TransactionNo | Links to header |
| ItemNo | ItemCode | Product/item code |
| Unit | UnitID | Sales unit (box, piece, etc.) |
| *(auto-increment)* | ItemSerial | Line sequence (BO auto) |
| Qty | Quantity | Quantity sold |
| Bonus | Bonus | Free goods quantity |
| Price | Price | Unit selling price |
| DiscountAmount | DiscountAmount | Line discount value |
| DiscountPercent | DiscountPercent | Line discount % |
| VouDiscount | VoucherDiscount | Voucher discount |
| TaxType | TaxType | Tax type (inclusive/exclusive) |
| TaxPercent | TaxPercent | Tax percentage |
| TaxAmount | TaxAmount | Tax amount |
| UPrice | UPrice | Net unit price after discount |
| TaxPercent_1 | TaxPercent1 | Secondary tax 1 |
| TaxAmount_1 | TaxAmount1 | |
| TaxType_1 | TaxType1 | |
| TaxPercent_2 | TaxPercent2 | Secondary tax 2 |
| TaxAmount_2 | TaxAmount2 | |
| TaxType_2 | TaxType2 | |
| ItemStatus | ItemStatus | Item status flag |
| CustomerDiscountAmount | CustomerDiscountAmount | Customer-level discount |
| ForeignPrice | ForeignPrice | Foreign currency price |
| ForeignDiscountAmount | ForeignDiscountAmount | |
| ForeignVouDiscount | ForeignVouDiscount | |
| Manual_Bonus | Manual_Bonus | Manually added bonus |
| Manual_Disc | Manual_Disc | Manually applied discount |
| SP_Qty | SP_Qty | Special price quantity |
| ItemBarcode | ItemBarcode | Scanned barcode |
| QtyAsBonus | QtyAsBonus | Quantity treated as bonus |
| ReturnReason | ReturnReason | Reason for return (if return) |
| BonusAmount | BonusAmount | Bonus value |
| BonusTax | BonusTax | Tax on bonus |
| Notes | Notes | Line notes |
| LineSort | LineSort | Line sort order |
| — | CurrentQty | Stock snapshot at time of sale (BO only) |

**Key behavior:**
- FK to `OT_InvoiceHF`/`TransactionsHeaders` via `(CompNo, VouType, VouYear, VouNo)`.
- FK to `Items` via `(CompanyID, ItemCode)`.
- FK to `ItemsUnits` via `(CompanyID, UnitID)`.
- BO has `ItemSerial` as additional auto-increment PK column for unique line identification.
- BO also has `ExchangeRate`, `Approve` columns not in OSFA.

---

## 3. `OT_ConsOrderHF` ↔ `TransfersOrdersHeaders`

**Flow Direction:** OSFA → BO

**Description:** Consignment/transfer order headers. Used for stock transfers between vans (salesperson to salesperson) or from warehouse to van. Represents movement of inventory, not a sale.

| Side | Table | PK Columns |
|---|---|---|
| OSFA | `OT_ConsOrderHF` | `CompNo`, `OrderYear`, `OrderNo`, `VouType` |
| BO | `TransfersOrdersHeaders` | `CompanyID`, `OrderYear`, `OrderNo`, `VouType` |

**Main Columns:**

| OSFA (OT_ConsOrderHF) | BO (TransfersOrdersHeaders) | Notes |
|---|---|---|
| CompNo | CompanyID | |
| OrderYear | OrderYear | |
| OrderNo | OrderNo | |
| VouType | VouType | Transfer type (issue/receive/transfer) |
| OrderDate | OrderDate | Date of transfer |
| SalesmanNo | SalesPersonID | Salesperson (source/destination) |
| Posted | *(sync flag)* | 1=Ready for BO sync |
| GPSX / GPSY | Latitude / Longitude | Location |
| StoreNo | StoreNo | Warehouse/store reference |
| Notes | Notes | |
| TrDateTime | TrDateTime | Transaction timestamp |
| PrintOriginalCount | PrintOriginalCount | Print count |
| PrintCopyCount | PrintCopyCount | |
| ServerDate | ServerDate | Server-side timestamp |
| IssendSMS | — | SMS notification flag (OSFA only) |

**Key behavior:**
- BO has additional fields: `PostedToERP`, `Approve`, `WFApproved`, `TotalStock`, `ApproveDate`, `ApprovedBy`, `FirstApproval`, `UnloadBatchNo`, `PostToInvoice`.
- FK to `SalesPersons` and `Companies`.
- The `VouType` distinguishes different transfer types (e.g., issue from van, receive to van, warehouse-to-van).

---

## 4. `OT_ConsOrderDF` ↔ `TransfersOrdersDetails`

**Flow Direction:** OSFA → BO

**Description:** Transfer order line items — which items and quantities are being transferred.

| Side | Table | PK Columns |
|---|---|---|
| OSFA | `OT_ConsOrderDF` | `CompNo`, `OrderYear`, `OrderNo`, `VouType`, `ItemNo`, `UnitCode` |
| BO | `TransfersOrdersDetails` | `CompanyID`, `OrderYear`, `OrderNo`, `ItemCode`, `UnitID`, `VouType` |

**Main Columns:**

| OSFA (OT_ConsOrderDF) | BO (TransfersOrdersDetails) | Notes |
|---|---|---|
| CompNo | CompanyID | |
| OrderYear | OrderYear | |
| OrderNo | OrderNo | |
| VouType | VouType | Same as header |
| ItemNo | ItemCode | Item being transferred |
| UnitCode | UnitID | Unit of measure |
| Qty | Quantity | Quantity transferred |
| Notes | Notes | |
| — | QtyAfterApprove | Approved quantity (BO only) |
| — | DateAfterApprove | Approval date (BO only) |

**Key behavior:**
- FK to `OT_ConsOrderHF`/`TransfersOrdersHeaders` via `(CompNo, OrderYear, OrderNo, VouType)`.
- FK to `Items` and `ItemsUnits`.
- BO adds approval tracking fields (`QtyAfterApprove`, `DateAfterApprove`).

---

## 5. `OT_CustomerMF` ↔ `Customers` + `CustomersFinancialDetails`

**Flow Direction:** BO → OSFA (master data push)

**Description:** Customer master data. Created/maintained in BO, pushed to OSFA for the salesperson's tablet. `OT_CustomerMF` contains both customer info and financial settings. In BO this is split into two tables: `Customers` (identity/contact) and `CustomersFinancialDetails` (financial/assignment).

| Side | Table | PK Columns |
|---|---|---|
| OSFA | `OT_CustomerMF` | `CompNo`, `CustomerNo`, `SalesmanNo` |
| BO | `Customers` | `CompanyID`, `ID` |
| BO | `CustomersFinancialDetails` | `CompanyID`, `CustomerID`, `PositionsID`, `BusinessUnitID` |

**Main Columns — Customer Identity:**

| OSFA (OT_CustomerMF) | BO (Customers) | Notes |
|---|---|---|
| CompNo | CompanyID | |
| CustomerNo | ID | Customer ID |
| ArName | Name | Arabic name |
| EngName | ForeignName | English name |
| CustType | TypeID | Customer type |
| CustClass | ClassID | Customer class |
| Tel | TelephoneNo | Phone |
| Email | Email | |
| GPS X_COORD / Y_COORD | Latitude / Longitude | Coordinates |
| FullAddress | Address | |
| TaxNum | TaxNumber | VAT registration |
| CustomerBarcode | Barcode | |
| IsSuspended | IsSuspended | Suspended flag |
| ContactPerson | *(ContactPersons)* | Contact person |
| Notes | Notes | |
| GeoLevel1–5 | *(via LocationID)* | Geographical hierarchy |
| Group_ID | Group_ID | Customer group |

**Main Columns — Financial/Assignment:**

| OSFA (OT_CustomerMF) | BO (CustomersFinancialDetails) | Notes |
|---|---|---|
| SalesmanNo | *(via PositionsID → Positions → SalesPersons.PositionID)* | Customer-to-salesperson assignment |
| PriceLevel | PriceListID | Price list |
| CreditLimit | CreditLimit | Credit limit |
| CurrBalance | CustomerBalance | Current balance |
| ChqsBalance | ChqBalance | Cheques balance |
| Due | DueDays | Credit due days |
| ChqDue | ChqsDueDays | Cheque due days |
| TaxInclude | TaxInclude | Tax inclusive pricing |
| CreditCash | CreditCash | 1=Cash, 0=Credit |
| AllowChqs | AllowChqs | Allow cheques |
| DiscountPerc | DiscountPerc | Default discount % |
| PaymentTypeID | PaymentTypeID | Payment type |
| MaxInvoiceValue | MaxInvoiceValue | |
| MaxInvoiceCount | MaxInvoiceCount | |
| ChqLimit | ChqLimit | |
| ReturnCreditLimit | ReturnCreditLimit | |
| DeliveryDays | DeliveryDays | |
| CurrencyID | CurrencyID | |

**Key behavior:**
- Customer-to-salesperson assignment chain: `OT_CustomerMF.SalesmanNo` → `CustomersFinancialDetails.PositionsID` → `Positions.ID` → `SalesPersons.PositionID`.
- A customer can be assigned to different salespersons per business unit (each `(CustomerID, PositionsID, BusinessUnitID)` is a unique row in `CustomersFinancialDetails`).
- Master data is pushed from BO to OSFA (clear OSFA tables, re-insert with current data).
- `OT_CustomerMF` is denormalized — it combines customer info AND financial settings in one table.

---

## 6. `OT_SalesmanMF` ↔ `SalesPersons`

**Flow Direction:** BO → OSFA (master data push)

**Description:** Salesperson master data / user accounts for the tablet. Includes login credentials, permissions, serial number tracking, and targets.

| Side | Table | PK Columns |
|---|---|---|
| OSFA | `OT_SalesmanMF` | `CompNo`, `SalesmanNo` |
| BO | `SalesPersons` | `CompanyID`, `ID` |

**Main Columns:**

| OSFA (OT_SalesmanMF) | BO (SalesPersons) | Notes |
|---|---|---|
| CompNo | CompanyID | |
| SalesmanNo | ID | Salesperson ID |
| ArbSalesmanName | Name | Arabic name |
| EngSalesmanName | ForeignName | English name |
| Password | *(via UserID)* | Login password |
| Active | IsSuspended | 0=Suspended, 1=Active |
| StoreNo | *(DefaultStoreID)* | Default warehouse |
| SalesmanGroup_ID | GroupID | Group membership |
| UserName | UserID | Login username |
| SalesmanTel | TelephoneNo | Phone |

**Permissions / Feature Flags (in `OT_SalesmanMF`):**

| OSFA Column | Description |
|---|---|
| AllowSales | Can create sales invoices |
| AllowReturnSales | Can create return invoices |
| AllowOrder | Can create orders |
| AllowRec | Can record receipts/payments |
| AllowCons | Can create consignment transfers |
| AllowCustStock | Can manage customer stock |
| AllowVanTransfer | Can do van-to-van transfer |
| AllowChangePrice | Can override prices |
| AllowItemDisc | Can apply item discounts |
| AllowVouDisc | Can apply voucher discounts |
| AllowMakeBonus | Can add free goods (bonus) |
| AllowAddCust | Can add new customers |
| AllowSalesQuotation | Can create quotations |
| AllowItemsReplacment | Can do item replacements |
| UseMultiStoreInSales | Can sell from multiple stores |

**Next Serial Tracking (per salesperson):**

| OSFA Column | What it tracks |
|---|---|
| NextSerial | Next order number |
| InvNextSerial | Next invoice number |
| RetInvNextSerial | Next return invoice number |
| RecNextSerial | Next receipt number |
| ConsNextSerial | Next consignment number |
| CustStockNextSerial | Next customer stock number |
| SalesmanStockNextSerial | Next van stock number |
| ReturnOrderNextSerial | Next return order number |
| VanTransferNextSerial | Next van transfer number |

**Targets (in `OT_SalesmanMF`):**

| OSFA Column | Description |
|---|---|
| MonthlySalesTarget | Monthly sales target |
| MonthlySalesAmount | Current month's sales achieved |
| MonthlyCollectionTarget | Collection target |
| MonthlyCollectionAmount | Current month's collection achieved |
| CreditLimit | Salesperson's credit limit |
| SalesmanBalance | Balance amount |
| VouDiscLimit | Voucher discount limit |

**Key behavior:**
- FK to `Positions` via `PositionID` in BO (`SalesPersons.PositionID → Positions.ID`).
- FK to `SalesPersonsGroups` via `GroupID`.
- FK to `CompanyBranches` via `CompanyBrancheID`.
- BO has additional fields: `Parent` (hierarchy), `DeviceID`, `BusinessUnitID`, `SalesPersonType`, `DayOff`, `Level`, `VehicleId`, `CarID`, `CoverageTargetPer`, `ProductivityTargetPer`, `MaxStockValue`, etc.

---

## 7. `OT_StoreItemsQty` ↔ *(Warehouse Stock Reference)*

**Flow Direction:** BO → OSFA (master data push)

**Description:** Store/warehouse item stock quantities. This data represents the current stock levels in a specific warehouse or van. It is sent from BO to OSFA so the tablet knows available quantities. There is also `OT_StoreItemsQty_Main` which adds a `SalesmanNo` scope.

| Side | Table | PK Columns |
|---|---|---|
| OSFA | `OT_StoreItemsQty` | `CompNo`, `StoreNo`, `ItemNo` |
| OSFA | `OT_StoreItemsQty_Main` | `CompNo`, `SalesmanNo`, `StoreNo`, `ItemNo` |

**Main Columns:**

| Column | Type | Notes |
|---|---|---|
| CompNo | smallint | Company |
| StoreNo | int | Store/warehouse code |
| *(SalesmanNo)* | int | OT_StoreItemsQty_Main only |
| ItemNo | varchar(100) | Item/product code |
| Qty | money | Current stock quantity |

**BO counterpart:**
There is no single direct BO equivalent table. Relevant BO tables include:

- **`SalesPersonItemsBalance`** → `(CompanyID, SalesPersonID, ItemCode, UnitCode, ItemQuantity)` — Tracks each salesperson's van stock balance.
- **`StoresItemsQty`** (or similar store inventory tables) — Tracks warehouse-level stock.

**Key behavior:**
- `OT_StoreItemsQty` is warehouse-level stock (no salesperson scope).
- `OT_StoreItemsQty_Main` is per-salesperson van stock (scoped by `SalesmanNo`).
- Both are populated from BO and pushed to OSFA during master data sync.
- When a salesperson creates invoices on the tablet, the system deducts from this stock.
- After posting to BO, the BO updates its own stock tables accordingly.
