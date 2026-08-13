---
type: relation
database: Olives_BO
name: PriceListDetails--PriceLists
tags: [#fk, #backoffice]
support_relevance: high
parent_table: [[PriceListDetails]]
referenced_table: [[PriceLists]]
columns: "PriceListDetails.PriceListID → PriceLists.ID"
---

# PriceListDetails → PriceLists

**FK**: PriceListDetails.PriceListID → [[PriceLists]].ID

**Business meaning**: Each price list contains multiple item-specific pricing rules. This FK groups details under their parent list.

**Source table**: [[PriceListDetails]]
**Target table**: [[PriceLists]]
