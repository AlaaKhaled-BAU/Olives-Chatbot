---
type: shared
name: Duplicate-Keys
tags: [#runbook, #support]
support_relevance: high
last_verified: 2026-07-14
---
# Duplicate-Keys

## Symptom
An import or sync batch fails with a primary-key / unique-key violation. A receipt or transaction appears to have been posted twice, or BO rejects the row with "Violation of UNIQUE KEY constraint".

## Why it happens
Re-sent tablet batches (network retries, double-tap sync) re-insert rows whose `TabletSysID` already exists in BO, or the integration post step runs twice against [[IntegrationPostedTransactions]]. Without an idempotency guard on the unique key, the second write collides. The `*_CheckExist` procs are meant to guard this but may be bypassed on direct imports.

## Diagnosis
1. Capture the exact key/constraint name from the error.
2. In BO, search the conflicting table for the existing row: `SELECT * FROM <table> WHERE <key> = <value>`.
3. Inspect [[IntegrationPostedTransactions]] for a prior successful post of the same source transaction.
4. Inspect [[IntegrationErrorLog]] for the duplicate-insert attempt and the originating tablet batch.
5. Check whether the `*_CheckExist` proc (e.g. [[OT_InvoiceHF_CheckExist]]) was called before insert.

## Fix
1. If the row already exists and is valid, discard the duplicate import and mark the batch processed.
2. If two distinct business rows collided on a reused key, re-key one with a fresh unique value.
3. De-duplicate via the existing maintenance procs where available (e.g. FixCustomerMFDuplicateError, FixDuplicate_All).
4. Re-run the post step once the duplicate is cleared.

## Prevention
- Always call the matching `*_CheckExist` proc before `*_Insert` in import paths.
- Add an idempotency/UQ guard on [[IntegrationPostedTransactions]] keyed by source `TabletSysID` + doctype.
- Make sync retries idempotent (skip-if-already-posted).

## Related
- [[IntegrationPostedTransactions]]
- [[IntegrationErrorLog]]
- [[OT_InvoiceHF_CheckExist]]
- [[SP_IntegrationErrorLog]]
