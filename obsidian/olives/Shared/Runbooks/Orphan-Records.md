---
type: shared
name: Orphan-Records
tags: [#runbook, #support]
support_relevance: high
last_verified: 2026-07-14
---
# Orphan-Records

## Symptom
A report or screen errors out with a foreign-key / null-reference failure, or a child record (e.g. a customer transaction) shows no parent. Queries that `JOIN` parent tables return missing or incomplete rows.

## Why it happens
Offline tablet inserts can create child rows whose parent was never synced, was deleted in BO, or failed import. Because the tablet enforces few FK constraints locally, rows like [[OT_InvoiceHF]] can reference a `CustomerSysID` that does not exist in BO [[Customers]], or a [[OT_NewCustomers]] row whose [[Companies]] branch link is missing. The BO relation notes document the expected parent/child edges.

## Diagnosis
1. Reproduce the failing query and capture the FK error.
2. Check relation notes for the expected parent: [[Customers--SalesPersons]], [[OrdersHeaders--Customers]], [[TransactionsHeaders--Customers]], [[IntegrationPostedTransactions--TransactionsHeaders]].
3. Run an anti-join: select child rows whose parent `SysID` is absent in the parent table.
4. Inspect [[OT_ErrorLogInteg]] for import rows that were skipped (parent missing) leaving orphans.

## Fix
1. Create the missing parent (e.g. re-import the customer / company) so the FK resolves.
2. If the parent is permanently gone, re-link the child to a valid parent or soft-delete the orphan.
3. Re-run the affected report/procedure (e.g. [[Pro_Customers]]) to confirm the failure clears.

## Prevention
- Add a post-sync integrity job that anti-joins `OT_*` children against BO parents and flags orphans.
- Enforce FK validation at import time in the integration layer.
- Regularly review [[Exceptions]] for recurring orphan patterns.

## Related
- [[Customers]]
- [[Companies]]
- [[Customers--SalesPersons]]
- [[IntegrationPostedTransactions--TransactionsHeaders]]
