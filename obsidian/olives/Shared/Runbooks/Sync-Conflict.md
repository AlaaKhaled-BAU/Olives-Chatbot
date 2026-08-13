---
type: shared
name: Sync-Conflict
tags: [#runbook, #support]
support_relevance: high
last_verified: 2026-07-14
---
# Sync-Conflict

## Symptom
A record edited on a tablet (OSFA_DB) and in the back office (Olives_BO) at the same time shows only one version after sync; data the user just entered is gone. You may also see a duplicate `TabletSysID`, orphan tablet rows with no BO parent, or an `IsPosted` flag stuck on `false` so the row never reaches integration.

## Why it happens
The tablet is an occasionally-connected offline store. Sync uses a last-write-wins merge keyed on `TabletSysID` (the local tablet identity) and the BO `SysID` assigned on import. If two edits race, the second import overwrites the first with no conflict detection. Duplicate `TabletSysID` values (from a re-imaged tablet or a copied database) make inserts collide or merge wrong rows, leaving orphan `OT_*` rows whose `SysID` has no counterpart in the BO table, and `IsPosted` stays `false` when the post step errors out and is never retried.

## Diagnosis
1. Find the offending row in the tablet store: inspect [[OT_InvoiceHF]] / [[OT_InvoiceDF]] and confirm `TabletSysID` / `IsPosted` values.
2. Look for duplicate `TabletSysID` with `SELECT TabletSysID, COUNT(*) ... GROUP BY TabletSysID HAVING COUNT(*)>1` on the relevant `OT_*` table.
3. Check `IsPosted = 0` rows and the failure detail in [[OT_ErrorLogInteg]].
4. In BO, trace the import result in [[IntegrationPostedTransactions]] and [[IntegrationErrorLog]].
5. Confirm parent existence: the BO row referenced by the tablet's `SysID` must exist; missing parent = orphan.

## Fix
1. Identify the losing edit from [[OT_ErrorLogInteg]] timestamps and re-enter it manually in BO if the data is still needed.
2. De-duplicate `TabletSysID`: re-key the tablet DB with a fresh unique seed (do not reuse a copied DB).
3. For `IsPosted = false` stuck rows, re-run the post step after clearing the error in [[IntegrationErrorLog]]; or mark the row for manual reprocessing.
4. Re-point orphan rows: either create the missing BO parent or soft-delete the orphan tablet row.

## Prevention
- Enforce unique `TabletSysID` at the tablet DB level; block DB copy/clone between devices.
- Add a sync conflict queue instead of blind last-write-wins for high-value rows.
- Alert on `IsPosted = false` rows older than the sync window via [[OT_ErrorLogInteg]].

## Related
- [[OT_InvoiceHF]]
- [[IntegrationPostedTransactions]]
- [[OT_ErrorLogInteg]]
- [[IntegrationErrorLog]]
