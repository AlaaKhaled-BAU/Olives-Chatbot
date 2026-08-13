---
type: shared
name: Credit-Limit-Block
tags: [#runbook, #support]
support_relevance: high
last_verified: 2026-07-14
---
# Credit-Limit-Block

## Symptom
A salesman's order or invoice is rejected at the tablet with "credit limit exceeded" even though the customer/salesman should be allowed. A big order keeps getting blocked and never reaches BO, or the user waits indefinitely on an approval that never fires.

## Why it happens
Credit enforcement compares the open balance against the limit stored on [[Customers]] / [[SalesPersonItemsBalance]] and the per-transaction request tables. When the balance is over limit, the tablet raises a `RequestToExceed*` record that must travel through the workflow engine ([[WF_SetupHeader]] / [[WF_SetupDetails]]) for approval. If the WF has no approver configured, the request sits unapproved and the order is blocked; if the limit was raised in BO but not pushed to the tablet, the tablet still blocks.

## Diagnosis
1. Confirm the block: check the open balance vs limit in [[Customers]] and the request row in [[RequestToExceedCustomerCreditLimit]] (or [[RequestToExceedCustomerCreditLimitInOrder]], [[RequestToExceedSalesmanCreditLimit]]).
2. Check whether a matching WF approval exists: inspect [[WF_SetupHeader]] / [[WF_SetupDetails]] for the exceed-credit workflow and its approvers.
3. Confirm the tablet received the updated limit via the last sync ([[OT_ErrorLogInteg]] for the push).
4. For aging context use [[CustomersFinancialDetails]] / [[Rpt_CheckAging]].

## Fix
1. If the limit is wrong, correct it in BO on [[Customers]] and re-push to the tablet.
2. If legitimate, approve the `RequestToExceed*` row through the configured WF approver.
3. If the WF has no approver, configure one in [[WF_SetupDetails]] and re-submit the request.
4. For historical aging questions, run [[Rpt_CheckAging]] / [[Rpt_WF_FinancialAging]].

## Prevention
- Validate WF approver configuration for every `RequestToExceed*` type at onboarding.
- Push limit/balance changes to tablets on each sync and verify receipt.
- Monitor stuck `RequestToExceed*` rows older than SLA.

## Related
- [[RequestToExceedCustomerCreditLimit]]
- [[RequestToExceedSalesmanCreditLimit]]
- [[WF_SetupHeader]]
- [[CustomersFinancialDetails]]
