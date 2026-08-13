---
type: shared
name: Invoice-Posting-Failure
tags: [#runbook, #support]
support_relevance: high
last_verified: 2026-07-14
---
# Invoice-Posting-Failure

## Symptom
A customer or finance team says "the invoice never reached SAP / the ERP". In BO the invoice exists in [[TransactionsHeaders]] but has no corresponding posted integration record, or it is stuck in [[IntegrationPostedTransactions]] with a permanent error status.

## Why it happens
Posting is a two-stage flow: the transaction is written to [[TransactionsHeaders]] (and [[TransactionsDetails]]) by the sales/invoicing proc, then an integration procedure picks it up and writes a row to [[IntegrationPostedTransactions]], calling the target ERP adapter (e.g. SAP_Integ_SendSalesInvoices). If the adapter throws, the error is recorded in [[IntegrationErrorLog]] and the posted row stays in a failed/queued state, so the ERP never receives it. Common causes: missing customer master in ERP, item-not-found, or a transient API failure never retried.

## Diagnosis
1. Confirm the invoice header exists: `SELECT * FROM TransactionsHeaders WHERE ...` (use [[Pro_TransactionsHeaders]]).
2. Check [[IntegrationPostedTransactions]] for the invoice's `TransactionSysID` — is it missing, queued, or errored?
3. Read the failure detail in [[IntegrationErrorLog]] (source = the integration proc, e.g. [[SAP_Integ_SendSalesInvoices]]).
4. Verify the customer/item masters exist in the target ERP before resend.

## Fix
1. Resolve the root cause in the ERP (create missing master, fix mapping).
2. Clear/acknowledge the error row in [[IntegrationErrorLog]] and reset the posted-transaction status.
3. Re-run the integration post step (the relevant `SAP_Integ_*` / `GP_Integ_*` / `X3_Integ_*` proc) to resend.
4. Confirm a success row now appears in [[IntegrationPostedTransactions]] and the ERP shows the invoice.

## Prevention
- Alert on aged failed rows in [[IntegrationPostedTransactions]].
- Add a pre-send validation that masters exist in the target ERP.
- Make the post step idempotent so safe-retry does not double-post (see [[Duplicate-Keys]]).

## Related
- [[TransactionsHeaders]]
- [[IntegrationPostedTransactions]]
- [[IntegrationErrorLog]]
- [[SAP_Integ_SendSalesInvoices]]
