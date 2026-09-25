# Ticket 0022: Item Sold at 8.017 Instead of ~9.3 — Op 12 (Price Tax) Mismatch (Yan)

* **Date & Time**: 2026-09-22 (documented)
* **Client**: Yan
* **System Component**: OSFA (Tablet) pricing — Price lists (`PriceListDetails`), customer tax flag (`OT_CustomerMF.TaxInclude` / `CustomersFinancialDetails.TaxInclude`), System Options (`OT_SystemOptions`, Op_ID 12)
* **Symptom Category**: Configuration / Pricing-Tax
* **Reported Issue**:
  An item was being sold at **8.017** while it should have been around **9.3**.

* **Root Cause & Diagnosis**:
  - Checked the **price list** to see if the tax is included — looked correct.
  - Checked the **customer** (tax-included flag) — correct.
  - Checked the **tablet**: it reads the price as **6.98 + 1.022 tax** (≈ 8.00 ≈ 8.017 sold price).
  - Root cause was **system option 12 (Price Tax) = 1**: value 1 means **the price sent is tax-included**, while in this case the list price was actually tax-exclusive. The tablet therefore backed the base out / treated the gross as net and re-added only a small tax instead of adding full tax on top.
  - Math cross-check (approximate): correct net 8.017 + ~16% tax ≈ 9.30; tablet computed ≈ 6.98 base + 1.022 tax ≈ 8.00, i.e. it treated the incoming price as already containing tax.

* **Resolution / Customer Action**:
  - Set **Op_ID 12 = 0** (price sent is tax-exclusive) for the affected salesman(s) / company, matching how the price list is actually maintained.
  - Run **tablet data update** and re-test the same item/customer — expected price ≈ 9.3.

* **Vault Validation Notes**:
  - ✅ **Op_ID 12 = "Price Tax" — `0=Off | 1=On`** confirmed in `knowledge/reference/system option explained.md` (line 14) and `apps/support-agent/system_options_guide.md` (`12 | Price Tax | 0=Off`, Pricing & Discounts). Description is terse but not wrong — 1 = prices sent tax-included. No KB correction needed.
  - ✅ Customer tax flag path exists: `OT_CustomerMF.TaxInclude [bit]` (`db/osfa_tables.md`) mirrors BO financial-details tax setting — consistent with the "checked customer tax-included" step.
  - ✅ Price-list source path exists: `OT_SendItemsInfo` reads `PriceListDetails` → `OT_ItemsMF` (obsidian `OT_SendItemsInfo.md`), so a wrong Op 12 flips tablet-side gross/net interpretation for every price-list item.

* **Suggested Verification Queries**:
  ```sql
  -- 1) Check op 12 for the salesman (or SalesmanNo=0 default)
  SELECT CompNo, Op_ID, SalesmanNo, Op_Desc, Op_Value
  FROM OSFA_DB.dbo.OT_SystemOptions
  WHERE Op_ID = 12 AND CompNo = <company>
    AND (SalesmanNo = 0 OR SalesmanNo = <salesman_no>);

  -- 2) Price-list row for the item (is the list price net or gross?)
  SELECT PriceListID, ItemCode, UnitID, Price, TaxType, TaxPercent
  FROM Olives_BO.dbo.PriceListDetails
  WHERE CompanyID = <company> AND ItemCode = N'<item>';

  -- 3) Customer tax-included flag
  SELECT CompanyID, CustomerID, PriceListID, TaxInclude
  FROM Olives_BO.dbo.CustomersFinancialDetails
  WHERE CompanyID = <company> AND CustomerID = <customer_no>;
  ```

* **Verification Result**: Price-list and customer flags were correct; tablet split (6.98 + 1.022) proves Op 12 = 1 mis-declared a net price as tax-included. Fix = Op 12 → 0 + tablet data update. Re-verify sold price ≈ 9.3.

(End of file)
