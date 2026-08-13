---
type: shared
name: Duplicate-Visit
tags: [#runbook, #support, #sync, #osfa]
support_relevance: high
last_verified: 2026-07-14
---

# Duplicate-Visit

## Symptom
A salesman reports the same customer visit logged twice on the tablet, or the same visit appears as two rows in Back Office `CustomersVisitActivity`. Routes/visit counts are inflated and downstream attendance or KPI reports are wrong.

## Why it happens
The tablet stores visits in `MMS_OrderVisits` (OSFA_DB) and syncs them to `CustomersVisitActivity` (Olives_BO). A duplicate arises when:
- The tablet double-inserts the visit (network retry, double-tap) and the `*_CheckExist` idempotency guard was bypassed.
- A sync batch is re-posted to BO, writing the same visit twice into `CustomersVisitActivity`.
- A salesman manually re-logs a visit that auto-logged on GPS check-in.

## Diagnosis
1. On the tablet, find the duplicate rows:
   `SELECT CustomerID, SalesPersonID, VisitDate, COUNT(*) FROM OT_MMS_OrderVisits GROUP BY CustomerID, SalesPersonID, VisitDate HAVING COUNT(*) > 1;`
2. In BO, confirm the mirror duplicates:
   `SELECT CustomerID, SalesPersonNo, PositionsID, CompanyID FROM CustomersVisitActivity WHERE CustomerID = <id> ORDER BY VisitTime DESC;`
3. Inspect [[IntegrationPostedTransactions]] for two posts of the same source visit (same TabletSysID + doctype).
4. Inspect [[IntegrationErrorLog]] for the duplicate-insert attempt and the originating tablet batch.
5. Check whether the visit `*_CheckExist` proc was called before insert.

## Fix
1. If the row already exists and is valid, discard the duplicate import and mark the batch processed.
2. De-duplicate via the existing maintenance procs where available (e.g. [[FixDuplicate_All]], [[FixCustomerMFDuplicateError]]).
3. Re-run the post step once the duplicate is cleared.

## Prevention
- Always call the matching `*_CheckExist` proc before the visit `*_Insert`.
- Make sync retries idempotent (skip-if-already-posted) keyed on `TabletSysID`.
- Train salesmen not to manually re-log a visit that auto-logged on GPS check-in.

## Related
- [[MMS_OrderVisits]]
- [[CustomersVisitActivity]]
- [[IntegrationPostedTransactions]]
- [[IntegrationErrorLog]]
- [[Duplicate-Keys]]
