# -*- coding: utf-8 -*-
import sys
import os
import json
from pathlib import Path

# Force UTF-8 stdout
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from core import agent

TEST_CASES = [
    {
        "id": "Q1",
        "difficulty": "Easy - Operational Classification",
        "question": "مين المناديب اللي شغالين كاش فان ومين اللي شغالين طلبات بس؟",
        "expected_themes": ["كاش فان", "طلبات", "Cash Van", "Order Taking", "فواتير", "صلاحيات"],
    },
    {
        "id": "Q2",
        "difficulty": "Medium - Entity Identification & Vehicle Join",
        "question": "بدي اعرف المندوب عبد الرزاق بيشتغل كاش فان ولا مندوب طلبات وشو رقمه وسيارته؟",
        "expected_themes": ["عبد الرزاق", "كاش فان", "سيارة"],
    },
    {
        "id": "Q3",
        "difficulty": "Hard - Dual Inventory (Van vs Central Warehouse)",
        "question": "كم كمية الصنف 3001001 في سيارات المناديب مقارنة بالمستودع؟",
        "expected_themes": ["كمية", "رصيد", "مستودع", "SalesPersonItemsBalance", "StoresBalances"],
    },
    {
        "id": "Q4",
        "difficulty": "Hard - Transfer Orders Lifecycle & Type 6/7 Guard",
        "question": "كيف بنعرف إذا أوامر التحميل والتنزيل تحولت لحركات مبيعات ومخزون ولا لسا معلقة؟",
        "expected_themes": ["أوامر تحميل", "حركات", "TransfersOrders", "تحويل", "نوع"],
    },
    {
        "id": "Q5",
        "difficulty": "Very Hard - Multi-Intent Pipeline & Hybrid Reporting",
        "question": "أعطيني ملخص شامل للمبيعات والطلبيات: كم إجمالي الفواتير الفعلية وكم الطلبيات اللي لسا ما تسلمت؟",
        "expected_themes": ["فواتير", "طلبيات", "مبيعات", "معتمدة", "إجمالي"],
    },
]

def run_tests():
    results = []
    print("=" * 80)
    print("STARTING 5 NATURAL LANGUAGE DIVERSE COMPLEXITY EVALUATION")
    print("=" * 80)

    for tc in TEST_CASES:
        print(f"\n---> Testing {tc['id']} [{tc['difficulty']}]:")
        print(f"Question: {tc['question']}")
        
        try:
            res = agent.ask("105", tc["question"], conversation={"CompanyID": 1})
            answer = res.get("answer") or res.get("needs_ask") or ""
            sql_used = res.get("answer_sql") or ""
            sources = res.get("sources") or []
            
            print(f"Status: {res.get('status')}")
            print(f"SQL Generated:\n{sql_used}\n" if sql_used else "No SQL generated (Hot Cache / Docs / Fast path)")
            print(f"Answer snippet:\n{answer[:350]}...\n")
            
            score = "PASS"
            notes = []
            if not answer.strip():
                score = "FAIL"
                notes.append("Empty answer")
            
            results.append({
                "id": tc["id"],
                "difficulty": tc["difficulty"],
                "question": tc["question"],
                "answer": answer,
                "sql": sql_used,
                "score": score,
                "notes": notes,
            })
        except Exception as e:
            print(f"ERROR running {tc['id']}: {e}")
            results.append({
                "id": tc["id"],
                "difficulty": tc["difficulty"],
                "question": tc["question"],
                "score": "ERROR",
                "notes": [str(e)],
            })

    output_path = BASE_DIR / "evals" / "natural_language_5q_results.json"
    output_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n" + "=" * 80)
    print(f"Results successfully saved to {output_path}")
    print("=" * 80)

if __name__ == "__main__":
    run_tests()
