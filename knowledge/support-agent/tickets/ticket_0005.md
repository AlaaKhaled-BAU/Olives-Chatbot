# Ticket 0005: Bonus Report Shows Wrong Values (7 Instead of 107)

* **Date & Time**: 2026-06-24
* **System Component**: Back Office (Report / Stored Procedure)
* **Symptom Category**: DB (Data Integrity / Query Logic)
* **Reported Issue**:
  A user creates a report and the bonuses column shows 7 instead of the expected 107. The discrepancy is caused by negative bonus values being stored in the database — the report's HAVING clause was filtering them out, and the SUM was not converting stored negatives to positives.

---

## Root Cause & Diagnosis

The stored procedure generating the report had a HAVING clause that only included rows where `SUM(Bonus) > 0`. However, some bonus records are stored as negative values in the database (e.g., corrections, voided transactions, or entries that use negative signs to indicate direction). This caused the query to either:

1. **Exclude groups** where the sum of bonuses was zero or negative after netting positive and negative values (giving 7 instead of 107 — the sum of only the positive subset).
2. **Sum raw values** without converting stored negatives to positives, producing a net figure instead of the total bonus volume.

### Correct Pattern (from `OT_SalesmanItemBonusTarget` sync procedure in `procedures.md`)

The existing bonus target sync procedure at lines ~10710-10775 uses the correct approach:

**For `TransactionsDetails.Bonus`** (line 10728):
```sql
isnull(abs(SUM(TransactionsDetails.Bonus)),0) AS BONUS
```
and HAVING (line 10737):
```sql
HAVING ... AND (ABS(SUM(TransactionsDetails.Bonus)) > 0)
```

**For `TransactionsPromotions.Bonus`** (lines 10753, 10766):
```sql
isnull(SUM(TransactionsPromotions.Bonus),0)*-1 as Bonus
```
and HAVING (lines 10762, 10775):
```sql
HAVING ... AND (ABS(SUM(TransactionsPromotions.Bonus)) > 0)
```

The key fixes applied to the report:

1. **Changed `HAVING SUM(Bonus) > 0` to `HAVING ABS(SUM(Bonus)) > 0`** — this ensures groups are not excluded when the sum happens to be zero or negative due to stored negative values.
2. **Multiplied the bonus column by `-1`** — converts stored negative values to positives so `SUM` produces the correct total (e.g., 107 instead of 7).

---

## Solution

Modify the report's SQL query:

**Before:**
```sql
SELECT ..., SUM(Bonus) AS Bonuses
FROM ...
GROUP BY ...
HAVING SUM(Bonus) > 0
```

**After:**
```sql
SELECT ..., SUM(Bonus) * -1 AS Bonuses
FROM ...
GROUP BY ...
HAVING ABS(SUM(Bonus)) > 0
```

*(Use `abs(SUM(Bonus))` or `SUM(Bonus) * -1` depending on whether the stored negatives need flipping or just absolute summing — the existing procedure at lines 10728-10762 uses both patterns as a reference.)*

---

## Tables Referenced

| Table | Role |
|---|---|
| `TransactionsDetails.Bonus` | Stores invoice/order bonus quantities (may have negative values) |
| `TransactionsPromotions.Bonus` | Stores promotion-related bonus (multiplied by `-1` in correct queries) |
| `SalesPersonItemBonusTarget` | Defines bonus targets per salesman per item/month |
| `OSFA_DB.dbo.OT_SalesmanItemBonusTarget` | Tablet-side replica of bonus target data |

---

## Verification Result

After applying the HAVING and sign-flip fixes, the report shows the correct bonus total (107 instead of 7).
