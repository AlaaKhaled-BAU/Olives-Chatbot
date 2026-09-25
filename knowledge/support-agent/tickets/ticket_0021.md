# Ticket 0021: Change Route Customers Section Colors on Tablet — Op 369 + OT_CustomersClasses (Blue Diamond)

* **Date & Time**: 2026-09-20 (documented)
* **Client**: Blue Diamond
* **Reported Via**: Bassam
* **System Component**: OSFA (Tablet) — Route customers list, System Options (`OT_SystemOptions`, Op_ID 369), `OT_CustomersClasses` / `CustomersClasses`
* **Symptom Category**: Configuration / How-to
* **Reported Issue**:
  Customer asked to **change the colors of the route customers section on the tablet**.

* **Root Cause & Diagnosis**:
  - Route-list coloring is controlled by system option **Op_ID 369 = "Route List Coloring By Cust Class"** (`0=Off | 1=On`).
  - When **369 = 1**, the tablet colors the route customers list **by customer class**.
  - The colors themselves are defined from the customer-classes master data — tablet side **`OT_CustomersClasses`** (`CompNo, SalesmanNo, Class_ID, ArDesc, EngDesc, Ref1, Ref2`), synced from BO **`CustomersClasses`** (`CompanyID, ID, Name, ShortName, Reference1, Reference2`).
  - Related option **Op_ID 361 = "Route Cust View Type"** (`0=By Route | 1=By Cust Type | 2=By Cust Class`) controls grouping/view of the same route list — use `2=By Cust Class` together with 369 when the goal is class-based display.

* **Resolution / Customer Action**:
  - Enable **Op_ID 369 = 1** for the target salesman(s) (or `SalesmanNo = 0` default row) in `OT_SystemOptions`.
  - Define/adjust the per-class colors in the customer-classes definition (`OT_CustomersClasses` / BO `CustomersClasses` screen — Customers → Customers Classes, Image 75).
  - Run **data update on the tablet** so the new option value + class definitions sync down, then re-open the Route section to verify colors.

* **Vault Validation Notes**:
  - ✅ **Op_ID 369 = "Route List Coloring By Cust Class" — `0=Off | 1=On`** confirmed in `knowledge/reference/system option explained.md` (line 364) and in `apps/support-agent/system_options_guide.md` (`369 | Route List Coloring By Cust Class | 0=Off`).
  - ✅ **Op_ID 361 = "Route Cust View Type" — `0=By Route | 1=By Cust Type | 2=By Cust Class`** confirmed in `knowledge/reference/system option explained.md` (line 356) — relevant companion view mode.
  - ✅ **OSFA `OT_CUSTOMERSCLASSES`** confirmed in `db/osfa_tables.md` (lines 491–499): `CompNo, SalesmanNo, Class_ID, ArDesc, EngDesc, Ref1, Ref2` — PK `(CompNo, SalesmanNo, Class_ID)`; obsidian note `obsidian/olives/OSFA_DB/Tables/OT_CustomersClasses.md` exists.
  - ✅ **BO `CUSTOMERSCLASSES`** confirmed in `db/bo_tables.md` (lines 635–642): `CompanyID, ID, Name, ShortName, Reference1, Reference2`; obsidian note `obsidian/olives/Olives_BO/Tables/CustomersClasses.md` exists, with `OT_SendCustomersInfo` reading `CustomersClasses` for the tablet sync.
  - ⚠️ **Schema gap noted**: neither vault copy currently documents an explicit `Color` column on `OT_CustomersClasses` / `CustomersClasses` (only `Ref1/Ref2` + desc fields). Colors are set on the class records per Bassam's flow (BO Customers Classes screen); if live DB has a newer `Color` column it is not yet in `db/*_tables.md` / obsidian — flagged for drift check.
  - ⚠️ **Docs gap noted**: `knowledge/back-office/customers.md` §4.13 says classes "are not shown in salesman tablet" — outdated when 369=1 (they drive route-list colors). Left as-is here; needs a one-line correction.

* **Suggested Verification Queries**:
  ```sql
  -- 1) Check op 369 for the salesman (or SalesmanNo=0 default)
  SELECT CompNo, Op_ID, SalesmanNo, Op_Desc, Op_Value, Notes
  FROM OSFA_DB.dbo.OT_SystemOptions
  WHERE Op_ID = 369 AND CompNo = <company>
    AND (SalesmanNo = 0 OR SalesmanNo = <salesman_no>);

  -- 2) Companion view mode (expect 2 = By Cust Class for class-based route view)
  SELECT CompNo, Op_ID, SalesmanNo, Op_Value
  FROM OSFA_DB.dbo.OT_SystemOptions
  WHERE Op_ID = 361 AND CompNo = <company>
    AND (SalesmanNo = 0 OR SalesmanNo = <salesman_no>);

  -- 3) Class definitions pushed to the tablet (colors live here per case flow)
  SELECT CompNo, SalesmanNo, Class_ID, ArDesc, EngDesc, Ref1, Ref2
  FROM OSFA_DB.dbo.OT_CustomersClasses
  WHERE CompNo = <company> AND SalesmanNo IN (0, <salesman_no>)
  ORDER BY Class_ID;

  -- 4) BO master (source of the sync)
  SELECT CompanyID, ID, Name, ShortName, Reference1, Reference2
  FROM Olives_BO.dbo.CustomersClasses
  WHERE CompanyID = <company>
  ORDER BY ID;

  -- 5) Enable coloring (via BO-supported path, then tablet data-update;
  --    do NOT hand-edit OT_SystemOptions permanently — BO sync overwrites it)
  --    Set Op_Value = '1' for Op_ID 369 (SalesmanNo = 0 = all salesmen).
  ```

* **Verification Result**: Case flow verified against vault — **Op 369 = 1 enables route-list coloring by customer class; colors are defined in `OT_CustomersClasses` / `CustomersClasses`**. No code change; configuration + tablet data-update required. Open item: confirm live `CustomersClasses` color column/field name if it differs from `Ref1/Ref2` in this snapshot.

(End of file)
