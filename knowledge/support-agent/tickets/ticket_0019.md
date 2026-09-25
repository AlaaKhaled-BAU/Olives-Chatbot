# Ticket 0019: Report Returns No Data — Manager Hierarchy / FilterCust (Parent vs Tree)

* **Date & Time**: 2026-07-21 (investigation / fix cycle)
* **Client**: أحمد / جزر الملايو (Ahmad / Malay Islands)
* **Reported Via**: محمد عبدو (Mohammad Abdo)
* **System Component**: Olives_BO — Reports / Stored Procedures
  - Primary: `dbo.RptOnlineRptReturnDetailsForWF`
  - Reference (working): `dbo.RptSalesPersonItemBalance` (ELSE block)
  - Related hierarchy helpers: `dbo.Fun_GetSalesPersonTree` / `dbo.Fun_GetSalesmanTreeByID`
  - Follow-up candidate (same family): `dbo.RptDailySalesSummary`
* **Symptom Category**: DB / Report — Empty Result Set (Hierarchy + Customer Filter)
* **Reported Issue**:
  Report `RptOnlineRptReturnDetailsForWF` returns **no header/detail rows** when run for a salesman/manager (validated case: **SalesmanNo = 1003**, CompanyID = 1), even though approved non-void transactions exist in the requested date range. Need to align salesman–parent filtering with a **working report** without changing unrelated procedure logic, and **comment old code** (do not delete).

---

## Root Cause & Diagnosis

### What the report was trying to do

The procedure builds a **header** result set (and a **details** set) from:

1. `TransactionsHeaders` (+ `Customers`, `SalesPersons`)
2. A customer scope subquery **`FilterCust`** (customers linked via `CustomersFinancialDetails` ↔ salesman `PositionID`)
3. A salesman hierarchy filter via **`Fun_GetSalesPersonTree(@CompanyID, @SalesPersonID)`**, where `@SalesPersonID` was looked up from `SalesPersons` using **`PositionID = @SalesmanNo`**

### Working pattern (Query 2 — `RptSalesPersonItemBalance` ELSE)

```sql
WHERE ...
  AND (SalesPersons.Parent = @SalesmanNo OR @SalesmanNo = -1)
```

- Treats `@SalesmanNo` as a **SalesPerson ID (parent/manager)**, not only a Position lookup key.
- Includes the parent’s **direct children** via `Parent`.
- Supports **`-1` = all salesmen**.

### Broken pattern (Query 1 — `RptOnlineRptReturnDetailsForWF`)

```text
@SalesmanNo
  → lookup SalesPersonID WHERE PositionID = @SalesmanNo
  → Fun_GetSalesPersonTree(CompanyID, SalesPersonID)
  → JOIN headers on SalesPersonID IN tree

AND FilterCust:
  SalesPersons.ID = @SalesmanNo
  JOIN CustomersFinancialDetails ON PositionID = PositionsID
```

### Diagnostic evidence (Salesman 1003, CompanyID 1)

| Check | Result | Meaning |
|-------|--------|---------|
| SalesPerson lookup | ID **1003** exists | Person is valid |
| Hierarchy / parents | 1003 → Parent **1000** → **2000** | Org chain exists |
| **FilterCust** (`sp.ID = 1003` + CFD on Position) | **0 rows** | **Primary killer** |
| Headers in date range (approved, not void, type match) | **~23,763** | Data exists |
| Top `SalesPersonID`s on headers | 1005, 1120, 1099, … | **1003 not a high-volume direct seller** |
| Date span on table | Valid | Not a date-range bug |

### Root cause (precise)

1. **FilterCust was too narrow for managers**  
   It only kept customers assigned to **`SalesPersons.ID = @SalesmanNo`** through `CustomersFinancialDetails.PositionsID = SalesPersons.PositionID`.  
   Manager **1003** has **no (or insufficient) direct customer-position assignments**. Customers sit on **child salesmen positions**.  
   `FilterCust` → empty → **INNER JOIN** wipes the entire header set **before** hierarchy usefulness matters.

2. **Hierarchy approach mismatched the working report**  
   Tree/function path + PositionID lookup did not match the proven **`Parent = @SalesmanNo OR @SalesmanNo = -1`** pattern used in `RptSalesPersonItemBalance`.

3. **Side lesson — `Fun_GetSalesmanTreeByID`**  
   Function correctly returns the downline (e.g. for `Fun_GetSalesmanTreeByID(1, 1003)` many rows with **`SalesPersonType = 4`**).  
   Combining the tree with `SalesPersonType < 4` **and** `ID <> @SalesmanNo` yields **zero rows**, because leaf reps are type 4 and the only type&lt;4 node is often the root manager.  
   Types **4, 7, 8** are treated as leaf/checked nodes inside `Fun_GetSalesmanTreeByID` (no further expansion under them).

```
Transactions exist ✓
Tree / Parent chain exists ✓
FilterCust for manager ID only → 0 customers ✗  ← failure point
INNER JOIN FilterCust → report empty
```

---

## Resolution

### Design rules applied

- Keep procedure business logic (dates, Approve, IsVoid, TransactionType, customer number range, detail columns).
- **Comment out** old Position→ID tree path; do not delete.
- Align salesman scope with working ELSE pattern:
  - self: `ID = @SalesmanNo`
  - children: `Parent = @SalesmanNo`
  - all: `@SalesmanNo = -1`

### Header — FilterCust (NEW)

```sql
INNER JOIN (
    SELECT DISTINCT sp.CompanyID, cdf.CustomerID
    FROM SalesPersons sp
    INNER JOIN CustomersFinancialDetails cdf
        ON sp.CompanyID = cdf.CompanyID
       AND sp.PositionID = cdf.PositionsID
    WHERE sp.CompanyID = @CompanyID
      AND (
            sp.ID = @SalesmanNo
         OR sp.Parent = @SalesmanNo
         OR @SalesmanNo = -1
          )
) AS FilterCust
    ON Customers.CompanyID = FilterCust.CompanyID
   AND Customers.ID = FilterCust.CustomerID
```

### Header — salesman filter on transaction owner (NEW)

```sql
AND (
       SalesPersons1.ID = @SalesmanNo
    OR SalesPersons1.Parent = @SalesmanNo
    OR @SalesmanNo = -1
    )
```

*(Old `Fun_GetSalesPersonTree` join and `PositionID`→`SalesPersonID` lookup commented out.)*

### Details — same Parent pattern (NEW)

```sql
LEFT JOIN SalesPersons AS TxnSalesPerson
    ON TransactionsHeaders.CompanyID = TxnSalesPerson.CompanyID
   AND TransactionsHeaders.SalesPersonID = TxnSalesPerson.ID
...
AND (
       TxnSalesPerson.ID = @SalesmanNo
    OR TxnSalesPerson.Parent = @SalesmanNo
    OR @SalesmanNo = -1
    )
```

### What changed (summary)

| Location | Old (broken for manager 1003) | New (aligned with working report) |
|----------|-------------------------------|-----------------------------------|
| `@SalesmanNo` usage | PositionID lookup → tree | Treated as SalesPerson ID (parent/self) |
| FilterCust | `sp.ID = @SalesmanNo` only | `ID` **OR** `Parent` **OR** `-1` |
| Header salesman scope | `Fun_GetSalesPersonTree` | `ID` / `Parent` / `-1` |
| Details salesman scope | `Fun_GetSalesPersonTree` | same Parent pattern |
| All-salesmen fallback | None | `@SalesmanNo = -1` |

### Related function note (`Fun_GetSalesmanTreeByID`)

If a caller needs **full multi-level downline** (not only direct children), prefer the tree function **without** `SalesPersonType < 4` when the goal is field reps (type 4).  
The procedure fix used **one-level Parent** to match `RptSalesPersonItemBalance` ELSE — intentional consistency, not a full recursive rebuild.

---

## Verification Queries

```sql
-- 1) Manager exists + parent chain
SELECT ID, Name, PositionID, Parent, SalesPersonType
FROM Olives_BO.dbo.SalesPersons
WHERE CompanyID = 1 AND (ID = 1003 OR PositionID = 1003);

-- 2) OLD FilterCust (expected 0 for manager without direct CFD link)
SELECT DISTINCT cdf.CompanyID, cdf.CustomerID
FROM SalesPersons sp
INNER JOIN CustomersFinancialDetails cdf
  ON sp.CompanyID = cdf.CompanyID AND sp.PositionID = cdf.PositionsID
WHERE cdf.CompanyID = 1 AND sp.ID = 1003;

-- 3) NEW FilterCust scope (self + children)
SELECT DISTINCT sp.ID, sp.Name, sp.Parent, cdf.CustomerID
FROM SalesPersons sp
INNER JOIN CustomersFinancialDetails cdf
  ON sp.CompanyID = cdf.CompanyID AND sp.PositionID = cdf.PositionsID
WHERE sp.CompanyID = 1
  AND (sp.ID = 1003 OR sp.Parent = 1003 OR 1003 = -1);

-- 4) Who reports to 1003?
SELECT ID, Name, PositionID, Parent, SalesPersonType
FROM SalesPersons
WHERE CompanyID = 1 AND (Parent = 1003 OR ID = 1003);

-- 5) Tree function sample (multi-level; mostly type 4 under 1003)
SELECT * FROM dbo.Fun_GetSalesmanTreeByID(1, 1003);

-- 6) Execute fixed report
EXEC dbo.RptOnlineRptReturnDetailsForWF
  @CompanyID = 1,
  @FromDate = '2025-01-30',
  @ToDate = '2027-01-30',
  @SalesmanNo = 1003,
  @TransactionTypeID = 1;

-- 7) All salesmen smoke test (new capability)
EXEC dbo.RptOnlineRptReturnDetailsForWF
  @CompanyID = 1,
  @FromDate = '2025-01-30',
  @ToDate = '2027-01-30',
  @SalesmanNo = -1,
  @TransactionTypeID = 1;
```

---

## Tables / Objects Referenced

| Object | Role |
|--------|------|
| `TransactionsHeaders` / `TransactionsDetails` | Report fact data |
| `Customers` / `CustomersFinancialDetails` | Customer master + position assignment |
| `SalesPersons` (`ID`, `Parent`, `PositionID`, `SalesPersonType`) | Org hierarchy + position link |
| `Fun_GetSalesPersonTree` / `Fun_GetSalesmanTreeByID` | Recursive downline (old/alternate path) |
| `RptOnlineRptReturnDetailsForWF` | Broken → fixed procedure |
| `RptSalesPersonItemBalance` | Working reference pattern (ELSE / Parent) |
| `RptDailySalesSummary` | Same-family follow-up if ELSE still uses tree |

---

## Verification Result

- **Root cause confirmed**: empty **FilterCust** for manager **1003** (no direct CFD customers on his position), not missing transactions.
- **Fix**: comment tree/Position lookup path; apply **Parent / self / -1** pattern from working report on header FilterCust, header salesman filter, and details.
- **Client**: أحمد / جزر الملايو — case from **محمد عبدو**.
- **Status**: Documented from investigation thread; confirm production `ALTER` deployed and report returns rows for 1003 + spot-check `-1`.
- **Caveat / prevention**: Parent filter is **one level deep**. Multi-level teams may still need `Fun_GetSalesmanTreeByID` (without hostile type filters) or a recursive CTE. Confirm UI passes **SalesPerson ID** consistently with the new parameter meaning. Consider fixing other reports still on tree+FilterCust-manager-only pattern (`RptDailySalesSummary` debug block prepared).

(End of file)
