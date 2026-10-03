"""User-facing Arabic labels keyed by structured codes (I1). No literals in thread.py."""

LABELS: dict[str, str] = {
    "tax.incl": "شامل الضريبة",
    "tax.excl": "قبل الضريبة",
    "returns.gross": "بدون خصم المرتجعات",
    "returns.net": "بعد المرتجعات",
}

COUNT_NOTE_USER = (
    "تنبيه: العدد المذكور كفواتير هو عدد البنود، وليس عدد رؤوس الفواتير."
)

HEADER_COUNT_SUFFIX = "عدد الفواتير: {n}"


def label(code: str) -> str:
    return LABELS.get(code, code)
