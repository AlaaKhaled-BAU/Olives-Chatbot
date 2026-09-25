# Ticket 0023: Delivery Salespersons (Type 7) See Zero-Qty Items — OT_SendItemsInfo Filtered via Bonanza View (Khashram)

* **Date & Time**: 2026-09-22 (documented)
* **Client**: Khashram
* **System Component**: Olives_BO — `OT_SendItemsInfo` (called by `OT_SendSalesmanData`) → `OT_ItemsMF`; `ClientsActive`; `SalesPersons.SalesPersonType = 7` (delivery)
* **Symptom Category**: DB / Master-data sync (custom procedure change)
* **Reported Issue**:
  Requirement: **delivery salespersons (`SalesPersonType = 7`) should read only `>0` quantity items** on the tablet.

* **Root Cause & Diagnosis**:
  - Out of the box, `OT_SendItemsInfo` sends the full assigned item set (reads `Items`, `PriceListDetails`, `ItemsUnits`, etc., writes `OT_ItemsMF`) regardless of on-hand quantity.
  - Checked their **`ClientsActive`** handling inside `OT_SendItemsInfo` to scope the change to the right client/salesmen.
  - **Altered the procedure** so that for delivery salespersons it reads a **view on Bonanza** holding **all non-zero quantities**: if the item is in that view (`qty > 0`), insert it; otherwise skip it.

* **Resolution / Customer Action**:
  - Custom `OT_SendItemsInfo` branch (Khashram only): for `SalesPersonType = 7`, inner-join / exists-check the Bonanza non-zero-qty view before inserting into `OT_ItemsMF`.
  - Normal salespersons unaffected (full item set as before).
  - Re-run Send Data / tablet data update for a delivery salesman and confirm zero-qty items no longer appear.

* **Vault Validation Notes**:
  - ✅ **`OT_SendItemsInfo`** confirmed in vault (`db/name_index.json` → `obsidian/olives/Olives_BO/Procedures/OT_SendItemsInfo.md`): params `@CompNo, @ClientActive, @SalesmanNo, @PositionsID`; reads `Items`, `PriceListDetails`, `ItemsUnits(+Details)`, `ItemsCategories`, `ItemsPriority`, `CustomersFinancialDetails`; writes `OT_ItemsMF`; caller `OT_SendSalesmanData`. Matches the "checked ClientsActive on OT_SendItemsInfo" step.
  - ✅ **`SalesPersons.SalesPersonType`** confirmed (`db/bo_tables.md:4388`; second occurrence 5586) — value 7 = delivery per case.
  - ⚠️ The **Bonanza view** is client-specific and not in the generic vault — by design. Any future `OT_SendSalesmanData` / procedure regeneration will overwrite this customization; keep the Khashram patch script under version control.

* **Suggested Verification Queries**:
  ```sql
  -- 1) Confirm the salesman is delivery type 7
  SELECT ID, Name, PositionID, Parent, SalesPersonType
  FROM Olives_BO.dbo.SalesPersons
  WHERE CompanyID = <company> AND ID = <salesman_no>;

  -- 2) Confirm the procedure branch references the Bonanza view + ClientsActive
  SELECT OBJECT_DEFINITION(OBJECT_ID(N'dbo.OT_SendItemsInfo')) AS ProcText;
  -- expect: @ClientActive filter + SalesPersonType = 7 + JOIN/EXISTS (<BonanzaNonZeroQtyView>)

  -- 3) Spot-check: an item with zero qty must NOT reach the tablet set for type-7 salesman
  -- (replace with the actual Bonanza view name used in the patch)
  SELECT ItemCode FROM <BonanzaNonZeroQtyView> WHERE ItemCode = N'<item>';
  ```

* **Verification Result**: Customization documented as reported — delivery (type 7) item sync filtered to `qty > 0` via Bonanza view inside `OT_SendItemsInfo`, scoped by `ClientsActive`. Verify on one delivery tablet that zero-qty items are gone while a normal salesman still sees the full list.

(End of file)
