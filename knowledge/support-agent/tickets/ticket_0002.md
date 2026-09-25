# Ticket 0002: New Items Missing in Front Office Custody Loading (Upload Order)

* **Date & Time**: 2026-06-21
* **System Component**: OSFA Android / Back Office Sync
* **Symptom Category**: DB
* **Reported Issue**:
  Salesmen report that new items are not appearing in the Front Office (OSFA tablet) when doing custody loading (Upload Order). Older items work fine. Only newly created items fail to appear.

---

## Root Cause & Diagnosis

### Chain of Causation (Items Visbility Pipeline)

```
Items table (BO)
  → SalesPersonItemsAssignment?           ← MOST COMMON BREAKAGE POINT
    → ItemsCategories? (INNER JOIN)        ← Missing category = invisible
      → ItemsUnits? (INNER JOIN)           ← Missing default unit = invisible
        → Items.IsSuspended = 0?           ← Suspended items excluded
          → OT_ItemsMF (on OSFA_DB)        ← Cleared & rebuilt per sync
            → Tablet displays items
```

### Primary Hypothesis (90% likelihood): Missing `SalesPersonItemsAssignment` Record

The stored procedure `OT_SendItemsInfo` populates `OT_ItemsMF` (the items master on the tablet) by JOINing:

```sql
FROM Items
INNER JOIN SalesPersonItemsAssignment ON (...)
INNER JOIN ItemsCategories ON (...)
INNER JOIN ItemsUnits ON (...)
WHERE (SalesPersonItemsAssignment.PositionsID = @PositionsID)
  AND (SalesPersonItemsAssignment.CompanyID = @CompNo)
```

**Key finding:** `SalesPersonItemsAssignment` is an INNER JOIN. If a new item doesn't have a row in this table for the salesman's position, the entire item row is excluded — the item never reaches `OT_ItemsMF`, and the tablet never shows it.

**Why it happens:** When a new item is created in the Back Office (Items table), there is no automatic process that inserts a corresponding row in `SalesPersonItemsAssignment`. The user must explicitly assign the item to salesman positions. If this step was missed, the new item exists in the `Items` table but has no link to any salesman.

### Secondary Hypothesis (7%): `ItemsCategories` or `ItemsUnits` Not Set

Both joins are `INNER JOIN`:
- If `Items.CategCode` is NULL or doesn't match an entry in `ItemsCategories` → item excluded
- If `Items.UnitID` (default unit) is NULL or doesn't match `ItemsUnits` → item excluded

New items that weren't properly categorized or didn't have a default unit assigned would fail these joins silently.

### Tertiary Hypothesis (5%): `SalesPersonItemsBalance` Filter (Client-Specific)

For certain client types (e.g., `@ClientActive = 197`), the item query includes:
```sql
AND ISNULL(SalesPersonItemsBalance.ItemQuantity, 0) > 0
```

If your `ClientActive` value is one of these filtered types, new items with zero balance would be excluded.

### Quaternary Hypothesis (3%): `Items.IsSuspended = 1`

For client types using the "Don't send suspended items" branch (client IDs: 5, 14, 8, 74, 12, 7, 35, 76, 87, 158, 82, 85, 51, 78, 132, 144, 173, 176), items with `IsSuspended = 1` are filtered out.

### Quinary Hypothesis (3%): Option 279 — "Filter Items Units in Upload Order"

If Option 279 is enabled, items with `UsedInUploadOrder = 0` are excluded from the upload order unit filter. However, `ISNULL(Items.UsedInUploadOrder, 1) = 1` means NULL defaults to include, so this only matters if explicitly set to 0.

### Senary Hypothesis (2%): Sync Not Run / Sync Procedure Error

The sync procedure clears and rebuilds `OT_ItemsMF`:
```sql
DELETE FROM [OSFA_DB].[dbo].[OT_ItemsMF] WHERE ...
-- (OT_SendItemsInfo called here)
```

If the salesman hasn't performed a data sync after the item was assigned, OR if the sync procedure hit a `goto EXITPRO` earlier (e.g., from stock balance errors, `IsUpdatedStock` validation), the new items wouldn't appear.

---

## Verification Queries to Confirm

### Check 1: Is the item assigned to the salesman's position?
```sql
-- Find the salesman's PositionID
SELECT ID, Name, PositionID 
FROM SalesPersons 
WHERE ID = <Salesman_ID>;

-- Check if the item is assigned to this position
SELECT * 
FROM SalesPersonItemsAssignment 
WHERE CompanyID = <CompanyID> 
  AND PositionsID = <PositionID> 
  AND ItemCode = '<New_Item_Code>';
```
If no row returned → **this is the root cause**.

### Check 2: Does the item have proper category and unit?
```sql
SELECT ItemCode, CategCode, UnitID, IsSuspended, UsedInUploadOrder, IsForSales
FROM Items 
WHERE CompanyID = <CompanyID> 
  AND ItemCode = '<New_Item_Code>';
```

### Check 3: Verify OT_ItemsMF has the item after sync
```sql
SELECT * FROM OSFA_DB.dbo.OT_ItemsMF 
WHERE CompNo = <CompanyID> 
  AND SalesmanNo = <Salesman_ID>
  AND ItemNo = '<New_Item_Code>';
```
If no row returned after sync → the item was excluded during sync.

---

## Solution

1. **Assign the item to salesman positions** in Back Office:
   - Go to Items Management → Item Assignment
   - Add the new item to the relevant salesman positions
   - Or insert directly:
     ```sql
     INSERT INTO SalesPersonItemsAssignment (CompanyID, PositionsID, ItemCode, DefinitionDate)
     VALUES (<CompanyID>, <PositionID>, '<New_Item_Code>', GETDATE());
     ```

2. **Run a full data sync** to the salesman's tablet (Send Data from BO).

3. **Verify** the item appears in `OT_ItemsMF` using Check 3 above.

---

## Verification Result

Pending user execution of SELECT queries to confirm the hypothesis.
