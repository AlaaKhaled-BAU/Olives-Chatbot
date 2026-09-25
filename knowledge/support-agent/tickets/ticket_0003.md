# Ticket 0003: Edit Invoice Printing Font on Salesman Printer

* **Date & Time**: 2026-06-21
* **System Component**: Back Office / OSFA Android (Bluetooth Printing)
* **Symptom Category**: Configuration
* **Reported Issue**:
  How to edit the invoice printing font (specifically font size) for a specific salesman (salesman #10) on their Bluetooth portable printer.

---

## Root Cause & Diagnosis

Invoice printing layout — including font family and font size — is controlled through **Layout Settings** defined in the Back Office. Each salesman is assigned a Layout Design (via the Salespersons page), which references a set of layout properties stored in `OSFA_DB.dbo.OT_Layout_Setting`.

The font is **PropertyID = 2 ("Font")** within a layout, where:
- `Value1` = font family name (e.g., `Arial`, `Calibri`)
- `Value2` = font size or additional style parameters

The layout properties defined in the system are:

| PropertyID | Description | Purpose |
|---|---|---|
| 1 | Layout Width | Overall print area width |
| **2** | **Font** | **Font name (Value1) and font size (Value2)** |
| 3 | Logo Size (Width, Height) | Printed logo dimensions |
| 4 | Sewoo 4 inch Page Width | Page width for 4-inch Sewoo printers |

The flow:
1. BO user assigns a `LayoutId` to a salesman via **Salespersons → Edit → Layout Design**
2. The OSFA tablet syncs and reads the assigned `LayoutId`
3. When printing an invoice/receipt on the Bluetooth printer, the OSFA app reads `OT_Layout_Setting` for that layout's properties
4. The Font property (PropertyID=2) determines the printed text appearance

---

## Verification Queries

### Check 1: Find which LayoutId is assigned to salesman 10

The layout-to-salesman link is stored in `OSFA_DB.dbo.OT_SystemOptions`. Run:

```sql
-- See all system options for salesman 10
SELECT Op_ID, Op_Desc, Op_Value, PrinterType
FROM OSFA_DB.dbo.OT_SystemOptions
WHERE SalesmanNo = 10
  AND CompNo = <CompanyID>
ORDER BY Op_ID;
```

Look for a row where `Op_Value` references a `LayoutId`. Also check in the BO UI: **Settings → Salespersons → edit salesman #10 → note the "Layout Design" field value**.

### Check 2: View current font settings for that layout

```sql
SELECT LayoutId, LayoutName, PropertyID, Description, Value1, Value2
FROM OSFA_DB.dbo.OT_Layout_Setting
WHERE LayoutId = <LayoutId>
  AND CompNo = <CompanyID>
ORDER BY PropertyID;
```

### Check 3: List all available layouts

```sql
SELECT CompNo, LayoutId, LayoutName
FROM OSFA_DB.dbo.OT_Layout_Setting
WHERE CompNo = <CompanyID>
GROUP BY CompNo, LayoutId, LayoutName;
```

---

## Solution

### Step 1: Identify the LayoutId

Use the BO UI or Check 1 query above to determine which `LayoutId` is assigned to salesman 10.

### Step 2: Update the Font property

```sql
-- Change font size for salesman 10's layout
-- Adjust Value1 (font name) and Value2 (font size) as needed
UPDATE OSFA_DB.dbo.OT_Layout_Setting
SET Value1 = 'Arial',       -- font family name
    Value2 = '10'            -- font size
WHERE LayoutId = <LayoutId>
  AND PropertyID = 2
  AND CompNo = <CompanyID>;
```

### Step 3: Sync the salesman's tablet

Perform a full **Send Data** from the Back Office to the salesman. The OSFA tablet will pick up the updated layout settings on next sync and apply the new font when printing invoices.

---

## Related System Options (for reference)

| Op_ID | Description | Relevance |
|---|---|---|
| 104 | Print Image Factor | Scales print image (1 = default, 1.25, 1.5, etc.) |
| 155 | Print Pause Time Between Images | Delay between print jobs (ms) |
| 156 | Print Spacing | Sewoo 3-inch (line count) / 4-inch (form height) |
| 234 | Sewoo Splitting Image Height | Image split height for Sewoo printers |
| 342 | Printing Image Quality | 0–100 quality setting |
| 745 | Grant 4-inch Printing on Chinese Printers | Enable 4-inch on Chinese printer models |

---

## Verification Result

Pending user execution of the SELECT queries to confirm the LayoutId for salesman 10, then UPDATE and sync to verify font change takes effect on invoice printing.
