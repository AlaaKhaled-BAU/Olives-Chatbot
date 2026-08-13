---
type: shared
name: Van-Stock-Mismatch
tags: [#runbook, #support]
support_relevance: high
last_verified: 2026-07-14
---
# Van-Stock-Mismatch

## Symptom
After a van load or unload, the physical van stock does not match the system. The salesman's on-hand balance diverges from SalesPersonsItemsBalance, shrinkage or phantom stock appears, or a load/unload order will not close.

## Why it happens
Van inventory is tracked across three moving parts: the load/unload documents ([[VanTransferHeader]] for van transfers, [[TransfersOrdersHeaders]] for transfer orders), the running salesman balance in SalesPersonsItemsBalance, and the stock-taking/load-order procedures that reconcile them ([[Pro_SalesmanStockAndReturnLoadOrders]] / [[Pro_CalcSalespersonItemBalance]]). A mismatch arises when an unload order is not posted (balance not decremented), a load order is partially received, a return is not captured, or shrinkage/theft is never recorded — leaving the BO balance out of step with reality.

## Diagnosis
1. Identify the van/salesman and date range; open the relevant [[VanTransferHeader]] and [[TransfersOrdersHeaders]] documents.
2. Compare posted quantities against the live balance in SalesPersonsItemsBalance.
3. Check whether the load/unload was actually posted via [[Pro_SalesmanStockAndReturnLoadOrders]] and whether [[Pro_CalcSalespersonItemBalance]] was run.
4. Look for unposted returns or stock-taking adjustments in [[OT_VanTransferHF]] / [[OT_VanTransferDF]] on the tablet side ([[OT_ErrorLogInteg]] for sync errors).

## Fix
1. Post any missing load/unload/return document so the balance updates.
2. If quantities were wrong, correct the document and re-run [[Pro_CalcSalespersonItemBalance]].
3. Record genuine shrinkage as a stock adjustment so BO matches physical count.
4. Re-validate the balance in SalesPersonsItemsBalance and close the order.

## Prevention
- Enforce that unload/load orders cannot close until posted and balanced.
- Run [[Pro_CalcSalespersonItemBalance]] on a schedule and alert on drift.
- Require stock-taking after each unload to catch shrinkage early.

## Related
- [[VanTransferHeader]]
- [[TransfersOrdersHeaders]]
- SalesPersonsItemsBalance
- [[Pro_SalesmanStockAndReturnLoadOrders]]
